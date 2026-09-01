# Output Templates

This document provides templates for generating ShipLift output.

---

## Quarter Achievement Template

### Basic Structure

```
### [Outcome-Oriented Title]

- [Point 1: Action + Measurable Result]
- [Point 2: Quality or Technical Improvement]
- [Point 3 (optional): Long-term Value or Broader Impact]
```

### Full Example

```
### Dark Mode Support with Accessibility

- Implemented theme switching using CSS variables for maintainability
- Added comprehensive theme persistence across 8 components (24 new tests)
- Enabled high-contrast mode and ARIA live regions for accessibility
```

### Title Formula

```
[Primary Outcome] + [Secondary Value]
```

**Examples:**
- `Feature Delivery & Reliability`
- `Performance Optimization & Bundle Reduction`
- `Test Quality & Regression Protection`
- `API Simplification & Developer Experience`
- `Security Hardening & Compliance`

---

## Standup Update Template

```
## Standup Update

**Done:**
- [Item 1 with PR reference]
- [Item 2 with PR reference]
- [Item 3 with PR reference]

**Next:**
- [In-progress item 1 with percentage complete]
- [In-progress item 2]
- [Upcoming item]

**Blockers:**
- [Blocker 1 with issue reference]
```

### Metadata

Add at the top:

```
**Week of:** [Date]
**Analyzed:** [Date]
```

---

## 1:1 Talking Points Template

### Full Structure

```
## 1:1 Talking Points

**What I Delivered:**
- [Delivery 1: Feature or improvement]
- [Delivery 2: Feature or improvement]
- [Delivery 3: Technical work]

**Impact:**
- [Impact statement 1 with measurement]
- [Impact statement 2 with measurement]
- [Impact statement 3: Long-term value]

**Challenges:**
- [Challenge 1: What was difficult?]
- [Challenge 2: How did you learn?]
- [Challenge 3: Skill developed?]

**Growth:**
- [Growth area 1: Skill, expertise, or scope]
- [Growth area 2: Technical depth]
- [Growth area 3: Leadership or collaboration]

**Next Focus:**
- [Next focus area 1]
- [Next focus area 2]
- [Next focus area 3]

**Topics to Discuss:**
- [Discussion topic 1]
- [Discussion topic 2]
- [Discussion topic 3]
```

### Metadata

Add at the top:

```
**Period:** [Date Range]
**Prepared:** [Date]
**Main Achievements:** [Number of significant deliverables]
```

---

## Goals Review Template

### Full Structure

```
# 🎯 Goals Review

## Goal 1 — [Goal]

### SMART Score
X/5

Specific       ✓ / ✗ / ?
Measurable     ✓ / ✗ / ?
Achievable     ✓ / ✗ / ?
Relevant       ✓ / ✗ / ?
Time-bound     ✓ / ✗ / ?

### Progress
[Not Started / Early Progress / On Track / Strong Progress / At Risk / Achieved / Unknown]

### Goal Alignment
[Direct / Strong Support / Supporting / Weak / No Clear Alignment]

### Supporting Achievements
- [Achievement A]
- [Achievement B]

### Evidence
- ✓ [Direct or supporting evidence]
- ⚠ [Missing evidence]

### Gaps
- [Missing information: baseline, target, deadline, etc.]

### Recommendation
[Short, useful, evidence-grounded recommendation]
```

Repeat the `## Goal N` block for each goal, then finish with:

```
## Overall Goal Review

### Strongest Areas
- [Goal or theme with the strongest evidence]

### Goals Needing Attention
- [Goal with low SMART score or weak evidence]

### Missing Evidence
- [Evidence gaps across goals]

### Suggested Focus
- [Where to focus next, grounded in gaps above]
```

### Suggested Goals Template (No Goals Provided)

```
Based on your recent work, I found [N] recurring themes:

1. [Theme 1]
2. [Theme 2]
3. [Theme 3]

Suggested Goals:

1. [Suggested goal 1]
2. [Suggested goal 2]
3. [Suggested goal 3]

These are suggestions, not confirmed goals.
```

### Metadata

Add at the top when useful:

```
**Goals Analyzed:** [Number]
**Achievements Considered:** [Number, with source: provided / ShipLift Quarter]
```

---

## CV Evidence Template

### Full Structure

```
# 📄 CV Evidence

## [Role / Company]

### Strongest Contributions

- [CV bullet: Action + Technical Context + Outcome]
- [CV bullet]
- [CV bullet]
- [CV bullet]
- [CV bullet]

### Technical Highlights

- [Technology or theme actually supported by evidence]
- [Technology or theme]
- [Technology or theme]
```

Optionally follow with an evidence-trace section so the user can validate each bullet:

