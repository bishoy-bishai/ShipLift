# 🚀 ShipLift

**Transform engineering work into meaningful achievements.**

ShipLift analyzes your repository and converts raw engineering activity into clear, evidence-backed achievements.

The goal is not to summarize commits.

The goal is to understand:

* What you shipped
* Why it matters
* What impact it had
* What evidence proves it
* How it connects to your goals
* How to communicate it clearly

ShipLift combines **code evidence** with **human evidence** — because Git can see your code, but it cannot see everything you do.

---

# 🚀 Installation

ShipLift follows the **Agent Skills** standard and can be installed into compatible AI coding agents.

## Recommended — Skills CLI

The easiest way to install ShipLift is using `npx skills`.

### Install ShipLift

```bash
npx skills add bishoy-bishai/ShipLift
```

The installer will detect the supported agents on your machine and let you choose where to install the skill.

### Install for specific agents

#### Claude Code

```bash
npx skills add bishoy-bishai/ShipLift -a claude-code
```

#### OpenAI Codex

```bash
npx skills add bishoy-bishai/ShipLift -a codex
```

#### Cursor

```bash
npx skills add bishoy-bishai/ShipLift -a cursor
```

#### Google Antigravity

```bash
npx skills add bishoy-bishai/ShipLift -a antigravity
```

### Install for multiple agents

You can install ShipLift into multiple agents with one command:

```bash
npx skills add bishoy-bishai/ShipLift \
  -a claude-code \
  -a codex \
  -a cursor \
  -a antigravity
```

### Install globally

To make ShipLift available across your projects:

```bash
npx skills add bishoy-bishai/ShipLift -g
```

Or globally for specific agents:

```bash
npx skills add bishoy-bishai/ShipLift \
  -g \
  -a claude-code \
  -a codex \
  -a cursor \
  -a antigravity
```

---

## GitHub CLI

If you use GitHub CLI, you can install ShipLift with `gh skill install`.

### Claude Code

```bash
gh skill install bishoy-bishai/ShipLift \
  --agent claude-code \
  --scope user
```

### OpenAI Codex

```bash
gh skill install bishoy-bishai/ShipLift \
  --agent codex \
  --scope user
```

### Cursor

```bash
gh skill install bishoy-bishai/ShipLift \
  --agent cursor \
  --scope user
```

### Antigravity

```bash
gh skill install bishoy-bishai/ShipLift \
  --agent antigravity \
  --scope user
```

---

# ✅ Verify Installation

After installation, open or restart your AI coding agent.

Run:

```text
ShipLift Pulse
```

If ShipLift is installed correctly, the agent should recognize the command and start the Pulse flow.

You can also test the main analysis:

```text
ShipLift Quarter
```

And the other commands:

```text
ShipLift Goals

ShipLift Standup

ShipLift 1:1

ShipLift CV
```

---

# 🔄 Update ShipLift

To update skills installed through the Skills CLI:

```bash
npx skills update
```

To update a GitHub CLI installation:

```bash
gh skill update
```

---

# 🛠️ Manual Installation

If you prefer to install ShipLift manually, clone the repository:

```bash
git clone https://github.com/bishoy-bishai/ShipLift.git
```

Then copy the ShipLift skill directory into the skills directory supported by your AI coding agent.

The skill entry point is:

```text
SKILL.md
```

The skill also includes:

```text
references/
scripts/
```

`SKILL.md` is the main entry point.

The `references/` directory contains ShipLift's intelligence, rules, frameworks, and output specifications.

The `scripts/` directory contains local helper scripts used by the skill.

> **Recommended:** Use `npx skills add bishoy-bishai/ShipLift` whenever possible. It handles the agent-specific installation for you.

---

# ⚡ Quick Start

After installation, start with:

```text
ShipLift Pulse
```

Pulse captures important work that Git cannot see.

Then run:

```text
ShipLift Quarter
```

to analyze your current quarter.

For goals:

```text
ShipLift Goals
```

For your standup:

```text
ShipLift Standup
```

For your next manager 1:1:

```text
ShipLift 1:1
```

For your CV:

```text
ShipLift CV
```

---

# 🧠 What ShipLift Does

ShipLift analyzes your engineering work and turns it into meaningful career evidence.

It uses two main evidence sources:

```text
                    SHIPLIFT
                       │
          ┌────────────┴────────────┐
          ↓                         ↓
     CODE EVIDENCE             HUMAN EVIDENCE
          │                         │
         Git                      Pulse
          │                         │
          └────────────┬────────────┘
                       ↓
                EVIDENCE ENGINE
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       Linking      Strength      Signals
          │            │            │
          └────────────┼────────────┘
                       ↓
                 IMPACT ANALYSIS
                       ↓
                ANTI-INFLATION
                       ↓
               CAREER INTELLIGENCE
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
    Achievements     Goals          CV
          │            │            │
          └────────────┼────────────┘
                       ↓
                 Standup / 1:1
```

