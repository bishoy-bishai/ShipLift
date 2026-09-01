# ShipLift Skill

**Transform engineering work into meaningful achievements.**

ShipLift analyzes your repository and converts raw engineering activity into clear, evidence-backed achievements. The goal is not to summarize commits—it's to understand what you shipped, why it matters, and communicate it clearly.

---

## Quick Start

### For Claude Code / OpenAI Codex Users

1. Copy the `shiplift/` directory to your skills directory
2. Use one of the commands:
   - `ShipLift Quarter` - Analyze current quarter (5-7 achievements)
   - `ShipLift Goals` - Map achievements to your professional goals
   - `ShipLift Standup` - Prepare standup update
   - `ShipLift 1:1` - Prepare manager 1:1 talking points
   - `ShipLift CV` - Turn your engineering history into CV-ready bullets

### Example Usage

```
ShipLift Quarter

ShipLift Goals

ShipLift Standup 2-weeks

ShipLift 1:1 3-months

ShipLift CV

ShipLift CV Senior
```

---

## What ShipLift Does

### The Pipeline

```
Repository
    ↓
Repository Analysis (Git history, diffs, PRs)
    ↓
Git Intelligence (Grouping related commits)
    ↓
Evidence Matrix (Gathering proof)
    ↓
Impact Engine (Ranking by value)
    ↓
Achievement Ranking (Prioritizing top achievements)
    ↓
Achievement Generator (Creating output)
    ↓
Command Output (Standup, 1:1, or Quarter)
```

### Key Philosophy

> **Make the value of the work clearer, not bigger.**

Every claim must be backed by evidence. Every metric must be calculated correctly. Every achievement must communicate impact, not activity.

---

## Commands

### ShipLift Quarter

Analyze the **current calendar quarter** and return 5–7 of your strongest achievements.

**Output includes:**
- Meaningful engineering impact
- Measurable improvements
- Product/reliability/quality value
- Long-term technical value

**Example:**

```
## Q3 2024 Achievements

### 1. Payment Flow Reliability & Feature Completion
- Implemented retry logic preventing duplicate charges
- Resolved 3 critical bugs in payment submission
- Expanded test coverage by 35% (120 → 162 tests)

### 2. Frontend Performance Optimization
- Reduced bundle size by 12% (245KB → 215KB)
- Improved load time from 3.2s to 2.1s (34% faster)
- Implemented lazy loading for product catalog

[... 3-5 more achievements ...]
```

### ShipLift Standup

Analyze recent activity and prepare concise standup update.

**Output format:**

```
## Standup Update

**Done:**
- Merged payment retry logic (PR #456)
- Completed form validation across 8 components (PR #457)

**Next:**
- Implementing dark mode support (60% complete)
- Testing edge cases in payment flow

**Blockers:**
- Waiting on security approval for API changes
```

### ShipLift Goals

Answers: **How did my work move my goals, and how much progress can I prove?**

Builds on `ShipLift Quarter` achievements and evaluates whether your goals are SMART, maps achievements to them, and reports evidence, progress, and gaps.

```
Achievements
     ↓
Goals
     ↓
SMART validation
     ↓
Goal alignment
     ↓
Evidence
     ↓
Progress
```

If you don't provide goals, ShipLift analyzes recent achievements, identifies recurring themes, and proposes **Suggested Goals** for you to confirm — it never invents official goals on your behalf.

**Example:**

```
ShipLift Goals

Goals:
1. Improve frontend code quality.

Achievements:
1. Test Quality & Regression Protection
```

```
# 🎯 Goals Review

## Goal 1 — Improve frontend code quality

### SMART Score
3/5

Specific       ✓
Measurable     ✗
Achievable     ?
Relevant       ✓
Time-bound     ✗

### Progress
Supporting evidence found (coverage progress: Unknown)

### Goal Alignment
Strong

### Supporting Achievements
- Test Quality & Regression Protection

### Evidence
✓ +35% test suite growth
⚠ Current coverage percentage is unavailable

### Gaps
- Missing measurable target and deadline

### Recommendation
Add a current coverage baseline, target, and deadline so progress can be measured.
```

See [references/goals-engine.md](references/goals-engine.md) for the full SMART validation, mapping, and progress rules.

### ShipLift 1:1

Prepare comprehensive talking points for a manager 1:1.

**Output includes:**
- What I Delivered
- Impact
- Challenges
- Growth
- Next Focus
- Topics to Discuss

**Example:**

