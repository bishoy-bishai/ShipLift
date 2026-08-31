# ShipLift Quick Reference

A one-page guide to using ShipLift effectively.

---

## The Three Commands

### ShipLift Quarter
Analyze your **current quarter** and get 5–7 strongest achievements.

```
ShipLift Quarter
```

**Best for:**
- Quarterly reviews
- Performance evaluations
- Resume updates
- Impact assessment

---

### ShipLift Standup
Prepare a **1-3 week update** in Done/Next/Blockers format.

```
ShipLift Standup 1-week
ShipLift Standup 2-weeks
```

**Best for:**
- Team standups
- Status updates
- Weekly check-ins
- Progress tracking

---

### ShipLift 1:1
Prepare **comprehensive talking points** for your manager 1:1.

```
ShipLift 1:1 1-month
ShipLift 1:1 3-months
```

**Best for:**
- Manager 1:1 meetings
- Career conversations
- Growth discussions
- Performance reviews

---

## The Golden Rule

> **Make the value of the work clearer, not bigger.**

Every achievement must:
- ✅ Be backed by evidence
- ✅ Have correct metrics
- ✅ Tell a real story
- ✅ Show genuine impact

---

## Achievement Format

```
[Outcome-Oriented Title]

- [Point 1: Action + Measurable Result]
- [Point 2: Quality or Technical Improvement]
- [Point 3 (optional): Long-term Value]
```

### Examples

```
Payment Flow Reliability & Feature Completion
- Implemented retry logic preventing duplicate charges
- Resolved 3 critical bugs in payment submission
- Expanded test coverage by 35% (120 → 162 tests)

Frontend Performance Optimization
- Reduced bundle size by 12% (245KB → 215KB)
- Improved load time from 3.2s to 2.1s (34% faster)
- Implemented lazy loading for product catalog
```

---

## Standup Format

```
**Done:**
- [Merged work with PR reference]

**Next:**
- [In-progress work with % complete]

**Blockers:**
- [Blocked item with issue reference]
```

---

## 1:1 Format

```
**What I Delivered:**
- [Achievement 1]

**Impact:**
- [Why it mattered]

**Challenges:**
- [What you learned]

**Growth:**
- [Skills developed]

**Next Focus:**
- [What's next]

**Topics to Discuss:**
- [Discussion question]
```

---

## Metric Quick Reference

### Test Count
```
Before: 120 tests
After: 162 tests
Calculation: (162-120)/120 = 35%
✓ "Expanded test suite by 35%"
```

### Coverage
```
Before: 78% coverage
After: 84% coverage
Calculation: 84 - 78 = 12 percentage points
✓ "Increased line coverage by 12 percentage points"
```

### Performance
```
Before: 3.2s load time
After: 2.1s load time
Calculation: (2.1-3.2)/3.2 = -34%
✓ "Improved load time by 34%"
```

### Bundle Size
```
Before: 245KB
After: 215KB
Calculation: (215-245)/245 = -12%
✓ "Reduced bundle size by 12%"
```

---

## Common Achievement Patterns

### Feature + Quality
```
Feature Implementation + Tests + Validation + Error Handling = 1 Achievement
```

### Bug Clustering
```
Related bugs in same flow = 1 Reliability Achievement
```

### Performance Clustering
```
Memoization + Lazy Loading + Bundle Reduction = 1 Performance Achievement
```

### Developer Experience
```
CI Improvements + Test Tooling + Automation = 1 DX Achievement
```

---

## The Anti-BS Checklist

Before submitting an achievement:

- [ ] Can I point to specific evidence?
- [ ] Are all metrics calculated correctly?
- [ ] Have I avoided inventing percentages?
- [ ] Have I avoided inventing business impact?
- [ ] Is this the truth, just clearly told?
- [ ] Would I defend this in code review?
- [ ] Could someone else verify this?

If you can't check all boxes, the achievement needs work.

---

## Evidence Priority

Use this order for claims:

1. **Direct measurement** ← Best
   - Metrics, benchmarks, test results

2. **Actual code/diff**
   - Files changed, lines added

3. **PR/Issue context**
   - Description, review comments

4. **Commit message**
   - Description from Git

5. **Inference** ← Avoid
   - Logical deduction only

---

## Red Flags

These are signs you've gone wrong:

❌ "Improved user experience"
→ Need evidence: performance metrics, user feedback

❌ "Fixed many bugs"
→ Be specific: "Resolved 3 issues in payment flow"

❌ "Made improvements"
→ Vague: specify what improved and by how much

❌ "Increased by 50%"
→ Without before/after: invent percentage?

❌ "Delighted customers"
→ Need evidence: support tickets, feedback

---

## Getting It Right

### Bad Achievement

```
"Added features and fixed bugs and wrote tests"
```

### Good Achievement

```
Settings Page Delivery & Reliability

- Implemented settings page with API integration
- Added comprehensive form validation and error handling
- Wrote 12 tests covering main flows and edge cases
```

**What's different:**
- ✅ Grouped related work
- ✅ Outcome-oriented title
- ✅ Specific work described
- ✅ Measurable (12 tests)
- ✅ Clear value

---

## When to Use ShipLift

### Perfect For
- ✅ Quarterly reviews
- ✅ Performance evaluations
- ✅ Manager 1:1s
- ✅ Resume/portfolio updates
- ✅ Communicating impact
- ✅ Understanding what you accomplished

### Not For
- ❌ Detailed commit history (use `git log`)
- ❌ Code review feedback
- ❌ Time tracking
- ❌ Task management

---

## File Organization

| File | Read This For |
|------|---|
| README.md | Installation & overview |
| SKILL.md | Core concepts & philosophy |
| achievement-framework.md | How to group work |
| intelligence-rules.md | Work pattern recognition |
| evidence-matrix.md | Evidence validation |
| metrics.md | Calculating metrics correctly |
| anti-bs-rules.md | What NOT to do |
| impact-engine.md | Ranking achievements |
| commands.md | Command specifications |
| output-templates.md | Output examples |

---

## Troubleshooting

### "ShipLift isn't recognizing my work"

**Check:**
1. Is work merged to main branch?
2. Does work have supporting commits?
3. Does work have PR/issue context?
4. Is evidence in actual diffs?

### "Achievement seems overblown"

**Check:**
1. Review anti-bs-rules.md
2. Reduce claims
3. Remove invented metrics
4. Check evidence hierarchy

### "Metrics don't seem right"

**Check:**
1. Verify before/after values
2. Recalculate using formulas in metrics.md
3. Use correct formula (%, points, absolute)

---

## The Final Principle

> **Do not make the work sound bigger. Make the value of the work clearer.**

When in doubt:
- Be honest
- Show evidence
- Focus on impact
- Keep it simple

---

## Quick Links

- **How to Install:** See README.md
- **Full Documentation:** See SKILL.md
- **Validation Proof:** See VALIDATION_REPORT.md
- **Detailed Rules:** See references/ directory

---

Last Updated: 2026-08-31
Ready to Use: ✅ YES
