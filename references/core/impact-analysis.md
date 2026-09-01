# Impact Analysis

Impact Analysis determines whether an outcome is actually supported by evidence — and if so, how directly. It is the layer that stops "activity" from silently becoming "impact."

Implementation: `evidence_engine.py` (`impact_level`), exposed as `evidence-engine.sh impact --id ID`.

---

## 1. Levels

```
Measured
Observed
Supported
Unknown
```

### Measured

A real before/after, baseline/target, or count exists in the evidence's own `metadata`.

```
Test coverage increased by 35%. (metadata: coverage_before, coverage_after)
→ Measured
```

### Observed

The evidence's own description states an observed behavior change (e.g. "the team adopted the pattern") — only when the user/evidence actually said this, never inferred.

```
"The team adopted the new testing pattern."
→ Observed
```

### Supported

A concrete outcome is described, without a measurement — currently recognized for outcome-oriented categories (`Unblocking`, `Collaboration`, `Mentoring`, `Incident Response`) where a real outcome is stated.

```
"Helped unblock a teammate on the deploy pipeline."
→ Supported
```

### Unknown

No measured, observed, or clearly supported outcome — the default for plain activity statements.

```
"Reviewed 3 PRs."
→ Unknown
```

---

## 2. Two Separate Confidences

Never confuse these:

```
Evidence Confidence   — how sure we are the FACT happened (High/Medium/Low, set at capture time)
Impact Confidence     — how sure we are about the OUTCOME (Measured/Observed/Supported/Unknown)
```

```
Fact: Reviewed 3 PRs.
Evidence confidence: High
Impact: Unknown
```

A fact can be High confidence while its impact is Unknown — these are not contradictory.

---

## 3. Rules

- `impact_level` never upgrades an item — it only recognizes impact evidence already present in the item's own `metadata`/`description`. It cannot invent a metric that isn't there.
- `Impact: Unknown` is a valid, complete, and expected result. It is not a failure of the engine.
- Downstream commands (Quarter, Goals, CV, 1:1) must preserve this label rather than replacing it with an assumed outcome — see [Anti-Inflation](anti-inflation.md).

---

## 4. Validation Checklist

- [ ] "Reviewed N PRs" without a finding/metric stays Unknown
- [ ] A real before/after value is classified Measured, never left Unknown
- [ ] Evidence confidence and impact are never conflated in output
- [ ] No command silently converts Unknown impact into a number
