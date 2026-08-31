# Evidence Matrix

## Evidence Priority (Strongest to Weakest)

ShipLift operates on a hierarchy of evidence. Use the strongest available evidence at each stage.

```
1. Direct measurement (metrics, benchmarks, test results)
                ↓
2. Actual code / diff (what was changed)
                ↓
3. PR / Issue context (description, review comments)
                ↓
4. Commit message (brief description)
                ↓
5. Inference (logical deduction from changes)
```

### Key Principle

**Never allow weak inference to override strong evidence.**

---

## Evidence Sources

### 1. Direct Measurement (Highest Priority)

**When available, always use:**

- Test count before/after with percentage change
- Coverage percentage change
- Performance metrics (load time, bundle size, render time, etc.)
- Benchmark results
- CI metrics (build time, etc.)
- Quantifiable data from actual runs

**Example:**

```
Before: 42 tests, 78% coverage
After: 64 tests, 84% coverage

Measurement: 52% increase in tests
             6 percentage point increase in coverage

Achievement: "Test Quality & Coverage Improvements"
- Expanded test suite by 52%.
- Increased line coverage from 78% to 84%.
```

---

### 2. Actual Code / Diff (Strong Evidence)

**Inspect:**

- Files changed
- Lines added/removed
- Function signatures
- Database schema changes
- Configuration changes
- API contract changes

**Example:**

```
Diff shows:
- 12 new test files added
- 340 lines of new test code
- New validation functions
- Error handling additions

Achievement: "Validation & Error Handling Expansion"
- Added comprehensive validation for form inputs
- Implemented error recovery mechanisms
```

---

### 3. PR / Issue Context (Moderate Evidence)

**Extract from:**

- PR title and description
- Issue title and description
- PR review comments and discussion
- Issue-PR linking
- Linked issues

**Example:**

```
PR #234: "Add dark mode support"
Description: "Implements dark mode using CSS variables for maintainability"
Related Issue #156: "Support dark mode for accessibility"

Achievement: "Dark Mode Support & Accessibility"
- Implemented dark mode using CSS variables
- Improved accessibility as requested in issue #156
```

---

### 4. Commit Message (Weak Evidence)

**Use only when stronger evidence unavailable:**

- Commit message subject
- Commit message body
- Commit author
- Commit date

**Important:** Commit messages are hints, not proof.

**Example (weak):**

```
Commit: "Fix authentication bug"

This is weak because:
- Doesn't specify what bug
- Doesn't show scope of fix
- Doesn't quantify impact

Better: Inspect the actual code change
```

---

### 5. Inference (Weakest Evidence)

**Use only as a last resort for context:**

- Logical deduction from code structure
- Architectural implications
- Performance implications (without benchmarks)
- Estimated scope

**Important:** Do not create achievements based primarily on inference.

**Example (too weak):**

```
Inference: "They probably improved performance by refactoring"

Better: Show actual performance benchmarks or measurements
```

---

## Inspection Checklist

For each achievement candidate, inspect:

- [ ] **Git history**: commits, messages, branches
- [ ] **Git diffs**: actual changes to files
- [ ] **Pull Requests/Merge Requests**: title, description, review comments
- [ ] **Issues**: linked issues and context
- [ ] **Changed files**: scope and nature of changes
- [ ] **Tests**: new tests, test changes, coverage impact
- [ ] **Coverage reports**: before/after coverage percentages
- [ ] **Build output**: size changes, warnings, optimizations
- [ ] **Benchmarks**: performance measurements
- [ ] **CI/CD results**: build times, test results
- [ ] **Configuration changes**: .yml, .json, .config files
- [ ] **Repository structure**: new directories, file organization
- [ ] **Documentation**: changes to README, docs, comments

---

## Evidence Validation Rules

### Rule 1: Verify Metrics

If a metric is claimed, verify it's mathematically correct.

**Example:**

```
Claim: "Increased test count by 35%"

Verify:
- Old count: 120 tests
- New count: 162 tests
- Calculation: (162 - 120) / 120 = 0.35 = 35% ✓

Valid evidence
```

