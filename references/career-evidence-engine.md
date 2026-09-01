# Career Evidence Engine

The Career Evidence Engine powers `ShipLift CV`. It answers a question none of the other commands answer:

> **What did I actually build and accomplish at this company?**

This file contains the detailed rules for `ShipLift CV`, `ShipLift CV Senior`, and `ShipLift CV Lead`. See [Commands](commands.md) for the command contract and [Output Templates](output-templates.md) for the exact output format.

---

## 1. Core Principle

`ShipLift CV` is NOT a Git commit summarizer. It is a Career Evidence Engine.

```
Repository
    ↓
Git History
    ↓
Changes
    ↓
Related Changes
    ↓
Engineering Stories
    ↓
Achievements
    ↓
Career Evidence
    ↓
CV Bullet Points
```

The other ShipLift commands look at a short window (a quarter, a week, a month). `ShipLift CV` looks across months or years to find the handful of contributions that are genuinely worth putting on a résumé.

> **Do not turn activity into achievements.**
> **Turn meaningful engineering work into evidence-backed career stories.**
>
> **Do not make the engineer sound more impressive than the evidence.**
> **Make the evidence easier to see.**

---

## 2. Architecture: Reuse, Don't Rebuild

The CV Engine must not reimplement Git interpretation. It consumes the same pipeline every other command uses:

```
Git Analysis
     ↓
Evidence Engine  (evidence-matrix.md)
     ↓
Achievement Engine  (achievement-framework.md, intelligence-rules.md, impact-engine.md)
     ↓
Career Evidence Engine  (this file)
     ↓
CV Generator
```

Concretely: run the same repository analysis used by `ShipLift Quarter`, but over the full requested time range, then apply a second, coarser aggregation pass described below (§4). Do not create a parallel achievement-generation system.

---

## 3. Default Scope

`ShipLift CV` with no arguments analyzes the **broadest useful history in the repository**, not just the current quarter.

- Use the full commit history available for the current user in this repository, unless it spans an unreasonably long or clearly unrelated period.
- If the repository's history predates the user's involvement, or contains long idle gaps, note this rather than treating the whole span as uniformly relevant.
- Always state clearly that the analysis represents **repository evidence**, not the user's complete employment history. A person's real contributions may span other repositories, systems, or non-code work this engine cannot see.

Never claim 100% coverage of someone's work.

---

## 4. Career Evidence Aggregation

This is the key difference between `ShipLift Quarter` and `ShipLift CV`.

```
Quarter:  One quarter          → 5–7 achievements
CV:       Months / years       → many achievements → engineering stories → strongest contributions
```

A CV bullet is often built from **many quarters' worth of achievements**, not one commit or one PR.

Example:

```
50 commits
30 files
12 pull requests
8 bug fixes
20 tests
```

may collapse into:

```
ONE CV-WORTHY ENGINEERING CONTRIBUTION
```

**Never generate one CV bullet per commit, and never generate one bullet per Quarter-style achievement.** Run the standard achievement clustering first, then cluster *again* across time: achievements that share a theme, component, or category (e.g. multiple quarters of testing work) collapse into a single higher-level engineering story.

### Engineering Story Patterns

| Underlying work | Story type |
|---|---|
| Feature + API integration + validation + tests + bug fixes | Feature delivery story |
| Component refactor + shared utilities + type improvements + tests | Architecture / maintainability story |
| Test additions + regression fixes + coverage improvements | Quality / reliability story |
| CI changes + build improvements + developer tooling | Developer experience story |

Only merge achievements into one story when they share real evidence (same component, same theme, same category) — don't force unrelated work together just to reduce bullet count.

---

## 5. CV-Worthy Contribution Categories

Identify contributions across categories such as:

```
Feature Delivery
Architecture
Code Quality
Testing
Reliability
Performance
Developer Experience
CI/CD
Technical Debt
Security
Accessibility
Product Improvements
Developer Productivity
Cross-System Integration
Technical Ownership
```

Only include categories the repository evidence actually supports.

---

## 6. Career Evidence Strength

Every candidate contribution gets an internal evidence-strength rating, inherited from and consistent with [Evidence Matrix](evidence-matrix.md):

```
Strong Evidence:
- Multiple related PRs/commits over time
- Clear feature/story implementation
- Tests and supporting changes
- A measurable metric

Medium Evidence:
- Clear implementation
- Several related changes
- Limited or no measurable impact

Weak Evidence:
- Single small commit
- Ambiguous purpose
- No meaningful outcome
```

Only **Strong** and **Medium** evidence contributions appear in the default CV output. Weak-evidence items may be listed separately (e.g. under an optional "Additional Contributions" note) but must never be dressed up as strong bullets.

---

## 7. CV Bullet Construction

Each bullet should answer three questions:

```
What did I do?
+
What technology/context was involved?
+
What improved?
```

Preferred shape:

```
Action + Technical Context + Outcome
```

**Example:**

```
Improved frontend reliability by expanding automated test
coverage across critical user flows and strengthening
regression protection.
```

### Strong vs. Weak Language

```
Weak:     Added tests.
Better:   Expanded automated testing across critical frontend flows.
Strong:   Strengthened regression protection across critical frontend
          flows by expanding the automated test suite and covering
          key edge cases.
```

Do not exaggerate impact beyond what the evidence supports.

### Avoid Repetition

Do not produce several bullets that say the same thing in different words.

```
Bad:
- Added tests.
- Improved tests.
- Expanded tests.
- Created regression tests.

Good (combined):
- Strengthened frontend regression protection by expanding
  automated testing across critical user flows and edge cases.
```

---

## 8. Technology Usage

Mention technologies only when genuinely relevant to the bullet, and avoid keyword stuffing.

