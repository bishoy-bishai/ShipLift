---
name: shiplift
description: Analyze a software repository and turn shipped engineering work into clear, evidence-based achievements, standup updates, and manager 1:1 talking points.
---

# ShipLift: Transform Engineering Work into Meaningful Achievements

**ShipLift** analyzes a software repository and converts engineering work into meaningful achievements. The goal is not to summarize commits—it's to understand what you shipped, determine why it matters, and communicate it clearly.

## What is ShipLift?

ShipLift bridges the gap between raw engineering activity and meaningful communication. It operates at one or two levels above implementation, while remaining completely truthful and evidence-driven.

```
Repository                    ShipLift Pulse (adaptive Q&A)
    ↓                                 ↓
Git Evidence                  Human Evidence
    └───────────────┬─────────────────┘
                     ↓
              EVIDENCE ENGINE
        (linking · strength · signals)
                     ↓
              Impact Analysis
                     ↓
             Anti-Inflation Layer
                     ↓
            Achievement Ranking
                     ↓
           Achievement Generator
                     ↓
              Command Output
                     ↓
(optional) Goals Engine → ShipLift Goals
```

Git and Pulse are both first-class evidence sources feeding one shared Evidence Engine — see [Evidence Engine](references/core/evidence-engine.md). Commands are interfaces; the Evidence Engine is the brain behind all of them.

## Supported Commands

### ShipLift Pulse

Answers: **What did I contribute that Git cannot see?**

Pulse is the **Human Work Evidence Engine**. It runs a short, adaptive Q&A (30–90 seconds) to capture collaboration, mentoring, code review, technical decisions, investigations, initiatives, and unblocking — the meaningful work that never becomes a commit.

```
What did you work on yesterday?
      ↓
Adaptive follow-up questions
      ↓
Raw Evidence (facts, not achievements)
      ↓
Stored locally, isolated by company
```

Pulse captures facts, not achievements. `Impact: Unknown` unless the user gave real evidence of outcome. Feeds Standup, Quarter, Goals, CV, and 1:1 as a second evidence source alongside Git — it is never a separate silo.

**Do not invent:**
- impact, percentages, or outcomes the user didn't state
- categories or metrics beyond what was said
- achievements — that's the Achievement Engine's job, not Pulse's

Full rules: [Pulse Engine](references/pulse-engine.md)

---

### ShipLift Quarter
Analyze the current calendar quarter. Returns the strongest **5–7 achievements** (or fewer if only fewer meaningful achievements exist).

**Focus on:**
- Meaningful engineering impact
- Measurable improvements
- Product/reliability/quality value
- Long-term technical value

**Not:** commit count

---

### ShipLift Standup
Analyze recent repository activity. Returns concise:
```
Done
Next
Blockers
```

**Do not invent:**
- meetings
- conversations
- blockers
- plans
- work that Git cannot prove

---

### ShipLift 1:1
Prepare talking points for a manager 1:1. Returns:

```
What I Delivered
Impact
Challenges
Growth
Next Focus
Topics to Discuss
```

**Do not invent:**
- promotion readiness
- stakeholder feedback
- personal challenges
- business outcomes
- leadership/ownership claims
(unless supported by evidence)

---

### ShipLift Goals

Answers: **How do my achievements support my professional goals, and how much progress can I prove?** — and, in reverse: **What goals does my work already indicate?**

Builds on `ShipLift Quarter` achievements (reused, not regenerated) and Pulse Memory (a first-class evidence source here too, not just for Standup). Evaluates goals for SMART quality, maps achievements to goals, gathers evidence from Git and Pulse together, and reports progress and gaps.

```
ShipLift Quarter                    Pulse Memory
      ↓                                  ↓
5–7 Achievements ──────────┬────────────┘
                            ↓
                     ShipLift Goals
                            ↓
  Existing-Goal Matching → Reverse Mapping → SMART Validation
                            ↓
        Evidence → Progress → Gaps → Recommendations
```

