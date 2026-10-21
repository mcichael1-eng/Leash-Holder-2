#!/usr/bin/env python3
"""Build the AI Field Guide into a small multi-page website plus a generated glossary.

Usage: python3 build.py <book_dir> <out_dir>
  <book_dir> holds outline.json, chapters/, appendices/ and optional extra-terms.json.
  <out_dir> receives index.html (the home page, no doctype: the artifact host wraps it),
  p1.html ... p10.html (one page per Part), reference.html, glossary.html, exercises.html.
Needs pandoc on PATH and node with mermaid-cli's node_modules next to render.mjs
(or set MERMAID_TOOLS to that directory).
"""
import hashlib
import html
import json
import os
import re
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
NODE_TOOLS = Path(os.environ.get("MERMAID_TOOLS", TOOLS))
BOOK = Path(sys.argv[1])
OUT = Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
CACHE = Path(os.environ.get("DIAGRAM_CACHE", BOOK / ".diagram-cache.json"))

outline = json.loads((BOOK / "outline.json").read_text())
ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]


def pandoc(md_path, prefix):
    res = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none", "--lua-filter", str(TOOLS / "filter.lua"),
         f"--id-prefix={prefix}-", str(md_path)],
        capture_output=True, text=True, check=True)
    return res.stdout


# ---------------------------------------------------------------- units and pages
units = []
for pi, part in enumerate(outline["parts"], 1):
    for ch in part["chapters"]:
        path = BOOK / "chapters" / ch["file"]
        if not path.exists():
            print(f"missing chapter file: {path}", file=sys.stderr)
            continue
        units.append({"kind": "chapter", "id": f"ch{ch['n']}", "num": ch["n"], "part": pi,
                      "page": f"p{pi}.html", "path": path, "md": path.read_text()})
for ap in outline.get("appendices", []):
    path = BOOK / "appendices" / ap["file"]
    if not path.exists():
        print(f"missing appendix file: {path}", file=sys.stderr)
        continue
    units.append({"kind": "appendix", "id": f"app{ap['letter']}", "num": ap["letter"], "part": None,
                  "page": "reference.html", "path": path, "md": path.read_text()})

page_of = {u["id"]: u["page"] for u in units}
valid_chapters = {u["num"] for u in units if u["kind"] == "chapter"}
valid_appendices = {u["num"] for u in units if u["kind"] == "appendix"}

for u in units:
    raw = pandoc(u["path"], u["id"])
    m = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.S)
    full = html.unescape(re.sub(r"<[^>]+>", "", m.group(1)).strip()) if m else u["path"].stem
    u["title"] = re.sub(r"^(Chapter\s+\d+|Appendix\s+[A-Z])\s*[:.\-—]\s*", "", full)
    u["html"] = raw[m.end():] if m else raw

# ---------------------------------------------------------------- diagrams
cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
src_re = re.compile(r'<pre class="mermaid-src">(.*?)</pre>', re.S)
pending = {}
for u in units:
    for m in src_re.finditer(u["html"]):
        code = html.unescape(m.group(1))
        key = hashlib.sha1(code.encode()).hexdigest()
        if key not in cache:
            pending[key] = code
if pending:
    tmp_in, tmp_out = BOOK / ".render-in.json", BOOK / ".render-out.json"
    tmp_in.write_text(json.dumps([{"id": "d" + k[:12], "code": c} for k, c in pending.items()]))
    subprocess.run(["node", str(TOOLS / "render.mjs"), str(tmp_in), str(tmp_out)], check=True,
                   env={**os.environ, "NODE_PATH": str(NODE_TOOLS / "node_modules")}, cwd=str(NODE_TOOLS))
    rendered = json.loads(tmp_out.read_text())
    for k in pending:
        cache[k] = rendered["d" + k[:12]]
    CACHE.write_text(json.dumps(cache))
    tmp_in.unlink()
    tmp_out.unlink()