```
## 1:1 Talking Points

**What I Delivered:**
- Settings page with API integration
- Improved test coverage from 78% to 84%

**Impact:**
- Enabled user customization feature
- Strengthened regression protection

**Challenges:**
- Learned async error handling patterns
- Coordinated with security team

**Growth:**
- Deepened payment systems expertise
- Improved testing strategy

**Next Focus:**
- Dark mode implementation
- Performance optimization sprint

**Topics to Discuss:**
- Ready for architectural decisions?
- Interested in [domain] deeper dive?
```

### ShipLift CV

Answers: **What did I actually build and accomplish at this company?**

ShipLift can analyze your engineering history and turn meaningful work into evidence-based CV bullets. Unlike the other commands, it looks across months or years rather than a single quarter. It:

- groups related commits into engineering stories
- identifies your most meaningful engineering contributions
- extracts measurable evidence (never confusing test count with coverage)
- highlights technical impact without inventing business impact
- avoids invented claims about leadership, ownership, or performance
- produces 5–8 CV-ready bullets, or fewer when evidence doesn't support more

Supports time scoping (`ShipLift CV 2026`, `ShipLift CV Q1 2026`, `ShipLift CV last 2 years`) and role-focused emphasis (`ShipLift CV Senior`, `ShipLift CV Lead`), which change what's emphasized, never what's invented.

**Example:**

```
ShipLift CV
```

```
# 📄 CV Evidence

## Frontend Engineer — shiplift-web

### Strongest Contributions

- Strengthened frontend regression protection by expanding the
  automated test suite by 35% (120 → 162 tests) and improving
  coverage of critical validation and edge-case scenarios.
- Simplified shared frontend architecture by consolidating
  reusable components and reducing duplicated implementation
  across multiple product flows.

### Technical Highlights

- React / TypeScript
- Testing / Quality
- CI/CD
```

See [references/career-evidence-engine.md](references/career-evidence-engine.md) for the full aggregation, evidence-strength, and anti-BS rules.

---

## Architecture

### Directory Structure

```
shiplift/
├── SKILL.md                          (Primary entry point)
├── README.md                         (This file)
├── VALIDATION.md                     (Acceptance criteria)
├── references/
│   ├── achievement-framework.md      (Grouping & clustering rules)
│   ├── commands.md                   (Command specifications)
│   ├── evidence-matrix.md            (Evidence hierarchy)
│   ├── impact-engine.md              (Ranking framework)
│   ├── intelligence-rules.md         (Work pattern recognition)
│   ├── anti-bs-rules.md              (Mandatory guardrails)
│   ├── metrics.md                    (Metric calculation)
│   ├── output-templates.md           (Output formatting)
│   ├── goals-engine.md               (SMART goals, mapping, progress)
│   └── career-evidence-engine.md     (CV aggregation, evidence strength, role modes)
└── scripts/
    └── git-analysis.sh               (Helper script)
```

### Core Components

#### 1. Achievement Framework
Defines how to recognize and group related work into coherent achievements.

**Key concepts:**
- Feature + tests + validation = ONE achievement
- Related commits = ONE story
- Test-only work = standalone only if broad
- Refactor + feature = group together

#### 2. Evidence Matrix
Establishes evidence hierarchy from strongest to weakest.

**Priority order:**
1. Direct measurement (metrics, benchmarks)
2. Actual code/diff
3. PR/Issue context
4. Commit message
5. Inference

#### 3. Intelligence Rules
Patterns for recognizing different types of work and grouping them appropriately.

**Patterns covered:**
- Feature + Quality
- Test-only work
- Refactor + Feature
- Bug clustering
- Performance clustering
- CI/Developer Experience

#### 4. Impact Engine
Ranking framework to prioritize achievements by value.

**Scoring dimensions:**
- Scope (breadth of impact)
- Complexity (difficulty)
- Impact (value created)
- Measurability (quantifiable?)
- Long-term value (lasting benefit?)
- Product relevance (alignment?)
- Evidence confidence (how sure?)

#### 5. Anti-BS Rules
Mandatory guardrails preventing overstatement.

**Forbidden:**
- Inventing percentages
- Inventing business impact
- Inventing customer impact
- Inventing hours saved
- Inventing leadership
- Unsourced stakeholder feedback

#### 6. Metrics
Precise rules for calculating and presenting metrics.

**Covered:**
- Percentage change formulas
- Percentage vs. percentage points
- Test metrics (count, coverage, pass rate)
- Performance metrics (load time, bundle size)
- Code metrics (files, lines)

#### 7. Commands
Specification for each of the four commands.

