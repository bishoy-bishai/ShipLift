#!/usr/bin/env python3
"""
ShipLift Evidence Engine

The intelligence layer that sits on top of the EvidenceStore
(pulse_store.py). It does not replace the agent's judgment — it provides
small, deterministic, testable building blocks the agent (and the
existing commands) can call instead of re-implementing this logic ad hoc:

    - evidence linking          (references/core/evidence-linking.md)
    - evidence strength         (references/core/evidence-strength.md)
    - impact analysis           (references/core/impact-analysis.md)
    - signal detection          (references/core/signal-detection.md)
    - blind spot detection      (references/core/blind-spots.md)
    - anti-inflation linting    (references/core/anti-inflation.md)
    - open-thread detection     (Quarter closure, see references/commands.md §21)
    - goal signal detection     (Reverse Achievement -> Goal Mapping, references/goals-engine.md §18-19)
    - goal matching             (existing-goal evidence linking, references/goals-engine.md §17)

This module reads/writes through pulse_store's load/save so there is a
single storage implementation (see references/core/evidence-engine.md §7
"Reuse, Don't Rebuild"). It never talks to disk directly.

All CLI output is JSON.
"""

import argparse
import json
import re
import sys
from datetime import datetime

import pulse_store as store

# ---------------------------------------------------------------------------
# Evidence Linking
# ---------------------------------------------------------------------------

STOPWORDS = {
    "the", "a", "an", "and", "or", "to", "of", "in", "on", "for", "with",
    "was", "were", "is", "are", "it", "this", "that", "we", "i", "our",
    "into", "at", "by", "from", "some", "about", "did", "do", "does",
}

LINK_DATE_WINDOW_DAYS = 10
LINK_KEYWORD_OVERLAP_THRESHOLD = 2
LINK_SCORE_THRESHOLD = 2


def keywords(text):
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9_+.#-]{2,}", text.lower())
    return {w for w in words if w not in STOPWORDS}


def days_apart(date_a, date_b):
    try:
        a = datetime.strptime(date_a, "%Y-%m-%d")
        b = datetime.strptime(date_b, "%Y-%m-%d")
    except (ValueError, TypeError):
        return None
    return abs((a - b).days)


def link_score(item_a, item_b):
    """Return (score, reasons) for whether two evidence items are related.

    This never claims certainty by itself — it's a candidate signal for
    the agent (or a human) to confirm. See evidence-linking.md §2 "Do not
    over-link".
    """
    if item_a.get("company") != item_b.get("company"):
        return 0, []

    reasons = []
    score = 0

    gap = days_apart(item_a.get("date"), item_b.get("date"))
    if gap is not None and gap <= LINK_DATE_WINDOW_DAYS:
        score += 1
        reasons.append(f"within {gap} day(s) of each other")

    kw_a = keywords(item_a.get("description", ""))
    kw_b = keywords(item_b.get("description", ""))
    overlap = kw_a & kw_b
    if len(overlap) >= LINK_KEYWORD_OVERLAP_THRESHOLD:
        score += 2
        reasons.append(f"shared keywords: {', '.join(sorted(overlap))}")
    elif len(overlap) == 1:
        score += 1
        reasons.append(f"shared keyword: {next(iter(overlap))}")

    meta_a, meta_b = item_a.get("metadata", {}) or {}, item_b.get("metadata", {}) or {}
    for key in ("project", "component", "technology", "initiative", "goal"):
        if key in meta_a and key in meta_b and meta_a[key] == meta_b[key]:
            score += 2
            reasons.append(f"shared metadata.{key}: {meta_a[key]}")

    return score, reasons


def find_related(items, target):
    candidates = []
    for item in items:
        if item["id"] == target["id"]:
            continue
        score, reasons = link_score(target, item)
        if score >= LINK_SCORE_THRESHOLD:
            candidates.append({
                "id": item["id"],
                "description": item["description"],
                "date": item.get("date"),
                "source": item.get("source"),
                "score": score,
                "reasons": reasons,
            })
    candidates.sort(key=lambda c: -c["score"])
    return candidates


def cmd_find_related(args):
    items = store.load_evidence(args)
    target = next((i for i in items if i["id"] == args.id), None)
    if target is None:
        print(json.dumps({"error": f"no evidence found with id {args.id}"}))
        sys.exit(1)
    print(json.dumps({"id": args.id, "candidates": find_related(items, target)}, indent=2))


# ---------------------------------------------------------------------------
# Evidence Strength
# ---------------------------------------------------------------------------

