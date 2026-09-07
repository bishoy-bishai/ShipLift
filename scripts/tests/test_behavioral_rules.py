#!/usr/bin/env python3
"""ShipLift behavioral rule regression tests.

ShipLift's achievement reasoning is performed by the coding agent
following SKILL.md and references/**, not by executable code — there is
no "achievement generator" function to unit test. These tests instead
verify, by scenario, that the reference documents the agent relies on
still contain the specific rule that scenario depends on. If a rule is
weakened, removed, or contradicted during an edit, the matching test
fails here instead of silently degrading agent behavior.

Two scenarios (B, C) also exercise real arithmetic, since the % vs.
percentage-point distinction is a pure calculation, not a judgment call.

Run: python3 scripts/tests/test_behavioral_rules.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
REFS = ROOT / "references"

failures = []


def read(*parts):
    path = REFS.joinpath(*parts)
    if not path.exists():
        failures.append(f"missing reference file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text()


def check(name, condition, detail):
    if not condition:
        failures.append(f"{name}: {detail}")


# --- Test A: commit count / activity volume is not an achievement ---
achievement_framework = read("achievement-framework.md")
anti_bs = read("anti-bs-rules.md")
check(
    "Test A (commit count != achievement)",
    "activity" in achievement_framework.lower() and "impact" in achievement_framework.lower(),
    "achievement-framework.md must instruct against activity-volume achievements",
)
check(
    "Test A (commit count != achievement)",
    re.search(r"commit count", anti_bs, re.IGNORECASE) is not None
    or re.search(r"commit count", read("evidence-matrix.md"), re.IGNORECASE) is not None
    or re.search(r"commit count", read("impact-engine.md"), re.IGNORECASE) is not None
    or re.search(r"commit count", read("commands.md"), re.IGNORECASE) is not None,
    "no reference explicitly warns against treating commit count as impact",
)

# --- Test B: test-suite growth percentage, calculated for real ---
before, added = 120, 42
after = before + added
pct = round((added / before) * 100)
check(
    "Test B (test suite growth math)",
    pct == 35,
    f"expected 35% growth for 120->162 tests, computed {pct}%",
)
metrics = read("metrics.md")
check(
    "Test B (documented formula matches)",
    "35%" in metrics and "120" in metrics,
    "metrics.md must document the 120->162 / 35% test-suite-growth example",
)

# --- Test C: coverage delta must be percentage points, not percent ---
cov_before, cov_after = 78, 84
pp_delta = cov_after - cov_before
check(
    "Test C (coverage delta math)",
    pp_delta == 6,
    f"expected a 6 percentage-point delta for 78->84, computed {pp_delta}",
)
check(
    "Test C (percentage points documented)",
    "percentage points" in metrics,
    "metrics.md must document the percentage-point vs percent distinction",
)
check(
    "Test C (percentage points documented)",
    "percentage point" in read("output-templates.md"),
    "output-templates.md must show a percentage-point example, not a bare percent",
)

# --- Test D: no invented business impact ---
check(
    "Test D (no invented business impact)",
    re.search(r"revenue", anti_bs, re.IGNORECASE) is not None,
    "anti-bs-rules.md must explicitly forbid invented revenue claims",
)
anti_inflation = read("core", "anti-inflation.md")
check(
    "Test D (no invented business impact)",
    re.search(r"productivity|retention|conversion", anti_inflation, re.IGNORECASE) is not None,
    "core/anti-inflation.md must forbid inferring business/productivity outcomes from technical evidence",
)

# --- Test E: no invented leadership claims ---
check(
    "Test E (no invented leadership)",
    re.search(r"leadership", anti_bs, re.IGNORECASE) is not None,
    "anti-bs-rules.md must explicitly forbid invented leadership claims",
)
check(
    "Test E (no invented leadership)",
    re.search(r"leadership|ownership", anti_inflation, re.IGNORECASE) is not None,
    "core/anti-inflation.md must forbid leadership/ownership claims without evidence",
)

# --- Test F: no invented human evidence when Pulse is empty ---
pulse_engine = read("pulse-engine.md")
check(
    "Test F (no invented human evidence)",
    re.search(r"invent", pulse_engine, re.IGNORECASE) is not None,
    "pulse-engine.md must forbid inventing evidence the user did not state",
)

# --- Test G: 'Impact: Unknown' must be a valid, non-failure output ---
impact_analysis = read("core", "impact-analysis.md")
check(
    "Test G (Impact: Unknown is valid)",
    "Impact: Unknown" in impact_analysis,
    "core/impact-analysis.md must document 'Impact: Unknown' as a valid result",
)
check(
    "Test G (Impact: Unknown is valid)",
    re.search(r"not a failure", impact_analysis, re.IGNORECASE) is not None,
    "core/impact-analysis.md must state that Unknown impact is not a failure of the engine",
)

# --- Test H: related work must cluster into one story, not per-commit ---
check(
    "Test H (clustering, not per-commit achievements)",
    re.search(r"one achievement|ONE achievement", achievement_framework) is not None,
    "achievement-framework.md must document that related work groups into one achievement",
)
commands = read("commands.md")
check(
    "Test H (clustering, not per-commit achievements)",
    re.search(r"one bullet per commit|one achievement per commit", commands, re.IGNORECASE) is not None,
    "commands.md must explicitly forbid one-achievement/bullet-per-commit output",
)


def main():
    if failures:
        print(f"FAILED — {len(failures)} behavioral rule check(s):")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    print("OK — all behavioral rule checks passed (8 scenarios).")


if __name__ == "__main__":
    main()