**Includes:**
- Input requirements
- Process steps
- Output format
- Validation rules

#### 8. Goals Engine
Rules for SMART goal validation, achievement-to-goal mapping, evidence, progress, and gaps behind `ShipLift Goals`.

#### 9. Career Evidence Engine
Rules for aggregating achievements across months/years into engineering stories, rating evidence strength, and role-focused emphasis (`Senior` / `Lead`) behind `ShipLift CV`.

#### 10. Output Templates
Templates and examples for generating achievement text.

**Includes:**
- Title formulas
- Point patterns
- Metric formatting
- Common examples

### Helper Script

**`scripts/git-analysis.sh`**

Provides repository snapshots to assist analysis:

```bash
./git-analysis.sh status              # Repository status
./git-analysis.sh log 7               # Last 7 days
./git-analysis.sh quarter 2024-Q3     # Specific quarter
./git-analysis.sh branches            # Recent branches
./git-analysis.sh stats               # Repo statistics
./git-analysis.sh diff HEAD~1 HEAD    # Compare commits
```

---

## How ShipLift Works

### Step 1: Repository Analysis

ShipLift gathers:
- Git log and commit history
- Pull requests and issues
- File changes and diffs
- Test changes and coverage
- Build/CI information

### Step 2: Git Intelligence

ShipLift groups related commits:
- Same PR = likely one feature
- Same issue = likely related work
- Same component = may be same story
- Overlapping files = likely connected
- Same time period = may be coordinated

### Step 3: Evidence Matrix

ShipLift validates each claim:
- Direct measurements first
- Actual code changes second
- PR context third
- Commit messages last
- Never rely on inference alone

### Step 4: Achievement Clustering

ShipLift identifies higher-level stories:
- Feature + tests + validation = ONE achievement
- Bug fixes in same flow = ONE reliability story
- Performance improvements in same area = ONE performance story
- Developer tooling improvements = ONE DX story

### Step 5: Impact Ranking

ShipLift scores achievements:
- Scope: How broad?
- Complexity: How difficult?
- Impact: How valuable?
- Measurability: How provable?
- Long-term value: Does it enable future work?
- Product relevance: Aligned with strategy?
- Evidence confidence: How certain?

### Step 6: Achievement Generation

ShipLift creates final output:
- Outcome-oriented titles
- 2-4 supporting points
- Correct metric calculations
- Clear, simple language
- Evidence-backed claims

### Step 7: Output Formatting

ShipLift presents results:
- Markdown format
- Appropriate for the command
- Ranked by impact
- Ready to share

---

## Core Principles

### 1. Evidence First

Every claim is backed by repository evidence. Never invent.

### 2. Impact Over Activity

Focus on what matters, not how much was done.

### 3. Truth in Simplicity

Communicate in simple language without exaggeration.

### 4. Measurability

Use metrics when available, but don't invent them.

### 5. Appropriate Grouping

Related work tells one story, not seven.

### 6. No BS

The Anti-BS Rules are mandatory and enforced.

---

## The Difference: Engineering Impact vs. Commit Summary

### Commit Summary Approach
```
"I made 8 commits this week"
"Fixed bug, added feature, improved tests"
"Worked on authentication and performance"
```

**Problem:** Focuses on activity, not impact.

### ShipLift Engineering Impact Approach
```
Settings Experience Delivery & Reliability

- Implemented settings page with API integration and full validation
- Added comprehensive error handling for API failures
- Wrote tests covering main flows and edge cases (12 new tests)

Frontend Performance Optimization

- Reduced bundle size by 12% (245KB → 215KB)
- Improved load time from 3.2s to 2.1s (34% faster)
```

**Benefit:** Communicates what you actually shipped and why it mattered.

---

## Installation

ShipLift follows the **Agent Skills** standard structure and can be installed into any supported coding agent.

### For Claude Code

1. Clone or download this repository: `https://github.com/bishoy-bishai/ShipLift`
2. Locate your Claude Code skills directory:
   - Run: `Claude: Show Skills Directory` in your command palette
   - Or check: `~/.claude/skills/`
3. Copy the repository folder to your skills directory
4. Restart Claude Code
5. Use commands like: `ShipLift Quarter`

