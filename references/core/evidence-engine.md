# Evidence Engine

The Evidence Engine is the shared intelligence layer underneath every ShipLift command. Commands are interfaces; the Evidence Engine is the brain.

> Git records what you changed.
> Pulse records what you contributed.
> ShipLift connects the two.

This file describes the unified model. The mechanics behind each stage live in their own files:

- [Evidence Linking](evidence-linking.md)
- [Evidence Strength](evidence-strength.md)
- [Impact Analysis](impact-analysis.md)
- [Signal Detection](signal-detection.md)
- [Blind Spots](blind-spots.md)
- [Anti-Inflation](anti-inflation.md)

Implementation: `scripts/pulse_store.py` (the EvidenceStore) + `scripts/evidence_engine.py` (linking, strength, impact, signals, blind spots, lint, open threads), exposed via `scripts/pulse-store.sh` and `scripts/evidence-engine.sh`.

---

## 1. Architecture

```
                         SHIPLIFT
                            │
                     Evidence Layer
                            │
              ┌─────────────┴─────────────┐
              ↓                           ↓
        CODE EVIDENCE                HUMAN EVIDENCE
              │                           │
             Git                        Pulse
              │                           │
              └─────────────┬─────────────┘
                            ↓
                    EVIDENCE ENGINE
                            │
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
          Linking        Signals       Strength
              │             │             │
              └─────────────┼─────────────┘
                            ↓
                     Impact Analysis
                            ↓
                   Anti-Inflation Layer
                            ↓
                  Career Intelligence
                            │
          ┌─────────────────┼─────────────────┐
          ↓                 ↓                 ↓
    Achievements          Goals               CV
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ↓
                     Standup / 1:1
```

Neither Git nor Pulse is "the real evidence" with the other as a supplement. Both are first-class evidence sources feeding one Evidence Engine — there is no separate intelligence system per source.

---

## 2. Unified Evidence Model

Every evidence item — regardless of source — has the same shape:

```
Evidence
├── id             unique identifier
├── company        which company/project this belongs to
├── workDate       when the work happened ("date" in storage)
├── capturedAt     when it was recorded
├── source         git | pulse | github | linear | slack | notion | jira | calendar | user
├── category       see Pulse categories (pulse-engine.md §4) or a git-derived category
├── description    a plain factual restatement — never an upgraded claim
├── confidence     High / Medium / Low — confidence in the FACT, not the impact
├── impact         Unknown unless real evidence of outcome exists (impact-analysis.md)
├── metadata       free-form structured details (e.g. before/after values, PR count)
└── links          ids of other evidence items this is related to
```

Only implement the sources currently in use (today: `user` via Pulse, and `git` when the agent records git-derived evidence through the same store). The schema reserves the rest so future integrations (GitHub, Linear, Slack, Notion, Jira, Calendar) can be added without redesigning the engine or its consumers.

`source: "user"` evidence follows the Pulse-specific category list and question-flow rules in [Pulse Engine](../pulse-engine.md). `source: "git"` (or other non-`user` sources) may use a broader, git-appropriate category vocabulary (e.g. Feature Delivery, Testing, Bug Fix, Performance, Architecture, CI/CD) consistent with the existing [Achievement Framework](../achievement-framework.md) and [Intelligence Rules](../intelligence-rules.md) — the store does not force git evidence into the Pulse category list (see `scripts/pulse_store.py` category validation).

---

## 3. Raw Evidence vs. Interpretation (Mandatory)

Never directly turn raw activity into an achievement. The pipeline is:

```
Raw Evidence
      ↓
Contribution
      ↓
Achievement
      ↓
Impact
```

```
Raw Evidence:   Reviewed 3 PRs.
Contribution:   Participated in code review and quality validation.
Achievement:    Potential contribution to engineering quality.
Impact:         Unknown.
```

The Evidence Engine (this layer) only produces Raw Evidence, plus the linking/strength/impact/signal analysis needed to support the later layers. It never generates a Contribution, Achievement, or Impact label itself — that remains the job of the existing Achievement Engine ([Achievement Framework](../achievement-framework.md), [Impact Engine](../impact-engine.md)), guided by [Anti-BS Rules](../anti-bs-rules.md) and [Anti-Inflation](anti-inflation.md).

