# Signal Detection

A signal is a recurring pattern across evidence — a hint that something consistent is happening, not yet an achievement.

Implementation: `evidence_engine.py` (`detect_signals`), exposed as `evidence-engine.sh signals [--quarter YYYY-QN]`.

---

## 1. Example

```
Git:    Repeated testing improvements.
Pulse:  Helped teammates with testing.
Pulse:  Started a testing initiative.
Goal:   Improve engineering quality.
```

Recognized as:

```
Signal: Consistent contribution to engineering quality.
```

---

## 2. Detection Rule

A category becomes a signal once it has at least `SIGNAL_MIN_OCCURRENCES` (3) evidence items — from any source — within the analyzed window (a quarter, or all-time when no window is given). The signal reports the category, occurrence count, contributing sources, and the date range.

---

## 3. Rules

- A signal is **descriptive**, not evaluative — it says a pattern exists, not that it's good, bad, promotion-worthy, or complete.
- A signal is never automatically an achievement. The Achievement Engine still applies its own evidence-strength and impact rules before anything from a signal becomes a Quarter/CV achievement.
- A signal becomes a *stronger* candidate for an achievement as more, and more varied, evidence accumulates behind it (see [Evidence Strength](evidence-strength.md)) — but strength must still be earned by real evidence, not by the existence of the signal alone.
- Do not detect signals below the occurrence threshold — a single or double occurrence is not a pattern.

---

## 4. Usage

- **Quarter**: signals can prompt the agent to look for a cluster-worthy achievement in that category.
- **1:1**: signals make good discussion-topic material ("You've had a consistent pattern of code review this quarter").
- **Goals**: a signal aligned with a goal's category strengthens (but does not prove) supporting evidence for that goal.

---

## 5. Validation Checklist

- [ ] Fewer than 3 occurrences never produces a signal
- [ ] Signal descriptions state a pattern, not a judgment or score
- [ ] Signals do not bypass evidence-strength or impact rules downstream
