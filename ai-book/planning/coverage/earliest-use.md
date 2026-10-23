# Earliest-use audit: is every term defined where a reader first meets it?

Date: October 23, 2026. Scope: all 66 chapters (outline.json order), then appendices A to F.

## Method

Script: `S/tools/earliest_use.py <book_dir> <out.json>` (S = the shared scratchpad). For every definition-callout label it:

- takes the main form (label without parentheses) and splits list labels ("CUDA, Triton and kernels", "MQA and GQA") into their parts;
- records the earliest file that defines the term. The main form, the words in parentheses and the list parts all count, so "GPU (Graphics Processing Unit)" also defines "Graphics Processing Unit";
- finds the earliest file whose prose uses the term. Prose means text outside fenced code (including indented fences), inline code, headings, URLs and Going deeper sections;
- matches on word boundaries and allows plurals and possessives. Matching is case-sensitive for acronyms and for proper names (capitalized forms the book almost never writes in lower case) and case-insensitive otherwise;
- flags every term first used at least one file before its first definition, with the context of that first use.

Every flagged term was then triaged by hand at its first use. Acronyms were also checked with `S/tools/acronyms.py`.

## Counts

| Measure | Count |
|---|---|
| Definition callouts in the book (before / after) | 4,578 / 4,579 |
| Distinct main forms searched | 3,400 |
| Terms used at least one file before their first definition | 902 |
| ...used 1 file early / 2 / 3 / 4 / 5 or more | 410 / 193 / 88 / 42 / 169 |
| Excluded automatically as everyday words used in their everyday sense (Frontier, Standard, Task, Row, Bill, Load, Data, Model...) | 181 |
| Reviewed by hand at first use (acronyms, organizations, products, technical terms) | 721 |
| ...judged fine as written | 647 |
| ...of those 647, ones whose first-use context named the defining chapter (automatic pointer match) | 120 |
| ...fixed in this round | 74 terms (73 glosses, 1 new definition callout) in 28 chapters |
| Acronyms with no glossary entry used in 3+ files (acronyms.py) | 20, all already defined or glossed at first use; no edit needed |

The script still reports 901 terms after the edits. That is expected: it measures where a term is used, not whether the use is glossed. The fixes below add glosses at those first uses. "Prompt" left the list because Chapter 1 now defines it.

## Changes

Each gloss is short and plain and sits at the term's first use in the book. Where useful it ends with a pointer to the chapter that defines the term properly. Wording follows the book's own later definition of the term.

