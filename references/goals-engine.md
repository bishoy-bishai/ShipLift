# Goals Engine

The Goals Engine converts engineering achievements into meaningful professional goals, and evaluates whether goals are clear, measurable, realistic, relevant, and time-bound.

It answers four questions:

1. What am I trying to achieve?
2. How will I know I'm making progress?
3. How does my engineering work support the goal?
4. Can I prove the progress?

The goal is not to create impressive-sounding goals. The goal is to create **clear goals that can be supported by real evidence**.

This file contains the detailed rules for the `ShipLift Goals` command. See [Commands](commands.md) for the command contract and [Output Templates](output-templates.md) for the exact output format.

---

## 1. Core Model

```
Goal
  ↓
Success Measure (Milestone)
  ↓
Achievements
  ↓
Evidence
```

Example:

```
Goal:
Improve frontend code quality.

Success Measure:
Increase automated test coverage from 72% to 85%.

Achievement:
Expanded the automated test suite by 35%.

Evidence:
120 → 162 tests
```

**Important:** An achievement can support a goal without proving the goal was achieved. Alignment ≠ completion.

### Internal Goal Model

Each goal is internally represented as:

```
Goal
Category
Description
Baseline
Target
Current Value
Metric
Deadline
SMART Score
Achievements
Evidence
Progress
Health
Gaps
Confidence
```

Only expose the fields that are useful in the output — do not dump the raw internal model at the user.

### Goal Categories

