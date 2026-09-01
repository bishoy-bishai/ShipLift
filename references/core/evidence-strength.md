# Evidence Strength

Every candidate contribution — a single evidence item or a linked group — gets an internal strength rating. This is separate from [Impact Analysis](impact-analysis.md): strength is about how well-supported the *evidence* is, not about how large the *outcome* was.

Implementation: `evidence_engine.py` (`evidence_strength`), exposed as `evidence-engine.sh strength --ids [...]`.

---

## 1. Levels

```
Strong Evidence
Moderate Evidence
Early Signal
```

### Strong Evidence

A group qualifies when it has a measurable metric (a real before/after value in `metadata`) **and** either multiple independent sources (e.g. Git + Pulse) or repetition (3+ related items).

```
Pulse:  Investigated flaky tests.
Git:    Fixed flaky tests (12 flaky runs/week → 0).
→ Strong Evidence (measurable + multi-source)
```

### Moderate Evidence

A group has *one* of: a measurable metric, multiple sources, or repetition — but not the combination Strong requires.

```
3 code reviews, no metric, same source (Pulse)
→ Moderate Evidence (repeated, no metric)
```

### Early Signal

A single, isolated item with no metric, no repetition, and no corroborating source.

```
"Reviewed a PR." (one item, no metadata)
→ Early Signal
```

---

## 2. Rules

- Strength is evaluated per **group** (the caller decides what's grouped, typically via [Evidence Linking](evidence-linking.md) or existing [Achievement Framework](../achievement-framework.md) clustering) — the engine does not decide grouping itself.
- Do not expose a raw numeric score to the user. Use the three levels and, when useful, the plain-language reasons (`evidence_strength` returns both).
- Never inflate strength because a claim *sounds* significant — only measurable metrics, multiple sources, and repetition count.
- Weak/Early-Signal contributions are appropriate to exclude from Quarter/CV output by the existing evidence-strength filtering rules ([Career Evidence Engine §6](../career-evidence-engine.md)), not to be dressed up as Strong.

---

## 3. Validation Checklist

- [ ] Strong Evidence always has a measurable metric plus multi-source or repetition
- [ ] Moderate Evidence never silently becomes Strong without a real metric
- [ ] Early Signal is not treated as achievement-worthy by itself
- [ ] No raw numeric score leaks into user-facing output
