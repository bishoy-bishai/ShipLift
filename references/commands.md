# Commands

This document specifies the four core ShipLift commands and their expected behavior.

---

## Command: ShipLift Quarter

### Purpose

Analyze the **current calendar quarter** and identify the strongest achievements.

### Input

- Current repository
- Current calendar quarter
- Full Git history for the quarter

### Output

5–7 achievements (or fewer if only fewer strong achievements exist)

**Important:** Do NOT create 7 achievements just to hit the target.

If the repository only supports 4 meaningful achievements, return 4.

### Focus

- Meaningful engineering impact
- Measurable improvements
- Product value / reliability / quality
- Long-term technical value

**NOT:** Commit count or activity volume

### Process

1. **Analyze** all commits and PRs from the current quarter
2. **Extract** work units using Git Intelligence rules
3. **Build** evidence matrix for each work unit
4. **Cluster** related work into achievements
5. **Rank** achievements using Impact Engine
6. **Select** top 5-7 by score
7. **Generate** final achievements with supporting points

### Example Output

```
## Q3 2024 Achievements

### 1. Payment Flow Reliability & Feature Completion
- Resolved 3 critical issues in payment submission flow
- Implemented payment retry logic and error recovery
- Expanded test coverage by 35% (120 → 162 tests)
- Enabled secure payment processing for 5 new currencies

### 2. Frontend Performance Optimization
- Implemented component memoization reducing re-renders
- Added image lazy loading to product catalog
- Reduced bundle size by 12% (245KB → 215KB)
- Improved initial page load by 34% (3.2s → 2.1s)

### 3. Test Quality & Regression Protection
- Added comprehensive validation tests across form suite
- Increased line coverage from 78% to 84%
- Established pattern for edge case testing
- Strengthened reliability of critical user flows

[... 2-4 more achievements ...]
```

### Validation

- [ ] 5-7 achievements (or fewer if justified)
- [ ] Each has strong evidence
- [ ] Top achievements by impact ranking
- [ ] No invented metrics or claims
- [ ] Clear value proposition for each

---

## Command: ShipLift Standup

### Purpose

Analyze recent repository activity and prepare concise standup update.

### Input

- Current repository
- Last 1-3 weeks of Git history (configurable)
- Branch/PR information

### Output

Concise standup format:

```
Done
Next
Blockers
```

### Important Constraints

**Do NOT invent:**
- Meetings or conversations
- Plans not evidenced by branches/PRs
- Blockers not evidenced by Git or issue tracking
- Work not provable by Git history
- Speculative next steps

Only report what Git can prove.

### Process

1. **Collect** recent commits, PRs, and branches
2. **Group** by work unit (PR, issue, feature branch)
3. **Categorize** as:
   - Merged/completed (Done)
   - In progress (Next)
   - Blocked/waiting (Blockers)
4. **Describe** in natural language
5. **Output** in standup format

### Example Output

```
## Standup Update

**Done:**
- Implemented form validation across 8 components (PR #456)
- Added error handling and retry logic (PR #457)
- Merged payment processing security hardening (PR #458)

**Next:**
- Completing dark mode support (PR #459, 80% done)
- Testing payment flow edge cases
- Addressing code review comments on form validation

**Blockers:**
- Waiting on security team approval for payment API (issue #234)
```

### Validation

- [ ] Only includes merged/completed work
- [ ] In-progress work is from current branches
- [ ] Blockers are documented issues or PRs
- [ ] Nothing is invented
- [ ] Easy to recite in 2-3 minutes

---

## Command: ShipLift 1:1

### Purpose

Prepare comprehensive talking points for a manager 1:1 meeting.

### Input

- Current repository
- Specified time period (default: last month)
- Any linked issues/projects

### Output

Structured 1:1 talking points:

```
What I Delivered
Impact
Challenges
Growth
Next Focus
Topics to Discuss
```

### Focus

Help the engineer communicate:
- What they delivered
- Why it mattered
- How their scope evolved
- Technical challenges faced
- Growth opportunities identified
- Useful discussion topics with manager

### Important Constraints

**Do NOT invent:**
- Promotion readiness
- Stakeholder feedback (without evidence)
- Personal challenges
- Business outcomes
- Leadership claims (without evidence)

Only report what can be proven.

### Process

1. **Analyze** achievements from specified period
2. **Identify** delivery outcomes
3. **Extract** measurable impact
4. **Note** technical challenges faced
5. **Identify** growth areas and learning
6. **Suggest** discussion topics based on evidence
7. **Output** in 1:1 format

### Example Output