The core idea:

> **Make the value of the work clearer, not bigger.**

---

# ✨ What ShipLift Can Do

## 🏆 Quarterly Achievements

Analyze the current calendar quarter and return **5–7 strongest achievements**.

ShipLift does not simply list commits.

Instead, it groups related work into meaningful engineering stories.

For example:

```text
Added 12 tests
Fixed 4 bugs
Updated 6 components
Reviewed 8 PRs
```

can become:

### Test Quality & Regression Protection

**8 points**

* Increased the automated test suite by 35%.
* Added regression tests for critical flows.
* Improved coverage of important edge cases.

The goal is to communicate the **achievement**, not the activity list.

---

# 🎯 Goals

ShipLift connects your achievements and evidence to your professional goals.

Example:

```text
Achievement
     ↓
Goal
     ↓
SMART validation
     ↓
Goal alignment
     ↓
Evidence
     ↓
Progress
     ↓
Gaps
```

ShipLift can also identify recurring themes in your work and suggest possible goals.

It never presents a suggested goal as an official goal unless you confirm it.

---

# 🗣️ Standup

ShipLift combines recent Git activity with Pulse evidence.

Example:

```text
## Standup

Done:
- Fixed authentication validation issue
- Added regression tests
- Helped a teammate with a React issue

Next:
- Continue authentication edge cases

Blockers:
- None
```

---

# 🤝 1:1

ShipLift prepares evidence-backed talking points for your manager 1:1.

It can surface:

* What you delivered
* Impact
* Challenges
* Goal progress
* Technical ownership
* Collaboration
* Investigations
* Initiatives
* Growth
* Topics to discuss

---

# 📄 CV

ShipLift can analyze your engineering history and turn meaningful work into CV-ready bullets.

It focuses on:

```text
Real evidence
+
Clear contribution
+
Measured results
+
Known impact
```

It never invents metrics.

Example:

```text
Increased the automated test suite by 35% and added
regression coverage for critical frontend flows.
```

You can also scope the analysis:

```text
ShipLift CV 2026

ShipLift CV Q1 2026

ShipLift CV last 2 years

ShipLift CV Senior

ShipLift CV Lead
```

The scope changes what is emphasized — never what is invented.

---

# 🧘 Pulse

Not everything you do appears in Git.

That's why ShipLift has **Pulse**.

Pulse is a short, adaptive Q&A designed to capture the work Git cannot see.

For example:

```text
Did you help anyone yesterday?

Did you review someone's code?

Did you make an important technical decision?

Did you investigate something?

Did you start an initiative?

Did you unblock anyone?

Did you do anything important that wouldn't show up in Git?
```

Pulse is:

* **Short** — usually 30–90 seconds
* **Adaptive** — avoids unnecessary questions
* **Evidence-based** — records what you actually said
* **Local-first** — stored under `~/.shiplift/`
* **Integrated** — feeds Quarter, Goals, Standup, 1:1, and CV

"Nothing" and "Not sure" are valid answers.

Pulse never pressures you to manufacture an achievement.

---

# 🔗 Evidence Linking

ShipLift does not treat every activity as a separate achievement.

It connects related evidence.

For example:

```text
Started investigation
        ↓
Found root cause
        ↓
Implemented fix
        ↓
Added regression tests
        ↓
Shared findings with the team
```

This can become one meaningful engineering story.

---

# 📈 Impact Analysis

ShipLift separates:

```text
Activity
Contribution
Impact
Outcome
```

These are not the same thing.

For example:

```text
Reviewed 5 PRs
```

does not automatically mean:

```text
Improved team productivity by 30%.
```

If the impact is unknown, ShipLift says:

```text
Impact: Unknown
```

That's intentional.

---

# 🛡️ Anti-BS Engine

ShipLift follows one important rule:

> **Never make the engineer sound more impressive than the evidence allows.**

ShipLift does not invent:

* Percentages
* Productivity improvements
* Revenue impact
* Cost savings
* Users affected
* Time saved
* Business results
* Leadership claims

It also avoids turning small activities into huge achievements.

```text
Activity ≠ Impact

Volume ≠ Impact

Attendance ≠ Contribution

Contribution ≠ Business Result
```

---

# 🧠 Career Signals

Over time, ShipLift can identify recurring patterns.

For example:

```text
Repeated code reviews
+
Helping teammates
+
Testing improvements
+
Technical discussions
```

may indicate:

> Consistent contribution to engineering quality and collaboration.

Signals are not automatically treated as achievements.

They become stronger as evidence accumulates.

---

# 🔍 Blind Spots

ShipLift can identify areas where evidence is limited.

Example:

