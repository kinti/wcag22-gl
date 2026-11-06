#!/usr/bin/env python3
"""Deterministic preview: inline every data-include before serving.

python -m http.server randomly drops fragment fetches under ReSpec's
parallel load (respec-offender-data-include-failed-* sections appear
and whole SCs vanish from the render). Pre-inlining the includes the
way ReSpec's data-include-replace does (textual swap) removes the race.

Usage: inline_preview.py <index.html> <base_dir> <out.html>
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PAT = re.compile(
    r'<(section|dt|div)\b([^>]*\bdata-include="([^"]+)"[^>]*data-include-replace="true"[^>]*)>\s*</\1>'
    r'|<(section|dt|div)\b([^>]*\bdata-include-replace="true"[^>]*\bdata-include="([^"]+)"[^>]*)>\s*</\4>'
)


def main(argv: list[str]) -> int:
    index, base, out = Path(argv[1]), Path(argv[2]), Path(argv[3])
    t = index.read_text(encoding="utf-8")
    n = 0

    def sub(m: re.Match) -> str:
        nonlocal n
        inc = m.group(3) or m.group(6)
        frag = (base / inc).read_text(encoding="utf-8")
        n += 1
        return frag

    t = PAT.sub(sub, t)
    assert "data-include=" not in t, "quedan data-include sen inliner"
    out.write_text(t, encoding="utf-8")
    # sanidade: os 88 SC e 102 termos presentes
    sc = len(re.findall(r'<section id="[^"]+" class="sc', t))
    terms = len(re.findall(r"<dt><dfn id=", t)) + len(re.findall(r'<dt class="new"><dfn', t)) + len(re.findall(r'<dt><dfn[ >]', t))
    print(f"inlined {n} includes -> {out.name} | secciones sc: {sc} | dt-dfn: {len(re.findall(r'<dfn id=', t))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
