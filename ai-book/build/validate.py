#!/usr/bin/env python3
"""Validate every mermaid diagram in the given markdown files.
Usage: python3 validate.py chapter1.md [chapter2.md ...]
Prints OK or each failing diagram with its first lines and the parser error."""
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
items = []
for f in sys.argv[1:]:
    md = Path(f).read_text()
    for i, m in enumerate(re.finditer(r"^```mermaid\s*\n(.*?)^```", md, re.S | re.M), 1):
        line = md[:m.start()].count("\n") + 1
        items.append({"id": f"v{len(items)}", "code": m.group(1).rstrip("\n"), "file": f, "n": i, "line": line})
if not items:
    print("no mermaid diagrams found")
    sys.exit(0)
with tempfile.TemporaryDirectory() as td:
    inp, out = Path(td) / "in.json", Path(td) / "out.json"
    inp.write_text(json.dumps([{"id": it["id"], "code": it["code"]} for it in items]))
    subprocess.run(["node", str(TOOLS / "render.mjs"), str(inp), str(out)], check=True, cwd=str(TOOLS),
                   stdout=subprocess.DEVNULL)
    res = json.loads(out.read_text())
bad = 0
for it in items:
    r = res.get(it["id"], {})
    if "error" in r:
        bad += 1
        print(f"FAIL {it['file']} diagram #{it['n']} (line {it['line']}):")
        print("  " + "\n  ".join(it["code"].splitlines()[:4]))
        print("  ERROR: " + r["error"].replace("\n", "\n         ")[:500])
print(f"{len(items) - bad}/{len(items)} diagrams valid")
sys.exit(1 if bad else 0)