Recognize (but don't force) these categories:

```
Quality
Reliability
Performance
Delivery
Developer Experience
Architecture
Technical Debt
Security
Accessibility
Product Impact
```

If a goal doesn't clearly fit a category, leave it uncategorized rather than guessing.

### Goal Lifecycle

```
Draft → Active → On Track / At Risk → Achieved / Completed
```

Never claim a goal is "Achieved" or "Completed" just because related work exists — completion requires evidence that the success criteria were actually met.

---

## 2. Command Input Modes

`ShipLift Goals` supports four input shapes:

### Mode A — Goals only

```
ShipLift Goals

Goals:
1. Improve frontend code quality.
2. Increase delivery efficiency.
3. Improve product reliability.
```

Validate and analyze the goals. If no achievements are supplied, inspect the repository (reusing the Quarter Engine) to find supporting evidence.

### Mode B — Goals + Achievements

```
ShipLift Goals

Goals:
1. Improve frontend code quality.
2. Improve product reliability.

Achievements:
1. Test Quality & Regression Protection
2. Feature Delivery & Reliability
3. Frontend Architecture Improvements
```

Map the supplied achievements to the supplied goals. Prefer these achievements over re-deriving new ones.

### Mode C — Single Goal

```
ShipLift Goals

Goal:
Improve frontend code quality.
```

Analyze this one goal independently, following the same SMART + mapping + evidence process.

### Mode D — No Goals Provided

```
ShipLift Goals
```

Do **not** invent official goals. Instead:

1. Run (or reuse) the Quarter achievement analysis.
2. Identify recurring engineering themes across achievements.
3. Generate a small number (2–4) of **Suggested Goals**.
4. Label them clearly as suggestions.
5. Ask the user to confirm or edit them.

Example:

```
Based on your recent work, I found three recurring themes:

1. Code quality
2. Reliability
3. Developer experience

Suggested Goals:

1. Improve frontend quality and reliability across critical
   user flows.

2. Improve frontend maintainability by simplifying shared
   architecture.

3. Reduce development friction through better tooling and CI.

These are suggestions, not confirmed goals.
```

Never present generated goals as goals the user officially owns until they confirm.

---

## 3. SMART Validation

Every goal is evaluated against five dimensions:

```
S — Specific
M — Measurable
A — Achievable
R — Relevant
T — Time-bound
```

Each dimension is scored `✓` (met), `✗` (not met), or `?` (not enough evidence to judge). Uncertainty is not a failure — use `?` honestly rather than forcing a verdict.

Report:

```
SMART Score: X/5

Specific       ✓ / ✗ / ?
Measurable     ✓ / ✗ / ?
Achievable     ✓ / ✗ / ?
Relevant       ✓ / ✗ / ?
Time-bound     ✓ / ✗ / ?
```

### S — Specific

The goal must state what should improve, which area is affected, and what outcome is expected.

```
Bad:     Improve code quality.
Better:  Improve frontend code quality by strengthening automated
         testing for critical user flows.
```

Do not silently rewrite the user's goal — first explain what's missing, then optionally offer an improved version (see §5).

### M — Measurable

Look for a baseline, a target, and a measurable success criterion.

```
Measurable:     Increase test coverage from 72% to 85%.
Not Measurable: Improve testing.
```

If a baseline or target is missing, say so. **Never invent one.**

### A — Achievable

Assess using available evidence: timeframe, scope, baseline, target, complexity, current achievements, repository evidence, and the user's apparent responsibility.

Use one of:

```
Likely achievable
Potentially ambitious
Cannot assess
```

Never make a definitive achievability claim when important context is missing.

### R — Relevant

Determine whether the goal relates to the user's role, current engineering responsibilities, current work, or team/product priorities (when known). Do not assume ownership.

If responsibility is unclear:

```
Relevance: Unclear
```

### T — Time-bound

Look for an explicit timeframe (e.g. "by the end of Q4", "by December 31", "within the next quarter").

If none exists:

```
Time-bound: ✗
```

Do not invent a deadline.

---

## 4. Goal Improvement

After SMART validation, offer an improved version when useful.

```
Current:
Improve code quality.

Suggested:
Increase automated test coverage for critical frontend
user flows from [current baseline] to [target] by the
end of Q4.
```

If the repository doesn't provide a baseline or target, use an explicit placeholder like `[current baseline]` / `[target]`. **Never invent real-looking numbers** (e.g. do not fabricate `72%` or `85%`).

A high-quality goal ideally contains:

```
Outcome + Metric + Baseline + Target + Timeframe
```

---

## 5. Achievement → Goal Mapping

For every achievement, determine whether it supports one or more goals.

Relationship types:

```
Direct
Strong Support
Supporting
Weak
No Clear Alignment
```

Example:

```
Goal:        Improve frontend code quality.
Achievement: Test Quality & Regression Protection
Evidence:    +35% test suite growth
Alignment:   Strong Support
```

### One Achievement, Multiple Goals

An achievement may support more than one goal — do not force a single mapping.

```
Achievement: Improved CI test execution time by 40%.

Goal 1: Improve developer experience.
Goal 2: Increase delivery efficiency.
```

Only create a mapping when evidence supports it. Do not create weak mappings just to increase goal coverage.

---

## 6. Evidence

Every goal should have an evidence list, classified as:

```
Direct Evidence
Supporting Evidence
Missing Evidence
```

Example:

```
Goal: Improve frontend code quality.

Evidence:
✓ Automated test suite increased by 35%.
✓ Added regression tests for critical flows.
✓ Improved validation coverage.

⚠ Current coverage percentage is unavailable.
```

### Critical Metric Rule (inherited from [Metrics](metrics.md))

Never confuse related but different metrics:

```
120 tests → 162 tests   =  +35% test suite growth   (NOT test coverage)
72% → 84% coverage      =  +12 percentage points      (NOT +12%)
```

All existing ShipLift metric validation and anti-BS rules apply unchanged inside the Goals Engine.

---

## 7. Goal Progress

Supported statuses:

```
Not Started
Early Progress
On Track
Strong Progress
At Risk
Achieved
Unknown
```

Progress must be evidence-based.

### Critical Progress Rule

An achievement supporting a goal does **not** automatically mean the goal is achieved, or that progress has a specific percentage.

```
Goal:        Increase test coverage from 72% to 85%.
Achievement: Expanded test suite by 35%.

Correct:
  Goal Alignment: Strong
  Progress: Supporting evidence found
  Coverage Progress: Unknown

Incorrect:
  Goal Progress: 35%
```

### Measurable Goal Progress

Only calculate a numeric progress percentage when **all** of the following hold:

- Baseline exists
- Target exists
- Current value exists
- All three values represent the same metric
- The direction of improvement is known

Formula for a straightforward increasing metric:

```
Progress = (Current - Baseline) / (Target - Baseline)
```

Example:

```
Baseline: 70%
Target:   85%
Current:  80%

Progress = (80 - 70) / (85 - 70) = 66.7%
```

Otherwise, use a qualitative progress status instead of a percentage.

---

## 8. Goal Health

```
Healthy
Needs Attention
At Risk
Unknown
```

Health should consider progress, evidence, deadline, target, recent achievements, and missing information. Do not claim a goal is "At Risk" solely because there are few commits — that alone is not evidence of risk.

---

## 9. Goal Gaps

Identify missing evidence and missing goal components.

```
Goal Quality: 3/5

Missing:
- measurable target
- deadline

Progress:
Supporting evidence exists, but progress cannot be quantified.
```

For goals with no meaningful achievement support:

```
No strong repository evidence found for this goal.
```

Do not manufacture evidence to fill a gap.

---

## 10. Goal Suggestions

When generating suggested goals from achievements (Mode D), look for recurring patterns.

```
Achievements:
- Test Quality & Regression Protection
- Reliability Improvements
- Frontend Architecture Simplification
- CI Improvements

Suggested Goals:
1. Improve frontend quality and reliability across critical user flows.
2. Improve frontend maintainability by simplifying shared architecture.
3. Reduce development friction through better CI and tooling.
```

Always label these `Suggested Goal` until the user confirms them.

---

## 11. Output Format

See [Output Templates](output-templates.md) for the exact `ShipLift Goals` output template (per-goal SMART score, progress, alignment, evidence, gaps, recommendation) and the closing "Overall Goal Review" summary.

---

## 12. Integration with ShipLift Quarter

The Goals Engine reuses the existing Quarter Engine — it does not duplicate achievement generation.

```
ShipLift Quarter
       ↓
Achievements
       ↓
ShipLift Goals
       ↓
Goal Mapping
```

If achievements from a recent `ShipLift Quarter` run are already available, use them directly. Otherwise, `ShipLift Goals` may inspect the repository itself and generate the achievement candidates it needs (via the same Git Intelligence / Evidence Matrix / Impact Engine pipeline).

---

## 13. Integration with ShipLift 1:1

When goals are available, `ShipLift 1:1` may reference:

- strongest goal progress
- achievements supporting goals
- goals needing attention
- missing evidence
- suggested next focus

This is additive context only — it must not change or break the existing `ShipLift 1:1` output contract (`What I Delivered / Impact / Challenges / Growth / Next Focus / Topics to Discuss`).

---

## 14. Language Rules

Use simple English, the same tone as the rest of ShipLift.

**Avoid:** strategic alignment optimization, cross-functional synergy, organizational transformation.

**Prefer:** Strong alignment, Good progress, More evidence is needed, The goal needs a measurable target.

The output should sound like a senior engineer talking to their manager.

---

## 15. Anti-BS Rules (Goals Engine)

All existing ShipLift [Anti-BS Rules](anti-bs-rules.md) apply. The Goals Engine must additionally never:

- invent a baseline
- invent a target
- invent a deadline
- invent business outcomes
- invent progress percentages without a valid baseline/target/current triple
- claim goal completion without evidence
- claim ownership without evidence
- convert technical metrics into business metrics
- turn test count into coverage
- turn achievement existence into goal completion

When information is unavailable, say `Unknown` or `More evidence needed` — never fill the gap with a plausible-sounding guess.

---

## 16. Evidence Sources: Git + Pulse Together

`ShipLift Goals` must use both evidence sources, combined through the shared [Evidence Engine](core/evidence-engine.md) — never analyzed in isolation when the other is available:

```
Git Evidence
     +
Pulse Memory
     ↓
Evidence Engine
     ↓
Pattern Detection
     ↓
Goal Signals / Goal Mapping
```

Pulse Memory (the same EvidenceStore behind `ShipLift Pulse`, read via `pulse-store.sh`) is a first-class evidence source for Goals — not just for Standup. It contributes to goal discovery, existing-goal evidence, and progress the same way Git evidence does.

```
Existing goal:  Improve frontend code quality.

Evidence:
- Git:   Added automated tests, +35% coverage
- Git:   Added ESLint architectural rules
- Pulse: Reviewed 3 PRs, found a validation issue
- Pulse: Helped a teammate debug a testing pattern
```

Both sources go through the same clustering, [evidence-strength](core/evidence-strength.md), and [anti-inflation](core/anti-inflation.md) rules — Pulse evidence gets no special treatment or extra credibility, and neither does Git.

---

## 17. Existing Goals First

Before suggesting anything new, check whether recorded evidence already supports one of the user's existing goals. Use `evidence-engine.sh match-goal --company ID --goal "<goal text>"` — it scores recorded evidence (Git + Pulse) against the goal's own wording by keyword overlap, so relevant evidence surfaces without guessing at a semantic match.

```
Existing Goal → Evidence Engine match → Link Evidence → Estimate Progress
```

If matching evidence exists, attach it to the existing goal (§5, §6) — do not create a duplicate goal that says roughly the same thing.

---

## 18. Reverse Achievement → Goal Mapping

`ShipLift Goals` must also work backwards: given achievements (from `ShipLift Quarter`) and Pulse Memory, what goal do they indicate?

```
Achievements + Pulse Memory + Repository Evidence
                    ↓
        Potential Goals
```

Do **not** convert each achievement into its own goal. Instead:

```
5 Achievements
      ↓
Group by intent
      ↓
Find recurring patterns
      ↓
Identify the common engineering objective
      ↓
Suggest 2-4 meaningful goals
```

Example:

```
Achievements:
- Server-First Component Architecture
- BFF / API Client Modernization
- Reliability & Correctness Fixes
- Test Coverage Improvements

→ One goal, not four:
  Improve frontend architecture, reliability, and maintainability.
```

Prefer fewer, stronger goals over one goal per achievement — only split into separate goals when the evidence clearly indicates independent objectives (e.g. a testing-focused body of work and a completely unrelated incident-response body of work).

This grouping is the agent's judgment call, using the same [Achievement Framework](achievement-framework.md) clustering logic already used elsewhere in ShipLift — it is not a second, parallel grouping system.

---

## 19. Pulse-Derived Goal Signals

Some goals are visible only in Pulse Memory — Git never sees them. Use `evidence-engine.sh goal-signals --company ID` to detect recurring *themes* across evidence descriptions, independent of category (see [Signal Detection](core/signal-detection.md) for the category-based version; goal signals cluster by shared keywords instead, since a theme like "AI-generated code" can appear across Code Review, Investigation, and Problem Solving evidence alike).

```
Pulse:  Reviewed AI-generated code.
Pulse:  Fixed issues in AI-generated implementation.
Pulse:  Improved AI-generated code quality.
Pulse:  Created better validation around AI-generated code.
Pulse:  Helped teammates review AI-generated changes.

→ Goal Signal: Improve AI-generated code quality.
```

When the agent turns a detected signal into a Suggested Goal, mark its source:

```
Source: Pulse-derived Goal Signal
```

when the signal is primarily Pulse evidence, or a combined source when Git evidence contributed too. The signal itself (`goal-signals` output: theme keywords, occurrences, sources, categories, item ids) is raw material — the agent still writes the actual goal wording; the engine never phrases a goal on its own.

### Signal Confidence (repetition thresholds)

Reusing [Evidence Strength](core/evidence-strength.md)'s building blocks (measurable metric, multi-source, repetition) rather than a second scoring system:

```
1 mention                                    → Weak Signal
2-3 related mentions, single source, no metric → Emerging Signal
3+ mentions AND (multiple sources OR a metric) → Strong Goal Signal
```

Never create a strong goal from one weak signal, and never call repeated Pulse mentions alone (no repository evidence, no metric) a Strong Goal Signal — that combination stays Emerging/Moderate until Git evidence or a real metric corroborates it.

---

## 20. Never Invent Goals

Do not create goals just because they sound good for a software engineer. Forbidden without evidence:

```
Become a technical leader.
Improve communication.
Become better at mentoring.
Increase business impact.
Lead cross-functional initiatives.
```

If evidence is insufficient for a suggested-goal candidate:

```
No strong goal signal detected.
```

is a valid, complete result — not a failure to fix by lowering the bar.

---

## 21. Goal Hierarchy

Do not confuse these levels — a goal must sit above an achievement, not restate a task:

```
Task              → Add ESLint rule
Activity          → (the raw commit/PR/Pulse entry)
Achievement       → Established architectural enforcement for Client Components
Goal              → Improve frontend architecture and maintainability
Career Direction  → Technical leadership / architecture (only with real evidence)
```

```
Achievement: Added 18 regression tests.
Goal:        Improve automated test coverage and regression protection.
NOT a goal:  Add 18 regression tests.        (that's the achievement, restated)
```

---

## 22. Output Structure

`ShipLift Goals` produces up to four sections — only include a section when it has real content (e.g. skip "Suggested Goals" entirely if none clear the evidence bar):

1. **Existing Goal Progress** — for each existing goal with supporting evidence: progress, supporting achievements, Pulse evidence, code evidence, gaps (uses §17 matching plus the existing §7-§9 progress/health/gap rules).
2. **Suggested Goals** — new goals detected via reverse mapping (§18) or Pulse-derived signals (§19) strong enough to propose, each with: goal title, a SMART-checked goal statement, why it was detected, supporting achievements/Pulse evidence/code evidence, evidence strength, confidence, and missing information. Always labeled as suggestions requiring confirmation (§2 Mode D).
3. **Goal Signals** — emerging patterns not yet strong enough to suggest as a goal (§19's Emerging Signal tier), shown so the user can see what ShipLift is starting to notice.
4. **Evidence Gaps** — what's missing to make a goal (existing or suggested) more measurable, e.g. "strong evidence of improving AI-generated code, but no measurable quality metric yet."

See [Output Templates](output-templates.md) for the exact formatting of each section.

---

## The Principle

> A good goal is not a sentence that sounds ambitious. It is a measurable outcome that can be proven.

The complete loop:

```
Goal → SMART Validation → Success Criteria → Achievements → Evidence → Progress → Gaps → Next Focus
```

Do not make the user's progress sound bigger. Make the evidence behind the progress clearer.