MEASURABLE_METADATA_KEYS = {
    "before", "after", "baseline", "target", "current", "metric",
    "pr_count", "test_count_before", "test_count_after",
    "coverage_before", "coverage_after",
}


def has_measurable_metric(item):
    metadata = item.get("metadata", {}) or {}
    return any(k in metadata for k in MEASURABLE_METADATA_KEYS)


def evidence_strength(items_for_contribution):
    """Rate a *group* of related evidence items (see evidence-strength.md).

    items_for_contribution: evidence items already linked/grouped as one
    candidate contribution — this function does not decide grouping.
    """
    if not items_for_contribution:
        return "Early Signal", ["no evidence"]

    sources = {i.get("source") for i in items_for_contribution}
    has_measurable = any(has_measurable_metric(i) for i in items_for_contribution)
    repeated = len(items_for_contribution) >= 3
    multi_source = len(sources) >= 2

    reasons = []
    if has_measurable:
        reasons.append("has a measurable before/after value")
    if multi_source:
        reasons.append(f"backed by multiple evidence sources ({', '.join(sorted(sources))})")
    if repeated:
        reasons.append(f"repeated across {len(items_for_contribution)} evidence items")

    if has_measurable and (multi_source or repeated):
        return "Strong Evidence", reasons
    if has_measurable or multi_source or repeated:
        return "Moderate Evidence", reasons or ["clear contribution, limited supporting evidence"]
    return "Early Signal", ["isolated activity with no supporting metric or repetition"]


def cmd_strength(args):
    ids = json.loads(args.ids)
    items = store.load_evidence(args)
    by_id = {i["id"]: i for i in items}
    group = [by_id[i] for i in ids if i in by_id]
    missing = [i for i in ids if i not in by_id]
    level, reasons = evidence_strength(group)
    print(json.dumps({"strength": level, "reasons": reasons, "missing_ids": missing}, indent=2))


# ---------------------------------------------------------------------------
# Impact Analysis
# ---------------------------------------------------------------------------

OBSERVED_KEYWORDS = (
    "adopted", "started using", "now uses", "team adopted", "picked up the pattern",
)


def impact_level(item):
    """Classify impact as Measured / Observed / Supported / Unknown.

    This NEVER upgrades an item's own stated impact — it only recognizes
    when the item's own metadata/description already contains that level
    of evidence. See references/core/impact-analysis.md.
    """
    description = item.get("description", "") or ""

    if has_measurable_metric(item):
        return "Measured", "metadata contains a before/after or baseline/target value"

    lowered = description.lower()
    if any(kw in lowered for kw in OBSERVED_KEYWORDS):
        return "Observed", "description states an observed behavior change"

    if item.get("category") in {"Unblocking", "Collaboration", "Mentoring", "Incident Response"} \
            and description.strip():
        return "Supported", "a concrete outcome is described, without a measurement"

    return "Unknown", "no measured, observed, or clearly supported outcome stated"


def cmd_impact(args):
    items = store.load_evidence(args)
    target = next((i for i in items if i["id"] == args.id), None)
    if target is None:
        print(json.dumps({"error": f"no evidence found with id {args.id}"}))
        sys.exit(1)
    level, reason = impact_level(target)
    print(json.dumps({"id": args.id, "impact": level, "reason": reason}, indent=2))


# ---------------------------------------------------------------------------
# Signal Detection
# ---------------------------------------------------------------------------

SIGNAL_MIN_OCCURRENCES = 3


def detect_signals(items):
    """Group evidence by category and detect recurring patterns over time.

    A signal is descriptive ("consistent contribution to X"), never itself
    an achievement — see references/core/signal-detection.md.
    """
    by_category = {}
    for item in items:
        by_category.setdefault(item.get("category", "Other"), []).append(item)

    signals = []
    for category, group in by_category.items():
        if len(group) < SIGNAL_MIN_OCCURRENCES:
            continue
        sources = sorted({i.get("source") for i in group})
        dates = sorted(i.get("date", "") for i in group if i.get("date"))
        signals.append({
            "category": category,
            "occurrences": len(group),
            "sources": sources,
            "first_date": dates[0] if dates else None,
            "last_date": dates[-1] if dates else None,
            "description": f"Consistent contribution to {category.lower()} "
                            f"({len(group)} items across {', '.join(sources)}).",
        })

    signals.sort(key=lambda s: -s["occurrences"])
    return signals


def cmd_signals(args):
    items = store.load_evidence(args)
    if args.quarter:
        start, end = store.quarter_bounds(args.quarter)
        items = [i for i in items if start <= i.get("date", "") <= end]
    print(json.dumps({"signals": detect_signals(items)}, indent=2))


