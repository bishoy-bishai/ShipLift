# Metrics

This document defines how to calculate, validate, and present metrics in ShipLift achievements.

---

## Core Principle

**Metrics must be mathematically correct.**

Never invent a metric. Never extrapolate beyond available data.

---

## Metric Types

### 1. Percentage Change

**Formula:**

```
Percentage Change = ((After - Before) / Before) × 100
```

**Example:**

```
Before: 120 tests
After: 162 tests

Change = ((162 - 120) / 120) × 100
       = (42 / 120) × 100
       = 0.35 × 100
       = 35%

Correct claim: "Expanded test suite by 35%"
```

---

### 2. Percentage Points

Use when reporting coverage or percentages.

**Formula:**

```
Percentage Points = After - Before
```

**Example:**

```
Before: 72% coverage
After: 84% coverage

Change = 84 - 72 = 12 percentage points

Correct claim: "Increased coverage by 12 percentage points"

Do NOT say: "Increased coverage by 16.7%" (that's the relative change)
```

**Relative change (if useful):**

```
Relative change = (84 - 72) / 72 × 100 = 16.7%

Could say: "Increased coverage by 12 percentage points (16.7% relative improvement)"
```

---

### 3. Absolute Numbers

**When to use:**

- Count changes: "Added 24 new endpoints"
- Size changes: "Reduced bundle by 45KB"
- Time changes: "Improved build time from 2m 30s to 1m 30s"

**Example:**

```
Before: 2 minute 30 second build
After: 1 minute 30 second build

Correct claim: "Reduced build time by 60 seconds" (1 minute)
Or: "Improved build time by 40%"

Calculation: (90 - 150) / 150 × 100 = -60 / 150 × 100 = -40%
(negative means reduction)
```

---

### 4. Ratio / Multiplier

**When to use:**

- Performance improvements: "2x faster"
- Scale improvements: "10x increase"

**Formula:**

```
Multiplier = After / Before
```

**Example:**

```
Before: 5 seconds
After: 1 second

Multiplier = 5 / 1 = 5x

Correct claim: "Improved speed by 5x" or "Made it 5x faster"
```

---

## Common Metrics

### Test Metrics

#### Test Count

```
Before: 80 tests
After: 110 tests

Percentage: ((110 - 80) / 80) × 100 = 37.5%
Claim: "Expanded test suite by 37.5%"

Do NOT claim: "Increased test quality by 37.5%"
(Quality is not measured by count alone)
```

#### Test Coverage

```
Before: 65% line coverage
After: 78% line coverage

Change: 78 - 65 = 13 percentage points
Claim: "Increased line coverage by 13 percentage points"

Relative: (78 - 65) / 65 × 100 = 20%
Extended claim: "Increased coverage by 13 percentage points (20% improvement)"
```

#### Test Pass Rate

```
Before: 94% pass rate (6 failures out of 100)
After: 99% pass rate (1 failure out of 100)

Change: 99 - 94 = 5 percentage points
Claim: "Improved test pass rate by 5 percentage points"
```

---

### Performance Metrics

#### Load Time

```
Before: 3.2 seconds
After: 2.1 seconds

Reduction: 3.2 - 2.1 = 1.1 seconds
Percentage: (2.1 - 3.2) / 3.2 × 100 = -34.4% = 34.4% improvement
Claim: "Reduced load time by 1.1 seconds (34% improvement)"

Or: "Improved load time from 3.2s to 2.1s"
```

#### Bundle Size

```
Before: 245 KB
After: 215 KB

Reduction: 245 - 215 = 30 KB
Percentage: (215 - 245) / 245 × 100 = -12.2% ≈ 12%
Claim: "Reduced bundle size by 30KB (12% reduction)"
```

#### Render Time

```
Before: 450ms
After: 180ms

Reduction: 450 - 180 = 270ms
Multiplier: 450 / 180 = 2.5x
Claim: "Improved render time by 2.5x (from 450ms to 180ms)"

Or percentage: (180 - 450) / 450 × 100 = -60%
Claim: "Reduced render time by 60%"
```

---

### Code Metrics

#### Lines of Code

```
Feature added 340 lines

Claim: "Added 340 lines of implementation code"

Do NOT claim: "Improved by 340 lines"
(More code isn't inherently improvement)

Better context: "Added 340 lines of implementation code and corresponding tests"
```

#### Files Changed

```
Modified 12 files

Claim: "Updated 12 files across the form validation system"

Do NOT claim: "Improved 12 files"
(Scope indicator, not quality indicator)
```

---

### Build Metrics

#### Build Time

