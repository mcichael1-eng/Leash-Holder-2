#!/usr/bin/env python3
"""Write ai-book/README.md from outline.json and the stats line printed by build.py.

Usage: python3 gen_readme.py <book_dir> '<stats json>' [artifact_url]
"""
import json
import sys
from pathlib import Path

book = Path(sys.argv[1])
stats = json.loads(sys.argv[2])
url = sys.argv[3] if len(sys.argv) > 3 else ""
outline = json.loads((book / "outline.json").read_text())
roman = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

lines = [
    "# The AI Field Guide",
    "",
    "*Everything about artificial intelligence, built up from nothing. October 2026 edition.*",
    "",
    "A complete book for someone with almost no computer-science background who uses AI chatbots every day "
    "and wants to understand all of it: how computers work, the math, how machines learn, neural networks and "
    "Transformers, how frontier labs build large language models, how to build with AI, chips and compute, "
    "data centers and energy, every major branch of AI, safety, law and society, and the skills, careers and "
    "opportunities that come with it.",
    "",
    f"- **{stats['parts']} parts, {stats['chapters']} chapters, {len(outline.get('appendices', []))} appendices**",
    f"- **{stats['terms']:,} terms** in a searchable glossary (every term is defined where it first appears)",
    f"- **{stats['diagrams']} diagrams**, plus tables and hand-worked numeric examples",
    f"- **{stats['exercises']} exercises** from Easy to Challenge, none of which require prior coding experience",
    f"- About **{round(stats['words'], -4):,} words**",
    "",
    "## How to read it",
    "",
]
if url:
    lines += [f"- **Online:** {url} (contents sidebar, every diagram drawn, searchable glossary, reading progress).", ""]
lines += [
    "- **Offline:** open `site/index.html` in a browser after building (see below), or read the Markdown chapters "
    "in `chapters/` directly on GitHub, which also renders the diagrams.",
    "- Read in order if you are new: each chapter assumes only the ones before it. Chapter 1 maps the whole field and "
    "suggests three reading paths.",
    "- Look for the boxes: **Definition** (every term), **Key idea**, **Analogy**, **Try it** (a one-minute experiment), "
    "**At the frontier (2026)** (what leading labs do now) and **Watch out** (common mistakes).",
    "",
    "## Contents",
    "",
]
for pi, part in enumerate(outline["parts"], 1):
    lines.append(f"### Part {roman[pi]}: {part['title']}")
    lines.append("")
    lines.append(f"*{part.get('blurb', '')}*")
    lines.append("")
    for ch in part["chapters"]:
        lines.append(f"{ch['n']}. [{ch['title']}](chapters/{ch['file']})")
    lines.append("")
lines += ["### Reference", ""]
for ap in outline.get("appendices", []):
    lines.append(f"- Appendix {ap['letter']}: [{ap['title']}](appendices/{ap['file']})")