| Term | First use | First definition | Change |
|---|---|---|---|
| Prompt | Ch 1 (used in 17 chapters before Ch 25) | Ch 25 | New definition callout after the NLP callout; added to Ch 1 Key terms |
| Sentiment analysis | Ch 1 | Ch 54 | Gloss |
| Mathematical function | Ch 1 (Key idea) | Ch 5 | Gloss + pointer |
| NVIDIA | Ch 1 (AI stack table) | Ch 3 | Gloss "the leading AI-chip designer" |
| Accelerator | Ch 1 (Chip definition) | Ch 2 | Gloss |
| CNN | Ch 1 (Parts table) | Ch 7 | Expansion + gloss |
| API | Ch 1 (reading path B) | Ch 4 | Gloss (pointer existed) |
| Fine-tuning | Ch 1 (reading path B) | Ch 8 | Gloss |
| Median | Ch 2 | Ch 6 | Gloss "(middle)" |
| AMD | Ch 2 | Ch 7 | Gloss "Intel or its rival AMD" |
| Google Colab, Notebook | Ch 2 (Exercise 7) | Ch 8, Ch 3 | Gloss + pointer |
| Python | Ch 2 (Exercise 8) | Ch 3 | Gloss + pointer |
| Matrix, matrix multiplication | Ch 2 (Exercise 8) | Ch 5 | Gloss + pointer |
| Logarithmic axis | Ch 2 (Exercise 10) | Ch 6 / Ch 39 | Gloss + pointer |
| PyTorch | Ch 2 (opportunities) | Ch 13 | Gloss + pointer |
| HVAC | Ch 2 (opportunities) | Ch 62 | Expansion |
| Pretrained model | Ch 3 | Ch 14 | Gloss |
| Substation | Ch 4 | Ch 38 | Gloss + pointer |
| Load balancing | Ch 4 | Ch 17 (different sense) | Gloss of the networking sense |
| Sparse (and compressed) attention | Ch 5 | Ch 15 | Gloss |
| Hidden layer | Ch 5 | Ch 12 | Gloss |
| Scaling law | Ch 5 (used in 5 chapters before Ch 19) | Ch 19 | Gloss + pointer |
| Semantic search | Ch 5 | Ch 14 | Gloss |
| Interpretability | Ch 5 | Ch 10 | Gloss |
| Loss spike | Ch 6 | Ch 13 | Gloss + pointer |
| EU AI Act | Ch 7 (used in 7 chapters before Ch 59) | Ch 59 | Gloss + pointer |
| Agentic AI Foundation | Ch 7 | Ch 28 | Gloss + pointer |
| Deep Research | Ch 7 | Ch 25 | Gloss + pointer |
| Total parameters | Ch 7 | Ch 17 | Gloss (mixture of experts) + pointer |
| Harness | Ch 7 | Ch 21 | Gloss + pointer |
| GWh | Ch 7 | Ch 39 | Expansion |
| International AI Safety Report | Ch 7 | Ch 59 | Gloss + pointer |
| Logarithmic scale | Ch 7 (exercise) | Ch 39 | Gloss + pointer to Ch 6 |
| Run-rate | Ch 7 (opportunities) | Ch 43 | Gloss + pointer |
| Post-training | Ch 8 (used in 5 chapters before Ch 20) | Ch 20 | Gloss + pointer |
| Decision tree | Ch 8 | Ch 10 | Gloss + pointer |
| Foundation model | Ch 8 | Ch 14 | Gloss + pointer |
| Phishing | Ch 9 (exercise) | Ch 53 | Gloss |
| Kaggle competition | Ch 10 | Ch 65 | Gloss + pointer |
| HTML | Ch 11 | Ch 29 | Gloss |
| Triton (and CUDA) | Ch 12 | Ch 13 | Gloss + pointer |
| MiniMax (company) | Ch 15 | none (App D only) | Gloss "a Shanghai AI company" |
| Multi-hop reasoning | Ch 15 | Ch 17 | Gloss (pointer existed) |
| Backend | Ch 15 | Ch 29 (different sense) | Rephrased: "a built-in option (a 'backend')" |
| Shared expert | Ch 15 | Ch 17 | Gloss + pointer |
| Throughput | Ch 17 | Ch 23 | Gloss + pointer |
| Model spec | Ch 18 | Ch 20 | Gloss + pointer |
| System card | Ch 18 | Ch 24 | Gloss + pointer |
| Reasoning effort | Ch 18 | Ch 21 | Gloss + pointer |
| Verifier | Ch 19 | Ch 21 | Gloss + pointer |
| Moral status | Ch 20 | Ch 60 | Gloss + pointer |
| Structured outputs | Ch 23 (engines table) | Ch 26 | Gloss + pointer |
| Tool definition | Ch 23 | Ch 28 | Gloss + pointer |
| FTC | Ch 31 | Ch 59 | Expansion + pointer |
| Pod | Ch 32 (TPU history) | Ch 34 | Gloss |
| Optical circuit switch | Ch 32 | Ch 34 | Gloss + pointer |
| Chiplet | Ch 33 | Ch 34 | Gloss + pointer |
| Interactivity | Ch 33 | Ch 37 | Gloss + pointer |
| Profiler | Ch 33 | Ch 37 | Gloss |
| Alternating current | Ch 34 | Ch 39 | Gloss + pointer |
| Solid-state transformer | Ch 34 | Ch 39 | Gloss + pointer |
| Straggler | Ch 34 | Ch 37 | Gloss |
| Process node | Ch 35 | Ch 36 | Gloss + pointer |
| Switchgear | Ch 38 (Gray space definition) | Ch 39 | Gloss |
| UPS | Ch 38 (Gray space definition) | Ch 39 | Expansion + gloss + pointer |
| OSINT | Ch 38 | Ch 42 | Expansion |
| EIA | Ch 39 (table caption) | Ch 41 | Expansion |
| PPA | Ch 39 | Ch 41 | Expansion + gloss + pointer |
| Demand response | Ch 39 | Ch 41 | Gloss + pointer |
| Long-lead item | Ch 39 (Switchgear definition) | Ch 42 | Gloss |
| Recognized revenue | Ch 43 | Ch 60 | Gloss |
| Adversarial example | Ch 44 | Ch 45 | Gloss |
| Preprint | Ch 52 | Ch 65 | Gloss |