```
Before: 3 minutes 45 seconds = 225 seconds
After: 1 minute 30 seconds = 90 seconds

Reduction: 225 - 90 = 135 seconds (2 minutes 15 seconds)
Percentage: (90 - 225) / 225 × 100 = -60%
Multiplier: 225 / 90 = 2.5x

Claim: "Reduced build time by 60% (from 3m 45s to 1m 30s)"
Or: "Improved build time by 2.5x"
```

---

### API / Endpoint Metrics

#### Endpoint Count

```
Before: 8 endpoints
After: 12 endpoints

Added: 12 - 8 = 4 new endpoints
Percentage: (12 - 8) / 8 × 100 = 50%

Claim: "Added 4 new API endpoints (50% increase in API surface)"
```

#### Endpoint Simplification

```
Before: Average 8 parameters per endpoint
After: Average 5 parameters per endpoint

Reduction: 8 - 5 = 3 parameters
Percentage: (5 - 8) / 8 × 100 = -37.5%

Claim: "Reduced average endpoint complexity by 37.5%"
Or: "Simplified endpoints by removing 3 average parameters"
```

---

## Metric Validation Checklist

Before claiming a metric:

- [ ] Can I identify the "before" and "after" values?
- [ ] Are both values from reliable sources?
- [ ] Is the calculation mathematically correct?
- [ ] Have I used the right formula (%, points, or absolute)?
- [ ] Does the claim match what the metric actually measures?
- [ ] Could this metric be misleading without context?
- [ ] Have I avoided extrapolating to unrelated claims?

---

## Anti-Patterns: Invalid Metrics

### Pattern 1: Confusing Percentage with Percentage Points

**Wrong:**

```
Coverage increased from 72% to 84%
Claim: "Increased coverage by 16.7%"

Problem: Misleading - the improvement is 12 percentage points
Correct: "Increased coverage by 12 percentage points"
```

---

### Pattern 2: Counting Commits as Work

**Wrong:**

```
"Made 24 commits"

Problem: Commit count ≠ work quality
Correct: Describe the actual work accomplished
```

---

### Pattern 3: Inferring One Metric from Another

**Wrong:**

```
Test count increased by 30%
Inferred claim: "Reduced bugs by 30%"

Problem: No evidence of bug reduction
Correct: "Expanded test coverage by 30%"
```

---

### Pattern 4: Rounding Too Aggressively

**Wrong:**

```
Before: 523 tests
After: 567 tests
Claim: "Increased tests by 50%"

Reality: ((567 - 523) / 523) × 100 = 8.4%
```

**Correct:**

```
Claim: "Added 44 tests (8% increase)"
```

---

### Pattern 5: Including Unrelated Changes in Metric

**Wrong:**

```
"Reduced component from 500 lines to 450 lines"

Without inspecting code:
- Did functionality improve?
- Was code actually removed or moved?
- Was it refactored or improved?

Could be rearrangement, not improvement
```

**Correct:**

Inspect code, then claim:
```
"Simplified component architecture by removing 50 lines of boilerplate
while maintaining full functionality"
```

---

### Pattern 6: Comparing Different Measurements

**Wrong:**

```
"Improved performance" (comparing CPU time to memory usage)
```

**Correct:**

```
Compare same metric: "Improved CPU time" or "Reduced memory usage"
```

---

## Metric Presentation Guidelines

### Good Metric Presentation

```
"Expanded test suite by 35% (120 → 162 tests)"
"Reduced bundle size by 12% (245KB → 215KB)"
"Improved load time by 40% (3.2s → 1.9s)"
"Increased API coverage from 45% to 72% (+27 percentage points)"
```

### Bad Metric Presentation

```
"Made improvements" (vague)
"Did a lot of work" (unmeasured)
"Significant gains" (subjective)
"Optimized things" (nonspecific)
"Better performance" (unmeasured)
```

---

## When Metrics Are Unavailable

If measurement is impossible:

1. **Use qualitative evidence instead:**
   ```
   "Simplified form validation by consolidating 4 separate
   validation functions into 1 composable utility"
   ```

2. **Describe scope and quality:**
   ```
   "Added comprehensive error handling covering edge cases
   in payment flow"
   ```

3. **Combine quantitative and qualitative:**
   ```
   "Added 24 new tests focusing on error scenarios
   and edge cases"
   ```

4. **Never invent metrics:**
   ```
   ✗ "Improved developer experience by 30%"
   ✓ "Improved developer experience by automating test setup"
   ```

---

## Checklist: Metric Quality

For each metric in an achievement:

- [ ] Is this mathematically correct?
- [ ] Have I used the right formula?
- [ ] Is this what the metric actually measures?
- [ ] Could I be extrapolating beyond evidence?
- [ ] Have I avoided confusing % with percentage points?
- [ ] Have I included context (before/after or percentage)?
- [ ] Is this measurable and verifiable?