ATTR_NUM = re.compile(r'(\s(?:d|transform|x|y|x1|y1|x2|y2|cx|cy|r|rx|ry|width|height|points|viewBox|style|dx|dy)=")([^"]*)"')


def shrink_svg(svg, page_styles):
    """Move the diagram's scoped <style> into a shared per-page block and round coordinates."""
    m = re.search(r'<svg[^>]*\sid="([^"]+)"', svg)
    rd = re.search(r'aria-roledescription="([^"]+)"', svg)
    if m:
        sid = m.group(1)
        kind = "mmd-" + re.sub(r"[^a-z0-9-]", "", (rd.group(1) if rd else "x").lower())
        st = re.search(r"<style>(.*?)</style>", svg, re.S)
        if st:
            css = st.group(1).replace("#" + sid, "." + kind)
            page_styles.setdefault(css, kind)
            svg = svg[:st.start()] + svg[st.end():]
            svg = re.sub(r"<svg\b", f'<svg data-k="{kind}"', svg, count=1)
            if re.search(r'<svg[^>]*\sclass="', svg[:400]):
                svg = re.sub(r'(<svg[^>]*\sclass=")', r"\1" + kind + " ", svg, count=1)
            else:
                svg = re.sub(r"<svg\b", f'<svg class="{kind}"', svg, count=1)

    def rnd(mm):
        return mm.group(1) + re.sub(r"(\d+\.\d)\d+", r"\1", mm.group(2)) + '"'
    return ATTR_NUM.sub(rnd, svg)


failures = []
page_styles = {}  # page -> {css: kind}


def diagram(m, u):
    code = html.unescape(m.group(1))
    r = cache.get(hashlib.sha1(code.encode()).hexdigest(), {})
    if "svg" in r:
        svg = shrink_svg(r["svg"], page_styles.setdefault(u["page"], {}))
        return f'<figure class="diagram"><div class="diagram-scroll">{svg}</div></figure>'
    failures.append((u["id"], r.get("error", "not rendered")[:200], code.splitlines()[0] if code else ""))
    return f'<figure class="diagram diagram-text"><pre>{html.escape(code)}</pre></figure>'


for u in units:
    u["html"] = src_re.sub(lambda m: diagram(m, u), u["html"])
    u["html"] = re.sub(r"<p><em>((?:Figure|Table)\s+[\w.]+[:.].*?)</em></p>",
                       r'<p class="caption">\1</p>', u["html"], flags=re.S)
    u["html"] = u["html"].replace("<table>", '<div class="table-scroll"><table>').replace("</table>", "</table></div>")

# ---------------------------------------------------------------- cross links
SKIP = {"a", "h1", "h2", "h3", "h4", "code", "pre", "svg", "summary"}


def href(uid, anchor=None):
    return f'{page_of.get(uid, "index.html")}#{anchor or uid}'


def link_refs(text):
    def ch(m):
        n = int(m.group(2))
        if n in valid_chapters:
            return f'<a class="xref" href="{href(f"ch{n}")}">{m.group(1)} {n}</a>'
        return m.group(0)

    def ap(m):
        L = m.group(1)
        if L in valid_appendices:
            return f'<a class="xref" href="{href(f"app{L}")}">Appendix {L}</a>'
        return m.group(0)
    text = re.sub(r"\b(Chapter|chapter|Ch\.)\s+(\d{1,2})\b", ch, text)
    return re.sub(r"\bAppendix\s+([A-Z])\b", ap, text)


def crosslink(doc):
    out, stack = [], []
    for p in re.split(r"(<[^>]+>)", doc):
        if p.startswith("<"):
            m = re.match(r"<(/?)([a-zA-Z0-9]+)", p)
            if m and m.group(2).lower() in SKIP:
                name = m.group(2).lower()
                if m.group(1):
                    if name in stack:
                        while stack and stack.pop() != name:
                            pass
                elif not p.endswith("/>"):
                    stack.append(name)
            out.append(p)
        else:
            out.append(p if stack else link_refs(p))
    return "".join(out)


