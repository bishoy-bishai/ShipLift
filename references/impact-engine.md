# Impact Engine

The Impact Engine ranks and evaluates candidate achievements to determine which are most meaningful.

---

## Ranking Framework

Use this framework to score candidate achievements and prioritize them.

### Scoring Dimensions

Each dimension is scored 0-10.

#### 1. Scope (0-10)

**What's the breadth of impact?**

- **0-2**: Tiny scope
  - 1 line change
  - 1 component
  - Single fix to one function

- **3-4**: Small scope
  - Single component improvements
  - One feature
  - Focused bug fix

- **5-6**: Medium scope
  - Multiple related components
  - System-wide improvement
  - Several related bugs

- **7-8**: Large scope
  - Major feature or system
  - Cross-cutting concern
  - Affects many components/workflows

- **9-10**: Massive scope
  - Architectural changes
  - Framework-wide improvements
  - Major product capability

---

#### 2. Complexity (0-10)

**How difficult was this work?**

- **0-2**: Simple
  - Straightforward implementation
  - No novel problems
  - Routine work

- **3-4**: Moderate
  - Some challenges to solve
  - Required learning
  - Non-trivial effort

- **5-6**: Complex
  - Significant challenges
  - Required research
  - Multiple iterations needed

- **7-8**: Very complex
  - Hard problems to solve
  - Deep expertise required
  - Architectural decisions

- **9-10**: Extremely complex
  - Breakthrough problem-solving
  - Requires state-of-art knowledge
  - Novel approach

---

#### 3. Impact (0-10)

**What's the value of this work?**

- **0-2**: Low impact
  - Nice-to-have improvement
  - Minimal user or product effect
  - Incremental work

- **3-4**: Modest impact
  - Addresses known problem
  - Improves one area
  - User benefit unclear

- **5-6**: Good impact
  - Solves important problem
  - Benefits multiple users/flows
  - Clear product value

- **7-8**: High impact
  - Solves critical problem
  - Broad user benefit
  - Significant product improvement

- **9-10**: Transformational impact
  - Enables new capability
  - Major competitive advantage
  - Transforms user experience

---

#### 4. Measurability (0-10)

**How well can we measure this?**

- **0-2**: Unmeasurable
  - Purely qualitative
  - No metrics available
  - Hard to quantify

- **3-4**: Partially measurable
  - Some metrics available
  - Requires estimation
  - Indirect measurement

- **5-6**: Measurable
  - Clear metrics available
  - Quantifiable improvement
  - Before/after data exists

- **7-8**: Highly measurable
  - Multiple metrics
  - Clear baseline and target
  - Easy to prove

- **9-10**: Perfectly measurable
  - Direct metrics
  - Precise before/after
  - Reproducible measurement

---

#### 5. Long-term Value (0-10)

**Does this create lasting value?**

- **0-2**: No lasting value
  - One-time fix
  - Doesn't enable future work
  - Technical debt

- **3-4**: Limited lasting value
  - Helps with current project
  - May need future updates
  - Local improvement

- **5-6**: Good lasting value
  - Enables future work
  - Reduces future friction
  - Platform improvement

- **7-8**: High lasting value
  - Foundational for future work
  - Enables many possibilities
  - Strategic platform move

- **9-10**: Transformational lasting value
  - Enables entire new capability set
  - Removes entire categories of problems
  - Architectural foundation

---

#### 6. Product Relevance (0-10)

**How aligned is this with product goals?**

- **0-2**: Not relevant
  - Internal only
  - Doesn't affect product
  - Random improvement

- **3-4**: Weakly relevant
  - Supports infrastructure
  - Nice-to-have
  - May help product indirectly

- **5-6**: Relevant
  - Supports product goals
  - Enables features
  - Improves experience

- **7-8**: Highly relevant
  - Core to product roadmap
  - Blocks other features
  - Customer requested

- **9-10**: Critical
  - Top product priority
  - Requested by major customers
  - Competitive necessity

---

#### 7. Evidence Confidence (0-10)

**How confident are we in this achievement?**

- **0-2**: Low confidence
  - Weak evidence
  - Mostly inference
  - Uncertain scope

- **3-4**: Modest confidence
  - Some evidence
  - Some inference needed
  - Measurements estimated

- **5-6**: Good confidence
  - Strong evidence
  - Measurements verified
  - PR/issue confirms

- **7-8**: High confidence
  - Multiple evidence sources
  - All measurements confirmed
  - Stakeholders validated

- **9-10**: Absolute confidence
  - Overwhelming evidence
  - All metrics precise
  - Peer reviewed

---

## Ranking Process

### Step 1: Score Each Achievement

Create a scoring matrix:

