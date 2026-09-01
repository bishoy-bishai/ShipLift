#!/usr/bin/env python3
"""
ShipLift EvidenceStore

A small, dependency-free local JSON store for ShipLift evidence. It was
introduced for Pulse (Human Evidence) and is now the shared store for
every evidence source (Git, Pulse, and future integrations) — see
references/core/evidence-engine.md for the unified evidence model this
implements. This script is a storage abstraction only — it does NOT
decide what counts as evidence, link evidence, generate achievements, or
interpret impact. That logic lives in scripts/evidence_engine.py and the
agent, guided by references/pulse-engine.md and references/core/*.md.

Storage layout (MVP implementation — JSONStore):

    ~/.shiplift/
    ├── config.json
    └── companies/
        └── <company-id>/
            └── evidence.json

Usage:
    pulse_store.py init [--company ID] [--home PATH]
    pulse_store.py add --company ID --category CAT --description TEXT
                        [--work-date YYYY-MM-DD] [--source user]
                        [--confidence High|Medium|Low] [--metadata JSON]
                        [--links JSON-array-of-ids]
    pulse_store.py check-duplicate --company ID --description TEXT [--category CAT]
    pulse_store.py update --company ID --id ID [--description TEXT]
                        [--metadata JSON] [--confidence High|Medium|Low]
    pulse_store.py link --company ID --id ID --to ID [--reason TEXT]
    pulse_store.py list --company ID [--category CAT] [--since YYYY-MM-DD]
                        [--until YYYY-MM-DD] [--date YYYY-MM-DD] [--source SRC]
    pulse_store.py recent --company ID [--days N]
    pulse_store.py by-quarter --company ID --quarter YYYY-QN
    pulse_store.py companies [--home PATH]

All output is JSON on stdout so the calling agent can parse it.
Raw evidence text is stored locally only — never printed to logs beyond
this store's own JSON output, and never uploaded anywhere.

Category validation: the Pulse category list (VALID_CATEGORIES) is
enforced for source="user" evidence, since that list is part of the
Pulse contract (references/pulse-engine.md §4). Other sources (e.g.
"git") may use their own category vocabulary (see
references/core/evidence-engine.md) and are not forced into the Pulse
list — this store only checks that a category is a non-empty string
for non-user sources.
"""

import argparse
import difflib
import json
import os
import sys
import uuid
from datetime import datetime, timezone

DEFAULT_HOME = os.path.expanduser("~/.shiplift")

VALID_CATEGORIES = {
    "Collaboration",
    "Mentoring",
    "Code Review",
    "Technical Decision",
    "Investigation",
    "Initiative",
    "Incident Response",
    "Documentation",
    "Knowledge Sharing",
    "Planning",
    "Communication",
    "Problem Solving",
    "Unblocking",
    "Process Improvement",
    "Other",
}

VALID_CONFIDENCE = {"High", "Medium", "Low"}

DUPLICATE_SIMILARITY_THRESHOLD = 0.6


def home_dir(args):
    return args.home or DEFAULT_HOME


def company_dir(args):
    return os.path.join(home_dir(args), "companies", args.company)


def evidence_path(args):
    return os.path.join(company_dir(args), "evidence.json")


def config_path(args):
    return os.path.join(home_dir(args), "config.json")


def ensure_company(args):
    d = company_dir(args)
    os.makedirs(d, exist_ok=True)
    path = evidence_path(args)
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump([], f)
    return path


def load_evidence(args):
    path = ensure_company(args)
    with open(path) as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_evidence(args, items):
    path = ensure_company(args)
    with open(path, "w") as f:
        json.dump(items, f, indent=2, sort_keys=True)
        f.write("\n")


def cmd_init(args):
    os.makedirs(home_dir(args), exist_ok=True)
    if args.company:
        ensure_company(args)
    cfg_path = config_path(args)
    if not os.path.exists(cfg_path):
        with open(cfg_path, "w") as f:
            json.dump({"created": now_iso(), "storage": "json"}, f, indent=2)
    print(json.dumps({"ok": True, "home": home_dir(args)}))


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def similarity(a, b):
    return difflib.SequenceMatcher(None, a.lower().strip(), b.lower().strip()).ratio()