for u in units:
    u["html"] = crosslink(u["html"])

# ---------------------------------------------------------------- glossary
def_re = re.compile(
    r'<div id="([^"]+)"\s+class="callout def"\s+data-term="([^"]*)">\s*<p><span class="def-term">.*?</span>\s*(.*?)</p>\s*</div>',
    re.S)


def gkey(term):
    k = re.sub(r"\s*\(.*?\)\s*", " ", term).strip().lower()
    return re.sub(r"[^a-z0-9+#./ -]", "", k)


gloss = {}
for u in units:
    for m in def_re.finditer(u["html"]):
        anchor, term, body = m.group(1), html.unescape(m.group(2)), m.group(3).strip()
        e = gloss.setdefault(gkey(term), {"term": term, "body": body, "refs": []})
        if len(term) > len(e["term"]):
            e["term"] = term
        label = f"Ch {u['num']}" if u["kind"] == "chapter" else f"App {u['num']}"
        if not any(r[1] == label for r in e["refs"]):
            e["refs"].append((f'{u["page"]}#{anchor}', label))
extra_file = BOOK / "extra-terms.json"
n_extra = 0
if extra_file.exists():
    for t in json.loads(extra_file.read_text()):
        k = gkey(t["term"])
        if k and k not in gloss:
            gloss[k] = {"term": t["term"], "body": html.escape(t["definition"]), "refs": [], "extra": True}
            n_extra += 1


def first_letter(term):
    f = (re.sub(r"[^A-Za-z0-9]", "", term)[:1] or "#").upper()
    return "#" if f.isdigit() else f


entries = sorted(gloss.values(), key=lambda e: re.sub(r"[^a-z0-9]", "", e["term"].lower()) or e["term"])
letters, gl_html, cur = [], [], None
for e in entries:
    L = first_letter(e["term"])
    if L != cur:
        if cur is not None:
            gl_html.append("</dl>")
        cur = L
        letters.append(L)
        gl_html.append(f'<h3 class="gl-letter" id="gl-{"num" if L == "#" else L}">{L}</h3><dl class="gl-list">')
    refs = " ".join(f'<a href="{a}">{l}</a>' for a, l in e["refs"])
    search = html.escape((e["term"] + " " + re.sub(r"<[^>]+>", "", e["body"])).lower(), quote=True)
    gl_html.append(f'<div class="gl-entry" data-search="{search}"><dt>{html.escape(e["term"])}</dt>'
                   f'<dd>{e["body"]} <span class="gl-refs">{refs}</span></dd></div>')
if cur is not None:
    gl_html.append("</dl>")
letter_nav = "".join(f'<a href="#gl-{"num" if L == "#" else L}">{L}</a>' for L in letters)
glossary_main = (f'<section class="unit glossary" id="glossary"><header class="unit-head">'
                 f'<p class="eyebrow">Reference</p><h1>Glossary</h1>'
                 f'<p class="lede">Every term in the book, {len(entries):,} in all. Entries with chapter tags link to the place '
                 f'where the term is explained in context.</p></header>'
                 f'<div class="gl-tools"><label for="gl-search">Find a term</label>'
                 f'<input id="gl-search" type="search" placeholder="Try: token, HBM, PUE, RLHF" autocomplete="off">'
                 f'<p id="gl-count" class="gl-count" aria-live="polite"></p></div>'
                 f'<nav class="gl-letters" aria-label="Glossary letters">{letter_nav}</nav>'
                 + "".join(gl_html) + "</section>")

md_lines = ["# Glossary", "", f"*Every term in the book ({len(entries)} terms), generated from the chapters.*", ""]
cur = None
for e in entries:
    L = first_letter(e["term"])
    if L != cur:
        cur = L
        md_lines += ["", f"## {L}", ""]
    body = html.unescape(re.sub(r"<[^>]+>", "", e["body"]))
    refs = ", ".join(l.replace("Ch ", "Chapter ").replace("App ", "Appendix ") for _, l in e["refs"])
    md_lines.append(f"- **{e['term']}** — {body}" + (f" *({refs})*" if refs else ""))
