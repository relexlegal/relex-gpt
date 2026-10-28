#!/usr/bin/env python3
"""Build the ZIP uploaded to the OpenAI Plugins portal (ChatGPT + Codex).

The portal reads the Agent Plugins layout from the ZIP root: plugin.json
(identity + extensions.com.openai listing/review data), mcp.json, skills/,
assets/. It requires a SKILL.md in every immediate child of skills/, so the
jurisdiction packs (reference files, not a skill) get a small SKILL.md in the
ZIP only. Host-specific folders that ChatGPT does not load (commands/,
agents/, .grok-plugin/) are left out. Nothing here uploads anything.

  python3 scripts/build_openai_zip.py [out.zip]   # default dist/relex-legal-openai.zip
"""
from __future__ import annotations

import pathlib
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent / "plugin"
EXCLUDE_TOP = {"commands", "agents", ".grok-plugin", ".claude-plugin", ".codex-plugin"}
JURISDICTIONS_SKILL = """---
name: jurisdictions
description: Reference packs for the Relex skills — per-jurisdiction citation formats, official sources and deadline orientation for AU, CA, CH, DE, ES, EU, FR, IT, JP, RO, UK and US. Read the pack for the forum of the matter.
---

# Relex jurisdiction packs

One file per jurisdiction (`<XX>.md`). The other Relex skills link here as
`../jurisdictions/<XX>.md`. `_TEMPLATE.md` is the format for new packs.
"""


def main() -> int:
    out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "dist" / "relex-legal-openai.zip"
    out.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(ROOT.rglob("*")):
            rel = p.relative_to(ROOT)
            if not p.is_file() or rel.parts[0] in EXCLUDE_TOP or p.name == ".DS_Store":
                continue
            z.write(p, str(rel)); n += 1
        if not (ROOT / "skills" / "jurisdictions" / "SKILL.md").exists():
            z.writestr("skills/jurisdictions/SKILL.md", JURISDICTIONS_SKILL); n += 1
    print(f"wrote {out} ({n} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
