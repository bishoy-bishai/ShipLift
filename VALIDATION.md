# VALIDATION

This document defines acceptance criteria and validation tests for the ShipLift skill.

---

## Validation Principles

ShipLift must:

1. ✅ **Be truthful** - Never invent claims
2. ✅ **Be evidence-driven** - Every claim has proof
3. ✅ **Be meaningful** - Focus on impact, not activity
4. ✅ **Be proportional** - Match claim to evidence strength
5. ✅ **Be clear** - Communicate to non-engineers
6. ✅ **Be measurable** - Quantify when possible
7. ✅ **Be actionable** - Help engineer understand value

---

## Acceptance Criteria

### Criterion 1: Evidence Hierarchy

**Pass if:**
- Direct measurements are used when available
- Strong evidence (diffs, PRs) is used when measurements unavailable
- Weak evidence (commit messages) is used only as hints
- Inference is avoided when stronger evidence exists

**Fail if:**
- Commitment messages override code evidence
- Inference is presented as fact
- Weak evidence supports strong claims

---

### Criterion 2: No Invented Metrics

**Pass if:**
- Every percentage has calculation shown
- Before/after values are documented
- Sources of data are identifiable
- Math is correct

**Fail if:**
- Percentage is claimed without before/after
- Calculation is wrong
- Source is unclear
- Metric is estimated

---

### Criterion 3: No Invented Business Impact

**Pass if:**
- Technical claims match technical evidence
- Business claims have business evidence
- Causal links are documented
- Extrapolation is avoided

**Fail if:**
- "Improved performance" becomes "improved revenue"
- "Added tests" becomes "improved user satisfaction"
- "Fixed bug" becomes "increased customer retention"
- Causal links are assumed

---

### Criterion 4: Proper Language

**Pass if:**
- Claims are simple and clear
- No corporate buzzwords
- "Added" not "developed"
- Accurate attribution

**Fail if:**
- Buzzwords like "leveraged", "synergized"
- Vague language like "improved things"
- Inaccurate attribution of work

---

### Criterion 5: Appropriate Grouping

**Pass if:**
- Related commits are grouped
- Different stories are separated
- Feature + tests = one achievement
- Refactor + feature properly grouped

**Fail if:**
- One-liner achievements for each commit
- Unrelated work is clustered
- Feature and tests are separated
- Tests are counted as separate achievements

---

### Criterion 6: Impact Focus

**Pass if:**
- Achievements prioritize impact
- Measurable improvements highlighted
- Value is clear
- Activity is contextualized

**Fail if:**
- Commit count is prominent
- Activity volume emphasized
- Value is unclear
- Focus is on hours/effort

---

### Criterion 7: Correct Metrics

**Pass if:**
- Percentages are calculated correctly
- Percentage vs. percentage points are distinct
- Multipliers are accurate
- Rounding is reasonable

**Fail if:**
- Math is wrong
- Percentage/points are confused
- Rounding obscures meaning
- Metrics don't match evidence

---

## Test Cases

### Test 1: Commit Count Doesn't Become Activity Achievement

**Scenario:**
```
Repository activity:
- 24 commits over 3 weeks
- 30 files changed
- 340 lines added
```

**Fail condition:**
```
Achievement: "Delivered 24 commits across 30 files"
(Activity count, not meaningful impact)
```

**Pass condition:**
```
Inspect actual work:
- 8 commits adding tests (35% increase in test count)
- 12 commits for feature X
- 4 commits for bug fixes

Output: Cluster by work type, not by commit count
```

---

### Test 2: Test-Only Work Is Properly Handled

**Scenario:**
```
Repository activity:
- 120 existing tests
- 42 new tests added
- Coverage: 78% → 84%
- 3 bug fixes
- 1 refactor
- 1 feature
- 8 commits total
```

**Fail condition:**
```
Achievements:
1. Added tests
2. Added 42 tests
3. Fixed bug #1
4. Fixed bug #2
5. Fixed bug #3
6. Refactored component
7. Added feature
```

**Pass condition:**
```
Achievement 1: Test Quality & Regression Protection
- Expanded test suite by 35% (120 → 162 tests)
- Increased coverage from 78% to 84%
- Focused on edge cases and feature flows

Achievement 2: Feature Delivery & Reliability
- Implemented feature X
- Added validation and error handling
- Resolved 3 related edge case bugs
```

