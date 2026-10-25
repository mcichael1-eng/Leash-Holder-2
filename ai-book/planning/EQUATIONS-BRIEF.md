# Appendix G, "The Equations of AI" — brief

The reader of "The AI Field Guide" (/home/user/Leash-Holder-2/ai-book) asked: "is every single math equation that is
currently used to make AI included?" The book already has the core formulas (Appendix B, the Math Cheat Sheet,
collects the ones it uses), but many equations are explained only in words and some are missing. The target is
finite and checkable: EVERY equation that is standard in the field's textbooks and courses (AIMA, Goodfellow,
d2l, Bishop/Murphy, Sutton & Barto, CS229/231n/224n/336, Huyen, How to Scale Your Model, Datacenter as a Computer,
Hennessy & Patterson) and EVERY equation in active use at frontier labs as of October 2026 (from their papers,
model cards, docs). Variants that differ only trivially are merged into one entry with a note.

Paths (S = /tmp/claude-0/-home-user-Leash-Holder-2/aef38a40-e2d5-5d7b-af1e-cec85a236b62/scratchpad):
- Style guide: S/STYLE.md (definition callout format is parsed by the build; follow it exactly; no emojis)
- Appendix B (notation to copy exactly): /home/user/Leash-Holder-2/ai-book/appendices/B-math-cheat-sheet.md
- Outline (which chapter owns which topic): S/OUTLINE.md
- Checkers: python3 S/tools/validate.py FILE.md ; python3 S/tools/check.py /home/user/Leash-Holder-2/ai-book N

## Notation (the book renders no LaTeX)
Formulas go in backtick code spans in the plain notation Appendix B uses: `×`, `÷`, `^`, `sqrt()`, `exp()`,
`ln()`, `log2()`, `sum over i of (...)` or `sum(...)`, subscripts with underscore (`x_i`, `W_q`), Greek letters
spelled or as Unicode (η, β, γ, λ, σ, θ, ε are fine but each one is explained), `E[...]` for expected value,
`max`, `min`, `argmax`, `P(a | b)` may be written `P(a given b)`. Matrix shapes as `m × n`. Never use LaTeX.

## Entry format (one H3 per equation)

    ### Name of the equation (common short name)

    **What it does:** one sentence.

    `the formula`

    - **symbol**: what it means (every symbol, every time)

    **In plain words:** two to four sentences a beginner can follow.

    **Tiny example:** small numbers worked step by step, every step shown (recompute with Python to be sure).

    **Where it is used:** which systems use it and how, including 2025-2026 practice where relevant (sourced facts only).
    **In the book:** Chapter N (section name), or "Only here" if no chapter shows it.

Terms that have no definition in the book (check /home/user/Leash-Holder-2/ai-book/GLOSSARY.md) get a definition callout
`> **Definition — Term:** ...` right after the entry. Each category section also gets at least one mermaid diagram
(rules in STYLE.md: quoted labels, no styles, max ~15 nodes) showing how its equations connect, captioned
`*Figure G.X: ...*` (literal X; numbers are assigned at assembly).
