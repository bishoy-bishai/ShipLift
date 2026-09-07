#!/usr/bin/env python3
"""ShipLift skill structure validator.

Checks SKILL.md frontmatter, the plugin manifest, and that every file
referenced from SKILL.md / references/ actually exists. Exits non-zero
on failure so it can be used as a CI gate.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

errors = []
warnings = []


def check_frontmatter():
    skill_md = ROOT / "SKILL.md"
    if not skill_md.exists():
        errors.append("SKILL.md is missing")
        return
    text = skill_md.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append("SKILL.md has no YAML frontmatter block")
        return
    fm = match.group(1)
    for field in ("name:", "description:"):
        if field not in fm:
            errors.append(f"SKILL.md frontmatter missing required field: {field.rstrip(':')}")
    if "name: shiplift" not in fm:
        warnings.append("SKILL.md frontmatter 'name' is not 'shiplift'")


def check_manifest():
    manifest_path = ROOT / ".claude-plugin" / "plugin.json"
    if not manifest_path.exists():
        errors.append(".claude-plugin/plugin.json is missing")
        return
    try:
        manifest = json.loads(manifest_path.read_text())
    except json.JSONDecodeError as e:
        errors.append(f".claude-plugin/plugin.json is not valid JSON: {e}")
        return
    for field in ("name", "description", "version", "author", "license", "skills"):
        if field not in manifest:
            errors.append(f"plugin.json missing required field: {field}")


def check_referenced_files():
    """Every relative markdown link in SKILL.md and references/ must resolve."""
    md_files = [ROOT / "SKILL.md"] + list((ROOT / "references").rglob("*.md"))
    link_re = re.compile(r"\]\(([^)]+)\)")
    for md_file in md_files:
        if not md_file.exists():
            continue
        text = md_file.read_text()
        for link in link_re.findall(text):
            if link.startswith(("http://", "https://", "#")):
                continue
            target, _, _anchor = link.partition("#")
            if not target:
                continue
            resolved = (md_file.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{md_file.relative_to(ROOT)}: broken link -> {link}")


def check_required_dirs():
    for d in ("references", "references/core", "scripts"):
        if not (ROOT / d).is_dir():
            errors.append(f"Required directory missing: {d}")


def check_no_hardcoded_paths():
    suspicious = re.compile(r"/Users/[A-Za-z0-9_.-]+|/home/[A-Za-z0-9_.-]+|C:\\\\Users")
    for path in ROOT.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.suffix not in (".md", ".sh", ".py", ".json"):
            continue
        try:
            text = path.read_text(errors="ignore")
        except OSError:
            continue
        if suspicious.search(text):
            warnings.append(f"{path.relative_to(ROOT)}: contains a hard-coded local path")


def main():
    check_frontmatter()
    check_manifest()
    check_required_dirs()
    check_referenced_files()
    check_no_hardcoded_paths()

    if warnings:
        print("Warnings:")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print("Errors:")
        for e in errors:
            print(f"  - {e}")
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s).")
        sys.exit(1)

    print(f"OK — 0 errors, {len(warnings)} warning(s).")


if __name__ == "__main__":
    main()
