# Coverage audit brief — The AI Field Guide

The book aims to teach "every single thing" about AI to a reader with no computer-science background. It is
written (66 chapters in /home/user/Leash-Holder-2/ai-book/chapters/, appendices in .../ai-book/appendices/).
Your job: prove, topic by topic, that the book covers everything the research mapped, and fill real gaps.

Paths (S = /tmp/claude-0/-home-user-Leash-Holder-2/aef38a40-e2d5-5d7b-af1e-cec85a236b62/scratchpad):
- Style guide (formats are parsed by the build; follow exactly): S/STYLE.md
- Outline (which chapter owns which topic): S/OUTLINE.md
- Research files: S/research/NN-*.md (section 1 = topic map with numbered items)
- Checkers: python3 S/tools/validate.py FILE.md ; python3 S/tools/check.py /home/user/Leash-Holder-2/ai-book N

## Steps
1. Read S/STYLE.md and S/OUTLINE.md.
2. For each research file assigned to you, go through EVERY item (and named sub-item) in section 1, the topic map.
   For each one, find where the book teaches it: use grep on the chapters for its key terms, then read the passage.
   Classify it:
   - COVERED: explained (not just mentioned) somewhere, at beginner level.
   - THIN: only mentioned, or explained in a way a beginner could not follow.
   - MISSING: not in the book.
3. For each THIN or MISSING item, add the explanation to the chapter that owns the topic per OUTLINE.md: usually a
   paragraph or short subsection (100–400 words) in plain English, with a definition callout in the exact STYLE.md
   format for any new term, and a worked example if numbers are involved. Use facts from the research file only;
   hedge anything the research marks [verify], [S] or unconfirmed. Insert it where it fits the chapter's flow (not
   at the end), and keep chapter structure, callout formats and figure numbering intact.
4. Run validate.py on every edited file and check.py on every edited chapter; both must be clean.
5. Write a coverage report to /home/user/Leash-Holder-2/ai-book/planning/coverage/<research-file-stem>.md:
   a markdown table with columns Item | Status before | Where covered (chapter and section) | Action taken,
   one row per topic-map item, followed by a one-paragraph summary.
6. Reply with at most 8 lines: counts of COVERED / THIN / MISSING before your edits, what you added where,
   and anything you could not resolve.

Other auditors are working on other research files at the same time and may edit the same chapters. Make small,
targeted edits with the Edit tool (never rewrite a whole chapter file), and re-read the passage right before
editing it.
