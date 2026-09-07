# Context Strategy

How the agent should gather repository evidence without repeatedly re-reading full git history and full diffs. This governs *how much of the repository to read*, the same way [Humanization](humanization.md) governs *how the output is phrased* — the two are independent and never interfere with each other.

Implementation: `scripts/repo_index.py`, exposed as `scripts/repo-index.sh`. It caches commit metadata only (hash, date, author, subject, files touched, insertion/deletion counts) — never full diff text, and never source code. Full diffs are always fetched live via `repo-index.sh diff --hash <hash>` (a thin wrapper over `git show`) when the agent actually decides a commit is worth reading.

---

## 1. Why This Exists

`ShipLift Quarter`, `ShipLift CV`, `ShipLift 1:1`, and `ShipLift Standup` all inspect git history over a period, sometimes spanning months or years (`ShipLift CV` in particular — see [Career Evidence Engine](../career-evidence-engine.md)). Without a shared index, each command re-runs the same `git log`/`git diff --stat` scans, and the [Evidence Matrix](../evidence-matrix.md) inspection checklist can tempt the agent into reading every commit's full diff to be thorough — most of which (dependency bumps, merge commits, formatting-only changes) carry no evidence value.

The goal is the same principle the Evidence Matrix already states for evidence *quality* — "never allow weak inference to override strong evidence" — applied to reading *cost*: read fewer, more relevant diffs in full rather than skimming everything shallowly or reading everything in full.

---

## 2. Workflow

```
Task (Quarter / CV / 1:1 / Standup) needs a date range
                    ↓
repo-index.sh build --since S --until U
   (cached commit metadata, incremental — only new commits are fetched)
                    ↓
repo-index.sh rank --since S --until U
   (splits cached commits into read_full_diff / skim_only, by §3)
                    ↓
For each commit in read_full_diff:
   repo-index.sh diff --hash H   (full diff, read now)
                    ↓
For commits in skim_only:
   use subject + files + insertion/deletion counts only —
   do not fetch the full diff unless a later step needs it
                    ↓
Continue the existing Evidence Matrix / Evidence Engine pipeline unchanged
```

This replaces ad hoc `git log`/`git diff` calls for date-range scans — it does not replace `git-analysis.sh`, which still covers status, branches, tags, and one-off diffs between two refs outside this cached-range flow.

---

## 3. Read-Priority Ranking

`rank` scores every cached commit deterministically:

- **Low value (score 0):** the commit is a merge commit, or every file it touches is a lockfile (`package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `poetry.lock`, `Gemfile.lock`, `composer.lock`, `Cargo.lock`).
- **Otherwise:** starts at 1, plus up to 10 for files touched, plus up to 10 for total insertions+deletions, plus 3 if any touched file path looks like a test (`test`, `spec`, `__tests__`).

Commits scoring `>= 4` land in `read_full_diff`; everything else lands in `skim_only`. This threshold is a heuristic aid, not a hard rule — exactly like the anti-inflation lint in [Anti-Inflation](anti-inflation.md) §2 is a heuristic aid, not an auto-filter. If a `skim_only` commit's subject or file list suggests it actually matters (e.g. a one-line change to a critical config file), read its diff anyway. The index makes unnecessary reading easier to skip — it never makes necessary reading unavailable.

---

## 4. What Stays Manual

This index only helps with **git commit evidence**. It does not:

- decide which commits belong to the same achievement (still [Intelligence Rules](../intelligence-rules.md))
- rate evidence strength or impact (still [Evidence Strength](evidence-strength.md) / [Impact Analysis](impact-analysis.md))
- read or summarize PR/issue descriptions (still gathered directly when available)
- inspect coverage reports, CI output, or benchmarks (still direct inspection per [Evidence Matrix](../evidence-matrix.md))

---

## 5. Caching and Invalidation

- Cache location: `~/.shiplift/repo-index/<repo-id>.json` — outside the analyzed repository, same convention as the EvidenceStore (`references/core/evidence-engine.md` §"Reuse, Don't Rebuild").
- `repo-id` is derived from the repository's absolute path, so each local clone gets its own cache.
- `build` is additive and keyed by commit hash: re-running it for an overlapping or repeated range only fetches commits not already cached — a full rebuild is never required for normal use.
- Cache entries never expire on their own (a commit's metadata doesn't change once committed). If the cache is missing, corrupted, or unavailable for any reason, `build` simply repopulates it — this never blocks a command.

---

## 6. Fallback

If `repo-index.sh` fails for any reason (git not available, not a git repository, unexpected error), fall back to the existing direct `git-analysis.sh` / raw `git log`/`git diff` exploration the command would otherwise use. The index is a performance aid, not a dependency — every ShipLift command must keep working exactly as before if it's unavailable.

---

## 7. Security and Privacy

- Nothing leaves the local machine — the cache is a local JSON file, built entirely from local `git` output.
- Only commit metadata (hashes, dates, authors, subjects, file paths, line counts) is cached — never file contents, never diff text, never secrets.
- The cache is scoped per company/repo the same way Pulse evidence is (`~/.shiplift/...`), and is never uploaded or transmitted anywhere.
