# Pulse Engine

The Pulse Engine powers `ShipLift Pulse` — the **Human Work Evidence Engine**.

It answers a question none of the other commands answer:

> **What did I contribute that Git cannot see?**

This file contains the detailed behavior and evidence rules for `ShipLift Pulse`. See [Commands](commands.md) for the command contract and [Output Templates](output-templates.md) for the exact output format.

---

## 1. Core Principle

> **Git records what you changed. Pulse records what you contributed.**

Pulse captures facts. It does not coach the user into exaggerating impact.

```
User:  "I reviewed 3 PRs."

Correct:
  Category: Code Review
  Description: Reviewed 3 PRs.
  Metadata: PR count = 3
  Source: User
  Impact: Unknown

Forbidden:
  "Improved team productivity by 30%."
  (Not said by the user, not evidenced.)
```

Every ShipLift [Anti-BS Rule](anti-bs-rules.md) applies to Pulse. Pulse adds one more: **never turn a user's statement into a bigger claim than the user made.**

---

## 2. Architecture: Pulse Is a Source, Not a Silo

```
                         ShipLift
                            │
                     Evidence Layer
                            │
              ┌─────────────┴─────────────┐
              ↓                           ↓
        CODE EVIDENCE               HUMAN EVIDENCE
              │                           │
             Git                        Pulse
              │                           │
              └─────────────┬─────────────┘
                            ↓
                    Evidence Engine
                            ↓
                  Achievement Engine
                            │
          ┌─────────────────┼─────────────────┐
          ↓                 ↓                 ↓
       Quarter            Goals              CV
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ↓
                           1:1
```

Pulse does not replace or duplicate the Achievement Engine, Goals Engine, or Career Evidence Engine. It feeds them a second evidence source. Do not build a parallel achievement/goal/CV system for Pulse data.

### Layers (mandatory, do not collapse)

```
Pulse Input        — the user's raw natural-language answer
    ↓
Raw Evidence        — a structured EvidenceItem (this file, §3)
    ↓
Contribution        — an interpretation made later by the Achievement Engine
    ↓
Achievement          — a Quarter/CV-style achievement, if evidence supports it
    ↓
Impact               — only when real evidence of outcome exists
    ↓
Goals / CV / 1:1 / Quarter
```

Pulse only produces the first two layers (Input → Raw Evidence). It must never generate a Contribution, Achievement, or Impact label itself — that is the Achievement Engine's job, using the existing rules in [Achievement Framework](achievement-framework.md), [Impact Engine](impact-engine.md), and [Anti-BS Rules](anti-bs-rules.md).

---

## 3. Evidence Model

Each Pulse evidence item (an "EvidenceItem") conceptually contains:

```
id            unique identifier
date          the work date (when the work happened)
captured_at   when Pulse recorded it (may differ from date — see §9)
company       which company/project this belongs to
category      one of the categories in §4, or omitted if unclear
description   a plain factual restatement of what the user said
source        "user" for Pulse-created evidence (see §5)
confidence    High / Medium / Low (see §8)
metadata      free-form structured details (e.g. PR count)
impact        "Unknown" unless the user gave real evidence of outcome
```

Implementation reference: `scripts/pulse-store.sh` (backed by `scripts/pulse_store.py`) implements this model as the MVP `JSONStore`. See §12.

### Description Must Be a Restatement, Not an Upgrade

```
User:      "Helped Ahmed fix a React rendering issue."
Correct:   "Helped a teammate resolve a React rendering issue."
Forbidden: "Provided technical mentorship that resolved a critical
            frontend defect."
```

---

## 4. Categories

```
Collaboration
Mentoring
Code Review
Technical Decision
Investigation
Initiative
Incident Response
Documentation
Knowledge Sharing
Planning
Communication
Problem Solving
Unblocking
Process Improvement
Other
```

If a user's answer doesn't clearly map to one category, either:
- pick the closest fit and note the ambiguity in `description`, or
- use `Other` rather than forcing a bad fit.

Never invent a category outside this list without clear justification, and never leave an item mis-categorized just to avoid using `Other`.

---

## 5. Evidence Source

Pulse-created evidence is always recorded with:

```
source: user
```

The store's data model reserves this field for future non-Pulse integrations so they can be added without a schema change:

```
git
github
linear
slack
notion
calendar
```

Pulse itself never sets any source other than `user`.

---

## 6. Privacy and Storage

Career evidence is personal data.

- **Local only by default.** Never upload, sync, or transmit Pulse content anywhere unless the user explicitly opts into a future sync/integration feature.
- **Never store inside the project repository.** Pulse data does not belong in Git history, `.git/`, or any tracked file — see §12 for the storage location.
- **Never log raw Pulse answers** in application/agent logs beyond the EvidenceStore's own JSON file.
- Company isolation is mandatory — see §11.

---

## 7. The Question Flow

Pulse is question-driven, not a blank "what did you do today?" prompt.

### Opening question

```
What did you work on yesterday?
```

### Adaptive branches (ask only what's relevant; skip what isn't)