```
Achievement                          Scope  Complex  Impact  Measure  LT Value  Product  Evidence  TOTAL
─────────────────────────────────────────────────────────────────────────────────────────────────────────
Test Quality & Regression Protection  7     5       6       9        7         5        8        47/70
Dark Mode Support                      5     3       6       8        6         7        9        44/70
Payment Flow Reliability               6     6       8       9        8         9        9        55/70
Form Validation Standardization        6     4       6       8        7         6        8        45/70
```

### Step 2: Weight by Priority

Adjust weighting based on company priorities:

**Default weight (equal):**
All dimensions = 1.0x

**Product-focused weight:**
Impact and Product Relevance = 2.0x
Other dimensions = 1.0x

**Engineering-focused weight:**
Complexity and Long-term Value = 2.0x
Other dimensions = 1.0x

### Step 3: Calculate Weighted Score

```
Weighted Score = (Scope × w) + (Complex × w) + (Impact × w) + (Measure × w) + 
                 (LTValue × w) + (Product × w) + (Evidence × w)
```

### Step 4: Rank Highest to Lowest

```
1. Payment Flow Reliability (highest score)
2. Test Quality & Regression Protection
3. Form Validation Standardization
4. Dark Mode Support
5. ...
```

---

## Selection Rules

### Rule 1: Prefer Impact Over Activity

Given a choice:

```
Option A: "Refactored 15 files" (high activity, medium impact)
Option B: "Reduced payment errors by 40%" (lower activity, high impact)

Choose: Option B
```

### Rule 2: Prefer Measurable Over Qualitative

Given a choice:

```
Option A: "Improved performance" (qualitative)
Option B: "Reduced load time by 35%" (measurable)

Choose: Option B
```

### Rule 3: Prefer Product Value Over Technical Elegance

Given a choice:

```
Option A: "Refactored service layer with dependency injection" (technical)
Option B: "Enabled dark mode support" (product feature)

Choose: Option B
```

### Rule 4: Prefer Broad Over Narrow

Given a choice:

```
Option A: "Fixed authentication edge case" (narrow)
Option B: "Hardened authentication across 5 flows" (broad)

Choose: Option B
```

---

## Duplicate Detection

Before finalizing, check for duplicates:

```
Achievement 1: "Improved API response time by 25%"
Achievement 2: "Optimized API performance"

Problem: Same story, different framing
Action: Merge into one achievement
```

---

## Acceptance Rules

For Quarter output (5-7 achievements):

**Minimum score for inclusion:**
- Impact score ≥ 5 (moderate impact minimum)
- Evidence confidence ≥ 6 (good confidence minimum)
- OR Scope ≥ 7 AND Impact ≥ 6 (large scope with good impact)

**Acceptable distribution:**

```
❌ 7 small fixes (low impact)
❌ 1 massive achievement (lacks breadth)
✓ 3-5 high-impact achievements
✓ 1-2 medium-impact achievements
✓ Mix of product and technical value
```

---

## Special Ranking Rules

### Rule: Don't Overscore Familiar Work

Familiar work often feels more impactful than it is.

**Correction:**
- Score objectively against the framework
- Compare against other achievements
- Don't let comfort bias the score

### Rule: Don't Underscore Novel Work

Novel work might feel uncertain.

**Correction:**
- Score on proven impact, not perception
- Use evidence confidence for uncertainty
- Don't let novelty bias downward

### Rule: Cluster Scores

Achievements shouldn't spread evenly across the scale.

**Natural distribution for tech team:**

```
10 highest-score achievements
 5 high-score achievements
 2-3 medium-score achievements
 0-1 low-score achievements (usually excluded)
```

---

## Impact Decay

As time passes from achievement, impact perception may change:

- **Immediate impact** (first month): Use measured data
- **Medium-term impact** (1-3 months): Monitor usage/feedback
- **Long-term impact** (3+ months): Observe compound effects

**Rule:** Don't artificially inflate scores based on potential.

---

## Context-Dependent Ranking

Impact scoring depends on context:

### In Startup Context:

- Product relevance: 2.0x weight (critical)
- Measurability: 0.5x weight (less data available)
- Long-term value: 1.5x weight (foundation matters)

### In Large Enterprise:

- Scope: 1.5x weight (broad impact valued)
- Complexity: 1.5x weight (expertise valued)
- Long-term value: 1.5x weight (platform thinking)

### In Data Company:

- Measurability: 2.0x weight (proof required)
- Impact: 1.5x weight (metrics-driven)
- Evidence confidence: 1.5x weight (rigor)

---

## Checklist: Impact Evaluation

For each achievement:

- [ ] Have I scored all seven dimensions?
- [ ] Are scores based on evidence, not gut feel?
- [ ] Have I compared against other achievements?
- [ ] Have I checked for duplicates?
- [ ] Is this meeting minimum thresholds?
- [ ] Have I weighted appropriately for context?
- [ ] Are rankings sorted high to low?
- [ ] Have I selected top achievements for output?
