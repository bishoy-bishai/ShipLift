# Blind Spots

Blind spot detection shows where ShipLift has little or no evidence — an evidence gap, never a performance judgment.

Implementation: `evidence_engine.py` (`evidence_distribution`, `blind_spots`), exposed as `evidence-engine.sh blind-spots [--quarter YYYY-QN]`.

---

## 1. Career Areas

```
Technical Delivery
Code Quality
Problem Solving
Technical Ownership
Architecture
Collaboration
Mentoring
Knowledge Sharing
Initiative
Leadership
Cross-team Contribution
Developer Experience
Incident Response
```

Each area maps to a set of evidence categories (see `AREA_CATEGORY_MAP` in `evidence_engine.py`). This mapping is intentionally coarse — it's for visibility, not scoring — and an evidence item can count toward more than one area.

---

## 2. Levels

```
n >= 3 items  → Strong Evidence
n >= 1 item   → Moderate Evidence
n == 0 items  → Limited Evidence
```

---

## 3. The Critical Language Rule

**Do not say:**

```
"You do not mentor people."
```

**Say:**

```
"ShipLift has limited evidence of mentoring this quarter."
```

This is mandatory in all output. Zero evidence in an area means the engine hasn't seen supporting work — it does not mean the person didn't do it, and it must never be phrased as if it does.

---

## 4. Not an Employee Score

`blind_spots` / `evidence_distribution` must never be reduced to a single number or ranking.

```
❌ "Engineer Score: 82/100"
```

is forbidden in any ShipLift output. The output is a per-area evidence-level table, nothing else.

---

## 5. Usage

- **1:1**: blind spots can become growth-area or discussion topics ("limited evidence of cross-team work this quarter — worth raising if that's a growth focus").
- **Quarter**: blind spots contextualize why certain themes are missing from the achievement list — they don't force achievements to be manufactured to fill a gap.
- **CV**: an area with Limited Evidence is a reason a bullet doesn't exist yet, not a reason to invent one.

---

## 6. Validation Checklist

- [ ] Output never phrases a gap as "you didn't do X"
- [ ] Output never produces a single overall score
- [ ] Every area's level is backed by an actual evidence count, not an assumption