1. **Collaboration** — "Did you help anyone yesterday?" → if yes: "What did you help them with?"
2. **Code Review** — "Did you review someone else's code?" → if yes: "Roughly how many PRs?" → "Did you catch or discuss anything important?"
3. **Initiative** — "Did you start or contribute to something bigger than a single task?" → if yes: "What did you work on?"
4. **Technical Decisions** — "Did you have a technical discussion that affected how something will be built?" → if yes: "What was the decision or discussion about?" → when relevant: "Did you help evaluate or decide the approach?"
5. **Unblocking** — "Did something move forward because of something you did?" → if yes: "What moved forward?" (never ask the user to quantify impact unless they already know it)
6. **Investigation** — "Did you spend time investigating, researching, debugging, or learning something related to the work?" → if yes: "What were you investigating?"
7. **Non-Git catch-all** — "Is there anything important you did yesterday that wouldn't show up in Git?" (always asked last)

### Adaptive rules

- Do not ask every branch every day. Use the opening answer to skip branches that are clearly already covered (e.g. the user mentions "reviewed 3 PRs" in their opening answer — don't re-ask the Code Review question, just ask the follow-up).
- Ask branches in roughly the order above, but skip ahead or reorder when the user's answers make a branch obviously irrelevant or already answered.
- Target length: **30–90 seconds** for a normal day. If the user is answering "no" or "not sure" quickly, move faster — don't force all seven branches.
- The catch-all question is always asked, even on a quiet day, because it's the one designed to catch things the structured branches miss.

---

## 8. Accepting Natural Answers

Support free-form natural language for every question, including:

```
yes / no / nope / not really / not sure / nothing / skip
```

and full free-text answers. Do not force multiple-choice or structured input when a natural sentence is easier for the user.

### "Not sure" is valid

```
User: Not sure.
Pulse: No worries. Let's move on.
```

Do not pressure the user to be more certain than they are. If they do give an answer after "not sure," record it with `confidence: Medium` (or `Low` if still vague) — see below.

### "Nothing" / "skip" is valid

```
User: Nothing.
Pulse: (accepts and moves to the next question, or ends if it's the last one)
```

Never repeatedly re-ask a question to manufacture an achievement. If the whole session ends this way:

```
No additional evidence captured.
```

is a complete, valid Pulse run — not a failure.

### Confidence assignment

```
Clear, specific, factual statement           → High
Vague, hedged, or partial statement          → Medium
Highly uncertain ("I think maybe...")        → Low
```

```
User: "I think I helped someone with some React issue."
Confidence: Medium
```

Never convert a user's uncertainty into `High` confidence.

---

## 9. Date Handling

Two distinct dates exist and must not be conflated:

```
date          — the work date (when the work happened)
captured_at   — when Pulse recorded the entry (now)
```

- If the user says "yesterday," `date` = the calendar day before the capture date.
- If the user gives an explicit date, use it for `date`.
- If neither, default `date` to the capture date, but prefer asking rather than guessing when it matters (e.g. a correction session days later).

---

## 10. Duplicate Detection

Before saving new evidence, check existing evidence (same company, ideally same/nearby date and category) for similar descriptions using `pulse-store.sh check-duplicate`.

If a likely duplicate is found:

```
This looks similar to an existing entry:
"Helped Ahmed fix a React rendering issue." (2026-08-31)

Add as a new contribution or update the existing one?
```

Never silently merge two entries the agent isn't sure are duplicates — ask. Never silently create a duplicate either — always run the check first when saving.

---

## 11. Company Isolation

Every evidence item belongs to exactly one company. Never mix evidence across companies.

- If the current project/repository context makes the company obvious, use it without asking.
- If it's ambiguous (e.g. no repository context, or the user works across multiple companies), ask which company this evidence belongs to. Do not guess.
- The EvidenceStore enforces isolation structurally: each company has its own `evidence.json` under `~/.shiplift/companies/<company-id>/`.

---

## 12. Storage — EvidenceStore Abstraction

Pulse evidence is stored **outside the project repository**, under the user's home directory:

```
~/.shiplift/
├── config.json
└── companies/
    └── <company-id>/
        └── evidence.json
```

The MVP implementation is a `JSONStore`, implemented in `scripts/pulse_store.py` and exposed via `scripts/pulse-store.sh` (same pattern as `scripts/git-analysis.sh`). Do not hard-code file paths or JSON parsing elsewhere in the skill — always go through this script so storage can evolve later (e.g. `SQLiteStore`, `CloudStore`) without changing how commands consume evidence.

### CLI surface (mirrors the conceptual `EvidenceStore` API)

```
pulse-store.sh init [--company ID]
pulse-store.sh add --company ID --category CAT --description TEXT
                    [--work-date YYYY-MM-DD] [--confidence High|Medium|Low]
                    [--metadata JSON]
pulse-store.sh check-duplicate --company ID --description TEXT [--category CAT]
pulse-store.sh update --company ID --id ID [--description TEXT] [--metadata JSON]
pulse-store.sh list --company ID [--category CAT] [--date D] [--since D] [--until D]
pulse-store.sh recent --company ID [--days N]
pulse-store.sh by-quarter --company ID --quarter YYYY-QN
pulse-store.sh companies
```

These map directly onto the conceptual retrieval API used by other commands: `getRecent()`, `getByDate()`, `getByQuarter()`, `getByCompany()`, `getByCategory()`. Build only what current commands need — do not over-engineer additional query methods speculatively.

---

## 13. Correction Flow

A later `ShipLift Pulse` invocation may correct earlier evidence:

```
User: Actually, yesterday I didn't review 3 PRs. It was 2.
```

When the target entry is clear (recent, same category, matching description), update it in place via `pulse-store.sh update` rather than adding a new duplicate entry. If the target is ambiguous (e.g. multiple similar entries, or an old date), ask which entry the user means rather than guessing.

---

## 14. Summary Output

At the end of a Pulse session, show a concise, grouped summary of what was captured (see [Output Templates](output-templates.md) for the exact format), then ask:

```
Anything else?
```

If no:

```
Pulse saved.
```

Never produce a long report — Pulse's summary should be scannable in a few seconds.

---

## 15. Tone

Pulse should feel like:

> A friend asking simple questions to help you remember what you did.

Not:

> A manager asking you to justify your performance.

- Friendly, short, non-judgmental, conversational, simple English.
- No corporate language ("synergy," "leverage," "drove outcomes").
- Never imply the user under-performed if they say "nothing."

---

## 16. Integration Rules

### With ShipLift Standup

`ShipLift Standup` may combine Git evidence with recent Pulse evidence (matching the standup's time window) to produce a richer, still fully evidence-based `Done / Next / Blockers`. This does not change the Standup output contract. Pulse items appear as plain facts (e.g. "helped a teammate with a React issue," "reviewed 3 PRs"), never upgraded into invented impact.

### With ShipLift Quarter

Quarter's Achievement Engine may take Pulse evidence for the quarter as additional input alongside Git evidence, enabling achievements like "Technical Collaboration" or "Investigation & Problem Solving" to exist even with limited Git evidence. Pulse evidence goes through the same clustering, ranking, and Anti-BS validation as Git evidence — it gets no special treatment or extra credibility.

### With ShipLift Goals

Pulse evidence may be used as **supporting evidence** for goals (e.g. a "Collaboration" or "Technical Decision" goal). Per the [Goals Engine](goals-engine.md) rules, evidence existing does not mean a goal is achieved — apply the same progress and completion rules unchanged.

### With ShipLift CV

Pulse evidence may support CV bullets when the [Career Evidence Engine](career-evidence-engine.md) evidence-strength rules are met (§6 there). A single vague Pulse entry ("helped with something") is Weak evidence and should not produce a CV bullet on its own; multiple consistent Pulse entries across time (e.g. repeated PR reviews with real findings) can combine into Medium/Strong evidence exactly like repeated Git-based work does.

### With ShipLift 1:1

`ShipLift 1:1` may reference Pulse evidence (collaboration, mentoring, technical decisions, initiatives, investigations, unblocking, knowledge sharing) as discussion-ready talking points, without changing the existing 1:1 output contract (`What I Delivered / Impact / Challenges / Growth / Next Focus / Topics to Discuss`).

---

## 17. Anti-BS Rules (Pulse Engine)

All existing [Anti-BS Rules](anti-bs-rules.md) apply unchanged. Pulse adds:

- Never restate a user's factual statement as a bigger claim.
- Never invent a category, metric, or detail the user didn't say.
- Never convert "impact: unknown" into an invented number.
- Never pressure a "not sure" or "nothing" answer into a manufactured achievement.
- Never store or surface evidence across the wrong company.
- Never upload or sync Pulse data without explicit user opt-in.

For every captured item, the internal check is:

```
Did the user actually say this?
Is this a fact, or my interpretation?
Is the impact known, or should it say Unknown?
```

---

## 18. Validation Checklist (Pulse Engine)

- [ ] Opening question is concrete ("What did you work on yesterday?"), not "What did you accomplish?"
- [ ] Unanswered/irrelevant branches are skipped, not forced
- [ ] "Not sure" and "nothing" are accepted without pressure
- [ ] Session runs in roughly 30–90 seconds for a normal day
- [ ] Each evidence item has a category (or `Other`), description, source `user`, confidence, and `impact: Unknown` unless real evidence of outcome exists
- [ ] Duplicate check runs before saving new evidence
- [ ] Corrections update existing entries rather than duplicating
- [ ] Evidence is isolated per company
- [ ] Evidence is stored under `~/.shiplift/`, never inside the project repository
- [ ] Summary is concise, grouped by category, and ends with "Anything else?"
- [ ] No claim exceeds what the user actually said

---

## The Principle

> Some of the most important things engineers do never become a commit.
> If we don't capture it when it happens, we will probably forget it by review time.

Pulse should make remembering easy. It should never make exaggerating easy.