## Acronyms used in 3 or more files with no glossary entry

acronyms.py lists 370 acronyms with no glossary or definition entry. Twenty of them appear in 3 or more files. Each was checked at its first use:

- **Defined by a callout:** UTF (UTF-8, Ch 3), SWE (SWE-bench, Ch 24), SNE (t-SNE and UMAP, Ch 10), BBB (Credit rating, Ch 43). The tool does not split "UTF-8", "SWE-bench" or "t-SNE", so it keeps listing them.
- **Glossed or expanded:** RISC (RISC-V, Ch 2), EO (Ch 38), BWRX (BWRX-300, Ch 38, with pointer), CS (Ch 3), HR (Ch 25), UAE (Ch 42), DAIR (DAIR.AI, Ch 25), USB (Ch 7), SUMPRODUCT (Ch 5), UX (Ch 31), README (Ch 3), NGO (Ch 3), GET (Ch 4), QA (Ch 3), ARPANET (Ch 4), CV (Ch 25).

No edits were needed for these.

## Left as is (judgment calls)

The 647 terms judged fine fall into the groups below.

- **Already glossed at first use, or pointed to their chapter with enough context.**
- **False or different-sense matches:** robot "arm" vs the company Arm, "Adam Kalai" vs the Adam optimizer, "golden retriever" vs Retriever, the roman numeral "II", "lossless", "Embedding Projector".

- **Everyday words that later chapters define in a narrow sense:** "frontier", "standard", "load", "current", "bill", "grid", "feed" and similar. Early chapters use them in their ordinary meaning.
- **Uses already explained in the same sentence or the next one:** for example "IT power (the power the computers themselves use)", "METR, an independent research group that tests AI agents", "MNIST, 70,000 small images of handwritten digits".
- **Well-known names left without a gloss:** IBM (Ch 2) and Ethernet (Ch 32).
- **Self-describing labels in opportunity bullets:** "No-code ML trainer", "AI literacy trainer", "Data center developer".
- **False matches:** in the first run, pip matched "pipes". The plural rule now adds "es" only after s, x, z, ch and sh, and indented code fences are now stripped before matching.

## Sources checked on the web

These checks cover the glosses that state facts:

- **Agentic AI Foundation:** Linux Foundation press release (Dec 9, 2025: MCP, goose, AGENTS.md). https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
- **International AI Safety Report:** the report's site says it is backed by "over 30 countries and international organisations", is led by Yoshua Bengio and that the 2026 edition was published on 3 February 2026. The Ch 7 gloss now says "countries and international organizations". https://internationalaisafetyreport.org/
- **Deep Research:** OpenAI's Deep Research System Card (Feb 25, 2025) calls it a capability that "conducts multi-step research on the internet" and writes comprehensive reports. The gloss uses only that. https://cdn.openai.com/deep-research-system-card.pdf (openai.com pages returned 403).
- **MiniMax:** the company site describes a general AI company founded in early 2022. Wikipedia places its headquarters in Shanghai, which matches Appendix D. https://www.minimax.io/ and https://en.wikipedia.org/wiki/MiniMax_(company)

The other glosses restate the book's own later definitions and add no new facts.

## Checks

- `validate.py` on all 28 edited chapters: 220/220 diagrams valid.
- `check.py` on chapters 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 17, 18, 19, 20, 23, 31, 32, 33, 34, 35, 38, 39, 43, 44 and 52: all OK.
