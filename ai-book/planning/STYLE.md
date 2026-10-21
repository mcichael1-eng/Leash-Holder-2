# Style guide for writers of "The AI Field Guide"

## The reader
- Has almost zero computer-science knowledge. Has used ChatGPT/Claude/Gemini daily for over a year, so they know what a chatbot *feels* like but not how anything works underneath.
- Smart, curious, wants the real thing, not a dumbed-down version. Start every idea at the simplest level, then build up to how the most advanced labs (OpenAI, Anthropic, Google DeepMind, Meta, xAI, DeepSeek, etc.) do it today.
- Today's date is **October 2026**. Where facts are time-sensitive, say "as of late 2026" and prefer facts from the research files. Do not invent numbers, model names, dates or quotes. If unsure, say so plainly or leave it out.

## Voice
- Plain, warm, direct English. Short sentences. Second person ("you") is fine.
- Explain *why* things are the way they are, not just *what*.
- Use concrete examples from the reader's daily chatbot use wherever possible ("When you paste a long PDF into Claude...").
- No hype, no doom. Present debates fairly.
- Avoid filler phrases ("It's worth noting", "In today's fast-paced world", "delve", "Let's dive in").
- Do not use emoji anywhere.

## Every term gets an explicit definition
The first time a chapter uses a technical term (any word a non-CS person might not know: algorithm, parameter, GPU, token, latency, API, etc.), define it with a **definition callout** right after the paragraph that introduces it. Exact format — one line, one paragraph, no line breaks inside:

```
> **Definition — Token:** A small chunk of text (often a word or part of a word) that a language model reads and writes. "unbelievable" might be split into "un", "believ", "able".
```

Rules:
- The label must be exactly `**Definition — <Term>:**` (bold, the word Definition, a space, an em dash —, a space, the term, a colon, closing bold). The build script parses this to make the glossary, so follow it exactly.
- Put the abbreviation and full name together when relevant: `**Definition — GPU (Graphics Processing Unit):**`.
- Definitions are 1–3 sentences, plain English, self-contained (understandable without reading the chapter).
- Aim for **25–60 definitions per chapter**. Too many is better than too few. If a term was defined in an earlier chapter, you may re-define it briefly if it is central to your chapter; otherwise mention it in plain words and reference the chapter where it is defined ("(see Chapter 7)").

## Other callouts (same blockquote format, one paragraph each)
- `> **Key idea:** ...` — the one thing to remember from a section.
- `> **Analogy:** ...` — an everyday comparison.
- `> **Try it:** ...` — a quick 1–5 minute thing to do right now in a chatbot or browser.
- `> **At the frontier (2026):** ...` — what the most advanced companies are doing right now on this topic.
- `> **Watch out:** ...` — a common misconception or trap, corrected.

Use the exact bold labels above. Each callout is a single blockquote paragraph (no multi-paragraph blockquotes).

## Diagrams (required)
Each chapter needs **at least 4 diagrams**, of these kinds:
1. **Mermaid diagrams** in fenced code blocks marked `mermaid`. Allowed types: `flowchart` (LR or TD), `sequenceDiagram`, `pie`, `mindmap`, `timeline`, `quadrantChart`, `stateDiagram-v2`. Rules to keep them valid:
   - Always quote node labels: `A["Your phone"] --> B["Data center (Texas)"]`.
   - Use `<br/>` for line breaks inside labels. No markdown inside labels. Avoid the characters `"`, `#`, `;`, `{}`, and backticks inside labels.
   - Do NOT add `style`, `classDef`, `linkStyle`, `%%{init}%%` or any colors — the reader's theme handles colors.
   - Keep each diagram to at most ~15 nodes. Several small diagrams beat one giant one.
   - Every diagram needs a one-line italic caption right after it: `*Figure 3.2: How a request travels from your phone to the model and back.*` Number figures as `<chapter>.<n>`.
2. **ASCII diagrams** inside plain ``` fenced blocks (no language tag) are fine for things mermaid can't draw (a grid of pixels, a matrix, a rack layout, a number line). Keep them under 70 characters wide. Caption them too.
3. **Tables** for comparisons (markdown pipe tables).

## Chapter structure (use exactly these H2 headings, in this order, around your own content sections)
```
# Chapter N: Title

*One-sentence promise of what this chapter gives the reader.*

## What you'll learn
- 4–8 bullets

## Before you start
One short paragraph naming which earlier chapters help (by number and title). Chapter 1 says "Nothing. Start here."

## <Your content sections — as many H2/H3 sections as needed>
...

## In plain English
A 150–300 word recap of the whole chapter as if explaining to a friend.

## Key terms
A comma-separated list of every term defined in this chapter.

## Exercises
Numbered exercises, 6–12 per chapter, graded with a level tag at the start:
1. **[Easy] Title.** What to do, step by step (numbered sub-steps if needed), and **What you'll learn:** one sentence.
2. **[Medium] Title.** ...
3. **[Challenge] Title.** ...
Exercises must be doable by a non-programmer: chatbots, free websites, spreadsheets, pencil and paper, or Google Colab with code they can copy-paste (if you give code, give the complete code and explain what each part does in plain words). Include URLs only for well-known, stable sites.

## Areas of opportunity
Concrete careers, business ideas, skills in demand, and open problems tied to this chapter's topic. 5–12 bullets, each 1–3 sentences, specific (who would pay for it and why).

## Check your understanding
5–8 questions. Put answers inside one HTML details block:
<details><summary>Answers</summary>

1. ...
2. ...

</details>

## Going deeper
5–10 high-quality resources (books, courses, papers, videos, sites) with one line each on why. Prefer stable, well-known resources.
```

## Length and depth
- Target **6,000–9,000 words per chapter** (not counting exercises/answers). These chapters are the whole education for this reader: be thorough. Cover every subtopic in your brief.
- Build up within each chapter: simplest version first, then the real version, then what the frontier looks like.
- Use worked examples with real numbers wherever possible (e.g., actually compute a tiny dot product, actually estimate the electricity of a 100 MW site for a year).
- Cross-reference other chapters as "(see Chapter 12)" — plain text, the build script links them. Only reference chapter numbers from the outline.

## Markdown rules
- One `#` H1 per file (the chapter title). Use `##` and `###` below it. No `####` deeper than needed.
- Math: write it in plain text or code (`y = w * x + b`, `6 × N × D`), not LaTeX. Use × for multiplication in prose. Superscripts as 10^25 in code spans, or written out ("ten to the 25th").
- Code blocks with a language tag (```python) for code. Keep code short and fully commented.
- Do not use HTML except the `<details>`/`<summary>` answers block.
- Do not use emoji.
- Files are UTF-8.