```
## Evidence Behind the Bullets

### Bullet 1
Evidence:
- [Supporting fact 1]
- [Supporting fact 2]
- [Supporting fact 3]

Strength:
[Strong Evidence / Medium Evidence]

Metric:
[Metric, if any — e.g. "+35% test suite growth"]
```

### Metadata

Add at the top when useful:

```
**Period Analyzed:** [Date range, or "Full available history"]
**Repository:** [Repo name]
**Note:** This reflects repository evidence only, not complete employment history.
```

### Insufficient Evidence

```
Only 4 strong CV contributions were found. Additional smaller
changes exist but do not have enough evidence to support a
CV-ready bullet.
```

See [Career Evidence Engine](career-evidence-engine.md) for the full aggregation, evidence-strength, and anti-BS rules behind this output.

---

## Pulse Summary Template

### Full Structure

```
📝 Pulse captured

🤝 Collaboration
[Plain factual restatement of what the user said]

👀 Code Review
[Plain factual restatement, with count if given]

🔍 Investigation
[Plain factual restatement]

🚀 Initiative
[Plain factual restatement]
```

Use one emoji-labeled block per category actually captured — omit categories with nothing to report. Suggested emoji per category:

```
🤝 Collaboration            🧑‍🏫 Mentoring
👀 Code Review              🧭 Technical Decision
🔍 Investigation            🚀 Initiative
🚨 Incident Response        📄 Documentation
📚 Knowledge Sharing        🗓️ Planning
💬 Communication            🧩 Problem Solving
🔓 Unblocking                🔧 Process Improvement
📌 Other
```

After the summary, always ask:

```
Anything else?
```

Then close with one of:

```
Pulse saved.
```

```
No additional evidence captured.
```

### No Evidence Example

```
No additional evidence captured.
```

This is a complete, valid Pulse output when the user answered "nothing" or "not sure" throughout — do not manufacture evidence to avoid this outcome.

### Duplicate Prompt Example

```
This looks similar to an existing entry:
"Helped Ahmed fix a React rendering issue." (2026-08-31)

Add as a new contribution or update the existing one?
```

### Metadata

Add at the top when useful:

```
**Work Date:** [Date]
**Captured:** [Date]
**Company:** [Company/project]
```

See [Pulse Engine](pulse-engine.md) for the full evidence model, question flow, and anti-BS rules behind this output.

---

## Common Patterns for Points

### Measuring Implementation

**Pattern:**
```
[Action] + [Scope] + [Metric]
```

**Examples:**
```
- Implemented form validation across 8 components (added 24 tests)
- Refactored state management in UserProfile component
- Added error handling for 5 critical API failure scenarios
- Standardized logging pattern across backend services
```

---

### Measuring Performance

**Pattern:**
```
[Action] + [Before/After] + [Percentage or Absolute]
```

**Examples:**
```
- Reduced load time from 3.2s to 2.1s (34% improvement)
- Decreased bundle size by 45KB (12% reduction)
- Improved test execution time from 8 minutes to 3 minutes
- Optimized query by 60% through indexed column addition
```

---

### Measuring Quality/Coverage

**Pattern:**
```
[Action] + [Quantitative Change] + [Scope]
```

**Examples:**
```
- Increased test coverage from 72% to 84% (12 percentage points)
- Expanded test suite by 35% (120 → 162 tests)
- Resolved 3 critical bugs in payment flow
- Fixed all 12 accessibility warnings in form components
```

---

### Measuring Risk Reduction

**Pattern:**
```
[Problem Prevented] + [Scope/Evidence]
```

**Examples:**
```
- Prevented N+1 query vulnerability in user list endpoint
- Eliminated duplicate submission edge case
- Protected against XSS vulnerability in comment rendering
- Prevented data loss in form abandonment scenario
```

---

### Measuring Process Improvement

**Pattern:**
```
[Improvement] + [Impact] + [Scope]
```

**Examples:**
```
- Automated CI caching reducing build time by 40%
- Standardized test setup reducing flakiness by 60%
- Documented API integration patterns for new developers
- Created reusable component library reducing duplication
```

---

## Metric Formatting

### Test Count
```
"Expanded test suite by 35% (120 → 162 tests)"
```

### Coverage
```
"Increased line coverage from 72% to 84% (+12 percentage points)"
```

### Performance
```
"Improved load time from 3.2s to 2.1s (34% faster)"
```

### Bundle Size
```
"Reduced bundle by 45KB (12% reduction)"
```

### File/Component Count
```
"Updated 12 components to use new validation pattern"
```

---

## Standup Point Examples

### Done Examples

**Feature-based:**
```
- Merged payment retry logic (PR #456)
- Completed form validation across 8 components (PR #457)
```

**Bug fix-based:**
```
- Fixed authentication edge case causing logouts (PR #458)
- Resolved 2 critical bugs in payment flow (PR #459, #460)
```

