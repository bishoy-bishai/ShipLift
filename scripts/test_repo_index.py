#!/usr/bin/env python3
"""
Unit tests for the ShipLift Repository Index (repo_index.py).

Run: python3 scripts/test_repo_index.py
"""

import argparse
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import repo_index as ri  # noqa: E402


def run(cwd, *args):
    subprocess.run(["git"] + list(args), cwd=cwd, check=True,
                    capture_output=True, text=True)


def make_repo(tmpdir):
    run(tmpdir, "init", "-q")
    run(tmpdir, "config", "user.email", "test@example.com")
    run(tmpdir, "config", "user.name", "Test User")
    return tmpdir


def commit_file(repo, name, content, date, subject):
    path = os.path.join(repo, name)
    with open(path, "w") as f:
        f.write(content)
    run(repo, "add", name)
    env_date = f"{date}T12:00:00"
    subprocess.run(
        ["git", "commit", "-q", "-m", subject],
        cwd=repo, check=True, capture_output=True, text=True,
        env={**os.environ, "GIT_AUTHOR_DATE": env_date, "GIT_COMMITTER_DATE": env_date},
    )


def args_for(repo, home, **extra):
    ns = argparse.Namespace(repo=repo, home=home)
    for k, v in extra.items():
        setattr(ns, k, v)
    return ns


class RepoIndexTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = make_repo(self._tmp.name)
        self._home = tempfile.TemporaryDirectory()
        self.home = self._home.name

        commit_file(self.repo, "app.py", "print('a')\n" * 30, "2026-01-05", "Add feature A")
        commit_file(self.repo, "app_test.py", "def test_a(): pass\n" * 10, "2026-01-06", "Add tests for feature A")
        commit_file(self.repo, "package-lock.json", "{}\n", "2026-01-07", "Bump dependency")

    def tearDown(self):
        self._tmp.cleanup()
        self._home.cleanup()

    def test_build_caches_commits(self):
        args = args_for(self.repo, self.home, since="2026-01-01", until="2026-02-01")
        ri.cmd_build(args)
        data = ri.load_index(args)
        self.assertEqual(len(data["commits"]), 3)

    def test_build_is_incremental(self):
        args = args_for(self.repo, self.home, since="2026-01-01", until="2026-02-01")
        ri.cmd_build(args)
        commit_file(self.repo, "extra.py", "x = 1\n", "2026-01-08", "Add extra file")
        commits = ri.fetch_commits(self.repo, "2026-01-01", "2026-02-01")
        data = ri.load_index(args)
        added = sum(1 for c in commits if c["hash"] not in data["commits"])
        self.assertEqual(added, 1)

    def test_lockfile_only_commit_is_low_value(self):
        commits = ri.fetch_commits(self.repo, "2026-01-01", "2026-02-01")
        by_subject = {c["subject"]: c for c in commits}
        self.assertTrue(by_subject["Bump dependency"]["low_value"])
        self.assertEqual(by_subject["Bump dependency"]["read_priority"], 0)

    def test_test_file_commit_is_flagged_and_ranked_higher(self):
        commits = ri.fetch_commits(self.repo, "2026-01-01", "2026-02-01")
        by_subject = {c["subject"]: c for c in commits}
        test_commit = by_subject["Add tests for feature A"]
        lockfile_commit = by_subject["Bump dependency"]
        self.assertTrue(test_commit["touches_tests"])
        self.assertGreater(test_commit["read_priority"], lockfile_commit["read_priority"])

    def test_rank_splits_into_read_and_skim_tiers(self):
        args = args_for(self.repo, self.home, since="2026-01-01", until="2026-02-01", limit=None)
        ri.cmd_build(args)
        data = ri.load_index(args)
        commits = ri._commits_in_range(data, "2026-01-01", "2026-02-01")
        read_tier = [c for c in commits if c["read_priority"] >= ri.READ_PRIORITY_THRESHOLD]
        skim_tier = [c for c in commits if c["read_priority"] < ri.READ_PRIORITY_THRESHOLD]
        self.assertTrue(read_tier)
        self.assertIn("Bump dependency", [c["subject"] for c in skim_tier])

    def test_list_filters_by_date_range(self):
        args = args_for(self.repo, self.home, since="2026-01-01", until="2026-02-01")
        ri.cmd_build(args)
        data = ri.load_index(args)
        narrow = ri._commits_in_range(data, "2026-01-06", "2026-01-06")
        self.assertEqual(len(narrow), 1)
        self.assertEqual(narrow[0]["subject"], "Add tests for feature A")

    def test_index_cached_outside_repository(self):
        args = args_for(self.repo, self.home, since="2026-01-01", until="2026-02-01")
        ri.cmd_build(args)
        path = ri.index_path(args)
        self.assertTrue(path.startswith(self.home))
        self.assertFalse(path.startswith(self.repo))


if __name__ == "__main__":
    unittest.main()
