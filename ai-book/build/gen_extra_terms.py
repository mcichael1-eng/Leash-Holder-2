#!/usr/bin/env python3
"""Collect every glossary entry from the research files into <book>/extra-terms.json.

Usage: python3 gen_extra_terms.py <research_dir> <book_dir>
build.py adds only the terms that no chapter already defines, so the published glossary
covers every term the research identified, with chapter definitions taking priority.
"""
import json
import re
import sys
from pathlib import Path

research, book = Path(sys.argv[1]), Path(sys.argv[2])
line_re = re.compile(r"^\s*(?:\d+\.|[-*])\s+\*\*(.+?)\*\*\s*[:—–.\-]?\s*(.+)$")
out, seen = [], set()
for f in sorted(research.glob("[01]*.md")):
    text = f.read_text()
    m = re.search(r"^## 2\..*?$(.*?)^## 3\.", text, re.S | re.M)
    if not m:
        continue
    for line in m.group(1).splitlines():
        lm = line_re.match(line)
        if not lm:
            continue
        term = lm.group(1).strip().rstrip(":.").strip()
        d = lm.group(2).strip()
        if re.search(r"\[(verify|S|unverified)[^\]]*\]", d, re.I):
            continue
        d = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1", d)      # markdown links -> text
        d = re.sub(r"\s*\((?:see |source: )?https?://[^)]*\)", "", d)     # bare URL citations
        d = re.sub(r"https?://\S+", "", d)
        d = re.sub(r"\[(?:P|S|[0-9]+)\]", "", d)                           # source tags
        d = d.replace("**", "").replace("`", "").strip()
        d = re.sub(r"\s{2,}", " ", d)
        if not term or len(d) < 15 or len(term) > 80:
            continue
        key = term.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append({"term": term, "definition": d, "source": f.name})
(book / "extra-terms.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(f"{len(out)} research glossary terms written")
