# Achievement Framework

## Core Principle

Do NOT report low-level activity when a higher-level engineering story can be derived.

### The Transformation

```
Code Change
    ↓
Work
    ↓
Engineering Impact
    ↓
Achievement
```

**Example:**

Raw activity:
```
Added 42 tests
```

Should become:
```
Test Quality & Regression Protection

- Expanded the automated test suite by 35%.
- Added coverage for important edge cases and user flows.
- Made future changes safer to validate.
```

---

## Clustering Rules

Do NOT treat every commit as separate work.

ShipLift must understand that multiple commits may represent ONE FEATURE or ONE IMPROVEMENT.

### Group work using signals such as:

- Same PR
- Same issue
- Same branch
- Same component
- Same feature
- Same user flow
- Same technical goal
- Overlapping files
- Close dates
- Shared tests

### Example

These six commits:
```
Add settings page
Connect settings API
Add validation
Add error handling
Add tests
Fix edge case
```

Should become ONE achievement:
```
Settings Experience Delivery & Reliability
```

Rather than six separate achievements.

---

## Grouping Patterns

### Feature + Quality

When work includes:
- Feature implementation
- Tests
- Validation
- Reliability improvements

**Action:** Group as ONE coherent achievement

Example:
```
Feature: Add dark mode toggle

Related work:
- Implementation
- CSS variables update
- Test coverage (12 new tests)
- Edge case fixes
- Accessibility validation

Result:
ONE Achievement: "Dark Mode Support with Quality"
```

---

### Test-Only Work

Create a standalone test achievement ONLY when:

- Work is broad (not just one component)
- Improvement is measurable
- Strategic value is clear
- OR materially improves regression protection

**Do NOT create a test achievement for:**
- Small fixes to a single test
- Adding 1-2 tests
- Minor test refactoring
- Routine test updates

These should be part of the feature they test.

---

### Refactor + Feature

When refactoring primarily **enables** a feature:

**Action:** Group refactor WITH the feature, not separately

Example:
```
Bad:
1. Refactored component state management
2. Added new feature

Good:
1. Component State Simplification & Feature Delivery
   - Refactored state management for maintainability
   - Enabled new feature delivery
```

---

### Bug Clustering

Multiple fixes in the same flow may represent **one reliability story** rather than multiple tiny achievements.

**Example:**

Raw:
```
- Fixed bug #121 (validation edge case)
- Fixed bug #124 (error message display)
- Fixed bug #127 (form submission timeout)
```

All in the form submission flow.

Grouped:
```
Form Submission Reliability

- Resolved 3 related issues in the form submission flow
- Improved error handling and user feedback
- Prevented data loss in edge cases
```

---

### Performance Clustering

Combine related:
- Memoization improvements
- Lazy loading implementations
- Reduced API requests
- Rendering optimizations
- Bundle size reductions
- Benchmark validations

Into ONE performance story when they form a coherent improvement.

**Example:**

Raw:
```
- Added memoization to ProductList
- Implement lazy loading for images
- Reduced bundle by 12KB
```

Grouped:
```
Frontend Performance Improvements

- Implemented memoization and lazy loading strategies
- Reduced bundle size by 12KB (8% reduction)
- Measurably improved initial page load performance
```

---

### CI / Developer Experience

Group related:
- CI pipeline improvements
- Caching optimizations
- Test tooling enhancements
- Development scripts
- Automation improvements

When they form ONE meaningful engineering improvement.

**Example:**

Raw:
```
- Added CI cache layer
- Wrote test parallelization script
- Improved build time by 40%
```

Grouped:
```
CI Pipeline & Developer Experience

- Implemented smart caching and test parallelization
- Reduced build time by 40%
- Improved developer iteration speed and confidence
```

---

## Anti-Clustering Rules

### Do NOT group unrelated work

Just because multiple changes are in the same file doesn't mean they should be grouped.

**Example:**

```
Bad grouping:
1. "Service Updates"
   - Added validation to payment service
   - Added caching to user service
   - Fixed bug in notification service
```

These are different concerns. Better:
```
1. Payment Validation & Reliability
2. User Service Performance Optimization
3. Notification System Reliability
```

---

### Do NOT merge achievements that tell different stories

Even if work overlaps, if the stories are fundamentally different, keep them separate.

**Example:**

Good separation:
```
1. API Contract Simplification
   - Reduced endpoint parameters
   - Improved developer experience

2. Performance Optimization
   - Reduced payload size
   - Improved client performance
```

Bad merge:
```
1. "API Improvements"
   - Reduced endpoint parameters
   - Reduced payload size
   (story unclear)
```

---

## Duplicate Detection

Before finalizing achievements:

1. Check if two achievements describe essentially the same story
2. Merge if they are duplicates
3. Keep separate if they tell different stories

**Example of duplicates:**

```
Duplicate:
1. "Improved form validation"
2. "Form validation enhancements"

Solution: Merge into one achievement
```

**Example of related but separate:**

```
Keep separate:
1. "Form Validation & User Experience"
   - Added real-time validation feedback
   - Improved error messages
   
2. "Backend Form Validation Security"
   - Server-side validation enforcement
   - XSS/injection prevention
```

---

## Special Cases

### Documentation Work

Only create a standalone documentation achievement if:
- Documentation is comprehensive and strategic
- Significantly improves developer onboarding or API clarity
- Required substantial research and structure

### Configuration Changes

Only highlight configuration changes if they:
- Materially improve performance
- Fix a significant problem
- Enable a new capability
- Reduce operational burden

### Dependency Updates

Group dependency updates by strategic value:
- Security fixes (group by severity and scope)
- Feature enablement (group by feature)
- Do NOT count minor version bumps as achievements

---

## Checklist for Achievement Grouping

For each potential achievement:

- [ ] Have I identified the highest-level story?
- [ ] Are all related commits included?
- [ ] Does this tell a coherent story?
- [ ] Is there measurable evidence?
- [ ] Could this be merged with another achievement?
- [ ] Does this follow the evidence priority?
- [ ] Is the impact clear and quantifiable (when applicable)?
