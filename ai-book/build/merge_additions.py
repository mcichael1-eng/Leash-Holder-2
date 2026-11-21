#!/usr/bin/env python3
"""Insert verified Appendix G additions and renumber its figures.
Usage: merge_additions.py <G.md> <verified-*.json> [...]
Each JSON file holds {"additions": [{section, insert_after, name, markdown, source}]} (or a bare list)."""
import json
import re
import sys
from pathlib import Path

gp = Path(sys.argv[1])
adds = []
for f in sys.argv[2:]:
    d = json.loads(Path(f).read_text())
    adds += d["additions"] if isinstance(d, dict) else d
lines = gp.read_text().split("\n")


def find_line(text, start=0, end=None):
    t = text.strip()
    for i in range(start, len(lines) if end is None else end):
        if lines[i].strip() == t:
            return i
    return -1


done, failed = 0, []
for a in adds:
    md = a["markdown"].strip("\n")
    head = md.split("\n", 1)[0].strip()
    if find_line(head) != -1:
        failed.append((a["name"], "heading already present"))
        continue
    s = find_line(a["section"])
    if s == -1:
        failed.append((a["name"], "section not found"))
        continue
    e = next((i for i in range(s + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    pos = e
    if a.get("insert_after", "").strip():
        h = find_line(a["insert_after"], s, e)
        if h != -1:
            pos = next((i for i in range(h + 1, e) if lines[i].startswith("### ")), e)
    lines[pos:pos] = [""] + md.split("\n") + [""]
    done += 1

doc = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
n = 0


def renumber(m):
    global n
    n += 1
    return f"*Figure G.{n}:"


doc = re.sub(r"\*Figure G\.(?:X|[1-9]\d*):", renumber, doc)
gp.write_text(doc)
print(f"inserted {done}, failed {len(failed)}, figures {n}, entries {len(re.findall(r'^### ', doc, re.M))}")
for f in failed:
    print("  skipped:", f)