```
## 1:1 Talking Points

**What I Delivered:**
- Implemented form validation system across 8 components
- Improved test coverage from 78% to 84%
- Added payment retry and error recovery logic
- Standardized API error handling patterns

**Impact:**
- Payment flow reliability improved (3 critical issues resolved)
- Test suite expanded by 35% (stronger regression protection)
- Reduced validation bugs across the product
- Established reusable error handling patterns

**Challenges:**
- Learned new testing patterns for edge cases
- Balanced feature delivery with test coverage improvement
- Worked through complex async error scenarios
- Coordinated with security team on payment flow changes

**Growth:**
- Deepened expertise in async error handling
- Improved testing strategy and patterns
- Learned payment systems domain
- Strengthened code review skills

**Next Focus:**
- Dark mode feature implementation
- Performance optimization sprint
- Mentoring junior engineer on test patterns

**Topics to Discuss:**
- Am I tracking toward my growth goals?
- Should I take on more architectural decisions?
- Interested in payment systems deeper dive?
- How are my code review comments received?
```

### Validation

- [ ] Each section has concrete evidence
- [ ] No promotion claims without context
- [ ] No invented stakeholder feedback
- [ ] Growth points are genuine
- [ ] Topics are discussion-ready

---

## Command: ShipLift Goals

### Purpose

Evaluate whether the user's professional goals are SMART, map their engineering achievements to those goals, and report evidence, progress, and gaps.

### Input

One of:

- Goals only
- Goals + achievements
- A single goal
- No input (ShipLift proposes Suggested Goals from recent achievements)

### Output

Per goal: SMART score, progress, alignment, supporting achievements, evidence, gaps, and a recommendation. Finished with an "Overall Goal Review" summary.

See [Output Templates](output-templates.md) for the exact format.

### Process

1. **Parse** input mode (goals only / goals+achievements / single goal / none)
2. **If no achievements provided**, reuse the most recent `ShipLift Quarter` output, or run the Quarter pipeline to generate candidates
3. **If no goals provided**, identify recurring themes across achievements and produce 2-4 labeled **Suggested Goals**, then stop and ask for confirmation
4. **Validate** each goal against SMART (Specific, Measurable, Achievable, Relevant, Time-bound), using `✓ / ✗ / ?`
5. **Suggest** an improved goal version when useful (using placeholders for any missing baseline/target, never invented numbers)
6. **Map** each achievement to the goal(s) it supports (Direct / Strong Support / Supporting / Weak / No Clear Alignment)
7. **Collect** evidence per goal (Direct / Supporting / Missing)
8. **Evaluate** progress (Not Started / Early Progress / On Track / Strong Progress / At Risk / Achieved / Unknown) — only calculate a numeric percentage when baseline, target, and current value all exist for the same metric
9. **Assess** goal health (Healthy / Needs Attention / At Risk / Unknown) and identify gaps
10. **Output** in the Goals Review format, finishing with the Overall Goal Review summary

Full rules: [Goals Engine](goals-engine.md)

### Important Constraints

**Do NOT invent:**
- baselines, targets, or deadlines
- progress percentages without a valid baseline/target/current triple
- goal completion or achievement from mere existence of related work
- business outcomes from technical metrics (e.g. test count ≠ coverage)

### Example Output

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
- Frontend Architecture Improvements

### Evidence
✓ +35% test suite growth
✓ Added regression tests for critical flows
⚠ Current coverage percentage is unavailable

### Gaps
- Missing measurable target and deadline

### Recommendation
Add a current coverage baseline and target, plus a deadline, so progress can be measured.

## Overall Goal Review

### Strongest Areas
- Test quality and regression protection

### Goals Needing Attention
- Improve frontend code quality (missing measurable target)

### Missing Evidence
- Current test coverage percentage