# ---------------------------------------------------------------------------
# Goal Signals (Reverse Achievement -> Goal Mapping)
# ---------------------------------------------------------------------------
#
# detect_signals() above groups by an evidence item's own *category*
# ("3+ Code Review items"). A goal signal is broader: it clusters evidence
# by shared *theme* (keyword overlap) regardless of category, so a pattern
# like "reviewed AI-generated code" / "fixed AI-generated bug" / "improved
# AI-generated code quality" — which may land in different categories — is
# still recognized as one recurring theme. See references/goals-engine.md
# §16 "Pulse-Derived Goal Signals".

THEME_MIN_SHARED_KEYWORDS = 2
THEME_MIN_CLUSTER_SIZE = 2


def theme_clusters(items, min_shared_keywords=THEME_MIN_SHARED_KEYWORDS,
                    min_cluster_size=THEME_MIN_CLUSTER_SIZE):
    """Cluster evidence (within the same company) by shared description
    keywords, independent of category. Returns clusters of size >=
    min_cluster_size, largest first. Never merges evidence from different
    companies, and never invents a theme from a single item.
    """
    kw_cache = {item["id"]: keywords(item.get("description", "")) for item in items}
    parent = {item["id"]: item["id"] for item in items}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for i, item_a in enumerate(items):
        for item_b in items[i + 1:]:
            if item_a.get("company") != item_b.get("company"):
                continue
            overlap = kw_cache[item_a["id"]] & kw_cache[item_b["id"]]
            if len(overlap) >= min_shared_keywords:
                union(item_a["id"], item_b["id"])

    groups = {}
    for item in items:
        groups.setdefault(find(item["id"]), []).append(item)

    clusters = []
    for group in groups.values():
        if len(group) < min_cluster_size:
            continue
        freq = {}
        for item in group:
            for kw in kw_cache[item["id"]]:
                freq[kw] = freq.get(kw, 0) + 1
        shared_threshold = max(2, len(group) // 2)
        theme_keywords = sorted(
            (kw for kw, count in freq.items() if count >= shared_threshold),
            key=lambda kw: -freq[kw],
        )[:6]
        if not theme_keywords:
            continue
        sources = sorted({item.get("source") for item in group})
        categories = sorted({item.get("category") for item in group if item.get("category")})
        dates = sorted(item.get("date", "") for item in group if item.get("date"))
        clusters.append({
            "theme_keywords": theme_keywords,
            "occurrences": len(group),
            "sources": sources,
            "categories": categories,
            "first_date": dates[0] if dates else None,
            "last_date": dates[-1] if dates else None,
            "item_ids": [item["id"] for item in group],
            "descriptions": [item["description"] for item in group],
        })

    clusters.sort(key=lambda c: -c["occurrences"])
    return clusters


def goal_signal_confidence(group):
    """Confidence for a candidate goal signal, following the repetition
    thresholds in references/goals-engine.md §19:

        1 mention                              -> Weak Signal
        2-3 related mentions                   -> Emerging Signal
        repeated mentions + multi-source/metric -> Strong Goal Signal

    Reuses evidence_strength's own building blocks (has_measurable_metric,
    source counting) rather than introducing a second scoring system.
    """
    n = len(group)
    if n <= 1:
        return "Weak Signal", ["a single mention is not enough evidence for a goal"]

    sources = {item.get("source") for item in group}
    measurable = any(has_measurable_metric(item) for item in group)
    multi_source = len(sources) >= 2

    if n >= 3 and (multi_source or measurable):
        reasons = [f"{n} related items"]
        if multi_source:
            reasons.append(f"backed by multiple evidence sources ({', '.join(sorted(sources))})")
        if measurable:
            reasons.append("has a measurable before/after value")
        return "Strong Goal Signal", reasons

    return "Emerging Signal", [
        f"{n} related item(s) — not yet repeated with supporting repository evidence"
    ]


def detect_goal_signals(items):
    """Full goal-signal detection: theme clusters + confidence rating.

    This is descriptive raw material for the agent to phrase as a
    Suggested Goal (see references/goals-engine.md §19) — it never invents
    goal wording itself.
    """
    signals = []
    for cluster in theme_clusters(items):
        confidence, reasons = goal_signal_confidence(
            [i for i in items if i["id"] in cluster["item_ids"]]
        )
        signals.append({**cluster, "confidence": confidence, "reasons": reasons})
    return signals


def cmd_goal_signals(args):
    items = store.load_evidence(args)
    if args.quarter:
        start, end = store.quarter_bounds(args.quarter)
        items = [i for i in items if start <= i.get("date", "") <= end]
    print(json.dumps({"goal_signals": detect_goal_signals(items)}, indent=2))


# ---------------------------------------------------------------------------
# Goal Matching (existing goals first)
# ---------------------------------------------------------------------------

def match_goal(goal_text, items):
    """Score recorded evidence against an existing goal's own wording, so
    `ShipLift Goals` can check for supporting evidence before ever
    suggesting a new goal. Keyword overlap only — never a semantic guess.
    """
    goal_keywords = keywords(goal_text)
    scored = []
    for item in items:
        item_keywords = keywords(f"{item.get('description', '')} {item.get('category', '')}")
        overlap = goal_keywords & item_keywords
        if overlap:
            scored.append({
                "id": item["id"],
                "description": item.get("description"),
                "category": item.get("category"),
                "source": item.get("source"),
                "date": item.get("date"),
                "overlap": sorted(overlap),
                "score": len(overlap),
            })
    scored.sort(key=lambda s: -s["score"])
    return scored


def cmd_match_goal(args):
    items = store.load_evidence(args)
    matches = match_goal(args.goal, items)
    print(json.dumps({"goal": args.goal, "matches": matches}, indent=2))


# ---------------------------------------------------------------------------
# Blind Spots
# ---------------------------------------------------------------------------

CAREER_AREAS = [
    "Technical Delivery",
    "Code Quality",
    "Problem Solving",
    "Technical Ownership",
    "Architecture",
    "Collaboration",
    "Mentoring",
    "Knowledge Sharing",
    "Initiative",
    "Leadership",
    "Cross-team Contribution",
    "Developer Experience",
    "Incident Response",
]

# Maps evidence categories (Pulse + common git-derived categories) onto the
# broader career areas above. This is intentionally coarse — it groups
# evidence for *visibility*, not for scoring.
AREA_CATEGORY_MAP = {
    "Technical Delivery": {"Feature Delivery", "Planning"},
    "Code Quality": {"Code Review", "Testing", "Process Improvement"},
    "Problem Solving": {"Problem Solving", "Investigation", "Bug Fix"},
    "Technical Ownership": {"Technical Decision", "Architecture"},
    "Architecture": {"Architecture", "Technical Decision"},
    "Collaboration": {"Collaboration", "Communication", "Unblocking"},
    "Mentoring": {"Mentoring"},
    "Knowledge Sharing": {"Knowledge Sharing", "Documentation"},
    "Initiative": {"Initiative"},
    "Leadership": {"Initiative", "Technical Decision"},
    "Cross-team Contribution": {"Collaboration", "Unblocking"},
    "Developer Experience": {"Process Improvement", "CI/CD"},
    "Incident Response": {"Incident Response"},
}


def evidence_distribution(items):
    counts = {area: 0 for area in CAREER_AREAS}
    for item in items:
        category = item.get("category")
        for area, categories in AREA_CATEGORY_MAP.items():
            if category in categories:
                counts[area] += 1
    return counts


def blind_spots(items):
    counts = evidence_distribution(items)
    result = []
    for area in CAREER_AREAS:
        n = counts[area]
        if n >= 3:
            level = "Strong Evidence"
        elif n >= 1:
            level = "Moderate Evidence"
        else:
            level = "Limited Evidence"
        result.append({"area": area, "evidence_count": n, "level": level})
    return result


def cmd_blind_spots(args):
    items = store.load_evidence(args)
    if args.quarter:
        start, end = store.quarter_bounds(args.quarter)
        items = [i for i in items if start <= i.get("date", "") <= end]
    print(json.dumps({"areas": blind_spots(items)}, indent=2))


# ---------------------------------------------------------------------------
# Anti-Inflation Lint
# ---------------------------------------------------------------------------

# Phrases that assert an outcome/impact. If present without a measurable
# metric or a description that plainly states the same claim, this is
# flagged for the agent to review — it does not silently rewrite anything.
INFLATION_PATTERNS = [
    (re.compile(r"\d+%"), "contains a percentage"),
    (re.compile(r"\bimprov(ed|es)\s+\w+\s+by\b", re.I), "claims a quantified improvement"),
    (re.compile(r"\b(productivity|velocity|revenue|conversion|retention|engagement)\b", re.I),
     "claims a business/productivity outcome"),
    (re.compile(r"\b(led|drove|owned)\b", re.I), "claims leadership/ownership language"),
    (re.compile(r"\bteam of \d+\b", re.I), "claims a specific team size"),
]


def lint_evidence(item):
    """Flag likely Anti-BS violations: a claim in the text without the
    metadata to back it up. This is a heuristic aid, not a hard block —
    see references/core/anti-inflation.md.
    """
    findings = []
    description = item.get("description", "") or ""
    measurable = has_measurable_metric(item)

    for pattern, label in INFLATION_PATTERNS:
        if pattern.search(description) and not measurable:
            findings.append({"issue": label, "text": description})

    if item.get("impact") not in (None, "Unknown") and not measurable:
        findings.append({
            "issue": "impact is set to something other than Unknown without a measurable metric",
            "impact": item.get("impact"),
        })

    return findings


def cmd_lint(args):
    items = store.load_evidence(args)
    if args.id:
        items = [i for i in items if i["id"] == args.id]
    report = []
    for item in items:
        findings = lint_evidence(item)
        if findings:
            report.append({"id": item["id"], "description": item.get("description"),
                            "findings": findings})
    print(json.dumps({"violations": report, "checked": len(items)}, indent=2))


# ---------------------------------------------------------------------------
# Open Threads (Quarter closure intelligence)
# ---------------------------------------------------------------------------

OPEN_THREAD_CATEGORIES = {"Investigation", "Initiative", "Incident Response"}
RESOLUTION_KEYWORDS = (
    "found the root cause", "root cause", "fixed", "resolved", "concluded",
    "wrapped up", "shipped", "completed", "closed out", "landed",
)


def is_resolved(item, all_items_by_id):
    """An open-category item is resolved if it has a link to evidence whose
    description reads like a resolution, or if its own later update/metadata
    marks it resolved.
    """
    if item.get("metadata", {}).get("resolved"):
        return True
    if any(kw in (item.get("description") or "").lower() for kw in RESOLUTION_KEYWORDS):
        return True
    for linked_id in item.get("links", []) or []:
        linked = all_items_by_id.get(linked_id)
        if linked and any(kw in (linked.get("description") or "").lower() for kw in RESOLUTION_KEYWORDS):
            return True
    return False


def open_threads(items):
    by_id = {i["id"]: i for i in items}
    threads = []
    for item in items:
        if item.get("category") not in OPEN_THREAD_CATEGORIES:
            continue
        if is_resolved(item, by_id):
            continue
        threads.append({
            "id": item["id"],
            "category": item["category"],
            "date": item.get("date"),
            "description": item.get("description"),
            "follow_up_question": (
                f"You mentioned \"{item.get('description')}\" on {item.get('date')}. "
                "Did this lead to a fix, decision, or conclusion?"
            ),
        })
    return threads


def cmd_open_threads(args):
    items = store.load_evidence(args)
    if args.quarter:
        start, end = store.quarter_bounds(args.quarter)
        items = [i for i in items if start <= i.get("date", "") <= end]
    print(json.dumps({"open_threads": open_threads(items)}, indent=2))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser():
    p = argparse.ArgumentParser(description="ShipLift Evidence Engine")
    p.add_argument("--home", help="Override storage home (default: ~/.shiplift)")
    sub = p.add_subparsers(dest="command", required=True)

    sp = sub.add_parser("find-related")
    sp.add_argument("--company", required=True)
    sp.add_argument("--id", required=True)
    sp.set_defaults(func=cmd_find_related)

    sp = sub.add_parser("strength")
    sp.add_argument("--company", required=True)
    sp.add_argument("--ids", required=True, help="JSON array of evidence ids")
    sp.set_defaults(func=cmd_strength)

    sp = sub.add_parser("impact")
    sp.add_argument("--company", required=True)
    sp.add_argument("--id", required=True)
    sp.set_defaults(func=cmd_impact)

    sp = sub.add_parser("signals")
    sp.add_argument("--company", required=True)
    sp.add_argument("--quarter")
    sp.set_defaults(func=cmd_signals)

    sp = sub.add_parser("goal-signals")
    sp.add_argument("--company", required=True)
    sp.add_argument("--quarter")
    sp.set_defaults(func=cmd_goal_signals)

    sp = sub.add_parser("match-goal")
    sp.add_argument("--company", required=True)
    sp.add_argument("--goal", required=True)
    sp.set_defaults(func=cmd_match_goal)

    sp = sub.add_parser("blind-spots")
    sp.add_argument("--company", required=True)
    sp.add_argument("--quarter")
    sp.set_defaults(func=cmd_blind_spots)

    sp = sub.add_parser("lint")
    sp.add_argument("--company", required=True)
    sp.add_argument("--id")
    sp.set_defaults(func=cmd_lint)

    sp = sub.add_parser("open-threads")
    sp.add_argument("--company", required=True)
    sp.add_argument("--quarter")
    sp.set_defaults(func=cmd_open_threads)

    return p


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
