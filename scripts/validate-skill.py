#!/usr/bin/env python3
"""ShipLift skill structure validator.

Checks SKILL.md frontmatter, the plugin manifest, reference links, and
scans for hard-coded local paths and hard-coded secrets. Exits non-zero
on failure so it can be used as a CI gate. Standard library only.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

errors = []
warnings = []

TEXT_SUFFIXES = (".md", ".sh", ".py", ".json", ".yml", ".yaml")


def check_frontmatter():
    skill_md = ROOT / "SKILL.md"
    if not skill_md.exists():
        errors.append("SKILL.md is missing")
        return None
    text = skill_md.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append("SKILL.md has no YAML frontmatter block")
        return None
    fm = match.group(1)
    for field in ("name:", "description:"):
        if field not in fm:
            errors.append(f"SKILL.md frontmatter missing required field: {field.rstrip(':')}")
    if "name: shiplift" not in fm:
        warnings.append("SKILL.md frontmatter 'name' is not 'shiplift'")
    version_match = re.search(r'version:\s*"?([0-9]+\.[0-9]+\.[0-9]+)"?', fm)
    return version_match.group(1) if version_match else None


def check_manifest():
    manifest_path = ROOT / ".claude-plugin" / "plugin.json"
    if not manifest_path.exists():
        errors.append(".claude-plugin/plugin.json is missing")
        return None
    try:
        manifest = json.loads(manifest_path.read_text())
    except json.JSONDecodeError as e:
        errors.append(f".claude-plugin/plugin.json is not valid JSON: {e}")
        return None
    # Per the official plugin.json schema, only "name" is strictly required;
    # the rest are strongly recommended for a marketplace-facing plugin.
    if "name" not in manifest:
        errors.append("plugin.json missing required field: name")
    for field in ("description", "version", "author", "license"):
        if field not in manifest:
            warnings.append(f"plugin.json missing recommended field: {field}")
    if manifest.get("name") != "shiplift":
        warnings.append(f"plugin.json name is '{manifest.get('name')}', expected 'shiplift'")
    if manifest.get("license") != "MIT":
        warnings.append(f"plugin.json license is '{manifest.get('license')}', expected 'MIT'")
    return manifest.get("version")


def check_marketplace_manifest():
    path = ROOT / ".claude-plugin" / "marketplace.json"
    if not path.exists():
        warnings.append(
            ".claude-plugin/marketplace.json is missing — "
            "'/plugin marketplace add <owner>/<repo>' won't work without it"
        )
        return
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        errors.append(f".claude-plugin/marketplace.json is not valid JSON: {e}")
        return
    for field in ("name", "owner", "plugins"):
        if field not in data:
            errors.append(f"marketplace.json missing required field: {field}")
    if isinstance(data.get("owner"), dict) and "name" not in data["owner"]:
        errors.append("marketplace.json 'owner' is missing required field: name")
    for entry in data.get("plugins", []):
        if "name" not in entry or "source" not in entry:
            errors.append(f"marketplace.json plugin entry missing 'name' or 'source': {entry}")


def check_version_consistency(skill_version, manifest_version):
    if skill_version and manifest_version and skill_version != manifest_version:
        errors.append(
            f"version mismatch: SKILL.md metadata.version={skill_version!r} "
            f"!= plugin.json version={manifest_version!r}"
        )


HEADING_RE = re.compile(r"^#{1,6}\s+(.+)$", re.MULTILINE)


def slugify(heading):
    """Approximate GitHub's heading-anchor algorithm: strip emoji/punctuation
    (keeping word chars, spaces, hyphens), then replace each space with a
    hyphen individually — so consecutive spaces (e.g. around an em dash)
    become consecutive hyphens, matching GitHub's actual output."""
    slug = heading.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug, flags=re.UNICODE)
    slug = "".join("-" if ch == " " else ch for ch in slug)
    return slug


