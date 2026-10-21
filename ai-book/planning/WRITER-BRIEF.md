# Writer brief — The AI Field Guide

You are one of about 36 writers producing a complete book that teaches AI from zero to the 2026 frontier.
The reader has almost no computer-science knowledge but has used ChatGPT/Claude/Gemini daily for over a year.
Today is October 21, 2026.

Paths (S = /tmp/claude-0/-home-user-Leash-Holder-2/aef38a40-e2d5-5d7b-af1e-cec85a236b62/scratchpad):
- Style guide (MUST follow exactly): S/STYLE.md
- Master outline with every chapter's brief: S/OUTLINE.md
- Research files: S/research/01-foundations.md ... 10-skills-careers-opportunity.md
- Output folder: /home/user/Leash-Holder-2/ai-book/chapters/ (appendices: /home/user/Leash-Holder-2/ai-book/appendices/)
- Checkers: S/tools/validate.py and S/tools/check.py

## Steps
1. Read S/STYLE.md completely. Its formats (definition callouts, other callouts, mermaid rules, required H2 sections,
   exercise tags, answers in <details>) are parsed by the build script, so follow them exactly.
2. Read S/OUTLINE.md completely, so you know what every other chapter covers. Stay inside your brief: give
   neighbouring topics a short recap or a pointer ("see Chapter 23") instead of re-teaching them.
3. Read the research files named in your briefs IN FULL (all nine sections: topic map, glossary, prerequisites,
   current facts, diagram ideas, exercises, opportunities, misconceptions, analogies). They are your source of
   facts, terms, diagram ideas, exercises and analogies. Use their glossary to make sure every term you use is defined.
4. Write each chapter to its exact file name with the Write tool. Target 6,000–9,000 words of body text before the
   Exercises section, 25–60 definitions, at least 4 diagrams (mostly mermaid), 6–12 exercises, worked numeric
   examples, and plenty of Key idea / Analogy / Try it / At the frontier (2026) / Watch out callouts.
   If a chapter is too long for one Write call, write the first half with Write and append the rest with
   Bash: cat >> FILE <<'CHAPTER_EOF' ... CHAPTER_EOF
5. Validate, then fix and re-run until both are clean:
   - python3 S/tools/validate.py /home/user/Leash-Holder-2/ai-book/chapters/YOURFILE.md   (all diagrams must be valid)
   - python3 S/tools/check.py /home/user/Leash-Holder-2/ai-book N   (N = your chapter number; must print [OK ])
   Mermaid tips: always quote labels A["..."]; never use reserved words (end, graph, subgraph, class, style, click)
   as node IDs; no parentheses, quotes or semicolons in unquoted text; in sequenceDiagram keep participant
   aliases simple (participant P as Phone).
6. Reply with at most 8 lines: the files written, word count, number of definitions, diagrams and exercises
   (from check.py), and any facts you hedged or left out because the research flagged them as unverified.

## Facts and honesty rules
- Use facts from the research files. Never invent numbers, dates, names, quotes, prices, benchmark scores or
  product details. If you do not have a solid fact, explain the concept without the number.
- Items the research marks [verify], [S], "secondary", "unconfirmed", "reported" or "single-source" must be hedged
  ("reportedly", "according to company figures", "as of October 2026") or left out. Surprising corporate claims
  from a single secondary source should be left out.
- Time-sensitive statements carry "as of late 2026" or a date.
- Web search is not available (the shared budget is used up). Do not try to search. Work from the research files
  and your own solid background knowledge for stable, well-established facts (history, math, physics, how
  algorithms work).
- Present debates with the strongest version of each side.

## Quality bar
- Start each idea at the simplest level a smart 12-year-old could follow, then build to the real version,
  then to what the most advanced labs do in 2026.
- Every chapter should leave the reader able to explain the topic to a friend, do the exercises, and see where the
  opportunities are.
- Concrete beats abstract: worked examples with real numbers, the reader's own chatbot as the running example,
  diagrams for every process with more than three steps.
- No emoji, no hype, no filler.
