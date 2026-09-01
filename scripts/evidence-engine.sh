#!/bin/bash

# ShipLift Evidence Engine CLI wrapper.
# Thin wrapper around evidence_engine.py — linking, strength, impact
# analysis, signal detection, blind spots, anti-inflation lint, and
# open-thread detection over evidence stored via pulse-store.sh.
# See references/core/evidence-engine.md.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${SCRIPT_DIR}/evidence_engine.py"

if ! command -v python3 > /dev/null 2>&1; then
    echo '{"error": "python3 is required for the Evidence Engine"}'
    exit 1
fi

# -B: never write __pycache__/*.pyc next to this script. ShipLift may be
# installed inside a user's own project (e.g. a skills folder in their
# repo), and it must never leave generated files behind in their codebase
# — all real output goes through pulse-store.sh to ~/.shiplift.
exec python3 -B "$PY" "$@"