```text
Technical Delivery      Strong
Code Quality            Strong
Problem Solving         Strong
Ownership               Moderate
Collaboration           Moderate
Mentoring               Limited
Cross-team Impact       Limited
```

ShipLift does not say:

> "You did not mentor anyone."

It says:

> **"ShipLift has limited evidence of mentoring this quarter."**

ShipLift knows what it has evidence for.

It does not know everything you did.

---

# 📝 Writing Style

ShipLift uses a strict writing constitution.

The language should be:

* Simple
* Clear
* Direct
* Human
* Professional
* Evidence-based

It should sound like:

> **A senior engineer explaining their work to another engineer.**

Not like:

* HR
* A recruiter
* A consultant
* A marketing website
* An AI-generated performance review

### Example

❌

> Spearheaded a transformative initiative that significantly enhanced the organization's automated testing capabilities.

✅

> Increased automated test coverage by 35% and added regression tests for critical flows.

---

# 🚫 No Corporate Buzzwords

ShipLift avoids unnecessary language such as:

```text
spearheaded
leveraged
facilitated
orchestrated
synergized
empowered
fostered
cultivated
operationalized
best-in-class
world-class
game-changing
transformative
cutting-edge
```

Simple language wins.

---

# 🏗️ Architecture

## Directory Structure

```text
ShipLift/
│
├── SKILL.md
├── README.md
├── VALIDATION.md
│
├── references/
│   ├── achievement-framework.md
│   ├── commands.md
│   ├── evidence-matrix.md
│   ├── impact-engine.md
│   ├── intelligence-rules.md
│   ├── anti-bs-rules.md
│   ├── metrics.md
│   ├── output-templates.md
│   ├── goals-engine.md
│   ├── career-evidence-engine.md
│   └── pulse-engine.md
│
└── scripts/
    ├── git-analysis.sh
    ├── pulse-store.sh
    └── pulse_store.py
```

---

# 🧩 Core Intelligence

ShipLift's intelligence layer is built around:

### Evidence

What actually happened.

### Linking

Which pieces of evidence belong together.

### Strength

How strong the evidence is.

### Impact

What changed because of the work.

### Signals

Patterns that appear over time.

### Blind Spots

Areas where evidence is missing or weak.

### Anti-Inflation

Protection against unsupported claims.

### Writing Constitution

Rules controlling how ShipLift communicates.

---

# 🧪 Design Principles

## 1. Evidence Over Adjectives

Bad:

> Huge improvement in engineering quality.

Good:

> Increased test coverage by 35%.

---

## 2. Facts Over Assumptions

Bad:

> Improved productivity by 20%.

when there is no measurement.

Good:

> Added automated tests for critical flows.

---

## 3. Stories Over Activity Lists

Bad:

```text
Added test
Fixed bug
Reviewed PR
Changed component
```

Good:

> Improved automated testing by increasing coverage and adding regression protection for critical flows.

---

## 4. Real Work Over Impressive Language

ShipLift should make your work easier to see.

It should not make your story bigger.

---

# 🔄 Recommended Workflow

### During the week

Use:

```text
ShipLift Pulse
```

when you finish something meaningful that may not appear clearly in Git.

For example:

* Helped someone
* Reviewed code
* Investigated a problem
* Made a technical decision
* Started an initiative
* Documented something
* Unblocked the team

### During the quarter

Use:

```text
ShipLift Goals
```

to understand how your work supports your goals.

### Before standup

```text
ShipLift Standup
```

### Before your 1:1

```text
ShipLift 1:1
```

### End of quarter

```text
ShipLift Quarter
```

### CV update

```text
ShipLift CV
```

---

# 🛣️ Roadmap

ShipLift is designed to grow around the Evidence Engine.

Potential future evidence sources include:

```text
GitHub
Linear
Jira
Slack
Notion
Calendar
```

The architecture is intentionally designed so new sources can feed the same evidence system.

The goal is not to add more commands.

The goal is to make the existing commands smarter.

---

# 🤝 Contributing

Contributions are welcome.

When contributing, keep the core philosophy intact:

```text
Simple
Evidence-based
Local-first
Human
No unnecessary complexity
No inflated claims
```

If a feature makes ShipLift more complicated without making the evidence better, question whether it belongs.

---

# ⭐ The Philosophy

Most career systems ask:

> "What did you accomplish?"

ShipLift asks a better question:

> **"What evidence do we have of the value you created?"**

Because engineers are usually good at building things.

They're not always good at remembering them.

And they're even worse at explaining them six months later.

ShipLift helps with that.

---

# 🚀 Get Started

Install ShipLift:

```bash
npx skills add bishoy-bishai/ShipLift
```

Then run:

```text
ShipLift Pulse
```

Start capturing the work that Git cannot see.

When you're ready:

```text
ShipLift Quarter
```

See what you actually accomplished.

---

## ShipLift

> **Make your real work visible.**
