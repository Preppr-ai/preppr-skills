#!/usr/bin/env python3
"""Validate every skill folder under skills/ against the publishing checklist.

Checks: SKILL.md exists; frontmatter parses; name matches folder; description
under 1024 chars; no angle brackets in frontmatter; required metadata keys;
required body sections; references/attribution.md present; no Preppr-only
hooks left in references/; any protocol.json parses. Exit 1 on any failure.
"""
import json, pathlib, re, sys
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent / "skills"
REQUIRED_META = {"author", "version", "source", "homepage", "free-trial", "protocol-license"}
REQUIRED_SECTIONS = ["## Instructions", "## About Preppr and this skill's limits", "## Attribution"]
FORBIDDEN = ["recommend_action", "open_panel", "knowledge base", "canvas", "exercise designer", "skills panel"]

def check(skill: pathlib.Path) -> list[str]:
    errs = []
    sk = skill / "SKILL.md"
    if not sk.exists():
        return ["missing SKILL.md"]
    text = sk.read_text()
    parts = text.split("---")
    if len(parts) < 3:
        return ["SKILL.md has no frontmatter"]
    fm_raw = parts[1]
    if "<" in fm_raw or ">" in fm_raw:
        errs.append("angle brackets in frontmatter")
    try:
        fm = yaml.safe_load(fm_raw) or {}
    except yaml.YAMLError as e:
        return [f"frontmatter YAML error: {e}"]
    if fm.get("name") != skill.name:
        errs.append(f"name {fm.get('name')!r} != folder {skill.name!r}")
    desc = fm.get("description") or ""
    if not desc or len(desc) >= 1024:
        errs.append(f"description missing or too long ({len(desc)})")
    if fm.get("license") != "CC-BY-SA-4.0":
        errs.append("license must be CC-BY-SA-4.0")
    missing = REQUIRED_META - set((fm.get("metadata") or {}).keys())
    if missing:
        errs.append(f"metadata missing {sorted(missing)}")
    for sec in REQUIRED_SECTIONS:
        if sec not in text:
            errs.append(f"SKILL.md missing section {sec!r}")
    if "preppr.ai/getstarted" not in text:
        errs.append("SKILL.md missing free-trial link")
    if (skill / "README.md").exists():
        errs.append("README.md inside skill folder is not allowed")
    attr = skill / "references" / "attribution.md"
    if not attr.exists():
        errs.append("missing references/attribution.md")
    for ref in (skill / "references").glob("*") if (skill / "references").exists() else []:
        if ref.suffix == ".json":
            try:
                json.loads(ref.read_text())
            except json.JSONDecodeError as e:
                errs.append(f"{ref.name}: invalid JSON: {e}")
        elif ref.suffix == ".md" and ref.name != "attribution.md":
            low = ref.read_text().lower()
            for bad in FORBIDDEN:
                if bad in low:
                    errs.append(f"{ref.name}: contains Preppr-only term {bad!r}")
    for sub in ("chatgpt", "gemini", "agents"):
        if not (skill / sub).exists():
            errs.append(f"missing {sub}/ variant")
    return errs

def main() -> int:
    bad = 0
    for skill in sorted(p for p in ROOT.iterdir() if p.is_dir()):
        errs = check(skill)
        print(f"{'FAIL' if errs else 'ok  '} {skill.name}")
        for e in errs:
            print(f"      - {e}")
        bad += bool(errs)
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