```
Bad:  React, TypeScript, Jest, Cypress, Git, HTML, CSS, Node.js...

Good: Built and improved React/TypeScript frontend workflows,
      strengthening automated regression coverage with RTL and
      Cypress.
```

---

## 9. Metrics on the CV

All existing ShipLift metric rules ([Metrics](metrics.md)) apply unchanged.

Critical distinctions:

```
120 → 162 tests   →  "Expanded the automated test suite by 35%."
                      (NOT "increased test coverage by 35%")

72% → 84% coverage → "+12 percentage points"
                      (NOT "+12% coverage")
```

Test count and coverage percentage are different metrics. Never substitute one for the other.

---

## 10. Technical Impact vs. Business Impact

Keep these strictly separate.

```
Technical evidence:
- Reduced duplicated code.
- Expanded automated tests.
- Simplified architecture.
- Reduced build time.
- Improved error handling.

Business impact:
- Increased revenue.
- Improved conversion.
- Reduced customer churn.
```

Do not infer business impact from technical changes. If business impact evidence isn't in the repository (e.g. in a linked ticket or PR description), describe the technical impact clearly instead of guessing at a business outcome.

---

## 11. Anti-BS Rules (CV Engine)

All existing [Anti-BS Rules](anti-bs-rules.md) apply. The CV Engine must additionally never invent:

- business impact, revenue, or conversion figures
- user or customer counts
- percentage improvements not backed by a real before/after metric
- performance improvements not backed by a real benchmark
- hours or time saved
- leadership, ownership, or team size not evidenced by the repository
- stakeholder feedback, adoption, or customer satisfaction

Example of a forbidden transformation:

```
Evidence:  Added caching.
Forbidden: "Improved performance by 40%."
```

unless the repository contains a real measurement supporting that number.

---

## 12. Impact Levels and Ranking

Evaluate each candidate contribution as `High`, `Medium`, or `Low` impact, and rank using the same dimensions as [Impact Engine](impact-engine.md):

```
Impact
Evidence Strength
Technical Complexity
Scope
Ownership
Measurability
Relevance
Uniqueness
```

Prioritize High and strong Medium contributions. Do not expose a raw numeric score in the output — use it only to order the bullets.

---

## 13. Role-Focused Modes

Role modes change **emphasis**, not the underlying facts. They never invent new experience.

### `ShipLift CV Senior`

Emphasize evidence of:

- technical ownership
- architecture decisions
- complex problem solving
- reliability and quality work
- cross-cutting improvements
- mentoring-related evidence, only when explicitly supported (e.g. PR review patterns, onboarding docs)
- technical decision-making, only when evidence exists (e.g. RFCs, design docs, architectural PRs)

Do not invent leadership. If no mentoring or decision-making evidence exists, omit those angles rather than implying they happened.

### `ShipLift CV Lead`

Emphasize evidence of:

- technical direction
- architecture
- cross-system impact
- ownership
- engineering standards
- developer experience
- engineering process improvements

Only include leadership or ownership language when the repository evidence supports it (e.g. driving a cross-cutting migration, defining shared patterns adopted elsewhere). Do not automatically convert senior-level engineering work into leadership framing just because the mode was requested.

---

## 14. Company-Level / Career Summary

For long time ranges, identify recurring themes across the whole history and optionally produce a one- or two-sentence career-level summary.

```
Years of work:
Feature delivery, testing, architecture, reliability, CI, developer tooling

Potential summary:
Built and evolved React/TypeScript frontend systems across feature
delivery, architecture, automated testing, reliability, and developer
experience.
```

Only produce this summary when the underlying bullets actually support each clause in it.

---

## 15. Goals Integration

When `ShipLift Goals` data exists, it may be used as **context** to strengthen interpretation of an achievement (e.g. a goal about reliability makes a testing-related story easier to frame).

**Goals are context, not evidence.** Never use the existence of a goal itself as proof that something was accomplished — only repository evidence proves that.

---

## 16. 1:1 Integration

`ShipLift 1:1` may reference career-worthy contributions discovered by the CV engine as additional context. This must not change the existing `ShipLift 1:1` output contract (`What I Delivered / Impact / Challenges / Growth / Next Focus / Topics to Discuss`).

---

## 17. Output Length

Default output: **5–8 strong bullets.**

Do not pad with weak bullets to hit a target count.

```
"Only 4 strong CV contributions were found."
```

is a valid and expected output when evidence is limited — do not manufacture more to reach the range.

---

## 18. Time-Based Analysis

Support:

```
ShipLift CV                  → broadest useful repository history
ShipLift CV 2026             → specified year
ShipLift CV Q1 2026          → specified quarter
ShipLift CV last 2 years     → specified rolling window
ShipLift CV <company>        → scoped to a named project/company context if detectable (e.g. remote name, directory, or monorepo path)
```

See [Commands](commands.md) for the full command contract.

---

## 19. Validation Checklist (CV Engine)

- [ ] Related commits/PRs/achievements are grouped into engineering stories, not listed individually
- [ ] Duplicate or near-duplicate stories are merged
- [ ] Weak-evidence contributions are filtered from the default output
- [ ] Metrics are calculated correctly (test count ≠ coverage; percentage ≠ percentage points)
- [ ] Technical impact is never converted into business impact
- [ ] Leadership/ownership claims only appear with evidence
- [ ] Percentages and other numbers only appear with real before/after evidence
- [ ] Output contains 5–8 strong bullets when evidence supports it, fewer when it doesn't
- [ ] Output states the analysis is repository evidence, not complete employment history
- [ ] Role mode (`Senior` / `Lead`) changes emphasis only, never fabricates new experience

---

## The Principle

> The user should be able to trace every CV bullet back to real, verifiable work in the repository.

Do not make the engineer sound more impressive than the evidence. Make the evidence easier to see.