---

### Test 3: Metrics Are Calculated Correctly

**Scenario:**
```
120 tests → 162 tests
72% → 84% coverage
```

**Fail condition:**
```
"Increased test coverage by 35%"
(confuses test count % with coverage %)
```

**Pass condition:**
```
"Expanded test suite by 35% (120 → 162 tests)"
"Increased line coverage by 12 percentage points (72% → 84%)"
```

---

### Test 4: Percentage Calculation Accuracy

**Scenario:**
```
Before: 523 tests
After: 567 tests
```

**Fail condition:**
```
"Increased tests by 50%"
(actually only 8.4%)
```

**Pass condition:**
```
"Added 44 tests (8% increase)" or "44 additional tests"
```

---

### Test 5: Related Commits Are Grouped

**Scenario:**
```
Commits:
1. Add settings page
2. Connect settings API
3. Add validation
4. Add error handling
5. Add tests
6. Fix edge case
(All in same PR #456)
```

**Fail condition:**
```
6 separate achievements for 6 commits
```

**Pass condition:**
```
1 achievement: Settings Experience Delivery & Reliability
- Implemented settings page with API integration
- Added comprehensive validation and error handling
- Wrote tests covering main flows and edge cases
```

---

### Test 6: Unrelated Work Isn't Clustered

**Scenario:**
```
Changes:
- Sidebar button styling fix
- Dashboard API timeout
- Help text typo
```

**Fail condition:**
```
1 achievement: "Bug Fixes"
(Different components, different problems)
```

**Pass condition:**
```
Skip individual fixes or include in larger work
(not as standalone achievements)
```

---

### Test 7: Refactor + Feature Are Properly Grouped

**Scenario:**
```
PR #300:
- Refactor component state management
- Implement dark mode using new state structure
```

**Fail condition:**
```
Achievement 1: Component State Refactoring
Achievement 2: Dark Mode Support
```

**Pass condition:**
```
Achievement: Dark Mode & Component Architecture
- Refactored component state for maintainability
- Implemented dark mode using new structure
- Enables future theme customization
```

---

### Test 8: Quarter Returns Appropriate Number of Achievements

**Scenario:**
```
Q3 Repository Analysis:
- Multiple strong achievements (impact 8-9)
- Several medium achievements (impact 5-6)
- Many minor improvements (impact 2-3)
```

**Fail condition:**
```
7 achievements returned:
- 3 high impact ✓
- 3 medium impact ✓
- 1 low impact ✗ (padding to 7)
```

**Pass condition:**
```
5 achievements returned:
- 3 high impact
- 2 medium impact
(Honest assessment - only 5 meaningful)
```

---

### Test 9: No Invented Percentages

**Scenario:**
```
Git history shows:
- Form validation work
- 8 components changed
- No bug tracking data
```

**Fail condition:**
```
"Reduced form errors by 30%"
(No measurement shown)
```

**Pass condition:**
```
"Standardized form validation across 8 components"
or
"Added validation to 8 components"
```

---

### Test 10: No Invented Business Impact

**Scenario:**
```
Technical work:
- Reduced bundle by 12KB
- Improved load time by 34%
```

**Fail condition:**
```
"Increased conversion by 15%"
(No user data shown)
```

**Pass condition:**
```
"Improved load time by 34% (enables faster UX)"
or
"Reduced bundle by 12% (improves performance)"
(Technical claims only)
```

---

### Test 11: Achievement Titles Are Outcome-Oriented

**Scenario:**
```
Work completed:
- Added validation
- Wrote tests
- Fixed bugs
```

**Fail condition:**
```
Title: "Added Tests"
or
Title: "Fixed Bugs"
```

**Pass condition:**
```
Title: "Form Validation & Reliability"
or
Title: "Payment Flow Stability Improvements"
```

---

### Test 12: Evidence Confidence Is Appropriate

**Scenario:**
```
Achievement with:
- Direct measurements ✓
- Multiple sources ✓
- PR documentation ✓
- Peer review ✓
```

**Fail condition:**
```
Confidence: Medium
(With strong evidence should be High)
```

**Pass condition:**
```
Confidence: High
(Matches evidence strength)
```

---

## Validation Checklist

Before releasing ShipLift output:

