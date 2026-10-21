#!/usr/bin/env python3
"""Check chapters against STYLE.md. Usage: python3 check.py <book_dir> [chapter_numbers...]"""
import json
import re
import sys
from pathlib import Path

BOOK = Path(sys.argv[1])
only = {int(x) for x in sys.argv[2:]}
outline = json.loads((BOOK / "outline.json").read_text())
REQUIRED = ["What you'll learn", "Before you start", "In plain English", "Key terms", "Exercises",
            "Areas of opportunity", "Check your understanding", "Going deeper"]
emoji_re = re.compile("[\U0001F300-\U0001FAFF☀-⛿✀-➿]")
n_max = max(c["n"] for p in outline["parts"] for c in p["chapters"])

rows = []
for part in outline["parts"]:
    for ch in part["chapters"]:
        if only and ch["n"] not in only:
            continue
        path = BOOK / "chapters" / ch["file"]
        if not path.exists():
            rows.append((ch["n"], "MISSING", ["file not written yet"]))
            continue
        md = path.read_text()
        probs = []
        h1 = re.findall(r"^# (.+)$", md, re.M)
        if len(h1) != 1:
            probs.append(f"{len(h1)} H1s")
        elif not h1[0].startswith(f"Chapter {ch['n']}:"):
            probs.append(f"H1 should start 'Chapter {ch['n']}:' got {h1[0][:40]!r}")
        h2 = re.findall(r"^## (.+?)\s*$", md, re.M)
        for r in REQUIRED:
            if r not in h2:
                probs.append(f"missing section '{r}'")
        defs = re.findall(r"^> \*\*Definition — (.+?):\*\*", md, re.M)
        bad_defs = [l for l in re.findall(r"^> \*\*Definition.*$", md, re.M)
                    if not re.match(r"^> \*\*Definition — .+?:\*\* \S", l)]
        diagrams = len(re.findall(r"^```mermaid", md, re.M))
        ascii_d = len(re.findall(r"^```\s*$\n(?!\s*$)", md, re.M)) // 2
        tables = len(re.findall(r"^\|.*\|\s*$\n^\|[\s:|-]+\|\s*$", md, re.M))
        body = md.split("## Exercises")[0]
        words = len(re.findall(r"\w+", body))
        ex = re.findall(r"^\s*\d+\.\s+\*\*\[(Easy|Medium|Challenge)\]", md, re.M)
        callouts = {k: len(re.findall(rf"^> \*\*{k}", md, re.M))
                    for k in ["Key idea", "Analogy", "Try it", "At the frontier", "Watch out"]}
        if len(defs) < 20:
            probs.append(f"only {len(defs)} definitions")
        if bad_defs:
            probs.append(f"{len(bad_defs)} malformed definition lines e.g. {bad_defs[0][:60]!r}")
        if diagrams < 3:
            probs.append(f"only {diagrams} mermaid diagrams")
        if len(ex) < 6:
            probs.append(f"only {len(ex)} tagged exercises")
        if words < 4500:
            probs.append(f"short: {words} words before exercises")
        if emoji_re.search(md):
            probs.append("contains emoji")
        refs = {int(n) for n in re.findall(r"Chapter (\d+)", md)}
        badrefs = sorted(r for r in refs if r > n_max or r < 1)
        if badrefs:
            probs.append(f"refs to nonexistent chapters {badrefs}")
        if "<details>" not in md:
            probs.append("no <details> answers")
        stats = f"words={words} defs={len(defs)} mermaid={diagrams} tables={tables} ex={len(ex)} " + \
                " ".join(f"{k.split()[0].lower()}={v}" for k, v in callouts.items())
        rows.append((ch["n"], stats, probs))

for n, stats, probs in rows:
    flag = "OK " if not probs else "FIX"
    print(f"[{flag}] ch{n:02d} {stats}")
    for p in probs:
        print(f"        - {p}")
