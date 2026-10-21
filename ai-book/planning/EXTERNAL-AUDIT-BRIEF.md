# External-standard coverage audit — The AI Field Guide

The book (66 chapters in /home/user/Leash-Holder-2/ai-book/chapters/, appendices in .../ai-book/appendices/)
aims to teach everything about AI to a reader with no computer-science background, from the basics to the
October 2026 frontier. An earlier audit checked it against our own research maps. Your audit checks it against
EXTERNAL standards: the tables of contents of canonical textbooks and course syllabi in your area.

Paths (S = /tmp/claude-0/-home-user-Leash-Holder-2/aef38a40-e2d5-5d7b-af1e-cec85a236b62/scratchpad):
- Style guide (formats are parsed by the build; follow exactly): S/STYLE.md
- Outline (which chapter owns which topic): S/OUTLINE.md
- Research files (sourced facts): S/research/*.md
- Checkers: python3 S/tools/validate.py FILE.md ; python3 S/tools/check.py /home/user/Leash-Holder-2/ai-book N

## Steps
1. Read S/STYLE.md and S/OUTLINE.md.
2. For each standard assigned to you, write down its chapter and section topics as you know them (from your own
   knowledge; web search is unavailable). Where you are unsure of the exact structure, list the topics the
   standard is known to cover and say so in the report. Do not invent section titles.
3. For each topic, find where the book teaches it (grep the chapters for key terms, then read the passage) and
   classify it: COVERED (explained at beginner level), THIN (mentioned but not explained), MISSING, or
   OUT OF SCOPE (a topic so specialized or mathematical that a book for this reader should only point to it; say
   why, and make sure the book at least names it with a one-line explanation if it is a field the reader will
   hear about).
4. For each THIN or MISSING topic that belongs in this book, add a beginner-level explanation (usually 100–400
   words) in the chapter that owns the topic per OUTLINE.md, at the point where it fits the flow, with a
   definition callout in the exact STYLE.md format for every new term and a small worked example where numbers
   help. Stable textbook knowledge may come from your own expertise; anything about 2025–2026 must come from the
   research files or be left out. Use the Edit tool for small targeted insertions (other auditors may be editing
   other parts of the same chapters); re-read the passage right before editing.
5. Run validate.py on every edited file and check.py on every edited chapter; both must be clean.
6. Write /home/user/Leash-Holder-2/ai-book/planning/coverage/external-<your-area>.md: for each standard, a table
   Topic | Status before | Where in the book | Action; then a summary with the counts and the share of topics
   covered after your edits.
7. Reply with at most 8 lines: per standard, the counts before and after, what you added where, and anything
   you judged out of scope.