### Evidence
- [ ] Every quantitative claim has measurement
- [ ] Every measurement has before/after
- [ ] Math is correct
- [ ] Terminology is precise (% vs points)

### Language
- [ ] Titles are outcome-oriented
- [ ] Language is simple and clear
- [ ] No corporate buzzwords
- [ ] Attribution is accurate

### Grouping
- [ ] Related work is clustered
- [ ] Different stories are separated
- [ ] Duplicates are merged
- [ ] No arbitrary grouping

### Impact
- [ ] Focus is on value, not activity
- [ ] Achievements are ranked appropriately
- [ ] Quarter has 5-7 (or fewer) achievements
- [ ] No padding to hit targets

### Anti-BS
- [ ] No invented metrics
- [ ] No invented business claims
- [ ] No invented hours/revenue/customer impact
- [ ] No invented leadership/ownership
- [ ] No unsourced stakeholder feedback

---

## How to Run Validation Tests

1. **Manual inspection**: Read each achievement against criteria
2. **Peer review**: Have another engineer review claims
3. **Evidence audit**: Verify each claim with source data
4. **Repository check**: Confirm with `git log`, `git diff`, PRs
5. **Math check**: Recalculate all percentages
6. **Language check**: Scan for buzzwords and vague language

---

## Continuous Validation

After each ShipLift run:

- [ ] Check that quarter = 5-7 achievements (or justified fewer)
- [ ] Verify no achievement is padding
- [ ] Spot-check 3 random achievements for evidence
- [ ] Verify metrics math
- [ ] Confirm language is clear

---

## Acceptance Test: Real Example

### Given

```
Repository: Acme SaaS Platform
Period: Q3 2024

Commits analyzed: 87
PRs: 12
Issues: 24

Git evidence:
- PR #456: Payment retry logic (4 commits, 8 tests)
- PR #457: Form validation (6 commits, 24 tests)
- PR #458: Dark mode (5 commits, no tests)
- Issues: 3 payment bugs fixed
- Branch: performance-optimization (24 commits, 12KB bundle reduction)
```

### Expected Output

```
✓ Payment Flow Reliability & Feature Completion
  - Implemented retry logic preventing duplicate charges
  - Resolved 3 critical payment bugs
  - Expanded test coverage for payment flow

✓ Form Validation & Error Handling
  - Standardized validation across 8 components
  - Added comprehensive test coverage (24 new tests)
  - Improved error messaging and user feedback

✓ Frontend Performance Optimization
  - Reduced bundle size by 12KB (8% reduction)
  - Implemented lazy loading for product catalog
  - Improved load time from 3.2s to 2.1s

✓ Dark Mode Support
  - Implemented theme switching
  - Added high-contrast accessibility option
  (Note: Few tests - included for completeness)
```

### NOT Acceptable

```
✗ 87 commits (activity count)
✗ "Fixed bugs and improved things" (vague)
✗ "Increased user satisfaction" (invented)
✗ "Reduced errors by 50%" (unverified)
✗ 7 tiny achievements (padding)
```

---

## Failure Modes

### Failure Mode 1: Padding

**Detection:**
```
Quarter has 7 achievements
But only 4 have evidence confidence ≥ 6
```

**Fix:**
Return only 4 achievements with strong evidence.

---

### Failure Mode 2: Activity-Based Achievements

**Detection:**
```
Achievement: "Fixed 3 bugs"
No evidence of grouped impact
```

**Fix:**
Either group with feature work or skip if truly minor.

---

### Failure Mode 3: Invented Metrics

**Detection:**
```
Claim: "Improved by 30%"
No before/after data in evidence
```

**Fix:**
Remove percentage or find actual measurement.

---

### Failure Mode 4: Unsourced Claims

**Detection:**
```
Claim: "Customers loved this feature"
No customer feedback in evidence
```

**Fix:**
Remove or change to "Implemented feature X".

---

## Final Validation

ShipLift output is VALID if:

- ✅ All claims are evidence-backed
- ✅ All math is correct
- ✅ All language is clear and honest
- ✅ All grouping is meaningful
- ✅ No padding or invention
- ✅ Impact is clear
- ✅ Value is apparent

ShipLift output is INVALID if:

- ❌ Any claim lacks evidence
- ❌ Any metric is invented
- ❌ Any language is misleading
- ❌ Any grouping is arbitrary
- ❌ Achievements are padded
- ❌ Value is unclear
