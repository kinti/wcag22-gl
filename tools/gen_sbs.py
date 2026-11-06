#!/usr/bin/env python3
"""Generate side-by-side drafting sheets: EN | ES (Sidar 2.0) | GL (to write).

Data sources:
  guidelines/wcag.json   -> the 87 SC (num, handle, id slug, version folder)
  guidelines/sc/*/       -> EN fragment files (the translation source of truth)
  docs/es-sidar/es.json  -> Spanish reference (2.0 only; 2.1/2.2 does not exist)

Usage: gen_sbs.py            -> sheets for all four principles (p1..p4)
       gen_sbs.py 2.5        -> single guideline sheet
Output: docs/sbs/p{1..4}.md  — GL column intentionally empty: that is the work.
Stdlib only.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GL = ROOT / "source" / "guidelines"
ES = json.loads((ROOT / "docs" / "es-sidar" / "es.json").read_text(encoding="utf-8"))
OUT = ROOT / "docs" / "sbs"

TAGS = re.compile(r"<[^>]+>")


def plain(fragment: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", TAGS.sub("", fragment)).strip()


def fragment_path(slug: str) -> Path:
    for ver in ("20", "21", "22"):
        p = GL / "sc" / ver / f"{slug}.html"
        if p.exists():
            return p
    raise FileNotFoundError(slug)


def slug_of(sc_id: str) -> str:
    return sc_id.split(":", 1)[1]


def sheet(principle: dict, es_cache: dict) -> str:
    lines = [
        f"# Hoja side-by-side — Principio {principle['num']}: "
        f"{principle['handle']} / ES ref. — GL: __redactar aquí__",
        "",
        "> EN = fuente normativo (única autoridad de fidelidad). "
        "ES = referencia Sidar 2.0 (SOLO ayuda; no tiene autoridad y no existe "
        "para 2.1/2.2). Redactar ES→GL está permitido, verificar contra EN.",
        "",
    ]
    for g in principle["guidelines"]:
        lines += [f"## Pauta {g['num']} — EN: {g['handle']}",
                  f"### ES: {'(sin referencia española)' if g['num'] not in ('1','2','3','4') else ''}", ""]
        for sc in g["successcriteria"]:
            num, slug = sc["num"], slug_of(sc["id"])
            frag = fragment_path(slug).read_text(encoding="utf-8", errors="replace")
            es = es_cache.get(num)
            lines += [
                f"### {num} {sc['handle']}  (nivel {sc['level']}; "
                f"`sc/{slug}.html`)",
                "",
                "**EN (normativo):**",
                "",
                "```",
                plain(frag),
                "```",
                "",
                "**ES (Sidar 2.0):**" if es else
                "**ES: NO EXISTE — solo fuente EN**",
                "",
                "```" if es else "",
                es and f"{es['title']}: {es['text']}" or "",
                "```" if es else "",
                "",
                "**GL (redactar):**",
                "",
                "```",
                "",
                "```",
                "",
            ]
    return "\n".join(lines)


def main() -> int:
    data = json.loads((GL / "wcag.json").read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    args = sys.argv[1:]
    n = 0
    for principle in data["principles"]:
        if args and not any(principle["num"].startswith(a) for a in args):
            continue
        path = OUT / f"p{principle['num']}.md"
        path.write_text(sheet(principle, ES), encoding="utf-8")
        total = sum(len(g["successcriteria"]) for g in principle["guidelines"])
        print(f"wrote {path} — {total} SC")
        n += 1
    print(f"done — {n} sheet(s); ES cache covers {len(ES)} of 87 SC")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
