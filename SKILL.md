# ShipLift: Transform Engineering Work into Meaningful Achievements

**ShipLift** analyzes a software repository and converts engineering work into meaningful achievements. The goal is not to summarize commits—it's to understand what you shipped, determine why it matters, and communicate it clearly.

## What is ShipLift?

ShipLift bridges the gap between raw engineering activity and meaningful communication. It operates at one or two levels above implementation, while remaining completely truthful and evidence-driven.

```
Repository
    ↓
Repository Analysis
    ↓
Git Intelligence
    ↓
Evidence Matrix
    ↓
Impact Engine
    ↓
Achievement Ranking
    ↓
Achievement Generator
    ↓
Command Output
```

## Supported Commands

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

---

## How to Use ShipLift in a Coding Agent

1. **Invoke** the skill with a command: `ShipLift Quarter`, `ShipLift Standup`, or `ShipLift 1:1`
2. **Analyze** the repository using the Git Intelligence rules
3. **Build** an evidence matrix of changes
4. **Group** related work using clustering rules
5. **Rank** candidate achievements
6. **Generate** final achievements with supporting points
7. **Output** in the specified format for the command

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
│   └── output-templates.md
└── scripts/
    └── git-analysis.sh
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