def find_duplicates(items, description, category=None):
    candidates = []
    for item in items:
        if category and item.get("category") != category:
            continue
        score = similarity(item.get("description", ""), description)
        if score >= DUPLICATE_SIMILARITY_THRESHOLD:
            candidates.append({"id": item["id"], "description": item["description"],
                                "date": item.get("date"), "similarity": round(score, 2)})
    candidates.sort(key=lambda c: -c["similarity"])
    return candidates


def cmd_check_duplicate(args):
    items = load_evidence(args)
    dupes = find_duplicates(items, args.description, args.category)
    print(json.dumps({"duplicates": dupes}, indent=2))


def cmd_add(args):
    source = args.source or "user"

    if source == "user" and args.category not in VALID_CATEGORIES:
        print(json.dumps({"error": f"invalid category: {args.category}",
                           "valid_categories": sorted(VALID_CATEGORIES)}))
        sys.exit(1)
    if not args.category or not args.category.strip():
        print(json.dumps({"error": "category must not be empty"}))
        sys.exit(1)

    confidence = args.confidence or "High"
    if confidence not in VALID_CONFIDENCE:
        print(json.dumps({"error": f"invalid confidence: {confidence}"}))
        sys.exit(1)

    items = load_evidence(args)

    metadata = {}
    if args.metadata:
        try:
            metadata = json.loads(args.metadata)
        except json.JSONDecodeError:
            print(json.dumps({"error": "metadata must be valid JSON"}))
            sys.exit(1)

    links = []
    if args.links:
        try:
            links = json.loads(args.links)
        except json.JSONDecodeError:
            print(json.dumps({"error": "links must be a valid JSON array of ids"}))
            sys.exit(1)

    work_date = args.work_date or datetime.now().strftime("%Y-%m-%d")

    item = {
        "id": str(uuid.uuid4()),
        "date": work_date,
        "captured_at": now_iso(),
        "company": args.company,
        "category": args.category,
        "description": args.description,
        "source": source,
        "confidence": confidence,
        "metadata": metadata,
        "impact": "Unknown",
        "links": links,
    }

    items.append(item)
    save_evidence(args, items)
    print(json.dumps({"ok": True, "item": item}, indent=2))


def cmd_link(args):
    items = load_evidence(args)
    by_id = {i["id"]: i for i in items}
    if args.id not in by_id:
        print(json.dumps({"error": f"no evidence found with id {args.id}"}))
        sys.exit(1)
    if args.to not in by_id:
        print(json.dumps({"error": f"no evidence found with id {args.to}"}))
        sys.exit(1)
    if args.id == args.to:
        print(json.dumps({"error": "cannot link evidence to itself"}))
        sys.exit(1)

    a, b = by_id[args.id], by_id[args.to]
    a.setdefault("links", [])
    b.setdefault("links", [])
    if args.to not in a["links"]:
        a["links"].append(args.to)
    if args.id not in b["links"]:
        b["links"].append(args.id)

    save_evidence(args, items)
    print(json.dumps({"ok": True, "linked": [args.id, args.to], "reason": args.reason}, indent=2))


def cmd_update(args):
    items = load_evidence(args)
    target = None
    for item in items:
        if item["id"] == args.id:
            target = item
            break
    if target is None:
        print(json.dumps({"error": f"no evidence found with id {args.id}"}))
        sys.exit(1)

    if args.description is not None:
        target["description"] = args.description
    if args.confidence is not None:
        if args.confidence not in VALID_CONFIDENCE:
            print(json.dumps({"error": f"invalid confidence: {args.confidence}"}))
            sys.exit(1)
        target["confidence"] = args.confidence
    if args.metadata is not None:
        try:
            target["metadata"] = json.loads(args.metadata)
        except json.JSONDecodeError:
            print(json.dumps({"error": "metadata must be valid JSON"}))
            sys.exit(1)
    target["updated_at"] = now_iso()

    save_evidence(args, items)
    print(json.dumps({"ok": True, "item": target}, indent=2))