**Official Reference:** [Claude Code Skills](https://claude.ai/docs/skills)

### For OpenAI Codex

1. Clone this repository: `https://github.com/bishoy-bishai/ShipLift`
2. Locate your Codex plugins directory (configuration depends on your setup)
3. Copy the repository folder to your plugins directory
4. Register the skill with Codex using your tool's registration method
5. Use commands like: `ShipLift Quarter`

**Official Reference:** Check your OpenAI Codex documentation for skill/plugin installation

### For Cursor

1. Clone this repository: `https://github.com/bishoy-bishai/ShipLift`
2. Locate your Cursor skills directory:
   - Typically: `~/.cursor/skills/` or check Cursor settings
3. Copy the repository folder to your skills directory
4. Restart Cursor
5. Use commands like: `ShipLift Quarter`

**Official Reference:** [Cursor Skills Documentation](https://docs.cursor.com)

### For Google Antigravity

1. Clone this repository: `https://github.com/bishoy-bishai/ShipLift`
2. Follow your Antigravity agent setup for importing skills
3. Point Antigravity to the ShipLift repository location
4. Register the skill with your Antigravity configuration
5. Use commands like: `ShipLift Quarter`

**Official Reference:** Google Antigravity documentation (consult official Google AI agent docs)

### Manual Usage (No Coding Agent)

You can use ShipLift manually without an agent:

1. Read [SKILL.md](SKILL.md) for the framework
2. Analyze your repository against the rules in `references/`
3. Group your work using [intelligence-rules.md](references/intelligence-rules.md)
4. Rank using the [impact-engine.md](references/impact-engine.md)
5. Generate achievements using [output-templates.md](references/output-templates.md)
6. Validate against [VALIDATION.md](VALIDATION.md)

---

## Manual Usage

---

## Validation

ShipLift has been validated against 12 acceptance tests covering:

- ✅ Evidence hierarchy enforcement
- ✅ No invented metrics
- ✅ No invented business impact
- ✅ Proper language standards
- ✅ Correct grouping patterns
- ✅ Impact-focused output
- ✅ Metric accuracy
- ✅ Appropriate achievement counts
- ✅ Proper standup formatting
- ✅ Evidence confidence assessment
- ✅ Title quality standards
- ✅ No padding to hit targets

See `VALIDATION.md` for full test suite.

---

## When to Use ShipLift

### Perfect For

- ✅ Quarterly review of your accomplishments
- ✅ Preparing for performance reviews
- ✅ Updating your resume or portfolio
- ✅ Preparing manager 1:1 talking points
- ✅ Understanding what you actually accomplished
- ✅ Communicating impact to non-technical stakeholders

### Not Ideal For

- ❌ Commit history (use `git log` instead)
- ❌ Code review (use GitHub/GitLab)
- ❌ Time tracking (use time tracking tools)
- ❌ Task management (use project management tools)

---

## Support & Questions

### Understanding the Rules

1. Read `SKILL.md` for overview
2. Study `references/` files relevant to your question
3. Check `VALIDATION.md` for examples
4. Review `output-templates.md` for formatting

### Troubleshooting

**Issue: ShipLift seems to be missing work**

→ Verify work is:
- Merged to main branch
- Has supporting commits
- Has PR/issue context
- Has evidence in diffs

**Issue: Achievement seems overblown**

→ Review `anti-bs-rules.md` and reduce claims.

**Issue: Metrics don't seem right**

→ Verify calculations in `metrics.md`.

---

## Files Overview

| File | Purpose |
|------|---------|
| SKILL.md | High-level overview (start here) |
| README.md | This file - installation and usage |
| VALIDATION.md | Acceptance criteria and test suite |
| achievement-framework.md | How to group and cluster work |
| commands.md | Command specifications |
| evidence-matrix.md | Evidence hierarchy and validation |
| impact-engine.md | Ranking and prioritization framework |
| intelligence-rules.md | Work pattern recognition |
| anti-bs-rules.md | Mandatory guardrails |
| metrics.md | Metric calculations |
| output-templates.md | Output formatting |
| goals-engine.md | SMART goals, mapping, progress |
| career-evidence-engine.md | CV aggregation, evidence strength, role modes |
| git-analysis.sh | Repository snapshot helper |

---

## The Final Principle

> **Do not make the work sound bigger. Make the value of the work clearer.**

Every achievement should answer: **Why did this work matter?**

---

## License & Attribution

ShipLift is an AI agent skill designed for use with coding agents like Claude Code and OpenAI Codex.

Designed by engineering leaders who believe that engineering impact should be clear, honest, and evidence-driven.

---

## Questions?

If you have questions about how ShipLift works:

1. Check the relevant `references/` file
2. Review examples in `output-templates.md`
3. Test against cases in `VALIDATION.md`
4. Refer back to `SKILL.md` for principles

The documentation is comprehensive. If something seems unclear, the answer is usually in one of the reference files.