def check_referenced_files():
    """Every relative markdown link (and its #anchor, if any) must resolve."""
    md_files = [ROOT / "SKILL.md", ROOT / "README.md", ROOT / "VALIDATION.md"]
    md_files += list((ROOT / "references").rglob("*.md"))
    link_re = re.compile(r"\]\(([^)]+)\)")

    anchor_cache = {}

    def anchors_for(path):
        if path not in anchor_cache:
            if path.exists():
                headings = HEADING_RE.findall(path.read_text())
                anchor_cache[path] = {slugify(h) for h in headings}
            else:
                anchor_cache[path] = set()
        return anchor_cache[path]

    for md_file in md_files:
        if not md_file.exists():
            continue
        text = md_file.read_text()
        for link in link_re.findall(text):
            if link.startswith(("http://", "https://", "mailto:")):
                continue
            target, _, anchor = link.partition("#")
            resolved = md_file.parent / target if target else md_file
            resolved = resolved.resolve()
            if target and not resolved.exists():
                errors.append(f"{md_file.relative_to(ROOT)}: broken link -> {link}")
                continue
            if anchor and resolved.suffix == ".md":
                known = anchors_for(resolved)
                if known and anchor.lower() not in known:
                    warnings.append(
                        f"{md_file.relative_to(ROOT)}: anchor '#{anchor}' not found in "
                        f"{resolved.relative_to(ROOT)} (heading may have been renamed)"
                    )


def check_required_dirs():
    for d in ("references", "references/core", "scripts"):
        if not (ROOT / d).is_dir():
            errors.append(f"Required directory missing: {d}")


def iter_text_files():
    for path in ROOT.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.suffix not in TEXT_SUFFIXES:
            continue
        try:
            yield path, path.read_text(errors="ignore")
        except OSError:
            continue


SELF_DOCUMENTING_FILES = {"validate-skill.py", "VALIDATION.md"}


def check_no_hardcoded_paths():
    suspicious = re.compile(r"/Users/[A-Za-z0-9_.-]+|/home/[A-Za-z0-9_.-]+|[A-Za-z]:\\Users\\")
    for path, text in iter_text_files():
        if path.name in SELF_DOCUMENTING_FILES:
            continue  # these files describe the pattern itself, not an actual leak
        if suspicious.search(text):
            warnings.append(f"{path.relative_to(ROOT)}: contains a hard-coded local path")


# Secret patterns: specific enough to avoid flagging prose that merely
# *mentions* words like "API_KEY" or "TOKEN" as a concept (which several
# reference docs do, intentionally, when explaining what not to invent).
SECRET_PATTERNS = [
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS access key ID"),
    (re.compile(r"ghp_[A-Za-z0-9]{36}"), "GitHub personal access token"),
    (re.compile(r"gh[oprsu]_[A-Za-z0-9]{36}"), "GitHub token"),
    (re.compile(r"sk-[A-Za-z0-9]{20,}"), "OpenAI-style API key"),
    (re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"), "Slack token"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "embedded private key"),
    (
        re.compile(
            r"(?:api[_-]?key|secret|password|passwd|token|bearer)\s*[:=]\s*"
            r"['\"][A-Za-z0-9+/_.\-]{12,}['\"]",
            re.IGNORECASE,
        ),
        "assigned credential-like value",
    ),
]


def check_no_secrets():
    for path, text in iter_text_files():
        if path.name in SELF_DOCUMENTING_FILES:
            continue  # these files describe the pattern itself, not an actual leak
        for pattern, label in SECRET_PATTERNS:
            m = pattern.search(text)
            if m:
                line_no = text.count("\n", 0, m.start()) + 1
                errors.append(f"{path.relative_to(ROOT)}:{line_no}: possible {label}")


def main():
    skill_version = check_frontmatter()
    manifest_version = check_manifest()
    check_marketplace_manifest()
    check_version_consistency(skill_version, manifest_version)
    check_required_dirs()
    check_referenced_files()
    check_no_hardcoded_paths()
    check_no_secrets()

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