---

### Rule 2: Do Not Extrapolate Beyond Evidence

**Wrong:**

```
Code change: Reduced database queries by 30%
Extrapolated claim: "Improved user experience by 30%"

Problem: No evidence of user impact
```

**Right:**

```
Code change: Reduced database queries by 30%
Correct claim: "Optimized database query performance"

If user impact needed: Require separate user performance metrics
```

---

### Rule 3: Separate Technical Evidence from Business Evidence

**Technical evidence alone:**

```
✓ Reduced bundle size by 12%
✓ Improved test coverage from 72% to 84%
✓ Decreased build time by 40%
```

**Does NOT prove:**

```
✗ Increased user engagement
✗ Improved conversion rate
✗ Increased revenue
```

**Business evidence needed separately:**

```
✓ 12% bundle reduction + user performance metrics = UX improvement claim
✓ Test coverage increase + bug metrics = reliability improvement claim
✓ Build time reduction + developer surveys = developer experience claim
```

---

### Rule 4: Cross-Reference Evidence

When possible, validate with multiple sources:

```
Evidence 1: PR description says "Added input validation"
Evidence 2: Diff shows validation functions added
Evidence 3: Tests added for validation edge cases
Evidence 4: No regressions in CI

Confidence: High ✓
```

---

### Rule 5: Question Contradictory Evidence

If evidence conflicts, investigate:

```
Commit message: "Fixed major security bug"
Diff: 1 line change in comment
Test change: No new tests added

Flag: Mismatch between claim and evidence
Action: Inspect actual code, not message
```

---

## Special Evidence Cases

### Case: Zero New Tests

**Evidence:**

```
Change: Major refactoring
Tests: No new tests added
Problem: Did tests actually improve?
```

**Approach:**

1. Check if existing tests still pass
2. Check if coverage changed
3. Check test file modifications
4. Document uncertainty

**Claim:**

```
Safe claim: "Refactored component for maintainability"
Risky claim: "Improved reliability" (without evidence)
```

---

### Case: Test File Organization

**Evidence:**

```
Change: Moved 50 tests to better organized files
Claim: "Added 50 tests"

Problem: Misleading - test count didn't change
```

**Approach:**

1. Check for actual code changes
2. Verify test count increased
3. Verify coverage changed

**Claim:**

```
"Improved test organization and maintainability"
```

---

### Case: Partial Implementation

**Evidence:**

```
PR #456: "Implement dark mode"
Status: Draft or WIP
```

**Approach:**

1. Check if merged to main/develop
2. Check if feature is complete
3. Check if used in production

**Claim:**

Only include if feature is:
- Merged
- Complete
- Deployed (or soon to be)

---

## Evidence Documentation Template

When analyzing work, create an evidence matrix:

```
Achievement: [Title]

Evidence 1 (Direct Measurement):
- Type: Test count increase
- Before: 120 tests
- After: 162 tests
- Change: +35%
- Confidence: HIGH

Evidence 2 (Actual Diff):
- Files changed: 12 test files
- Lines added: 340
- Coverage change: +6 points (78% → 84%)
- Confidence: HIGH

Evidence 3 (PR Context):
- PR #234 description: "Expand test coverage for edge cases"
- Review approved by: @tech-lead
- Confidence: MEDIUM

Inference:
- Test quality likely improved
- Regression protection likely improved
- Confidence: MEDIUM (requires measurement confirmation)

Final Claim Strength: HIGH (multiple strong evidence sources)
```

---

## Quick Reference Checklist

For each claim in an achievement:

- [ ] What evidence type supports this? (1-5 ranking)
- [ ] Is this the strongest available evidence?
- [ ] Have I verified measurements are correct?
- [ ] Have I avoided extrapolation beyond evidence?
- [ ] Is this technical or business claim? Do I have right evidence?
- [ ] Could contradictory evidence exist? Have I checked?
- [ ] Am I confident enough to state this?
