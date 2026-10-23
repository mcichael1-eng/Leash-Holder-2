#!/usr/bin/env python3
"""List acronyms used in the book that have no glossary entry.
Usage: acronyms.py <book_dir> [--json out.json]"""
import json, re, sys
from pathlib import Path
from collections import defaultdict

book = Path(sys.argv[1])
outline = json.loads((book / "outline.json").read_text())
files = []
for p in outline["parts"]:
    for c in p["chapters"]:
        files.append((f"Ch {c['n']}", book / "chapters" / c["file"]))
for a in outline.get("appendices", []):
    files.append((f"App {a['letter']}", book / "appendices" / a["file"]))

gloss = (book / "GLOSSARY.md").read_text()
heads = re.findall(r"^- \*\*(.+?)\*\*", gloss, re.M)
known = set()
for h in heads:
    for tok in re.findall(r"[A-Za-z0-9&\-\.]+", h):
        known.add(tok.lower().strip(".-"))
        known.add(re.sub(r"s$", "", tok.lower()))
# also count inline definitions not in glossary yet: any "**Definition — X" in chapters
for _, f in files:
    if f.exists():
        for h in re.findall(r"\*\*Definition — (.+?):\*\*", f.read_text()):
            for tok in re.findall(r"[A-Za-z0-9&\-\.]+", h):
                known.add(tok.lower().strip(".-"))

STOP = set("I A AI OK US UK EU TV PC PM AM CEO CTO CFO PhD UN USA NYC LA IV VI VII VIII IX XI XII II III X V MIT FAQ PDF HTML URL USD".split())
acr = re.compile(r"(?<![A-Za-z0-9])([A-Z][A-Z0-9&]{1,9})(?:s|es)?(?![A-Za-z0-9])")
uses = defaultdict(list)
for label, f in files:
    if not f.exists():
        continue
    text = f.read_text()
    text = re.sub(r"```.*?```", "", text, flags=re.S)       # code, mermaid, ascii
    text = re.sub(r"`[^`]*`", "", text)
    text = re.sub(r"\(https?://[^)]*\)", "", text)
    for m in acr.finditer(text):
        a = m.group(1)
        if a in STOP or a.isdigit() or re.fullmatch(r"[0-9A-Z]*[0-9][0-9A-Z]*", a) and not re.search(r"[A-Z]{2}", a):
            continue
        uses[a].append(label)
missing = {}
for a, labs in uses.items():
    if a.lower() in known:
        continue
    seen = []
    for l in labs:
        if l not in seen:
            seen.append(l)
    missing[a] = {"count": len(labs), "where": seen}
items = sorted(missing.items(), key=lambda kv: -kv[1]["count"])
print(f"{len(uses)} distinct acronyms used; {len(missing)} with no glossary/definition entry")
for a, v in items[:int(dict(enumerate(sys.argv)).get(2, "0")) if False else None]:
    print(f"{a:10} {v['count']:4}  {', '.join(v['where'][:8])}{' ...' if len(v['where'])>8 else ''}")
if "--json" in sys.argv:
    by = defaultdict(list)
    for a, v in items:
        for l in v["where"]:
            by[l].append({"acronym": a, "chapters_using_it": len(v["where"]), "first_chapter": v["where"][0]})
    Path(sys.argv[sys.argv.index("--json") + 1]).write_text(json.dumps(by, indent=1))
