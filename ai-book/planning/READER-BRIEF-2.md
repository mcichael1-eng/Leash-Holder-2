# Full-book beginner read-through — The AI Field Guide

The book (66 chapters in /home/user/Leash-Holder-2/ai-book/chapters/, appendices in .../ai-book/appendices/)
promises to teach everything about AI to a reader with almost no computer-science background who has used
chatbots daily for a year, and to define every term explicitly. An earlier read-through covered only chapters
1, 2, 5, 12, 15, 18, 23, 33, 39 and 44 (see /home/user/Leash-Holder-2/ai-book/planning/coverage/reader-test.md
for the kind of problems it found and fixed). Your job is to do the same for the chapters assigned to you, in
full, start to finish.

Paths (S = /tmp/claude-0/-home-user-Leash-Holder-2/aef38a40-e2d5-5d7b-af1e-cec85a236b62/scratchpad):
- Style guide (formats are parsed by the build; follow exactly): S/STYLE.md
- Outline: S/OUTLINE.md
- Glossary of every term already defined, with the chapter that defines it: /home/user/Leash-Holder-2/ai-book/GLOSSARY.md
- Acronyms with no definition anywhere in the book, per chapter: S/acronyms-by-chapter.json
- Checkers: python3 S/tools/validate.py FILE.md ; python3 S/tools/check.py /home/user/Leash-Holder-2/ai-book N

## How to read
Read each assigned chapter in order, in full, as that reader: smart and curious, knows what a chatbot feels like,
knows nothing of programming, math beyond school arithmetic, hardware or the industry. They have read the
earlier chapters (so a term defined in an earlier chapter is fine, as long as the chapter points back when the
term is central). Check the glossary before treating a term as undefined.

## What to fix (small, surgical edits with the Edit tool; re-read the passage right before editing,
## because other agents are editing other chapters and late-arriving fact fixes may touch yours)
1. Undefined terms: a technical term, abbreviation or name used with no definition callout in this chapter or an
   earlier one and no plain gloss nearby. Add a definition callout in the exact STYLE.md format (and add it to
   the chapter's Key terms list), or a short plain-English gloss in the sentence for names of companies,
   organizations, products and laws. Work through every entry for your chapters in S/acronyms-by-chapter.json:
   an organization or product that appears in three or more chapters gets a definition callout in the first of
   your chapters that uses it (so it enters the glossary); any other entry gets at least a gloss at its first use
   in the chapter. Units (TFLOPS, PFLOPS, PB and similar) get a definition callout where first used.
2. Beginner jumps: a step of reasoning or arithmetic skipped, a formula used without saying what each symbol
   means, a diagram that uses words the text has not explained yet. Add one or two bridging sentences.
3. Exercises a beginner cannot do as written: missing steps, missing numbers, unclear instructions, answers that
   do not match the question. Fix them (and the answer).
4. Anything plainly wrong that you notice (arithmetic, contradictions with an earlier chapter, broken
   cross-references to the wrong chapter number). Do not change sourced facts about 2025–2026; flag them.

## What not to do
- Do not rewrite for style, restructure, rename headings or cut content.
- Do not change the formats of definitions, callouts, exercises, answers, figures or tables.
- No emojis. Do not run git. Do not publish.

## Finish
Run validate.py on every edited file and check.py on every edited chapter; both must be clean.
Write /home/user/Leash-Holder-2/ai-book/planning/coverage/reader-test-<your chapter range>.md with a table
Chapter | Where | Problem a beginner would hit | Fix applied, and a one-paragraph verdict per chapter (does the
difficulty ramp work; is every term defined). Reply in at most 8 lines: counts of fixes by type per chapter,
and anything you could not resolve.
