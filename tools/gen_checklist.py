#!/usr/bin/env python3
"""Generate the translation progress checklist from the w3c/wcag source.

Walks guidelines/sc/22 and guidelines/terms/22 fragment files, extracts the
English title of each, and writes docs/checklist.md with status columns.
Stdlib only.
"""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "source" / "guidelines"
OUT = ROOT / "docs" / "checklist.md"

# Special files outside sc/ and terms/
SPECIAL = [
    ("guidelines/index.html", "Main document (full REC)"),
    ("guidelines/input-purposes.html", "Input purposes table (SC 1.3.5/1.3.6)"),
    ("guidelines/relative-luminance.html", "Relative luminance calculator"),
    ("guidelines/respec-config.js", "ReSpec config — editors list"),
    ("fixup.js", "Published fixup.js (3 UI strings)"),
]

ACK_FILES = [
    "acknowledgements/ag-contributors.html",
    "acknowledgements/ag-wg-active.html",
    "acknowledgements/ag-wg-participants.html",
    "acknowledgements/funders.html",
]

H_PATTERNS = (
    r"<h2[^>]*>(.*?)</h2>",
    r"<h3[^>]*>(.*?)</h3>",
    r"<h4[^>]*>(.*?)</h4>",
    r"<h5[^>]*>(.*?)</h5>",
    r"<dfn[^>]*>(.*?)</dfn>",
    r"<title>(.*?)</title>",
)


def title_of(path: Path) -> str:
    """Extract the human title from an SC or terms fragment file."""
    text = path.read_text(encoding="utf-8", errors="replace")
    for pat in H_PATTERNS:
        m = re.search(pat, text, re.S)
        if m:
            t = re.sub(r"<[^>]+>", "", m.group(1))
            return html.unescape(t).strip()
    return "(no title)"


def table(rows: list[tuple[str, str]]) -> str:
    lines = ["| File | EN title | Status |", "|---|---|---|"]
    lines += [f"| `{f}` | {t} | ☐ pending |" for f, t in rows]
    return "\n".join(lines)


def main() -> int:
    sections: list[str] = []
    total = 0

    for sub, label in (
        ("sc/20", "Success Criteria WCAG 2.0 base — guidelines/sc/20"),
        ("sc/21", "Success Criteria added in 2.1 — guidelines/sc/21"),
        ("sc/22", "Success Criteria added in 2.2 — guidelines/sc/22"),
        ("terms/20", "Definitions 2.0 base — guidelines/terms/20"),
        ("terms/21", "Definitions added in 2.1 — guidelines/terms/21"),
        ("terms/22", "Definitions added in 2.2 — guidelines/terms/22"),
    ):
        files = sorted((SRC / sub).glob("*.html"))
        rows = [(f"guidelines/{sub}/{f.name}", title_of(f)) for f in files]
        total += len(rows)
        sections.append(f"### {label} ({len(rows)} files)\n\n{table(rows)}")

    total += len(SPECIAL)
    sections.append(f"### Special files ({len(SPECIAL)})\n\n{table(SPECIAL)}")
    total += len(ACK_FILES)
    sections.append(
        f"### Acknowledgements ({len(ACK_FILES)})\n\n{table([(f, '') for f in ACK_FILES])}"
    )

    header = (
        "# WCAG 2.2 galego — checklist de progreso\n\n"
        f"Fuente: w3c/wcag @ tag `WCAG22-20241212` · generado con "
        f"`tools/gen_checklist.py` · {total} piezas en total.\n\n"
        "Estados: ☐ pending · ✎ draft · ✓ reviewed (humano) · ★ approved\n\n"
    )
    OUT.write_text(header + "\n\n".join(sections) + "\n", encoding="utf-8")
    print(f"wrote {OUT} — {total} items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