### Suggested Focus
- Capture a coverage baseline to make this goal measurable
```

### Validation

- [ ] Every goal has a SMART score with honest `?` where evidence is missing
- [ ] Mappings only exist where evidence supports them
- [ ] Progress percentage only shown with baseline/target/current all present
- [ ] No invented baselines, targets, deadlines, or business outcomes
- [ ] Suggested Goals (when generated) are clearly labeled and require confirmation

---

## Command: ShipLift CV

### Purpose

Analyze the user's broader engineering history and convert it into evidence-backed, CV-ready contribution bullets. Answers: **What did I actually build and accomplish at this company?**

### Input

One of:

```
ShipLift CV
ShipLift CV 2026
ShipLift CV Q1 2026
ShipLift CV last 2 years
ShipLift CV <company>
ShipLift CV Senior
ShipLift CV Lead
```

- With no time period, use the broadest useful repository history (not just the current quarter).
- A year, quarter, or relative range scopes the analysis to that period.
- A company/project name scopes analysis to that project context if detectable.
- `Senior` / `Lead` change emphasis only — see [Career Evidence Engine](career-evidence-engine.md) §13.

### Output

**5–8 strongest contributions** (fewer if evidence doesn't support that many), each a CV-ready bullet, grouped under a "Strongest Contributions" section, plus a "Technical Highlights" summary and optional evidence trace.

### Process

1. **Run** the standard Git Intelligence / Evidence Matrix / Achievement Engine pipeline over the requested time range (reusing the Quarter pipeline, not reimplementing it)
2. **Aggregate** achievements across time into higher-level engineering stories (see [Career Evidence Engine](career-evidence-engine.md) §4)
3. **Rate** each candidate story's evidence strength (Strong / Medium / Weak)
4. **Filter** out Weak-evidence stories from the default output
5. **Rank** remaining stories by impact, evidence strength, complexity, scope, ownership, measurability, relevance, uniqueness
6. **Select** the top 5–8
7. **Generate** CV bullets (Action + Technical Context + Outcome)
8. **Apply** role-mode emphasis if `Senior` or `Lead` was requested
9. **Validate** against Anti-BS Rules and the CV-specific checklist
10. **Output** in the CV Evidence format

### Important Constraints

**Do NOT:**
- generate one bullet per commit
- confuse test count with test coverage
- convert technical impact into business impact
- invent leadership, ownership, or team size
- invent percentages, performance numbers, or business outcomes without evidence
- pad the output with weak bullets to hit 5–8

### Example Output

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
- Improved frontend performance by reducing bundle size by 12%
  and initial load time by 34% through code-splitting and lazy
  loading.

### Technical Highlights

- React / TypeScript
- Testing / Quality
- CI/CD
```

### Validation

See [Career Evidence Engine](career-evidence-engine.md) §19 for the full checklist.

---

## Command Variations

### Variations by Time Period

Each command can accept a time period parameter:

**Quarter:**
```
ShipLift Quarter Q3
ShipLift Quarter Q2 2024
ShipLift Quarter current
```

**Standup:**
```
ShipLift Standup (default: 1 week)
ShipLift Standup 2-weeks
ShipLift Standup 3-days
```

**1:1:**
```
ShipLift 1:1 (default: 1 month)
ShipLift 1:1 3-months
ShipLift 1:1 since-last-1:1
```

**CV:**
```
ShipLift CV (default: broadest useful repository history)
ShipLift CV 2026
ShipLift CV Q1 2026
ShipLift CV last 2 years
ShipLift CV <company>
ShipLift CV Senior
ShipLift CV Lead
```

### Variations by Branch/Project

Commands can be scoped to a branch or project:

```
ShipLift Quarter --branch feature/dark-mode
ShipLift 1:1 --project payment-systems
ShipLift Standup --since PR #456
```

---

## Error Handling

### Insufficient Evidence

If there's not enough data:

```
❌ DON'T: Invent work or speculate
✓ DO: Report what's available with honest assessment

"ShipLift Quarter: Limited activity detected for Q3 2024.
Based on current evidence, only 2 meaningful achievements identified:
1. [Achievement 1]
2. [Achievement 2]"
```

### Empty Repository

```
"No commits detected for the specified period."
```

### No Merged Work

```
"No merged work detected for the specified period.
Current work in progress:
- PR #456: Feature X (80% complete)
- PR #457: Feature Y (20% complete)"
```

---

## Output Format Guidelines

All commands output in Markdown.

### Achievement Format

```
### [Achievement Title]

- [Point 1: Specific action or change with metrics]
- [Point 2: Technical or quality improvement]
- [Point 3 (optional): Value or long-term benefit]
```

### Standup Format

```
## Standup Update

**Done:**
- [Item 1]
- [Item 2]

**Next:**
- [Item 1]
- [Item 2]

**Blockers:**
- [Item 1] (reference issue)
```

### 1:1 Format

```
## 1:1 Talking Points

**What I Delivered:**
- [Delivery 1]

**Impact:**
- [Impact 1]

**Challenges:**
- [Challenge 1]

**Growth:**
- [Growth area 1]

**Next Focus:**
- [Focus 1]

**Topics to Discuss:**
- [Topic 1]
```

---

## Metadata

Each command output should include:

```
Command: ShipLift Quarter
Time Period: Q3 2024 (Jul 1 - Sep 30, 2024)
Repository: [repo name]
Analysis Date: 2024-09-30
Evidence Confidence: High / Medium / Low
```

---

## Command Checklist

For each command execution:

- [ ] Input parameters are valid
- [ ] Time period is specified
- [ ] Repository analysis complete
- [ ] Evidence matrix built
- [ ] Work properly clustered
- [ ] Achievements ranked by impact
- [ ] Final selection made (5-7 for Quarter, etc.)
- [ ] Output generated in correct format
- [ ] No invented claims
- [ ] Metadata included
