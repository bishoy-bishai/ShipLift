# Anti-BS Rules

These rules are **mandatory**. Every ShipLift user must enforce them.

---

## Core Rule

**Do not invent claims without evidence.**

---

## Mandatory Rules

### Rule 1: Never Invent Percentages

**Forbidden:**

```
❌ "Reduced bugs by 30%"
   (No bug tracking data shown)

❌ "Improved performance by 25%"
   (No benchmarks provided)
```

**Allowed:**

```
✓ "Reduced test failures by 5 (from 12 to 7)"
✓ "Improved response time from 450ms to 280ms"
✓ "Increased test count by 35% (120 → 162)"
```

**Rule:**

If you claim a percentage, prove it with:
- Before/after measurements
- Mathematical calculation shown
- Source of data identified

---

### Rule 2: Never Invent Business Impact

**Forbidden:**

```
❌ "Improved user engagement"
   (No user data provided)

❌ "Increased conversion rate by 15%"
   (No analytics shown)

❌ "Reduced customer churn"
   (No customer data shown)
```

**Allowed:**

```
✓ "Improved load time by 40%"
  (Technical measurement - supports engagement claim if other evidence exists)

✓ "Reduced form validation errors"
  (Code evidence - improves UX but not proven conversion impact)
```

**Rule:**

Business impact claims require:
- Actual user/business data
- Analytics or feedback
- Not just technical improvement

---

### Rule 3: Never Invent Revenue Impact

**Forbidden:**

```
❌ "Generated $50,000 in revenue"
   (No financial tracking data)

❌ "Increased customer lifetime value"
   (No LTV data shown)
```

**Allowed:**

```
✓ "Enabled feature requested by top 5 customers"
  (If customer list and requests can be documented)

✓ "Implemented payment feature"
  (Describes work, not invented revenue)
```

**Rule:**

Revenue claims require:
- Financial tracking data
- Actual transaction records
- Clear causal link to your work

---

### Rule 4: Never Invent Conversion Impact

**Forbidden:**

```
❌ "Conversion improved by 8%"
   (No A/B test shown)

❌ "Click-through rate increased"
   (No analytics shown)
```

**Allowed:**

```
✓ "Improved button visibility and placement"
  (Design change - supports CTR improvement with data)

✓ "Reduced form friction by removing 3 fields"
  (UX improvement - may improve conversions with measurement)
```

**Rule:**

Conversion claims require:
- A/B test results
- Analytics data
- Clear measurement period
- Other variables controlled

---

### Rule 5: Never Invent Customer Impact

**Forbidden:**

```
❌ "Delighted our customers"
   (No customer feedback shown)

❌ "Customers love this feature"
   (Subjective - not verifiable)
```

**Allowed:**

```
✓ "Implemented feature requested in support tickets #234, #567, #891"
  (Specific customer requests documented)

✓ "Addressed top UX complaint from user research"
  (Research evidence shown)
```

**Rule:**

Customer impact claims require:
- Specific customer feedback
- Support ticket references
- User research evidence
- Net Promoter Score data

---

### Rule 6: Never Invent Hours Saved

**Forbidden:**

```
❌ "Saved developers 5 hours per week"
   (No measurement - just estimate)

❌ "Reduced deployment time by 2 hours"
   (No before/after data)
```

**Allowed:**

```
✓ "Reduced CI build time from 180s to 80s"
  (Measured - enables faster iteration)

✓ "Automated manual deployment step"
  (Process improvement - potential time savings if measured)
```

**Rule:**

Time savings claims require:
- Before/after measurement
- Clear methodology
- Or describe automation without claiming hours

---

### Rule 7: Never Invent Leadership

**Forbidden:**

```
❌ "Led the initiative"
   (When you contributed but didn't lead)

❌ "Owned the architecture"
   (When you implemented according to someone else's design)

❌ "Drove the team decision"
   (When you proposed and team discussed)
```

**Allowed:**

```
✓ "Implemented authentication system according to architectural spec"
  (Accurate description of role)

✓ "Proposed and implemented lazy loading strategy"
  (You proposed AND implemented)

✓ "Contributed to performance initiative led by @alice"
  (Accurate attribution)
```

**Rule:**

Leadership claims require:
- Evidence you made final decision
- Evidence you set direction
- Evidence you held accountability
- OR use "contributed to" language if shared

---

### Rule 8: Never Invent Ownership

**Forbidden:**

```
❌ "Owned the frontend transformation"
   (You worked on some components)

❌ "Owned quality improvements"
   (You fixed some bugs someone else found)
```

**Allowed:**

```
✓ "Improved UserProfile component reliability"
  (Specific scope you controlled)

✓ "Standardized form validation approach across 8 components"
  (Scope you actually implemented)
```

**Rule:**

Ownership claims require:
- Accountability for entire scope
- Evidence you controlled decisions
- Evidence you drove completeness

---

### Rule 9: Never Invent Stakeholder Feedback

**Forbidden:**

