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

ShipLift follows the **Agent Skills** standard (a plain `SKILL.md` at the repository root) and can be installed into any compatible AI coding agent. It also ships a `.claude-plugin/` manifest for Claude Code's native plugin system specifically. Use whichever matches your agent:

| Method | Best for |
|---|---|
| [Skills CLI](#recommended--skills-cli) (`npx skills`) | Any supported agent, cross-platform |
| [GitHub CLI](#github-cli) (`gh skill install`) | Anyone already using `gh` |
| [Claude Code plugin marketplace](#claude-code-plugin-marketplace) | Claude Code users who want native `/plugin` management |
| [Manual installation](#-manual-installation) | Any agent, no extra tooling required |

## Recommended — Skills CLI

The easiest way to install ShipLift is using `npx skills`. ✅ Every command in this section was smoke-tested against the live `bishoy-bishai/ShipLift` repository.

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

If you use GitHub CLI (v2.90.0+), you can install ShipLift with `gh skill install`. ⚠️ This syntax is verified against GitHub's official `gh skill` documentation; it has not been smoke-tested from this environment (`gh` is not installed here). Run `gh --version` first to confirm you have v2.90.0 or later.

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

## Claude Code Plugin Marketplace

ShipLift also ships a `.claude-plugin/marketplace.json`, so Claude Code can add this repository directly as a plugin marketplace and install ShipLift as a native plugin:

```text
/plugin marketplace add bishoy-bishai/ShipLift
/plugin install shiplift@shiplift
```

✅ Smoke-tested end-to-end (`claude plugin marketplace add`, `claude plugin install`, `claude plugin details`) against this repository — installs cleanly as a single `shiplift` skill, ~98 tokens always-on.

This is the Claude Code–specific path — the Skills CLI and GitHub CLI methods above work across every supported agent, including Claude Code.

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

# 💬 What You Can Ask

ShipLift recognizes plain-English requests, not just explicit commands:

```text
Analyze my work this quarter.
What did I accomplish this week?
Prepare me for my 1:1.
What are my strongest engineering achievements?
Turn my work into CV bullets.
How does my work map to my goals?
```

Explicit commands work too, and are equivalent:

```text
ShipLift Quarter
ShipLift Standup
ShipLift 1:1
ShipLift Goals
ShipLift CV
ShipLift Pulse
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
├── .claude-plugin/
│   ├── plugin.json          (Claude Code plugin manifest)
│   └── marketplace.json     (lets this repo be added as a plugin marketplace)
│
├── .github/workflows/
│   └── validate.yml         (CI: structure, security, and test validation)
│
├── SKILL.md
├── README.md
├── LICENSE
├── VALIDATION.md
│
├── references/
│   ├── achievement-framework.md
│   ├── anti-bs-rules.md
│   ├── commands.md
│   ├── evidence-matrix.md
│   ├── impact-engine.md
│   ├── intelligence-rules.md
│   ├── metrics.md
│   ├── output-templates.md
│   ├── goals-engine.md
│   ├── career-evidence-engine.md
│   ├── pulse-engine.md
│   └── core/
│       ├── evidence-engine.md
│       ├── evidence-linking.md
│       ├── evidence-strength.md
│       ├── impact-analysis.md
│       ├── signal-detection.md
│       ├── blind-spots.md
│       ├── anti-inflation.md
│       └── writing-constitution.md
│
└── scripts/
    ├── git-analysis.sh          (repository snapshot helper)
    ├── pulse-store.sh           (Pulse EvidenceStore CLI)
    ├── pulse_store.py
    ├── evidence-engine.sh       (Evidence Engine CLI)
    ├── evidence_engine.py
    ├── validate-skill.py        (structure / security validator)
    └── tests/
        └── test_behavioral_rules.py
```

---

# 🔒 Privacy & Security

This section describes what the code actually does, not a marketing claim.

**Where data lives:** Pulse evidence is stored as local JSON files under `~/.shiplift/companies/<company-id>/evidence.json` (see `scripts/pulse_store.py`). Nothing is written inside your project repository.

**Network access:** none of the scripts in `scripts/` make network requests. There is no `curl`, `wget`, `requests`, `urllib`, or socket usage anywhere in the codebase — verified by inspection, not assumed. Git operations (`git log`, `git diff`, etc.) talk to your local Git repository only; ShipLift never runs `git push`/`git fetch`/`git clone` on your behalf.

**Execution:** scripts are plain `bash`/`python3` with no `eval`, no dynamic code execution, and no shell interpolation of untrusted input. `python3 -B` is used to avoid writing `__pycache__` into your project.

**Credentials:** ShipLift requires no API keys, tokens, or accounts. It reads only local Git history and locally stored Pulse evidence.

**What we do *not* claim:** we don't say "100% local" or "no data ever leaves the machine" as a blanket guarantee — that depends on what your coding agent itself does with the conversation (e.g., if your agent sends conversation content to a cloud model, that's the agent's behavior, not ShipLift's). What we can state from the code: ShipLift's own scripts perform no network I/O and no telemetry.

---

# 🧭 Compatibility

- **Generic Agent Skills** (`SKILL.md` at the repository root): works with any agent that supports the open Agent Skills format — installable via the [Skills CLI](#recommended--skills-cli) or [GitHub CLI](#github-cli) into Claude Code, OpenAI Codex, Cursor, and others.
- **Claude Code plugin packaging** (`.claude-plugin/plugin.json` + `marketplace.json`): Claude Code–specific, enables native `/plugin marketplace add` / `/plugin install` management. Other agents ignore this directory.
- ShipLift makes no assumptions about your repository's language, framework, test runner, or CI system — see [Implementation Details](SKILL.md#implementation-details) in `SKILL.md`.

---

# ✅ Validation

Before relying on a change to this skill, run:

```bash
python3 scripts/validate-skill.py           # structure, manifest, links, secrets, hard-coded paths
python3 scripts/tests/test_behavioral_rules.py  # anti-inflation / evidence-safety rule checks
bash scripts/test-evidence-engine.sh
bash scripts/test-pulse-store.sh
python3 scripts/test_evidence_engine.py
```

All five run automatically in CI (`.github/workflows/validate.yml`) on every push and pull request.

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