(BOOK / "GLOSSARY.md").write_text("\n".join(md_lines) + "\n")

# ---------------------------------------------------------------- exercise index
ex_re = re.compile(r"^\s*\d+\.\s+\*\*\[(Easy|Medium|Challenge)\]\s+(.+?)\*\*", re.M)
ex_rows = {"Easy": [], "Medium": [], "Challenge": []}
for u in units:
    if u["kind"] != "chapter":
        continue
    sec = u["md"].split("## Exercises", 1)
    if len(sec) == 2:
        for m in ex_re.finditer(sec[1].split("\n## ", 1)[0]):
            ex_rows[m.group(1)].append((u, m.group(2).rstrip(".")))
n_ex = sum(len(v) for v in ex_rows.values())
ex_parts = ['<section class="unit exercises-index" id="exercises"><header class="unit-head">'
            '<p class="eyebrow">Reference</p><h1>Every exercise</h1>'
            f'<p class="lede">{n_ex} hands-on exercises, grouped by level. Start with Easy ones from any chapter you have read.</p></header>']
for lvl in ["Easy", "Medium", "Challenge"]:
    ex_parts.append(f'<h2>{lvl} <span class="count">{len(ex_rows[lvl])}</span></h2><ul class="ex-list">')
    for u, t in ex_rows[lvl]:
        ex_parts.append(f'<li><a href="{u["page"]}#{u["id"]}-exercises">Ch {u["num"]}</a> {html.escape(t)}</li>')
    ex_parts.append("</ul>")
ex_parts.append("</section>")
exercises_main = "".join(ex_parts)

# ---------------------------------------------------------------- shared pieces
parts = outline["parts"]
chapters_by_part = {pi: [u for u in units if u["kind"] == "chapter" and u["part"] == pi] for pi in range(1, len(parts) + 1)}
apps = [u for u in units if u["kind"] == "appendix"]


def toc(current_page):
    out = ['<ol class="toc-parts">']
    for pi, part in enumerate(parts, 1):
        here = " here" if current_page == f"p{pi}.html" else ""
        out.append(f'<li class="toc-part"><a class="toc-part-link{here}" href="p{pi}.html#part{pi}">'
                   f'<span class="toc-num">Part {ROMAN[pi]}</span> {html.escape(part["title"])}</a><ol>')
        for u in chapters_by_part[pi]:
            out.append(f'<li><a href="{u["page"]}#{u["id"]}" data-unit="{u["id"]}"><span class="toc-num">{u["num"]}</span>'
                       f'<span class="toc-title">{html.escape(u["title"])}</span></a></li>')
        out.append("</ol></li>")
    here = " here" if current_page in ("reference.html", "glossary.html", "exercises.html") else ""
    out.append(f'<li class="toc-part"><a class="toc-part-link{here}" href="reference.html#reference">'
               '<span class="toc-num">Reference</span> Look things up</a><ol>')
    for u in apps:
        out.append(f'<li><a href="reference.html#{u["id"]}"><span class="toc-num">{u["num"]}</span>'
                   f'<span class="toc-title">{html.escape(u["title"])}</span></a></li>')
    out.append('<li><a href="glossary.html#glossary"><span class="toc-num">G</span><span class="toc-title">Glossary</span></a></li>')
    out.append('<li><a href="exercises.html#exercises"><span class="toc-num">X</span><span class="toc-title">Every exercise</span></a></li>')
    out.append("</ol></li></ol>")
    return "".join(out)


def pager(prev, nxt):
    out = ['<nav class="pager" aria-label="Pages">']
    if prev:
        out.append(f'<a class="prev" href="{prev[0]}"><small>Previous</small><span>{html.escape(prev[1])}</span></a>')
    if nxt:
        out.append(f'<a class="next" href="{nxt[0]}"><small>Next</small><span>{html.escape(nxt[1])}</span></a>')
    out.append("</nav>")
    return "".join(out)