```
❌ "Stakeholders are thrilled"
   (No direct feedback)

❌ "Product team loved our architecture"
   (Not documented)

❌ "Security team approved"
   (Only implicitly through code review)
```

**Allowed:**

```
✓ "Implemented feature requested in product spec #456"
  (Documented requirement)

✓ "Security review passed with zero findings"
  (Documented approval)

✓ "Approved by @alice-security in PR #789"
  (Specific person, specific evidence)
```

**Rule:**

Stakeholder feedback requires:
- Direct quotes or documented feedback
- Named stakeholder
- Specific approval or comment
- Link to evidence

---

### Rule 10: Never Invent Problems You Didn't Find

**Forbidden:**

```
❌ "Solved the critical performance bottleneck"
   (You didn't identify the bottleneck)

❌ "Fixed the major security vulnerability"
   (Someone else reported it)
```

**Allowed:**

```
✓ "Identified and fixed N+1 query problem"
  (You found and fixed it)

✓ "Implemented fix for security vulnerability reported in #456"
  (You fixed something someone else found)

✓ "Prevented potential XSS vulnerability"
  (You proactively added protection)
```

**Rule:**

Use accurate language:
- "Identified and fixed" (you found and resolved)
- "Fixed" (you implemented the fix)
- "Implemented fix for" (someone reported, you fixed)
- "Prevented" (proactive measure)

---

## Consequence Framework

For each claim, ask:

```
1. What evidence proves this?
2. Can I point to specific data?
3. Could someone else verify this?
4. Am I extrapolating beyond that data?
5. Would I be comfortable explaining this in a code review?
```

If you can't answer 1-3 convincingly, the claim violates the Anti-BS Rules.

---

## Verification Checklist

Before committing to an achievement:

- [ ] Every quantitative claim has before/after data
- [ ] Every business claim has customer/analytics data
- [ ] No extrapolation beyond available evidence
- [ ] No invented metrics
- [ ] No invented hours saved
- [ ] No invented customer impact
- [ ] No invented revenue
- [ ] Accurate language about ownership and leadership
- [ ] No unsourced stakeholder feedback
- [ ] All claims could be verified by engineering review

---

## Examples: Before and After

### Example 1: Feature Work

**Before (violates rules):**

```
Dark Mode Implementation
- Implemented popular feature
- Improved user satisfaction
- Drove accessibility improvements
```

**After (follows rules):**

```
Dark Mode Support with Accessibility
- Implemented theme switching using CSS variables
- Added 18 tests covering theme persistence and edge cases
- Enabled high-contrast mode support
- Implemented ARIA live regions for theme announcements
```

**What changed:**

- Removed "popular" (no data)
- Removed "improved satisfaction" (no user data)
- Removed "drove" (you didn't drive - you implemented)
- Added specific implementation details
- Added measurable work (tests, accessibility features)
- Used accurate language

---

### Example 2: Performance Work

**Before (violates rules):**

```
Performance Optimization
- Significantly improved performance
- Increased user experience by a lot
- Big wins
```

**After (follows rules):**

```
Frontend Performance Optimization
- Implemented component memoization reducing unnecessary re-renders
- Added image lazy loading to ProductList
- Reduced bundle size by 12KB (8%)
- Improved Core Web Vitals: LCP from 3.2s to 2.1s (34% improvement)
```

**What changed:**

- Removed vague language ("significantly", "a lot", "big wins")
- Added specific techniques (memoization, lazy loading)
- Added measurements with before/after
- Used percentage correctly (34% improvement in time)

---

### Example 3: Bug Fixes

**Before (violates rules):**

```
Reliability Improvements
- Fixed many bugs
- Made the system more stable
- Resolved customer issues
```

**After (follows rules):**

```
Payment Flow Reliability
- Resolved 3 issues in payment submission flow
  - Fixed race condition in duplicate detection
  - Fixed error state handling that prevented retry
  - Fixed timeout recovery that lost user data
- Added 12 tests for failure scenarios
- Reduced error rate in payment flow by preventing data loss
```

**What changed:**

- Removed "many bugs" (vague)
- Removed "more stable" (unmeasured)
- Removed "customer issues" (not specific)
- Added: specific issues and problems
- Added: number of tests added
- Added: measurable impact (preventing data loss)
- Used specific component scope

---

### Example 4: Leadership vs. Contribution

**Before (violates rules):**

```
API Architecture Redesign
- Led the effort
- Owned the decision
- Drove architectural changes
- Improved system scalability
```

**After (follows rules):**

```
API Architecture Redesign (Contribution)
- Implemented new service layer architecture per design spec
- Migrated 8 endpoints to new structure
- Added 15 tests validating backwards compatibility
- Enabled future API versioning (per product roadmap)
```

**What changed:**

- If you didn't actually lead: removed leadership language
- Added specific scope (8 endpoints)
- Added specific contribution (implementation)
- Added what was delivered (tests, capability enabled)
- Removed ownership claims without evidence

---

## The Final Check

Before finalizing any achievement, ask yourself:

> **If the engineering lead asked me to prove this in a code review, could I?**

If not, remove or reword the claim.
