# Anti-Inflation

The Anti-Inflation layer is the Evidence Engine's enforcement of the existing [Anti-BS Rules](../anti-bs-rules.md), applied specifically to the evidence layer (before achievements, goals, or CV bullets are ever generated).

Implementation: `evidence_engine.py` (`lint_evidence`), exposed as `evidence-engine.sh lint [--id ID]`.

---

## 1. Core Distinctions

These are never equivalent:

```
Activity        ≠ Impact
Volume          ≠ Achievement
Attendance      ≠ Contribution
Contribution    ≠ Business Result
```

Forbidden inferences:

```
Reviewed 10 PRs                  → "Improved team productivity by 30%"
Attended architecture meetings   → "Demonstrated technical leadership"
Helped a teammate                → "Increased team velocity by 20%"
```

unless the evidence itself contains a real measurement supporting the claim.

---

## 2. What the Lint Checks

`lint_evidence` flags an evidence item when its `description` contains an inflation-prone pattern **and** the item has no measurable metric in `metadata` to back it up:

- a percentage (`\d+%`)
- a quantified-improvement phrase ("improved X by")
- a business/productivity outcome word (productivity, velocity, revenue, conversion, retention, engagement)
- a leadership/ownership claim ("led", "drove", "owned")
- a specific team-size claim ("team of N")

It also flags an item whose `impact` field has been set to anything other than `Unknown` without a measurable metric present.

This is a **heuristic aid**, not a hard block — matches are reported for the agent (or a human reviewer) to check, not silently deleted or auto-rewritten. A true positive should be fixed by removing the unsupported claim or adding the real metric; a false positive (e.g. a legitimately measured claim the heuristic didn't recognize) should simply be left as-is by the agent.

---

## 3. When Impact Is Unknown

```
Impact: Unknown
```

is a valid, expected, and often correct result. Never treat it as something to fix by inventing a number.

---

## 4. Rules

- Every quantitative claim must have a real before/after in evidence.
- Every business-impact claim must have real business/user evidence, not an inference from technical work.
- Leadership/ownership language requires evidence the person actually held that role, not just participated.
- When in doubt, remove the claim or rephrase using only what's confirmed.

All existing [Anti-BS Rules](../anti-bs-rules.md) rule-by-rule guidance (percentages, business impact, revenue, conversion, customer impact, hours saved, leadership, ownership, stakeholder feedback, problem attribution) applies unchanged at this layer — this file is the evidence-layer enforcement mechanism, not a replacement ruleset.

---

## 5. Validation Checklist

- [ ] No unsupported percentage passes through to output
- [ ] No business/productivity outcome is inferred from technical evidence alone
- [ ] No leadership/ownership/team-size claim survives without evidence
- [ ] `Impact: Unknown` is preserved rather than replaced with a guess
- [ ] Lint findings are surfaced for review, not silently discarded or auto-accepted
