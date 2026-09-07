#!/bin/bash

# ShipLift Repository Index CLI wrapper.
# Thin wrapper around repo_index.py — cached commit metadata and
# read-priority ranking so Quarter/CV/1:1/Standup avoid re-scanning full
# git history and diffs on every command. See
# references/core/context-strategy.md.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${SCRIPT_DIR}/repo_index.py"

if ! command -v python3 > /dev/null 2>&1; then
    echo '{"error": "python3 is required for the Repository Index"}'
    exit 1
fi

# -B: never write __pycache__/*.pyc next to this script — ShipLift may be
# installed inside a user's own project, and it must never leave
# generated files behind in their codebase. All real output goes to
# ~/.shiplift/repo-index.
exec python3 -B "$PY" "$@"
