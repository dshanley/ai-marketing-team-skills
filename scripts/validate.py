#!/usr/bin/env python3
"""Check every skills/*/SKILL.md against the Agent Skills spec limits.

Usage: python3 scripts/validate.py
Checks: name pattern and length, folder match, reserved words, description
length, metadata version and owner, body length. Exits 1 on any failure.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RESERVED = ("claude", "anthropic")
MAX_BODY_LINES = 150


def parse(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None, text
    fm, body, key = {}, m.group(2), None
    for line in m.group(1).split("\n"):
        if line.startswith("  ") and key:
            k, _, v = line.strip().partition(":")
            fm.setdefault(key, {})[k] = v.strip().strip('"')
        else:
            k, _, v = line.partition(":")
            key = k.strip()
            fm[key] = {} if not v.strip() else v.strip()
    return fm, body


def check(path):
    errs = []
    fm, body = parse(path.read_text())
    if fm is None:
        return ["missing frontmatter"]
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not NAME_RE.match(name) or len(name) > 64:
        errs.append(f"bad name {name!r}")
    if name != path.parent.name:
        errs.append(f"name {name!r} does not match folder {path.parent.name!r}")
    if any(w in name for w in RESERVED):
        errs.append("name contains a reserved word")
    if not desc or len(desc) > 1024:
        errs.append(f"description length {len(desc)} (need 1-1024)")
    meta = fm.get("metadata") or {}
    if not isinstance(meta, dict) or not meta.get("version") or not meta.get("owner"):
        errs.append("metadata needs version and owner")
    lines = len(body.strip().split("\n"))
    if lines > MAX_BODY_LINES:
        errs.append(f"body is {lines} lines (max {MAX_BODY_LINES})")
    if "## Changelog" not in body:
        errs.append("missing Changelog section")
    return errs, name, len(desc), lines


def main():
    failed = False
    for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
        res = check(p)
        if isinstance(res, list):
            errs, info = res, ""
        else:
            errs, name, dl, ln = res
            info = f"description {dl}/1024 chars, body {ln} lines"
        print(("FAIL " if errs else "ok   ") + p.parent.name + "  " + (info if not errs else "; ".join(errs)))
        failed |= bool(errs)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
