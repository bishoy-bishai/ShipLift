# ShipLift Skill

**Transform engineering work into meaningful achievements.**

ShipLift analyzes your repository and converts raw engineering activity into clear, evidence-backed achievements. The goal is not to summarize commits—it's to understand what you shipped, why it matters, and communicate it clearly.

---

## Quick Start

### For Claude Code / OpenAI Codex Users

1. Copy the `shiplift/` directory to your skills directory
2. Use one of the three commands:
   - `ShipLift Quarter` - Analyze current quarter (5-7 achievements)
   - `ShipLift Standup` - Prepare standup update
   - `ShipLift 1:1` - Prepare manager 1:1 talking points

### Example Usage

```
ShipLift Quarter

ShipLift Standup 2-weeks

ShipLift 1:1 3-months
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
│   └── output-templates.md           (Output formatting)
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
Specification for each of the three commands.

**Includes:**
- Input requirements
- Process steps
- Output format
- Validation rules

#### 8. Output Templates
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

## Installation

### For Claude Code

1. Locate your skills directory (ask Claude or check settings)
2. Clone or copy the `shiplift/` directory there
3. Restart Claude Code
4. Use commands like: `ShipLift Quarter`

### For OpenAI Codex / Other Coding Agents

1. Locate your skills/plugins directory
2. Copy `shiplift/` directory there
3. Follow your agent's skill registration process
4. Invoke with appropriate syntax for your agent

### Manual Usage

You can also use this skill manually:

1. Read `SKILL.md` for overview
2. Read `references/` files for detailed rules
3. Analyze a repository against these rules
4. Generate achievements following the patterns
5. Validate against `VALIDATION.md`

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

## Example: Before and After

### Raw Git Activity

```
Commits:
1. Add settings page UI
2. Connect settings API
3. Add form validation
4. Add error handling
5. Add tests for settings
6. Fix edge case bug
7. Update documentation
8. Refactor component state
```

### Without ShipLift

```
"I made 8 commits this week and updated settings features."
```

### With ShipLift

```
Settings Experience Delivery & Reliability

- Implemented settings page with API integration and full validation
- Added comprehensive error handling for API failures
- Wrote tests covering main flows and edge cases (12 new tests)
- Resolved edge case in settings persistence
- Refactored component state for improved maintainability
```

---

## Key Differences from Commit Summaries

### Commit Summary

```
"Fixed bug, added feature, improved tests"
```

### ShipLift Achievement

```
"Feature Delivery & Quality Improvements
- Implemented requested feature with validation
- Resolved 2 related bugs in the flow
- Expanded test coverage (120 → 162 tests)"
```

**ShipLift differs by:**
- ✅ Grouping related work
- ✅ Highlighting value, not activity
- ✅ Using evidence-backed metrics
- ✅ Telling a coherent story
- ✅ Focusing on impact

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