def chapter_section(u, pi):
    return (f'<section class="unit chapter" id="{u["id"]}" data-unit="{u["id"]}">'
            f'<header class="unit-head"><p class="eyebrow">Part {ROMAN[pi]} · Chapter {u["num"]}</p>'
            f'<h1>{html.escape(u["title"])}</h1></header>{u["html"]}'
            f'<footer class="unit-foot"><label class="read-toggle"><input type="checkbox" id="read-{u["id"]}" data-read="{u["id"]}"> '
            f'Mark chapter {u["num"]} as read</label></footer></section>')


stats = {
    "parts": len(parts),
    "chapters": len([u for u in units if u["kind"] == "chapter"]),
    "terms": len(entries),
    "exercises": n_ex,
    "diagrams": sum(len(re.findall(r'<figure class="diagram', u["html"])) for u in units),
    "words": sum(len(re.findall(r"\w+", u["md"])) for u in units),
}
tpl = (TOOLS / "template.html").read_text()
COLOPHON = ('<p class="colophon">The AI Field Guide, October 2026 edition. Researched and written with Claude. '
            'Facts about fast-moving areas (models, chips, data centers, law) reflect sources available in October 2026 '
            'and will date; the Going deeper lists point to primary sources.</p>')
DOC_HEAD = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
            'body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>')


def render_page(name, title, main, standalone=True):
    css = page_styles.get(name, {})
    style = "<style>" + "".join(css.keys()) + "</style>" if css else ""
    page = (tpl.replace("{{TITLE}}", html.escape(title)).replace("{{TOC}}", toc(name))
            .replace("{{PAGE_STYLE}}", style).replace("{{MAIN}}", main + COLOPHON)
            .replace("{{N_CHAPTERS}}", str(stats["chapters"])))
    if standalone:
        head, body = page.split("<header class=\"topbar\">", 1)
        page = DOC_HEAD + head + "</head><body><header class=\"topbar\">" + body + "</body></html>"
    (OUT / name).write_text(page)
    return len(page)


sizes = {}
# Home page
cover = (TOOLS / "cover.html").read_text()
cover = (cover.replace("{{N_PARTS}}", str(stats["parts"])).replace("{{N_CHAPTERS}}", str(stats["chapters"]))
         .replace("{{N_TERMS}}", f'{stats["terms"]:,}').replace("{{N_DIAGRAMS}}", str(stats["diagrams"]))
         .replace("{{N_EXERCISES}}", str(stats["exercises"]))
         .replace("{{STACK}}", "".join(f'<li><a href="{html.escape(s["href"])}">{html.escape(s["label"])} '
                                        f'<small>{html.escape(s["note"])}</small></a></li>' for s in outline.get("stack", []))))
home = [cover, '<section class="contents-home" aria-label="Contents"><h2>Contents</h2>']
for pi, part in enumerate(parts, 1):
    home.append(f'<div class="ch-part"><div><h3><a href="p{pi}.html#part{pi}"><small>Part {ROMAN[pi]}</small>'
                f'{html.escape(part["title"])}</a></h3><p>{html.escape(part.get("blurb", ""))}</p></div><ol>')
    for u in chapters_by_part[pi]:
        home.append(f'<li><a href="{u["page"]}#{u["id"]}" data-unit="{u["id"]}"><span class="toc-num">{u["num"]}</span>'
                    f'<span>{html.escape(u["title"])}</span></a></li>')
    home.append("</ol></div>")
home.append('<div class="ch-part"><div><h3><a href="reference.html#reference"><small>Reference</small>Look things up</a></h3>'
            '<p>Cheat sheets, a dated timeline, who is who, resources, the full glossary and every exercise.</p></div><ol>')