---

## 4. Evidence Lifecycle

```
Captured → Classified → Linked → Validated → Interpreted → Used
```

- **Captured**: the raw statement or commit is recorded as-is (Pulse question flow, or a git-derived entry).
- **Classified**: assigned a category and confidence.
- **Linked**: candidate relationships to other evidence are identified (see [Evidence Linking](evidence-linking.md)) — never forced.
- **Validated**: run through the anti-inflation lint (see [Anti-Inflation](anti-inflation.md)).
- **Interpreted**: the Achievement/Goals/CV engines turn validated evidence into Contributions/Achievements/Impact.
- **Used**: surfaced in Quarter, Standup, 1:1, Goals, or CV output.

**Raw evidence must remain available at every stage.** Never overwrite the original description with an AI interpretation — corrections update the record explicitly (see [Pulse Engine §13](../pulse-engine.md#13-correction-flow)), interpretation is layered on top, not substituted in.

---

## 5. Evidence History

The EvidenceStore retains full evidence history per company, queryable by week, month, quarter, or company (`pulse-store.sh list/recent/by-quarter`). This is the minimum abstraction needed today for Standup/Quarter/Goals/CV/1:1 to work — it does not implement long-term trend analytics (growth curves, promotion-readiness scoring, etc.) beyond what these commands already need. Add further history-based analysis only when an existing command actually requires it (see [§8, Do Not Over-Engineer](#8-do-not-over-engineer)).

---

## 6. Career Intelligence, Not Employee Scoring

The Evidence Engine classifies evidence into visibility categories (see [Blind Spots](blind-spots.md) §2) to show the *shape* of a quarter or career. It must never collapse this into a single score.

```
❌ Engineer Score: 82/100
```

is forbidden output from any command. The purpose is evidence visibility — showing where evidence is strong and where it's thin — not ranking or rating the person.

---

## 7. Reuse, Don't Rebuild

- One EvidenceStore (`pulse_store.py`), used by every source.
- One Evidence Engine (`evidence_engine.py`), used by every command.
- No parallel achievement-generation, goal-mapping, or CV-aggregation system for Pulse-only or Git-only data — see [Command Integrations](#9-command-integration-summary).
- No new user-facing commands. The Evidence Engine makes existing commands (`Quarter`, `Standup`, `1:1`, `Goals`, `CV`, `Pulse`) smarter; it does not add to the command surface.

---

## 8. Do Not Over-Engineer

ShipLift stays:

```
Simple · Fast · Local-first · Evidence-based · Easy to understand
```

Avoid: unnecessary frameworks, databases, complex scoring systems, black-box ratings, huge schemas, premature integrations, unnecessary commands. Build only the operations the current commands actually need (`scripts/pulse_store.py` and `scripts/evidence_engine.py` intentionally expose a small, fixed CLI surface — extend it only when a command requires a new capability, not speculatively).

---

## 9. Command Integration Summary

| Command | Uses Evidence Engine for |
|---|---|
| `ShipLift Quarter` | Combining Git + Pulse evidence before clustering; open-thread follow-ups (§ "Quarter Closure" in [commands.md](../commands.md)) |
| `ShipLift Standup` | Blending recent Pulse evidence into `Done/Next/Blockers` |
| `ShipLift 1:1` | Surfacing signals, blind spots, and Pulse evidence as talking points |
| `ShipLift Goals` | Using Git + Pulse evidence together as supporting evidence (never proof of completion) |
| `ShipLift CV` | Using Strong/Moderate evidence (from either source) to support CV bullets |
| `ShipLift Pulse` | Writing evidence through the EvidenceStore; duplicate detection |

None of these commands' output contracts change. They just draw on a richer, shared evidence layer.

---

## The Principle

> ShipLift does not measure how busy you were. It builds evidence of how you contributed.
> When the evidence is weak, ShipLift should say so instead of making the story bigger.
