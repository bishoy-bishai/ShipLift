#!/bin/bash

# CLI smoke tests for the Evidence Engine (scripts/evidence-engine.sh),
# wired against the EvidenceStore (scripts/pulse-store.sh).
#
# The detailed algorithmic behavior is covered by
# scripts/test_evidence_engine.py — this script verifies the CLI wiring:
# argument parsing, store integration, and end-to-end JSON output.
#
# Run: ./scripts/test-evidence-engine.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STORE="${SCRIPT_DIR}/pulse-store.sh"
ENGINE="${SCRIPT_DIR}/evidence-engine.sh"
TMP_HOME="$(mktemp -d)"

PASS=0
FAIL=0

cleanup() {
    rm -rf "$TMP_HOME"
}
trap cleanup EXIT

assert_contains() {
    local haystack="$1"
    local needle="$2"
    local label="$3"
    if echo "$haystack" | grep -qF "$needle"; then
        PASS=$((PASS + 1))
        echo "PASS: $label"
    else
        FAIL=$((FAIL + 1))
        echo "FAIL: $label"
        echo "  expected to find: $needle"
        echo "  in: $haystack"
    fi
}

store() { "$STORE" --home "$TMP_HOME" "$@"; }
engine() { "$ENGINE" --home "$TMP_HOME" "$@"; }
id_of() { python3 -c "import json,sys; print(json.load(sys.stdin)['item']['id'])"; }

echo "== Setup: Git + Pulse evidence for one linked story =="
inv_out=$(store add --company acme --category "Investigation" \
    --description "Investigated flaky Cypress tests in CI" \
    --work-date "2026-08-01" --source pulse)
inv_id=$(echo "$inv_out" | id_of)

fix_out=$(store add --company acme --category "Bug Fix" \
    --description "Fixed the Cypress flaky test CI issue" \
    --work-date "2026-08-03" --source git \
    --metadata '{"before": "12 flaky runs/week", "after": "0 flaky runs/week"}')
fix_id=$(echo "$fix_out" | id_of)

share_out=$(store add --company acme --category "Knowledge Sharing" \
    --description "Shared the Cypress flakiness fix with the team" \
    --work-date "2026-08-04" --source pulse)
share_id=$(echo "$share_out" | id_of)

echo "== Test: find-related discovers the linked story =="
out=$(engine find-related --company acme --id "$inv_id")
assert_contains "$out" "$fix_id" "find-related surfaces the Git fix for the Pulse investigation"

echo "== Test: link persists a bidirectional link =="
out=$(store link --company acme --id "$inv_id" --to "$fix_id" --reason "same investigation")
assert_contains "$out" '"ok": true' "link command succeeds"

echo "== Test: strength across linked git+pulse+metric evidence is Strong =="
ids_json="[\"$inv_id\", \"$fix_id\", \"$share_id\"]"
out=$(engine strength --company acme --ids "$ids_json")
assert_contains "$out" '"Strong Evidence"' "linked multi-source evidence with a metric is Strong"

echo "== Test: impact is Measured when a real before/after exists =="
out=$(engine impact --company acme --id "$fix_id")
assert_contains "$out" '"Measured"' "git fix with before/after metric is Measured impact"

echo "== Test: impact is Unknown with no metric or outcome language =="
plain_out=$(store add --company acme --category "Code Review" \
    --description "Reviewed 3 PRs" --work-date "2026-08-05" --source pulse)
plain_id=$(echo "$plain_out" | id_of)
out=$(engine impact --company acme --id "$plain_id")
assert_contains "$out" '"Unknown"' "plain code review with no metric is Unknown impact"

echo "== Test: anti-inflation lint flags an unsupported claim =="
bad_out=$(store add --company acme --category "Initiative" \
    --description "Led the initiative and improved productivity by 30%" \
    --work-date "2026-08-06" --source pulse)
out=$(engine lint --company acme)
assert_contains "$out" "violations" "lint runs across all evidence"
count=$(echo "$out" | python3 -c "import json,sys; print(len(json.load(sys.stdin)['violations']))")
if [ "$count" -ge 1 ]; then
    PASS=$((PASS + 1))
    echo "PASS: lint flags the unsupported productivity claim"
else
    FAIL=$((FAIL + 1))
    echo "FAIL: lint did not flag the unsupported claim"
fi

echo "== Test: signals require repeated evidence =="
for i in 1 2 3; do
    store add --company acme --category "Mentoring" \
        --description "Mentored a junior engineer on testing (session $i)" \
        --work-date "2026-08-0$i" --source pulse > /dev/null
done
out=$(engine signals --company acme)
assert_contains "$out" '"category": "Mentoring"' "signals detect repeated Mentoring evidence"

echo "== Test: blind-spots report Limited Evidence, not a judgment =="
out=$(engine blind-spots --company acme)
assert_contains "$out" "Limited Evidence" "blind-spots use neutral 'Limited Evidence' language"
if echo "$out" | grep -qi "did not"; then
    FAIL=$((FAIL + 1))
    echo "FAIL: blind-spots output contains judgmental language"
else
    PASS=$((PASS + 1))
    echo "PASS: blind-spots output avoids judgmental language"
fi

echo "== Test: open-threads flags the unresolved investigation, resolved one is excluded =="
resolved_out=$(store add --company acme --category "Investigation" \
    --description "Investigated slow CI builds" --work-date "2026-08-01" --source pulse)
resolved_id=$(echo "$resolved_out" | id_of)
store update --company acme --id "$resolved_id" --metadata '{"resolved": true}' > /dev/null

out=$(engine open-threads --company acme)
assert_contains "$out" "follow_up_question" "open-threads produces a follow-up question"
if echo "$out" | grep -q "slow CI builds"; then
    FAIL=$((FAIL + 1))
    echo "FAIL: a resolved thread was still reported as open"
else
    PASS=$((PASS + 1))
    echo "PASS: resolved thread is excluded from open-threads"
fi
# The investigation is now linked to its resolution (Bug Fix), so it should
# no longer appear as an open thread either.
if echo "$out" | grep -q "flaky Cypress"; then
    FAIL=$((FAIL + 1))
    echo "FAIL: investigation with a linked resolution still reported as open"
else
    PASS=$((PASS + 1))
    echo "PASS: investigation with a linked resolution is closed"
fi

echo ""
echo "===================="
echo "PASS: $PASS  FAIL: $FAIL"
echo "===================="

if [ "$FAIL" -ne 0 ]; then
    exit 1
fi
