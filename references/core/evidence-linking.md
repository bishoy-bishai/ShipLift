# Evidence Linking

Evidence linking connects related evidence items — across Git and Pulse — into one coherent body of work, instead of leaving them as unrelated facts.

Implementation: `evidence_engine.py` (`link_score`, `find_related`), exposed as `evidence-engine.sh find-related` and persisted via `pulse-store.sh link`.

---

## 1. Why Linking Matters

```
Pulse:  Started investigation into Cypress instability.
Git:    Added Cypress test fixes.
Git:    Added regression tests.
Pulse:  Shared findings with the team.
```

Without linking, this reads as four unrelated activities. With linking, it reads as one story:

```
Investigation → Implementation → Quality Improvement → Knowledge Sharing
```

The final achievement (built later by the Achievement Engine) should represent that story, not four disconnected line items.

---

## 2. Linking Signals

Two evidence items are candidates for linking when they share, within the same company:

- **Date proximity** — within `LINK_DATE_WINDOW_DAYS` (10 days) of each other
- **Keyword overlap** — meaningful words shared between descriptions (stopwords excluded)
- **Shared metadata** — matching `project`, `component`, `technology`, `initiative`, or `goal` fields
- **Same category family** — e.g. an `Investigation` followed by a `Bug Fix` or `Code Review` addressing it

Each signal contributes to a score; a pair links (as a candidate) once the score crosses `LINK_SCORE_THRESHOLD`.

## 3. Do Not Over-Link

- Different companies never link.
- A single weak signal (e.g. one shared common word) is not enough.
- If the relationship is uncertain, **keep the evidence separate.**
- `find_related` returns *candidates*, ranked by score and reasons — it never auto-merges evidence. Persisting a link (`pulse-store.sh link`) is a deliberate step, not an automatic side effect of scoring.
- Never fabricate a relationship that isn't supported by the evidence itself (no inferring a link from vibes or assumed context).

---

## 4. Using Links Downstream

- **Quarter**: linked evidence should be clustered into one achievement candidate rather than several, following the existing [Achievement Framework](../achievement-framework.md) grouping rules.
- **Quarter Closure**: an `Investigation`/`Initiative`/`Incident Response` item with a link to evidence containing resolution language (e.g. "fixed", "root cause", "resolved") is considered closed — see [commands.md](../commands.md) Quarter Closure Intelligence.
- **CV**: linked evidence across a longer time range is one input into an engineering story (see [Career Evidence Engine §4](../career-evidence-engine.md)).

---

## 5. Validation Checklist

- [ ] Evidence from different companies never links
- [ ] Isolated, unrelated evidence stays separate (no forced clustering)
- [ ] Every link has an identifiable reason (date, keyword, or metadata match)
- [ ] Linking is suggested, not silently applied, when ambiguous