Supports goals-only, goals+achievements, a single goal, or no goals at all (in which case ShipLift checks existing goals for supporting evidence first, then runs **Reverse Achievement → Goal Mapping** and Pulse-derived goal-signal detection to propose **Suggested Goals** — grouped into a few strong goals, not one per achievement — and asks for confirmation; it never invents official goals on the user's behalf).

**Do not invent:**
- baselines, targets, or deadlines
- progress percentages without a valid baseline/target/current triple
- goal completion without evidence
- business outcomes from technical metrics (e.g. test count ≠ coverage)

Full rules: [Goals Engine](references/goals-engine.md)

---

### ShipLift CV

Answers: **What did I actually build and accomplish at this company?**

Analyzes the user's broader engineering history (not just the current quarter) and turns it into evidence-backed, CV-ready contribution bullets. Reuses the same Git Intelligence / Evidence Matrix / Achievement Engine pipeline as `ShipLift Quarter`, then aggregates achievements across time into higher-level engineering stories.

```
Repository
      ↓
Git History (months / years)
      ↓
Achievements (via Quarter pipeline, reused)
      ↓
Career Evidence Engine
      ↓
5–8 Strongest Contributions
      ↓
CV Bullets
```

Supports time scoping (`ShipLift CV 2026`, `ShipLift CV Q1 2026`, `ShipLift CV last 2 years`) and role-focused emphasis (`ShipLift CV Senior`, `ShipLift CV Lead`) — role modes change emphasis only, never invent experience.

**Do not invent:**
- business impact, revenue, or customer numbers
- leadership, ownership, or team size without evidence
- percentages or performance numbers without a real before/after metric
- business impact from technical metrics

Full rules: [Career Evidence Engine](references/career-evidence-engine.md)

---

## Core Philosophy

The most important principle in ShipLift:

> **Do not make the work sound bigger. Make the value of the work clearer.**

### The Intelligence Loop

```
What bigger engineering story do these changes tell together?
                ↓
What evidence proves that story?
                ↓
Is the impact measurable?
                ↓
Can I explain it simply?
                ↓
Achievement
```

---

## Achievement Design

Every meaningful achievement must contain:

```
Title
+
2–4 Points
```

### Titles (Outcome-Oriented)

**Good examples:**
- Test Quality & Regression Protection
- Frontend Performance Improvements
- Simplified Frontend Architecture
- Feature Delivery & Reliability
- Developer Experience Improvements

**Bad examples:**
- Added Tests
- Changed React Components
- Fixed Some Bugs
- Various Refactoring

### Format

Each achievement should follow this pattern:

```
Title

- Point 1: Concrete action or change with metrics
- Point 2: Technical or quality improvement
- Point 3 (optional): Value or long-term benefit
```

---

## Language

Use simple, clear English suitable for a senior engineer and non-technical managers.

**Prefer:**
> Made the code easier to maintain.

**Not:**
> Introduced a compositional abstraction to decouple implementation concerns.

**Prefer:**
> Reduced unnecessary renders by 25%.

**Not:**
> Optimized the rendering pipeline through advanced memoization strategies.

**Avoid corporate buzzwords:**
- leveraged
- synergized
- revolutionized
- drove excellence
- best-in-class
- robust paradigm

---

## Key Rules

See detailed documentation in the `references/` folder:

- [Achievement Framework](references/achievement-framework.md) — Grouping and clustering rules
- [Evidence Matrix](references/evidence-matrix.md) — Evidence priority and validation
- [Intelligence Rules](references/intelligence-rules.md) — Patterns for different types of work
- [Metrics](references/metrics.md) — Correct metric calculation
- [Impact Engine](references/impact-engine.md) — Impact ranking and prioritization
- [Anti-BS Rules](references/anti-bs-rules.md) — Mandatory guardrails
- [Commands](references/commands.md) — Detailed command specifications
- [Output Templates](references/output-templates.md) — Command output formats
- [Goals Engine](references/goals-engine.md) — SMART goals, achievement mapping, progress, and gaps for `ShipLift Goals`
- [Career Evidence Engine](references/career-evidence-engine.md) — Career aggregation, evidence strength, and role modes for `ShipLift CV`
- [Pulse Engine](references/pulse-engine.md) — Evidence model, question flow, and storage rules for `ShipLift Pulse`
- [Evidence Engine](references/core/evidence-engine.md) — The shared intelligence layer behind every command:
  - [Evidence Linking](references/core/evidence-linking.md)
  - [Evidence Strength](references/core/evidence-strength.md)
  - [Impact Analysis](references/core/impact-analysis.md)
  - [Signal Detection](references/core/signal-detection.md)
  - [Blind Spots](references/core/blind-spots.md)
  - [Anti-Inflation](references/core/anti-inflation.md)
  - [Writing Constitution](references/core/writing-constitution.md)

---

## How to Use ShipLift in a Coding Agent

1. **Invoke** the skill with a command: `ShipLift Pulse`, `ShipLift Quarter`, `ShipLift Standup`, `ShipLift 1:1`, `ShipLift Goals`, or `ShipLift CV`
2. **Analyze** the repository using the Git Intelligence rules
3. **Build** an evidence matrix of changes
4. **Group** related work using clustering rules
5. **Rank** candidate achievements
6. **Generate** final achievements with supporting points
7. **Output** in the specified format for the command

---

## Agent Analysis Workflow

When you receive a ShipLift command, follow this process:

### 1. Detect and Validate Repository

- Detect the current repository location
- Identify the repository name and git URL
- Confirm access to git history and diffs
- Detect the current branch and default branch

### 2. Parse Command and Time Period

**ShipLift Quarter:**
- Determine current calendar quarter (or parse specified quarter)
- Set start date (e.g., 2024-Q3 = Jul 1 - Sep 30)
- Set end date (e.g., 2024-Q3 = Sep 30)

**ShipLift Standup:**
- Parse time period (default: 1 week)
- Set start date (e.g., 1-week-ago)
- Set end date (now)

**ShipLift 1:1:**
- Parse time period (default: 1 month)
- Set start date (e.g., 1-month-ago)
- Set end date (now)

**ShipLift CV:**
- Default: broadest useful repository history (not just the current quarter)
- Or parse specified period (year, quarter, "last N years") or company/project scope
- Note role mode if specified (`Senior` / `Lead`) — affects emphasis only

### 3. Gather Repository Evidence

Inspect (in priority order):

1. **Git History**
   - `git log` with the specified date range
   - Commit messages and authors
   - Commit timestamps

2. **Git Diffs**
   - `git diff` between relevant commits
   - Files changed, lines added/removed
   - Specific code changes

3. **Pull Requests/Issues** (if available)
   - PR titles and descriptions
   - Issue descriptions and linked PRs
   - Review comments and approvals

4. **Test Information** (if available)
   - Test file changes
   - Coverage reports or metrics
   - New tests added

5. **Build/CI Information** (if available)
   - CI logs and build times
   - Performance benchmark results
   - Deployment information

### 4. Build Evidence Matrix

For each group of related commits:

- **Direct Measurement:** Performance metrics, test counts, coverage percentages
- **Code Diffs:** Files changed, implementation details
- **PR Context:** Description, linked issues, review comments
- **Commit Messages:** Descriptions (as hints only)

**Never use inference alone.** Always ground claims in evidence from above.

### 5. Apply Git Intelligence Rules

Group related commits using:

- **Same PR:** Likely one feature
- **Same Issue:** Likely related work
- **Same Branch:** May be one feature/fix
- **Overlapping Files:** May be coordinated
- **Same Time Period:** May be related
- **Same Component:** May tell one story

Recognized patterns:
- Feature + Tests + Validation = ONE achievement
- Refactor + Feature (if enables feature) = ONE achievement
- Related bugs in same flow = ONE reliability story
- Related performance changes = ONE performance story
- Developer tooling improvements = ONE DX story

### 6. Rank Candidate Achievements

Score each achievement on 7 dimensions (0-10 scale):

1. **Scope:** Breadth of impact
2. **Complexity:** Difficulty to implement
3. **Impact:** Value created
4. **Measurability:** How quantifiable
5. **Long-term Value:** Enables future work
6. **Product Relevance:** Alignment with strategy
7. **Evidence Confidence:** How certain

**Quarter output:** Select top 5-7 achievements by score (or fewer if only fewer have strong evidence)

**Standup output:** Sort by recency and status (Done/Next/Blockers)

**1:1 output:** Use highest-scoring achievements plus learning/growth

**CV output:** Aggregate achievements across the full period into engineering stories (see [Career Evidence Engine](references/career-evidence-engine.md) §4), rate evidence strength, filter out Weak evidence, then select top 5-8 by score

### 7. Generate Final Achievements

For each achievement:

```
[Outcome-Oriented Title]

- Point 1: Specific action with metric (if applicable)
- Point 2: Technical or quality improvement
- Point 3 (optional): Value or long-term benefit
```

**Rules:**
- Title must describe the outcome, not activity
- Each point must have evidence
- Metrics must be calculated correctly
- Language must be simple and clear
- No corporate buzzwords
- No invented claims

### 8. Validate Against Anti-BS Rules

Before outputting, verify:

- ✅ No invented percentages
- ✅ No invented business impact
- ✅ No invented customer impact
- ✅ No invented hours saved
- ✅ No invented leadership
- ✅ Accurate attribution
- ✅ No unsourced stakeholder feedback

If uncertain about a claim, remove it or rephrase with evidence.

### 9. Format and Output

**Quarter output:**
```
# Q[quarter] [year] — Key Achievements

## 1. [Title]
- Point
- Point
- Point

## 2. [Title]
...

[5-7 total]
```

**Standup output:**
```
### Done
- Item with PR/issue reference

### Next
- Item with status/percentage

### Blockers
- Item with issue reference
```

**1:1 output:**
```
# 1:1 — Key Talking Points

### What I Delivered
- ...

### Impact
- ...

### Challenges
- ...

### Growth
- ...

### Next Focus
- ...

### Topics to Discuss
- ...
```

**Goals output:** see [Output Templates](references/output-templates.md) and [Goals Engine](references/goals-engine.md) for the full `ShipLift Goals` process (SMART validation, achievement mapping, evidence, progress, gaps, recommendations).

**CV output:** see [Output Templates](references/output-templates.md) and [Career Evidence Engine](references/career-evidence-engine.md) for the full `ShipLift CV` process (aggregation, evidence strength, role modes).

---

## Implementation Details

### Platform Compatibility
- Works with repositories in any language or framework
- Detects environment instead of assuming structure
- Compatible with any test framework, CI system, or package manager

### Helper Tools
- Git analysis script for repository snapshots
- Evidence collection from diffs, PRs, issues, and tests
- Metrics calculation engine

### Validation
See `VALIDATION.md` for acceptance criteria and test cases.

---

## Files in This Skill

```
shiplift/
├── SKILL.md                          (this file)
├── VALIDATION.md                     (acceptance criteria)
├── references/
│   ├── achievement-framework.md
│   ├── commands.md
│   ├── evidence-matrix.md
│   ├── impact-engine.md
│   ├── intelligence-rules.md
│   ├── anti-bs-rules.md
│   ├── metrics.md
│   ├── output-templates.md
│   ├── goals-engine.md
│   ├── career-evidence-engine.md
│   ├── pulse-engine.md
│   └── core/
│       ├── evidence-engine.md
│       ├── evidence-linking.md
│       ├── evidence-strength.md
│       ├── impact-analysis.md
│       ├── signal-detection.md
│       ├── blind-spots.md
│       ├── anti-inflation.md
│       └── writing-constitution.md
└── scripts/
    ├── git-analysis.sh
    ├── pulse-store.sh
    ├── pulse_store.py
    ├── evidence-engine.sh
    └── evidence_engine.py
```

---

## Getting Started

1. Read this `SKILL.md` for the high-level overview
2. Review `references/evidence-matrix.md` to understand evidence priorities
3. Study `references/intelligence-rules.md` to learn work grouping patterns
4. Follow `references/commands.md` for command-specific behavior
5. Use `references/output-templates.md` as formatting reference
6. Check `VALIDATION.md` to understand acceptance criteria

---

## The Final Principle

> Make the value of the work clearer, not bigger.

Every achievement should answer: **Why did this work matter?**

The full ShipLift command set:

```
🚀 ShipLift

ShipLift Pulse     — "What did I contribute that Git can't see?"
ShipLift Quarter   — "What did I accomplish?"
ShipLift Goals     — "How did my work move my goals?"
ShipLift Standup   — "What do I say today?"
ShipLift 1:1       — "What should I discuss with my manager?"
ShipLift CV        — "What did I actually build and accomplish at this company?"
```
