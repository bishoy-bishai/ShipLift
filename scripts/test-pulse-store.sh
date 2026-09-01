#!/bin/bash

# Tests for the Pulse EvidenceStore (scripts/pulse-store.sh / pulse_store.py).
#
# Covers the scenarios required by the Pulse implementation:
# basic add/list, categories, duplicate detection, correction/update,
# date handling (work date vs capture date), and company isolation.
#
# Run: ./scripts/test-pulse-store.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STORE="${SCRIPT_DIR}/pulse-store.sh"
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

run() {
    "$STORE" --home "$TMP_HOME" "$@"
}

echo "== Test: init =="
out=$(run init --company acme)
assert_contains "$out" '"ok": true' "init creates store"

echo "== Test: add collaboration evidence =="
out=$(run add --company acme --category "Collaboration" \
    --description "Helped Ahmed fix a React rendering issue." \
    --work-date "2026-08-31")
assert_contains "$out" '"category": "Collaboration"' "add sets category"
assert_contains "$out" '"impact": "Unknown"' "add defaults impact to Unknown"
assert_contains "$out" '"date": "2026-08-31"' "add stores work date"
assert_contains "$out" '"source": "user"' "add defaults source to user"

echo "== Test: add code review evidence with metadata =="
out=$(run add --company acme --category "Code Review" \
    --description "Reviewed 3 PRs and found a validation issue." \
    --work-date "2026-08-31" --metadata '{"pr_count": 3}')
assert_contains "$out" '"pr_count": 3' "add stores metadata"
review_id=$(echo "$out" | python3 -c "import json,sys; print(json.load(sys.stdin)['item']['id'])")

echo "== Test: reject invalid category =="
set +e
out=$(run add --company acme --category "Not A Category" --description "x" 2>&1)
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
    PASS=$((PASS + 1))
    echo "PASS: invalid category is rejected"
else
    FAIL=$((FAIL + 1))
    echo "FAIL: invalid category was accepted"
fi

echo "== Test: nothing / not sure are not forced into evidence =="
# Pulse's rule is that the agent simply does not call `add` for these answers.
# The store itself has no special-case — verify list is unaffected.
out=$(run list --company acme)
count=$(echo "$out" | python3 -c "import json,sys; print(json.load(sys.stdin)['count'])")
if [ "$count" -eq 2 ]; then
    PASS=$((PASS + 1))
    echo "PASS: no phantom evidence created for 'nothing'/'not sure'"
else
    FAIL=$((FAIL + 1))
    echo "FAIL: expected 2 items, got $count"
fi

echo "== Test: duplicate detection =="
out=$(run check-duplicate --company acme --category "Collaboration" \
    --description "Helped Ahmed solve the React issue.")
assert_contains "$out" "Helped Ahmed fix a React rendering issue." "duplicate check finds similar entry"

echo "== Test: correction / update =="
out=$(run update --company acme --id "$review_id" \
    --description "Reviewed 2 PRs and found a validation issue." \
    --metadata '{"pr_count": 2}')
assert_contains "$out" '"pr_count": 2' "update corrects metadata"
assert_contains "$out" "Reviewed 2 PRs" "update corrects description"

echo "== Test: filter by category =="
out=$(run list --company acme --category "Code Review")
assert_contains "$out" '"count": 1' "list filters by category"

echo "== Test: filter by date =="
out=$(run list --company acme --date "2026-08-31")
assert_contains "$out" '"count": 2' "list filters by work date"

echo "== Test: company isolation =="
run add --company beta --category "Investigation" \
    --description "Investigated flaky Cypress tests." \
    --work-date "2026-08-31" > /dev/null
out_acme=$(run list --company acme)
out_beta=$(run list --company beta)
assert_contains "$out_acme" '"count": 2' "acme evidence count unaffected by beta"
assert_contains "$out_beta" '"count": 1' "beta evidence isolated from acme"
if echo "$out_beta" | grep -q "Ahmed"; then
    FAIL=$((FAIL + 1))
    echo "FAIL: beta company can see acme's evidence"
else
    PASS=$((PASS + 1))
    echo "PASS: beta company cannot see acme's evidence"
fi

echo "== Test: by-quarter =="
out=$(run by-quarter --company acme --quarter "2026-Q3")
assert_contains "$out" '"count": 2' "by-quarter finds Q3 2026 items"

echo "== Test: companies listing =="
out=$(run companies)
assert_contains "$out" '"acme"' "companies lists acme"
assert_contains "$out" '"beta"' "companies lists beta"

echo ""
echo "===================="
echo "PASS: $PASS  FAIL: $FAIL"
echo "===================="

if [ "$FAIL" -ne 0 ]; then
    exit 1
fi
