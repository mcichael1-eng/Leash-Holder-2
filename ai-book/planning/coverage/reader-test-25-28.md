# Reader test: chapters 25 to 28

Tested by reading chapters 25 (Mastering the Chat Interface), 26 (APIs), 27 (Retrieval) and 28 (Tools and Agents) in order, in full, as the intended reader: almost no computer-science background, a daily chatbot user for a year, who has read chapters 1 to 24. Before treating a term as undefined I checked GLOSSARY.md for an earlier definition; a term defined in an earlier chapter was not counted as a problem. I worked through every entry for these chapters in acronyms-by-chapter.json. I re-ran the arithmetic in every worked example and every Check-your-understanding answer, and ran the chunking cells of the Chapter 27 Colab project to confirm the claim made about them. Edits are small: definition callouts, glosses, bridging sentences and clearer exercise steps. Nothing was cut or restructured.

After editing, all four files passed `validate.py` (6/6, 8/8, 8/8 and 9/9 diagrams valid) and `check.py` (ch25 to ch28 all `[OK]`).

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 25 | "Tokens: what the model reads", essay example | "2,000 × 1.8" and "2,000 × 1.33" appear with no link to the 555,000 and 750,000 words-per-million figures just given | Added the step: 1,000,000 ÷ 555,000 ≈ 1.8 and 1,000,000 ÷ 750,000 ≈ 1.33 tokens per word |
| 25 | Technique 7, frontier box | "Deprecated" used as if known (the glossary entry comes from Chapter 26) | Glossed as "officially on its way out" |
| 25 | Technique 10, Prefill definition | The chapter already used "prefill step" (Chapter 23's meaning: reading the prompt) 300 lines earlier; this definition gave the same word a different meaning, and the generated glossary merged both under one entry | Renamed the term "Prefilling the response", added "often just called prefill (not to be confused with Chapter 23's prefill step)", updated Key terms |
| 25 | Connectors, MCP definition | "Linux Foundation" never explained anywhere in the book, though it appears in six chapters and two appendices | New definition callout: Linux Foundation (added to Key terms) |
| 25 | Projects | "CV" (acronym list) | Glossed as "CV or résumé" |
| 25 | Exercise 3, step 4 | "Recompute the total" after compaction gave no method; a beginner would not know what each later turn reads | Spelled out that later turns read the 1,000-token summary plus 600 per new exchange (1,600, 2,200, ...) and to add all 30 turns |
| 25 | Exercise 8 | "DOIs" (acronym list) | Glossed as digital object identifiers, the permanent ID code on journal articles |
| 25 | Areas of opportunity | "HR" (acronym list) | Glossed as human resources |
| 25 | Going deeper | "DAIR.AI" (acronym list) unexplained; the acronym list also conflates it with Timnit Gebru's DAIR institute in Chapter 63 and Appendix D | Glossed DAIR.AI as an independent AI-education group and distinguished it from the DAIR institute (Chapter 63) |
| 26 | The web request | "Bearer" in the authorization header is unexplained | Glossed as the standard label meaning "whoever holds this key may use it" |
| 26 | Figure 26.4 | "5xx" in the diagram while the table says "500-599" | Caption now says 5xx is shorthand for any code from 500 to 599 |
| 26 | Prompt caching code | `"ephemeral"` appears in the code with no explanation | Added that it is Anthropic's name for the standard five-minute cache |
| 26 | Multimodal input | "JPG or PNG" (acronym list) | Glossed as the two most common image file formats (Chapter 3) |
| 26 | Model tier table | "Q&A" (acronym list) | Glossed as question answering |
| 26 | Exercise 2 | After typing the formula in F2, the exercise never says to copy it to the other rows, so only one row would get a cost; G had no cell | Added rows 2 to 5, how to copy F2 down, and where G2 goes |
| 26 | Areas of opportunity | "LLMOps" and "golden test sets" are first defined in Chapter 31 | Short glosses with a pointer to Chapter 31 |
| 27 | Map of meaning | Distances computed with "the square root of (9 − 8)² + ..." with no word on where the formula comes from | Named the straight-line (Euclidean) distance from Chapter 5 and described the steps |
| 27 | Keyword search | "Ctrl+F" assumed | Glossed as the find-in-page shortcut (Cmd+F on a Mac) |
| 27 | IDF worked example | log(20) = 1.3 and log(500) = 2.7 with no reminder of what a log is or how to get one | One-sentence reminder (Chapter 6) plus the calculator key and `=LOG10(20)` |
| 27 | Vector database table | "Postgres" unexplained | Glossed as PostgreSQL, a popular free, open-source database |
| 27 | Metadata filtering | "HR" (acronym list, first use in this chapter) | Glossed as human resources |
| 27 | Reranking analogy | "CVs" (acronym list) | Glossed as résumés |
| 27 | Knowledge graph definition | "Wikidata" unexplained | Glossed as a free database of facts run by the same foundation as Wikipedia |
| 27 | Multimodal RAG | "Exploded diagram" unexplained | Glossed as a drawing that shows a machine's parts pulled apart |
| 27 | Retrieval is an attack surface | "OWASP" first defined in Chapter 31 | Glossed as a nonprofit security community, with a pointer |
| 27 | Exercise 2 | Did not say which columns the passage vectors go in, or where labels go | Columns B to D, labels in A2 to A5 |
| 27 | Exercise 5, step 3 | "Which document that appeared in only one list ends up highest?" has two answers: Manual-3 and Forum-4 tie at 1/63 | Question now asks for the documents and says two of them tie, asking why |
| 27 | Going deeper | "TF-IDF" (acronym list entry TF) | Glossed as term frequency times IDF, a simpler ancestor of BM25 (Chapter 11) |
| 28 | Planning, history paragraph | "LangChain" named with no explanation; it is first described, barely, in a table 400 lines later | Glossed as the company behind the open-source toolkit of the same name |
| 28 | 30-step agent cost, caching line | "Roughly 955,000 of those tokens are cache reads and 65,000 are new" with no derivation | Added: each step writes only its own new tokens (5,000 + 2,000 × 30 ≈ 65,000); the rest of the 1,020,000 are reads |
| 28 | Believable agents | The 2023 Generative Agents study (25 agents, The Sims town, Valentine's party) is told twice, about 70 lines apart, with no acknowledgment; a reader thinks they have lost their place | Second telling now opens by pointing back to the memory section and saying it is the same study from another angle |
| 28 | Reliability compounds | "0.99^10" notation with no explanation of ^ or how to compute it | Explained ^ and gave `=0.99^10` for a spreadsheet |
| 28 | Where agents pay off | "Annual recurring revenue" first defined in Chapter 61 | Glossed as the yearly value of ongoing contracts |
| 28 | Same section | "MIT NANDA" (acronym list: five chapters, first use here) never defined | New definition callout: MIT NANDA (added to Key terms) |
| 28 | MCP analogy | "USB" (acronym list) | Expanded Universal Serial Bus and said what USB-C is |
| 28 | MCP host definition | "IDE" first defined in Chapter 29 | Glossed inside the definition |
| 28 | JSON-RPC definition | "RPC" (acronym list) never expanded | Added "remote procedure call" and what it means |
| 28 | MCP security history | "CVE-2025-6514" before CVE is defined (Chapter 31); "NSA" used later in the chapter but never linked to the National Security Agency | Glossed CVE with a pointer; added "(NSA)" after the agency's name |
| 28 | Who governs the standards | "Block" unexplained | Glossed as the payments company behind Square and Cash App |
| 28 | 2026 specification table | "Handshake" unexplained | Glossed as a greeting exchange in which both sides agree on settings |
| 28 | Browser agents | "CAPTCHAs" (acronym list) | Glossed as "prove you are human" puzzles |
| 28 | Exercise 2 | "YYYY-MM-DD" (acronym list) | Explained with an example date |
| 28 | Exercise 5, Option B | Node.js and the `npx` command in the config appear with no explanation | One sentence on what Node.js is and what npx does |
| 28 | Exercise 6 | "In each cell compute ..., for example `=$A2^B$1`" did not say which cells, where to start or what the $ signs do | Exact cells (A2 to A6, B1 to G1), start in B2, copy to B2:G6, and what the $ signs do |
| 28 | Exercise 9 | "Plan mode" first defined in Chapter 29 | Glossed with a pointer |
| 28 | Areas of opportunity | "CRMs" (acronym list) | Glossed as customer relationship management systems |

Acronym-list entries left without change because they are not acronyms in context: NO, ALL, CAPS, NEVER (shouted prompt words), BANANA (a word in a prompt-injection exercise), ZX ("ZX-4471B" is a part number), NW ("NW-12345" is an order-number format), CLAUDE (CLAUDE.md, defined), and DOM, ADK, AP2, POST, GET, which are already expanded or defined where they appear. MCPA is introduced as "a certification (MCPA) for MCP expertise", which is enough of a gloss; its expansion is not in the research files.

## Verdict per chapter

**Chapter 25.** The ramp works very well. It starts from what the reader already knows (the chat box), builds the three facts that explain everything (tokens, the context window, statelessness) with a clean worked example, and only then teaches techniques, each with a before-and-after. The move to context engineering at the end feels earned. Almost every term was already defined; the real problems were one skipped arithmetic step, a word ("prefill") used in two meanings in the same chapter, which the glossary had silently merged, an undefined organization that recurs across the book (the Linux Foundation), and a compaction exercise a beginner could not finish without being told what each later turn reads. All fixed.

**Chapter 26.** The strongest beginner chapter of the four: it recaps HTTP, JSON and Python before using them, reads a request line by line, and every cost calculation is shown in full (I re-checked all of them, including the router cascade and the caching table; all correct). The gaps were small: a few bits of literal code or notation shown without a word on what they mean (Bearer, 5xx, ephemeral), terms borrowed from Chapter 31 in the opportunities list, and a spreadsheet exercise that forgot to say "copy the formula down". Every term is now defined or glossed at first use.

**Chapter 27.** The ramp is good: a hand-drawn two-dimensional map, then cosine similarity computed by hand (correct to three places), then BM25, RRF (table re-checked, correct), vector indexes, the two pipelines, and the advanced techniques. The jumps were in the math: a distance formula and base-10 logarithms used without saying where they come from, both now tied back to Chapters 5 and 6. Several names (Postgres, Wikidata, OWASP) needed a gloss. One exercise had two correct answers because of a tie nobody mentioned. I ran the Colab chunking cells: they produce 12 chunks and the "half plot for a student" answer does need two chunks, as the text says.

**Chapter 28.** The densest chapter, with the most names (products, frameworks, protocols, organizations), and that is where nearly all the problems were: about a dozen names or acronyms were used before any definition, several defined only in Chapters 29, 31 or 61, and MIT NANDA was never defined anywhere in the book. The conceptual ramp itself (model only asks, tool definition, round trip, loop, workflows versus agents, memory, cost, reliability, MCP, other standards, security) is sound, and the worked numbers (tool-call cost, 30-step agent, METR doubling, compounding reliability) all check out. The one structural oddity is the Generative Agents study told twice; I added a back-reference rather than cut either telling.

## Flagged, not changed (sourced facts or outside these chapters)

- Tokenizer ratio: Chapters 25 and 26 quote Anthropic as saying the newer tokenizer gives "about 30% more tokens", but the figures given alongside (555,000 versus 750,000 words per million tokens) imply about 35%, and Chapter 27 says "up to about 35%". Worth a fact-checker's look so the three chapters agree.
- MIT NANDA report date: July 2025 in Chapters 28, 61, 63 and 64; August 2025 in Chapter 31 (898). The new Chapter 28 definition says only "2025".
- Glossary duplicates: "Sub-agent" (Chapter 25) and "Subagent" (Chapter 28) generate two entries for the same idea; Chapter 28 also uses both spellings.
- The acronym list counts DAIR as one organization in four chapters, but Chapter 25 and Appendix E mean DAIR.AI (prompt-guide publisher) while Chapter 63 and Appendix D mean the DAIR research institute. Neither reaches three chapters on its own, so DAIR.AI got a gloss, not a callout.
- GLOSSARY.md is generated by the build; it will pick up the two new callouts (Linux Foundation, MIT NANDA) and the renamed "Prefilling the response" on the next build, which will also drop the misleading Chapter 25 reference from the "Prefill" entry.
