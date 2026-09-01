#!/bin/bash

# ShipLift Pulse — EvidenceStore CLI wrapper
# Thin wrapper around pulse_store.py so Pulse has the same script-based
# interface as git-analysis.sh. This does NOT interpret evidence or run
# the question flow — that is the agent's job (see references/pulse-engine.md).

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${SCRIPT_DIR}/pulse_store.py"

if ! command -v python3 > /dev/null 2>&1; then
    echo '{"error": "python3 is required for the Pulse EvidenceStore"}'
    exit 1
fi

# -B: never write __pycache__/*.pyc next to this script. ShipLift may be
# installed inside a user's own project (e.g. a skills folder in their
# repo), and it must never leave generated files behind in their codebase
# — all real output goes to the EvidenceStore under ~/.shiplift.
exec python3 -B "$PY" "$@"