def cmd_list(args):
    items = load_evidence(args)
    result = items
    if args.category:
        result = [i for i in result if i.get("category") == args.category]
    if getattr(args, "source", None):
        result = [i for i in result if i.get("source") == args.source]
    if args.date:
        result = [i for i in result if i.get("date") == args.date]
    if args.since:
        result = [i for i in result if i.get("date", "") >= args.since]
    if args.until:
        result = [i for i in result if i.get("date", "") <= args.until]
    result = sorted(result, key=lambda i: i.get("date", ""))
    print(json.dumps({"count": len(result), "items": result}, indent=2))


def cmd_recent(args):
    items = load_evidence(args)
    days = args.days or 7
    cutoff = datetime.now().timestamp() - days * 86400
    result = []
    for i in items:
        try:
            d = datetime.strptime(i.get("date", ""), "%Y-%m-%d").timestamp()
        except ValueError:
            continue
        if d >= cutoff:
            result.append(i)
    result.sort(key=lambda i: i.get("date", ""), reverse=True)
    print(json.dumps({"count": len(result), "items": result}, indent=2))


def quarter_bounds(quarter_str):
    year_str, q_str = quarter_str.split("-Q")
    year = int(year_str)
    q = int(q_str)
    start_month = (q - 1) * 3 + 1
    end_month = start_month + 2
    start = f"{year}-{start_month:02d}-01"
    if end_month == 12:
        end = f"{year}-12-31"
    else:
        end_month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        end = f"{year}-{end_month:02d}-{end_month_days[end_month]:02d}"
    return start, end


def cmd_by_quarter(args):
    start, end = quarter_bounds(args.quarter)
    items = load_evidence(args)
    result = [i for i in items if start <= i.get("date", "") <= end]
    result.sort(key=lambda i: i.get("date", ""))
    print(json.dumps({"quarter": args.quarter, "start": start, "end": end,
                       "count": len(result), "items": result}, indent=2))


def cmd_companies(args):
    base = os.path.join(home_dir(args), "companies")
    if not os.path.isdir(base):
        print(json.dumps({"companies": []}))
        return
    companies = sorted(d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d)))
    print(json.dumps({"companies": companies}))


def build_parser():
    p = argparse.ArgumentParser(description="ShipLift Pulse EvidenceStore")
    p.add_argument("--home", help="Override storage home (default: ~/.shiplift)")
    sub = p.add_subparsers(dest="command", required=True)

    sp = sub.add_parser("init")
    sp.add_argument("--company")
    sp.set_defaults(func=cmd_init)

    sp = sub.add_parser("add")
    sp.add_argument("--company", required=True)
    sp.add_argument("--category", required=True)
    sp.add_argument("--description", required=True)
    sp.add_argument("--work-date")
    sp.add_argument("--source", default="user")
    sp.add_argument("--confidence")
    sp.add_argument("--metadata")
    sp.add_argument("--links")
    sp.set_defaults(func=cmd_add)

    sp = sub.add_parser("link")
    sp.add_argument("--company", required=True)
    sp.add_argument("--id", required=True)
    sp.add_argument("--to", required=True)
    sp.add_argument("--reason")
    sp.set_defaults(func=cmd_link)

    sp = sub.add_parser("check-duplicate")
    sp.add_argument("--company", required=True)
    sp.add_argument("--description", required=True)
    sp.add_argument("--category")
    sp.set_defaults(func=cmd_check_duplicate)

    sp = sub.add_parser("update")
    sp.add_argument("--company", required=True)
    sp.add_argument("--id", required=True)
    sp.add_argument("--description")
    sp.add_argument("--confidence")
    sp.add_argument("--metadata")
    sp.set_defaults(func=cmd_update)

    sp = sub.add_parser("list")
    sp.add_argument("--company", required=True)
    sp.add_argument("--category")
    sp.add_argument("--date")
    sp.add_argument("--since")
    sp.add_argument("--until")
    sp.add_argument("--source")
    sp.set_defaults(func=cmd_list)

    sp = sub.add_parser("recent")
    sp.add_argument("--company", required=True)
    sp.add_argument("--days", type=int)
    sp.set_defaults(func=cmd_recent)

    sp = sub.add_parser("by-quarter")
    sp.add_argument("--company", required=True)
    sp.add_argument("--quarter", required=True)
    sp.set_defaults(func=cmd_by_quarter)

    sp = sub.add_parser("companies")
    sp.set_defaults(func=cmd_companies)

    return p


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
