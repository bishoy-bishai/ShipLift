# Intelligence Rules

This document defines patterns and rules for recognizing different types of work and grouping them into coherent achievements.

---

## Pattern 1: Feature + Quality

### Recognition

A feature implementation that includes:
- Core feature code
- Tests for the feature
- Input validation
- Error handling
- Edge case fixes
- Related refactoring

### Rule

**Group as ONE coherent achievement.**

Do NOT split into:
- "Added feature X"
- "Added tests for X"
- "Added validation for X"
- "Fixed bugs in X"

### Example

Raw commits:
```
1. Add settings page UI
2. Connect settings API
3. Add form validation
4. Add error messages
5. Add tests for settings
6. Fix edge case in save flow
```

Grouped achievement:
```
Settings Page Delivery & Reliability

- Implemented new settings page with full API integration
- Added comprehensive form validation and error handling
- Wrote tests covering primary flows and edge cases
- Strengthened data persistence reliability
```

---

## Pattern 2: Test-Only Work

### When to Create Standalone Test Achievement

Create a standalone achievement ONLY if ALL these conditions are met:

- [ ] Test work is **broad** (multiple components or flows)
- [ ] Improvement is **measurable** (count, coverage, or impact)
- [ ] Strategic value is **clear** (enables future work or prevents regressions)
- [ ] OR materially improves regression protection

### When NOT to Create Test Achievement

Do NOT create if:
- [ ] Tests fix one component
- [ ] Adding 1-3 tests
- [ ] Routine test updates
- [ ] Tests are part of a feature

Instead, group with the feature they test.

### Example: Valid Standalone Test Achievement

Raw:
```
Added 42 new tests across:
- Form validation suite
- API integration tests
- Edge case coverage

Coverage change: 78% → 84%
```

Achievement:
```
Test Quality & Regression Protection

- Expanded automated test suite by 35% (120 → 162 tests)
- Increased line coverage from 78% to 84%
- Focused on edge cases and critical user flows
```

### Example: Invalid Standalone Test Achievement

Raw:
```
Added 2 tests to the UserForm component
```

Action: DO NOT create achievement
Instead: Include in Feature achievement if part of feature work

---

## Pattern 3: Refactor + Feature

### Rule

When refactoring primarily **enables** a feature:

**Group refactor WITH the feature, NOT separately**

### Recognition Signals

- PR description links refactor to feature
- Feature cannot be implemented cleanly without refactor
- Files changed overlap significantly
- Same branch/PR for both

### Example

**Bad separation:**

```
1. Component State Refactoring
   - Simplified state management
   
2. Dark Mode Feature
   - Added dark mode support
```

**Good grouping:**

```
Dark Mode & Component Architecture

- Refactored component state for maintainability
- Implemented dark mode using CSS variables
- Leveraged simpler state management for theme switching
```

### When to Keep Separate

If refactor has independent value:

```
Pattern recognition:
- Refactor merged/released separately
- Refactor provides benefit without feature
- Different PR/branch/timeline

Action: Keep as separate achievements
```

Example:
```
1. Redux State Simplification
   - Reduced boilerplate by 30%
   - Improved maintainability
   
2. Dark Mode Support (enabled by refactor)
   - Implemented with new state structure
```

---

## Pattern 4: Bug Clustering

### Rule

Multiple fixes in the same **flow** or **component** → ONE reliability achievement

Do NOT create separate achievement for each bug.

### Recognition Signals

- Same component
- Same user flow
- Same type of issue (e.g., all validation bugs)
- Close commit dates
- Related issue numbers

### Example: Cluster

Raw:
```
- Fixed bug #121: validation edge case
- Fixed bug #124: error message display
- Fixed bug #127: form submission timeout
(All in form submission flow)
```

Grouped:
```
Form Submission Reliability

- Resolved 3 related issues in form submission flow
- Improved error handling and user feedback
- Prevented edge case data loss scenarios
```

### Example: Do NOT Cluster

Raw:
```
- Fixed bug #150: button styling in sidebar
- Fixed bug #200: API timeout in dashboard
- Fixed bug #250: typo in help text
```

Action: DO NOT cluster (different components, different flows)

Better: Either include in feature achievements or skip if truly trivial

---

## Pattern 5: Performance Clustering

### Rule

Related performance improvements → ONE coherent performance story

### Combine:

- Memoization improvements
- Lazy loading implementations
- API request reduction
- Rendering optimizations
- Bundle size reductions
- Benchmark validations
- Caching strategies

### Example

Raw:
```
- Memoized ProductCard component
- Added image lazy loading
- Reduced bundle by 12KB
- Improved initial render by 200ms
```

