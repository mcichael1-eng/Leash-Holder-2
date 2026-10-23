#!/usr/bin/env python3
"""Group definition callouts by the glossary merge key (build.py gkey) to find homonyms and inconsistent repeats.
Usage: defgroups.py <book_dir> <out.json>"""
import json, re, sys
from pathlib import Path
book = Path(sys.argv[1])
o = json.loads((book / "outline.json").read_text())
files = [(f"Ch {c['n']}", book / "chapters" / c["file"]) for p in o["parts"] for c in p["chapters"]]
files += [(f"App {a['letter']}", book / "appendices" / a["file"]) for a in o.get("appendices", [])]
def gkey(term):
    k = re.sub(r"\s*\(.*?\)\s*", " ", term).strip().lower()
    return re.sub(r"[^a-z0-9+#./ -]", "", k)
groups = {}
for label, f in files:
    if not f.exists():
        continue
    for i, line in enumerate(f.read_text().split("\n"), 1):
        m = re.match(r"> \*\*Definition — (.+?):\*\*\s*(.*)", line)
        if m:
            groups.setdefault(gkey(m.group(1)), []).append(
                {"where": label, "file": str(f.relative_to(book)), "line": i, "term": m.group(1), "body": m.group(2)})
multi = {k: v for k, v in groups.items() if len(v) > 1}
Path(sys.argv[2]).write_text(json.dumps(multi, indent=1, ensure_ascii=False))
print(f"{len(groups)} distinct keys, {len(multi)} defined more than once, "
      f"{sum(len(v) for v in multi.values())} callouts in those groups")