lines += ["- [Glossary](GLOSSARY.md) (generated)", ""]
lines += [
    "## How it was made",
    "",
    "1. **Research.** Ten research agents mapped every area of AI (foundations, machine learning and data, deep learning, "
    "large language models, building with AI, compute and chips, data centers and energy, the branches of AI, "
    "safety and policy, careers and opportunity), checking 2025–2026 facts against sources.",
    "2. **Outline.** The findings became a 66-chapter outline with a brief for every chapter (`planning/OUTLINE.md`) "
    "and a house style (`planning/STYLE.md`).",
    "3. **Writing.** Writer agents drafted two chapters each from the research, then validated every diagram and "
    "checked every chapter against the style rules.",
    "4. **Editing.** One editor per Part re-checked worked calculations, facts, cross-references and consistency "
    "across chapters, and hedged anything the research could not confirm.",
    "5. **Coverage audit.** Every one of the 832 topics in the research topic maps (including every skill and every "
    "role) was traced to the chapter that teaches it. 819 were already fully taught, 13 were thin and none were "
    "missing; the 13 were filled. The per-topic tables are in `planning/coverage/`.",
    "6. **Beginner read-through.** A reader-test pass through ten chapters across the difficulty range, from the "
    "point of view of someone with no computer-science background, fixed 65 places where that reader would get "
    "lost (`planning/coverage/reader-test.md`).",
    "7. **External-standard audit.** The book was then checked against 15 outside references: Russell & Norvig's "
    "*Artificial Intelligence: A Modern Approach*, the ACM/IEEE CS2023 AI curriculum, Goodfellow et al.'s *Deep Learning*, "
    "*Dive into Deep Learning*, Stanford CS229, CS231n, CS224n and CS336, Chip Huyen's *AI Engineering* and *Designing "
    "Machine Learning Systems*, the Hugging Face LLM and Agents courses, Full Stack Deep Learning, *The Datacenter as a "
    "Computer*, Hennessy & Patterson on domain-specific architectures, *How to Scale Your Model*, Hendrycks' *AI Safety, "
    "Ethics, and Society*, BlueDot's alignment course and the EU AI Act. Of 878 topics, 819 are in scope for this "
    "reader (the rest are graduate-level mathematics, named where the reader will meet them). The book taught 541 of "
    "the 819 before the audit and teaches all 819 after it. Per-standard tables are in `planning/coverage/external-*.md`.",
    "8. **Verified online.** With web access, every one of those tables of contents was checked against the real "
    "published contents and syllabi (including newer editions such as the free 4th edition of *The Data Center as a "
    "Computer* and the 2026 Stanford course pages). Topics the first audit had missed were added and taught; "
    "the book now covers every in-scope topic of every standard, and every topic judged out of scope is explained "
    "in plain words in Appendix F, The Advanced Shelf.",
    "9. **Fact-check against current sources.** Ten fact-checkers, one per Part plus the appendices, checked about "
    "1,200 time-sensitive claims (models, prices, chips, data-center projects, laws, people) against primary sources "
    "as of October 2026: about 115 were corrected, about 50 recent developments were added, and claims that only "
    "the press supports are marked \"reported\". Every web link was checked (`planning/coverage/freshness-*.md`). "
    "A consistency sweep then made every corrected fact read the same in every chapter "
    "(`planning/coverage/consistency-sweep.md`).",
    "10. **Real readers' questions.** 528 questions that people actually ask online (help centers, forums, "
    "Hacker News, Stack Exchange, Quora) were checked against the book. It fully answered 421 before and 506 after; "
    "the rest are partly answered or depend on facts no primary source settles "
    "(`planning/coverage/questions-*.md`).",
    "11. **Every chapter read as a beginner.** Every chapter and appendix was read start to finish from the "
    "reader's point of view, fixing about 1,000 places where that reader would get lost, including defining every "
    "abbreviation and company name at first use, and testing the exercises (`planning/coverage/reader-test-*.md`, "
    "`earliest-use.md`, `code-tests.md`). Every term defined in more than one chapter was checked so the glossary "
    "never merges two different meanings (`definitions-*.md`).",
    "12. **Adversarial review.** Everything added in steps 8 to 11 was reviewed twice more, once for facts and "
    "arithmetic and once for clarity and integrity, by reviewers told to assume each passage was wrong until "
    "checked: about 3,000 passages, about 260 problems fixed (`planning/coverage/adversarial-review.md`). A final "
    "completeness critic re-read every report and closed what was still open.",
    "",
    "Facts about fast-moving areas (models, chips, data centers, prices, law) reflect sources available on October 23, 2026 "
    "and will date. Figures from secondary sources are marked as reported; check the Going deeper lists for primary sources.",
    "",
    "## Rebuilding the web version",
    "",
    "```bash",
    "cd ai-book/build",
    "npm install                       # mermaid-cli, used to draw the diagrams",
    "python3 gen_extra_terms.py ../planning/research ..   # optional: research glossary terms (needs the research files)",
    "python3 check.py ..               # style checks for every chapter",
    "python3 build.py .. ../site       # writes site/index.html, p1.html ... p10.html, reference, glossary, exercises",
    "```",
    "",
    "Needs Python 3, pandoc and Node.js. Set `CHROME_PATH` if Puppeteer cannot find a Chromium to render diagrams with.",
    "",
]
(book / "README.md").write_text("\n".join(lines))
print("README written")
