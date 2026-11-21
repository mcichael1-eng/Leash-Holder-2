#!/usr/bin/env python3
"""Check every internal link in the built site: the target page exists and the #anchor is an id on it.
Usage: linkcheck.py <site_dir>"""
import html
import re
import sys
from pathlib import Path

site = Path(sys.argv[1])
pages = {p.name: p.read_text() for p in site.glob("*.html")}
ids = {n: set(re.findall(r'\bid="([^"]+)"', t)) for n, t in pages.items()}
total, broken = 0, []
for name, text in pages.items():
    for href in re.findall(r'\bhref="([^"]+)"', text):
        href = html.unescape(href)
        if re.match(r"^[a-z][a-z0-9+.-]*:", href, re.I):
            continue  # external (http:, mailto:, data:)
        total += 1
        page, _, anchor = href.partition("#")
        target = page or name
        if target not in pages:
            if not (site / target).exists():
                broken.append((name, href, "no such file"))
            continue
        if anchor and anchor not in ids[target]:
            broken.append((name, href, "no such anchor"))
print(f"{len(pages)} pages, {total} internal links, {len(broken)} broken")
for b in broken[:50]:
    print("  ", *b)
sys.exit(1 if broken else 0)
