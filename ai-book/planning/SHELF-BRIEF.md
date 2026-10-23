# Appendix F: The advanced shelf — writer brief

The book (/home/user/Leash-Holder-2/ai-book/) teaches AI from zero to the October 2026 frontier for a reader with
almost no computer-science background. Audits against 15 textbooks and syllabi set aside some topics as
"OUT OF SCOPE": graduate-level mathematics, research niches, obsolete methods and code-level details. The reader
asked to know everything, so every one of those topics now gets a short, honest, plain-English entry in a new
appendix, so that nothing in the standard curriculum is left unexplained.

Paths (S = /tmp/claude-0/-home-user-Leash-Holder-2/aef38a40-e2d5-5d7b-af1e-cec85a236b62/scratchpad):
- Style guide: S/STYLE.md (definition callout format is parsed by the build; follow it exactly)
- Audit reports: /home/user/Leash-Holder-2/ai-book/planning/coverage/external-*.md (rows with OUT OF SCOPE in
  the status column, and "OUT OF SCOPE detail" notes inside COVERED rows; also the "Verified online" sections)
- Existing appendices for tone and format: /home/user/Leash-Holder-2/ai-book/appendices/*.md
- Glossary (terms already defined): /home/user/Leash-Holder-2/ai-book/GLOSSARY.md
- Checker: python3 S/tools/validate.py FILE.md

## What to write
File: /home/user/Leash-Holder-2/ai-book/appendices/F-advanced-shelf.md

    # Appendix F: The Advanced Shelf

    *One-sentence promise.*

Then a short introduction (what this appendix is: the topics specialists study after this book, each explained
in plain words so you know what it is when you meet it; how to use it; that the entries are grouped by field).
Then one H2 section per field (for example: Search, logic and planning; Probability and decision theory;
Learning theory and statistics; Classic neural-network ideas; Optimization mathematics; Generative-model
mathematics; Vision and language specifics; Data and ML engineering details; Systems and hardware details;
Safety, policy and governance details), and in each section one H3 entry per topic (merge near-duplicates):

    ### Topic name

    Two to six sentences: what it is in everyday words, a tiny concrete example or analogy, why specialists
    care, and where it connects to the book ("Chapter 9 explains the bias-variance idea this formalizes").

    > **Definition — Term:** One to three sentences, self-contained.

Every distinct term named in an entry gets a definition callout unless GLOSSARY.md already defines it (then
point to that chapter instead). Use stable textbook knowledge only; no 2025-2026 claims. No formulas the reader
cannot read: if a formula helps, say what each symbol means. Keep each entry short; aim for clarity over depth.

Include at least two diagrams for the appendix (mermaid per STYLE.md rules, captioned "*Figure F.1: ...*"),
for example a map of how the advanced topics hang off the book's parts. End with a "## Where to go next"
section pointing to the standards themselves (book and course names; no URLs needed).

## Wire it in
1. Add to /home/user/Leash-Holder-2/ai-book/outline.json under "appendices", after E:
   {"letter": "F", "title": "The Advanced Shelf", "file": "F-advanced-shelf.md"} (copy the exact key names the
   other appendix entries use; add any other keys they have).
2. In each external-*.md report, add one line under its summary: "All OUT OF SCOPE topics are explained in
   plain words in Appendix F (The Advanced Shelf)."

## Finish
Run validate.py on the new file. Count the entries and definitions. Reply in at most 6 lines: number of
OUT OF SCOPE topics found, entries written, definitions added, anything you could not place.