**Quality-based:**
```
- Added 35 new tests improving coverage to 84% (PR #461)
- Reviewed and approved PRs from team members (5 PRs)
```

---

### Next Examples

**Feature-based:**
```
- Implementing dark mode support (PR #462, 60% complete)
- Testing payment flow edge cases
```

**Bug-based:**
```
- Investigating form submission timeout issue
- Triaging support reports from this week
```

**Process-based:**
```
- Responding to code review comments on PR #456
- Updating API documentation
```

---

### Blocker Examples

**Waiting on approval:**
```
- Security team approval for payment API changes (issue #234)
- Product feedback on dark mode design (waiting since Mon)
```

**Waiting on dependency:**
```
- Blocked on backend API completion for dashboard (PR #500)
- Waiting for design team mockups for mobile flow
```

**Technical blocker:**
```
- Investigating flaky test in payment flow (3 failures this week)
- Performance regression in dashboard loading
```

---

## 1:1 Section Examples

### "What I Delivered" Examples

```
- Implemented settings page UI with full API integration
- Improved test coverage from 78% to 84%
- Refactored UserProfile component for maintainability
- Added error handling for payment flow edge cases
- Mentored new junior engineer on testing patterns
```

---

### "Impact" Examples

```
- Payment flow reliability improved through bug fixes and better error handling
- Test suite expansion (42 new tests) strengthens regression protection
- Settings page enables user customization (customer requested)
- New error handling pattern reduces developer friction
- Mentoring contributed to team's test quality improvements
```

---

### "Challenges" Examples

```
- Learned async/await error handling patterns for payment scenarios
- Balanced feature delivery with test coverage improvement
- Worked through complex race condition in form submission
- Coordinated with security team on data validation requirements
- Improved communication through code review processes
```

---

### "Growth" Examples

```
- Deepened expertise in payment systems architecture
- Improved testing strategy and edge case identification
- Developed stronger code review and communication skills
- Expanded knowledge of accessibility requirements (WCAG)
- Took on mentorship responsibilities with junior team member
```

---

### "Next Focus" Examples

```
- Dark mode implementation for feature parity
- Performance optimization sprint (targeting 20% improvement)
- Architectural improvements to API layer
- Deeper dive into GraphQL for future migration
- Expanding mentorship to 2nd junior engineer
```

---

### "Topics to Discuss" Examples

```
- Am I tracking toward my growth goals in [area]?
- Should I take on more architectural decisions in [domain]?
- Interested in [technology/domain] deeper dive opportunities?
- How is my impact on team testing practices perceived?
- Ready for more mentorship/leadership responsibilities?
- Are there areas where I should improve communication?
```

---

## Anti-Patterns to Avoid

### ❌ Vague Language

```
❌ "Made improvements"
✓ "Improved load time from 3.2s to 2.1s"

❌ "Fixed several bugs"
✓ "Resolved 3 related bugs in payment submission flow"

❌ "Worked on testing"
✓ "Added 24 tests expanding coverage from 72% to 84%"
```

### ❌ Exaggerated Claims

```
❌ "Transformed the codebase"
✓ "Refactored state management improving clarity"

❌ "Major breakthrough"
✓ "Identified and fixed N+1 query reducing queries by 60%"

❌ "Game-changing feature"
✓ "Implemented dark mode support (customer requested)"
```

### ❌ Unsupported Attribution

```
❌ "Increased user satisfaction"
✓ "Implemented feature requested in support tickets"

❌ "Improved conversion rates"
✓ "Reduced form friction by simplifying validation"

❌ "Led the team effort"
✓ "Contributed to team's test coverage improvements"
```

### ❌ Missing Context

```
❌ "Added 50 lines of code"
✓ "Added 50 lines of test code covering edge cases"

❌ "Updated dependencies"
✓ "Updated critical security dependencies (patching CVE-2024-1234)"

❌ "Fixed bug"
✓ "Fixed race condition in async payment flow preventing duplicate submissions"
```

---

## Template Checklist

For Quarter achievements:

- [ ] Title is outcome-oriented
- [ ] 2-4 supporting points
- [ ] Each point has specific evidence
- [ ] Metrics are calculated correctly
- [ ] No exaggerated language
- [ ] Clear value proposition

For Standup:

- [ ] Done items are merged/complete
- [ ] Next items reference PRs or branches
- [ ] Blockers reference issues
- [ ] Easy to say in 2-3 minutes
- [ ] Nothing invented

For 1:1:

- [ ] Delivery items are specific
- [ ] Impact has supporting evidence
- [ ] Challenges show learning
- [ ] Growth is genuine
- [ ] Topics are discussion-ready
- [ ] Nothing invented or exaggerated