for u in apps:
    home.append(f'<li><a href="reference.html#{u["id"]}"><span class="toc-num">{u["num"]}</span><span>{html.escape(u["title"])}</span></a></li>')
home.append('<li><a href="glossary.html#glossary"><span class="toc-num">G</span><span>Glossary</span></a></li>'
            '<li><a href="exercises.html#exercises"><span class="toc-num">X</span><span>Every exercise</span></a></li></ol></div></section>')
home.append(pager(None, ("p1.html#part1", f"Part I: {parts[0]['title']}")))
sizes["index.html"] = render_page("index.html", "The AI Field Guide", "".join(home), standalone=False)

# Part pages
for pi, part in enumerate(parts, 1):
    chs = chapter_section
    main = [f'<section class="part-opener" id="part{pi}"><p class="eyebrow">Part {ROMAN[pi]}</p>'
            f'<h1>{html.escape(part["title"])}</h1><p class="lede">{html.escape(part.get("blurb", ""))}</p>'
            '<ol class="part-chapters">'
            + "".join(f'<li><a href="#{u["id"]}"><span class="toc-num">{u["num"]}</span> {html.escape(u["title"])}</a></li>'
                      for u in chapters_by_part[pi]) + "</ol></section>"]
    main += [chapter_section(u, pi) for u in chapters_by_part[pi]]
    prev = (f"p{pi-1}.html#part{pi-1}", f"Part {ROMAN[pi-1]}: {parts[pi-2]['title']}") if pi > 1 else ("index.html", "Contents")
    nxt = (f"p{pi+1}.html#part{pi+1}", f"Part {ROMAN[pi+1]}: {parts[pi]['title']}") if pi < len(parts) else ("reference.html#reference", "Reference")
    main.append(pager(prev, nxt))
    sizes[f"p{pi}.html"] = render_page(f"p{pi}.html", f"Part {ROMAN[pi]}: {part['title']} · The AI Field Guide", "".join(main))

# Reference pages
ref = ['<section class="part-opener" id="reference"><p class="eyebrow">Reference</p><h1>Look things up</h1>'
       '<p class="lede">Cheat sheets, a dated timeline, who is who and where to learn more. The glossary and the exercise index have their own pages.</p>'
       '<ol class="part-chapters">' + "".join(f'<li><a href="#{u["id"]}"><span class="toc-num">{u["num"]}</span> {html.escape(u["title"])}</a></li>' for u in apps)
       + '<li><a href="glossary.html#glossary"><span class="toc-num">G</span> Glossary</a></li>'
       '<li><a href="exercises.html#exercises"><span class="toc-num">X</span> Every exercise</a></li></ol></section>']
for u in apps:
    ref.append(f'<section class="unit appendix" id="{u["id"]}"><header class="unit-head"><p class="eyebrow">Appendix {u["num"]}</p>'
               f'<h1>{html.escape(u["title"])}</h1></header>{u["html"]}</section>')
ref.append(pager((f"p{len(parts)}.html#part{len(parts)}", f"Part {ROMAN[len(parts)]}: {parts[-1]['title']}"), ("glossary.html#glossary", "Glossary")))
sizes["reference.html"] = render_page("reference.html", "Reference · The AI Field Guide", "".join(ref))
sizes["glossary.html"] = render_page("glossary.html", "Glossary · The AI Field Guide",
                                     glossary_main + pager(("reference.html#reference", "Reference"), ("exercises.html#exercises", "Every exercise")))
sizes["exercises.html"] = render_page("exercises.html", "Every exercise · The AI Field Guide",
                                      exercises_main + pager(("glossary.html#glossary", "Glossary"), ("index.html", "Contents")))

stats["extra_terms"] = n_extra
print(json.dumps(stats))
print("pages:", ", ".join(f"{k}={v/1e6:.2f}MB" for k, v in sizes.items()), f"total={sum(sizes.values())/1e6:.1f}MB")
for f in failures:
    print("DIAGRAM FAIL", f)