Grouped:
```
Frontend Performance Improvements

- Implemented memoization and lazy loading strategies
- Reduced bundle size by 12KB (8%)
- Improved initial page load performance by 200ms
```

### When NOT to Cluster

If improvements are in completely different domains:

```
BAD: "Performance Improvements"
- Fixed database query performance
- Improved CSS rendering
- Reduced API payload
(Different layers)

GOOD: Keep separate
1. "Database Query Optimization"
2. "Rendering Performance"
3. "API Payload Reduction"
```

---

## Pattern 6: CI / Developer Experience

### Rule

Related developer tooling and CI improvements → ONE coherent story

### Combine:

- CI/CD pipeline optimizations
- Caching improvements
- Test tooling enhancements
- Build automation
- Development scripts
- Local development improvements

### Example

Raw:
```
- Added GitHub Actions caching layer
- Wrote test parallelization script
- Improved build time by 40%
```

Grouped:
```
CI Pipeline & Developer Experience

- Implemented smart caching and test parallelization
- Reduced CI build time by 40%
- Improved developer iteration speed and confidence
```

---

## Pattern 7: API / Contract Changes

### Rule

Changes to API contracts, types, or interfaces → Group by strategic goal

### Recognize:

- API parameter changes
- Type system improvements
- Schema changes
- Contract simplification

### Example

Raw:
```
- Removed 5 unused API parameters
- Simplified endpoint responses
- Added API documentation
- Updated TypeScript types
```

Grouped:
```
API Simplification & Developer Experience

- Reduced endpoint complexity by 30%
- Simplified API contracts for consumers
- Improved API documentation completeness
```

---

## Pattern 8: Security Improvements

### Rule

Security fixes → Group by type and scope

### Group by:

- Vulnerability type (XSS, injection, auth, etc.)
- Scope (single endpoint, entire service, framework-wide)
- Impact (data, user, performance)

### Example

Raw:
```
- Fixed XSS vulnerability in comment display
- Fixed SQL injection in search
- Added input sanitization middleware
```

Grouped:
```
Security Hardening

- Fixed XSS vulnerability in comment display
- Fixed SQL injection vulnerability in search
- Implemented global input sanitization middleware
- Prevented 2 critical vulnerability vectors
```

---

## Pattern 9: Dependency & Tooling Updates

### Rule

Only highlight if strategic value exists.

### Highlight if:

- Security patches (critical vulnerabilities)
- Major version upgrades enabling features
- Tooling change improving developer experience
- Framework upgrade

### Do NOT highlight:

- Minor version bumps
- Routine maintenance updates
- Dependency tree cleanup

---

## Pattern 10: Documentation & Knowledge

### Rule

Only create standalone achievement if:

- [ ] Documentation is comprehensive and strategic
- [ ] Significantly improves developer onboarding
- [ ] Clarifies complex APIs or systems
- [ ] Requires substantial research/structure

### Example: Valid

```
API Documentation & Developer Onboarding

- Wrote comprehensive API reference guide
- Added interactive examples for all endpoints
- Documented common integration patterns
- Improved new developer onboarding time
```

### Example: Invalid

```
"Updated README"
(Too small for standalone achievement - include in feature work)
```

---

## Cross-Pattern Rules

### Rule: Don't Mix Unrelated Work

Do NOT group improvements from different domains just because they're in same time period.

**Wrong:**

```
"August Improvements"
- Database query optimization
- UI component refactoring
- CI pipeline improvements
(Three completely different stories)
```

**Right:**

```
1. Database Query Performance
2. Component Library Refactoring
3. CI Pipeline Optimization
```

### Rule: Same Component ≠ Same Achievement

Just because changes are in same file doesn't mean they're one achievement.

**Example:**

```
File: UserService.ts
- Added validation
- Added caching
- Fixed authorization bug

Better as:
1. "User Validation & Input Safety"
2. "User Service Performance Optimization"
3. Included in broader reliability work
```

---

## Decision Tree

Use this tree to decide grouping:

```
Do these changes address the SAME user need or technical goal?
    |
    ├─ YES → Are they in the same code area?
    |        ├─ YES → Group as ONE achievement
    |        └─ NO  → Group if same goal, separate if different
    |
    └─ NO  → Do they enable each other?
             ├─ YES (refactor enables feature) → Group
             └─ NO  → Keep SEPARATE
```

---

## Checklist

Before finalizing grouping:

- [ ] Have I identified the highest-level story?
- [ ] Are all related commits included?
- [ ] Does this tell one coherent story?
- [ ] Could I explain this in one sentence?
- [ ] Have I checked for unrelated work mixed in?
- [ ] Is the evidence strong enough?
- [ ] Would this make sense to a non-engineer?
