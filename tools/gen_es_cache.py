#!/usr/bin/env python3
"""Extract the Spanish WCAG 2.0 SC texts from the cached Sidar translation.

Sidar labels every success criterion with a <strong class="sc-handle"> that
starts with the SC number, so we key the cache by number (1.1.1 ... 4.1.1).
Output: docs/es-sidar/es.json  {num: {"title": ..., "text": ...}}
Stdlib only.
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "es-sidar" / "source.html"
OUT = ROOT / "docs" / "es-sidar" / "es.json"

# Sidar wraps each SC in: <p class="sctxt"><strong class="sc-handle">N.N.N
# Title:</strong> body (Nivel X)</p>  — body may contain inline markup.
BLOCK = re.compile(
    r'<p class="sctxt"><strong class="sc-handle">\s*(\d+\.\d+\.\d+)'
    r'[^<]*?</strong>(.*?)</p>',
    re.S,
)
TAGS = re.compile(r"<[^>]+>")


def clean(fragment: str) -> str:
    return html.unescape(re.sub(r"\s+", " ", TAGS.sub("", fragment))).strip()


def main() -> int:
    text = SRC.read_text(encoding="utf-8", errors="replace")
    cache: dict[str, dict[str, str]] = {}
    for num, body in BLOCK.findall(text):
        cache[num] = {"title": "", "text": clean(body)}
    # Titles: the handle strong text itself (number + title up to the colon).
    handle = re.compile(
        r'<strong class="sc-handle">\s*(\d+\.\d+\.\d+)\s*(.*?)</strong>', re.S
    )
    for num, title in handle.findall(text):
        if num in cache:
            cache[num]["title"] = clean(title).rstrip(":")
    OUT.write_text(
        json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    print(f"wrote {OUT} — {len(cache)} SC texts (Sidar covers WCAG 2.0 only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
