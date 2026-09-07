#!/usr/bin/env python3
"""
ShipLift Repository Index

A small local cache of commit metadata (hash, date, author, subject,
files touched, insertion/deletion counts) for the repository ShipLift is
analyzing. It exists to stop Quarter/CV/1:1/Standup from re-running the
same `git log` / `git diff --stat` scans on every command in a session,
and to give the agent a deterministic read-priority ranking so it reads
full diffs only for commits likely to matter (see
references/core/context-strategy.md) instead of every commit in a
multi-month CV period.

This module does NOT parse source code, build a symbol/call graph, or
attempt language-aware analysis — it indexes git metadata only. It also
never caches full diff *content*: `diff` always calls out to `git show`
live, since diff text is exactly the expensive part this index exists to
avoid reading until a commit is judged worth reading.

Storage: ~/.shiplift/repo-index/<repo-id>.json — same home-dir
convention as pulse_store.py, so nothing is left inside the analyzed
repository (see evidence-engine.sh's -B flag comment for why).

Usage:
    repo_index.py build --since DATE --until DATE [--repo PATH] [--home PATH]
    repo_index.py list  --since YYYY-MM-DD --until YYYY-MM-DD [--repo PATH] [--home PATH]
    repo_index.py rank  --since YYYY-MM-DD --until YYYY-MM-DD [--limit N] [--repo PATH] [--home PATH]
    repo_index.py diff  --hash HASH [--repo PATH]

`build` accepts any `git log --since/--until` syntax (relative or
absolute, matching git-analysis.sh). `list` and `rank` filter the cached
index and require plain YYYY-MM-DD bounds, since they compare against
already-stored commit dates rather than invoking git again.

All output is JSON on stdout.
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys

DEFAULT_HOME = os.path.expanduser("~/.shiplift")

# Files that, on their own, rarely justify a full diff read.
LOW_VALUE_FILE_PATTERNS = (
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock",
    "Gemfile.lock", "composer.lock", "Cargo.lock",
)

LOW_VALUE_SUBJECT_PATTERNS = (
    "merge branch", "merge pull request", "merge remote-tracking",
)

HIGH_VALUE_PATH_HINTS = ("test", "spec", "__tests__")

READ_PRIORITY_THRESHOLD = 4


def home_dir(args):
    return args.home or DEFAULT_HOME


def repo_path(args):
    return os.path.abspath(args.repo or ".")


def repo_id(path):
    return hashlib.sha1(path.encode("utf-8")).hexdigest()[:16]


def index_path(args):
    d = os.path.join(home_dir(args), "repo-index")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, f"{repo_id(repo_path(args))}.json")


def load_index(args):
    path = index_path(args)
    if not os.path.exists(path):
        return {"repo": repo_path(args), "commits": {}}
    with open(path) as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return {"repo": repo_path(args), "commits": {}}
    data.setdefault("commits", {})
    return data


def save_index(args, data):
    with open(index_path(args), "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")


def run_git(args_list, cwd):
    result = subprocess.run(
        ["git"] + args_list, cwd=cwd, capture_output=True, text=True, check=True,
    )
    return result.stdout


def is_low_value(subject, files):
    subject_lower = subject.lower()
    if any(p in subject_lower for p in LOW_VALUE_SUBJECT_PATTERNS):
        return True
    if files and all(any(p in f for p in LOW_VALUE_FILE_PATTERNS) for f in files):
        return True
    return False


def touches_tests(files):
    return any(any(hint in f.lower() for hint in HIGH_VALUE_PATH_HINTS) for f in files)


def read_priority(commit):
    """Deterministic score: higher = more worth reading the full diff.

    This is a heuristic aid for the agent, not a hard filter (see
    references/core/context-strategy.md §3) — a low-scored commit is
    still fully available via `diff` if the agent decides it matters.
    """
    if commit["low_value"]:
        return 0
    score = 1
    score += min(commit["files_changed"], 10)
    score += min((commit["insertions"] + commit["deletions"]) // 20, 10)
    if commit["touches_tests"]:
        score += 3
    return score


def _parse_stat(stat_output):
    files = []
    insertions = deletions = 0
    for line in stat_output.strip().splitlines():
        line = line.strip()
        if "|" in line:
            files.append(line.split("|")[0].strip())
        elif "changed" in line:
            for token in line.split(","):
                token = token.strip()
                if "insertion" in token:
                    insertions = int(token.split()[0])
                elif "deletion" in token:
                    deletions = int(token.split()[0])
    return files, insertions, deletions


def fetch_commits(path, since, until):
    log_format = "%H\x1f%aI\x1f%aN\x1f%s\x1e"
    raw = run_git(
        ["log", f"--since={since}", f"--until={until}",
         f"--pretty=format:{log_format}", "--no-merges"],
        cwd=path,
    )
    commits = []
    for entry in raw.split("\x1e"):
        entry = entry.strip()
        if not entry:
            continue
        sha, date, author, subject = entry.split("\x1f")
        stat_output = run_git(["show", "--stat", "--format=", sha], cwd=path)
        files, insertions, deletions = _parse_stat(stat_output)
        commit = {
            "hash": sha,
            "date": date[:10],
            "author": author,
            "subject": subject,
            "files": files,
            "files_changed": len(files),
            "insertions": insertions,
            "deletions": deletions,
        }
        commit["low_value"] = is_low_value(subject, files)
        commit["touches_tests"] = touches_tests(files)
        commit["read_priority"] = read_priority(commit)
        commits.append(commit)
    return commits


def cmd_build(args):
    path = repo_path(args)
    data = load_index(args)
    commits = fetch_commits(path, args.since, args.until)
    added = 0
    for c in commits:
        if c["hash"] not in data["commits"]:
            added += 1
        data["commits"][c["hash"]] = c
    save_index(args, data)
    print(json.dumps({"repo": path, "scanned": len(commits), "newly_cached": added}, indent=2))


def _commits_in_range(data, since, until):
    return [c for c in data["commits"].values() if since <= c["date"] <= until]


def cmd_list(args):
    data = load_index(args)
    commits = _commits_in_range(data, args.since, args.until)
    commits.sort(key=lambda c: c["date"])
    print(json.dumps({"count": len(commits), "commits": commits}, indent=2))


def cmd_rank(args):
    data = load_index(args)
    commits = _commits_in_range(data, args.since, args.until)
    commits.sort(key=lambda c: -c["read_priority"])
    if args.limit:
        commits = commits[: args.limit]
    print(json.dumps({
        "count": len(commits),
        "read_full_diff": [c for c in commits if c["read_priority"] >= READ_PRIORITY_THRESHOLD],
        "skim_only": [c for c in commits if c["read_priority"] < READ_PRIORITY_THRESHOLD],
    }, indent=2))


def cmd_diff(args):
    path = repo_path(args)
    out = run_git(["show", args.hash], cwd=path)
    print(json.dumps({"hash": args.hash, "diff": out}))


def build_parser():
    parser = argparse.ArgumentParser(description="ShipLift Repository Index")
    sub = parser.add_subparsers(dest="command", required=True)

    def common(p):
        p.add_argument("--repo")
        p.add_argument("--home")

    build_cmd = sub.add_parser("build")
    common(build_cmd)
    build_cmd.add_argument("--since", required=True)
    build_cmd.add_argument("--until", required=True)
    build_cmd.set_defaults(func=cmd_build)

    list_cmd = sub.add_parser("list")
    common(list_cmd)
    list_cmd.add_argument("--since", required=True)
    list_cmd.add_argument("--until", required=True)
    list_cmd.set_defaults(func=cmd_list)

    rank_cmd = sub.add_parser("rank")
    common(rank_cmd)
    rank_cmd.add_argument("--since", required=True)
    rank_cmd.add_argument("--until", required=True)
    rank_cmd.add_argument("--limit", type=int)
    rank_cmd.set_defaults(func=cmd_rank)

    diff_cmd = sub.add_parser("diff")
    common(diff_cmd)
    diff_cmd.add_argument("--hash", required=True)
    diff_cmd.set_defaults(func=cmd_diff)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except subprocess.CalledProcessError as e:
        print(json.dumps({"error": (e.stderr or str(e)).strip()}))
        sys.exit(1)


if __name__ == "__main__":
    main()
