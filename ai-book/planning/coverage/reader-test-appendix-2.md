# Reader test: Appendices D and E

I read Appendix D (Who's Who) and Appendix E (Resources) in full as the intended reader. That reader has no computer-science background, has used a chatbot daily and has read the 66 chapters. So a term defined in a chapter counts as defined, as long as the appendix row points to that chapter or the term is recognizable. GLOSSARY.md was checked before treating any term as undefined.

An earlier attempt at this task was cut off before it wrote a report. When this pass started, every acronym listed for these appendices in acronyms-by-chapter.json was already glossed at first use, so that work had been done by the earlier attempt or an earlier pass:
- App D: RISC-V, UAE, DAIR, BMW, MSL, TBD Lab, ERCOT, CAIS, ASE, EMIB, SSI, HPE, OCI, LLC, HELM.
- App E: CS, CS224N, DAIR.AI, EPRI, OECD.
- KLA, SN40L, NEO and the "SMT" in Carl Zeiss SMT are company or product names. Each one's row already says what it is.

The edits below are the ones made in this pass.

All edits are small and surgical, made with the Edit tool. Each passage was re-read just before editing, and every change was confirmed present afterward. No headings, table structures, table numbers or formats changed. `validate.py` passes on both files (neither has diagrams), and a scripted scan found no column-count mismatches, no emoji and no malformed definition lines. `check.py` does not apply to appendices, and no chapter was edited.

## Chapter-pointer audit

I extracted all 244 "More in Chapter N" pointers in Appendix D and searched each target chapter for the row's name. Where the name was absent, I searched for the topic the row is known for. Every pointer leads to a chapter that covers the topic. Rows whose subject is not named in its chapter point there for the topic, which matches the appendix's own rule ("the chapter where the topic is covered in depth"). Examples:
- Ai2 to Chapter 30: Open-source AI definition with weights, code and data.
- OpenRouter to Chapter 26: model routers.
- ElevenLabs to Chapter 46: voice cloning.
- Emily M. Bender to Chapter 58: present-day harms.
- Sam Altman to Chapter 61: OpenAI's business.

I found no wrong pointers. All 24 chapter references in Appendix E were checked the same way and are correct. For example, Chapter 65 has Stage 1, Tracks A to E and the "three resources at most" plan; Chapter 11 has "the four everyday moves" of SQL; and Chapter 12 defines automatic differentiation.

## Findings and fixes

| Appendix | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| D | Table D.1, Meta row | Contradicts Chapter 24. Only Muse Glimmer was listed as open, but Chapter 24 (text, Table 24.7, tiers table) says Meta also released Muse Spark Open on October 15, 2026 (queued in FINAL-FIXES) | Muse Spark now notes "its weights released openly as Muse Spark Open in October 2026". Verified on Meta's announcement (source below) |
| D | Table D.1, Reflection AI row | "Beam 1.0" is a bare name; the reader cannot tell what it is | "Beam 1.0, an open-weight model built for coding, reasoning and agent tasks" (Reflection's own site) |
| D | Table D.1, DeepSeek row | "(MIT license)" is unexplained in the appendix | "under the MIT license, a permissive license that lets anyone use, change and sell products built on them" (matches the Permissive license definition in Chapters 24 and 30) |
| D | Table D.1, Mistral row | "Large 3 (Apache-2.0)" is unexplained | "under Apache-2.0, another permissive license" |
| D | Table D.1, Ai2 row | Paul Allen not identified | "Microsoft co-founder Paul Allen" |
| D | Table D.4, Google Cloud row | "Vertex AI" is unexplained; it is used as if the reader knows it | "Vertex AI, its platform for building and running AI applications" |
| D | Table D.4, Nebius row | Yandex is unexplained | "Yandex, Russia's largest search-engine company" (Chapter 10's own wording) |
| D | Table D.4, Humain row | "Public Investment Fund" is unexplained | "(the Saudi government's sovereign wealth fund)"; the term is defined in Chapter 43, and Chapter 42 says the same |
| D | Table D.6, Databricks row | "Apache Spark" and "MosaicML" are both unexplained | Spark: "a widely used open-source system for processing huge datasets across many machines" (matches the MapReduce (Hadoop, Spark) definition); MosaicML: "a startup that helped companies train their own language models" |
| D | Table D.7, Waymo row | "Alphabet" is first used here, but it is explained only in Table D.10 | "Alphabet (Google's parent company)" |
| D | Table D.8, MATS, ARENA, BlueDot Impact | MATS and ARENA are bare acronyms and their pointer is a career chapter; the details are in Appendix E | Added "Appendix E describes each one" |
| D | Table D.9, John McCarthy | "the Lisp language" could read as a human language | "the Lisp programming language" |
| D | Table D.12, Meredith Whittaker | "Signal Foundation" is unexplained | "(the nonprofit behind the Signal encrypted messaging app)" |
| D | Table D.12, Alex Bores | The "RAISE Act" is unexplained in the appendix | "the state law requiring the largest frontier-model developers to publish safety frameworks and report serious safety incidents" (matches the RAISE Act definition and Table 59's row) |
| E | Beginner courses, Google "AI Essentials" | The cost column says "Coursera subscription", but Coursera is never explained in the appendix | "taught on Coursera, a large online-course platform" |
| E | Researcher courses, Stanford CS336 | "Tatsu Hashimoto" here but "Tatsunori Hashimoto" in Appendix D: a beginner could think these are two people | "Tatsunori (Tatsu) Hashimoto", the form the course page uses plus the nickname |
| E | Compute section, SEC EDGAR (first use in E) | SEC is not expanded at its first use in the appendix | "The database of company filings run by the SEC (Securities and Exchange Commission), the US regulator of stock markets" |

Counts:
- Appendix D: 14 fixes. 13 are undefined names, products, licenses or forward references; 1 is a contradiction with Chapter 24.
- Appendix E: 3 fixes. 2 are undefined names or abbreviations; 1 is an inconsistent name.
- Exercises, arithmetic and skipped steps: none (neither appendix has exercises or worked numbers).

## Verdicts

**Appendix D (Who's Who).** The appendix works as a beginner's reference:
- It is grouped by where each organization sits in the stack (labs, chips, foundries, clouds, builders and energy, tooling, applications, safety and policy, then people).
- Each row is a plain one- or two-line description with a pointer.
- Every pointer leads to a chapter that covers the topic.

The remaining beginner problems were names used as if already known. Licenses, platforms, parent companies, funds and laws appeared without a word on what they are; all are now glossed in place. Every abbreviation in the appendix is either expanded in its row or defined in the chapter it points to, which the glossary confirms. Examples: MTIA, LPU, wafer-scale engine, CoWoS, SMIC, EUV, NIST, HAI, PBC.

I checked the historical facts against standard knowledge and found no errors. These include the founding dates, the Turing Award and Nobel years (Pearl 2011; Hinton, LeCun and Bengio 2018; Sutton and Barto for 2024; the 2024 Physics and Chemistry Nobels), LSTM 1997, perceptron 1958, ELIZA 1966, the 1955 Dartmouth proposal and Lovelace's 1843 notes. The 2025 corporate events also check out: OpenAI Group PBC, the US 9.9% Intel stake and NVIDIA's $5 billion investment, Meta's 49% of Scale AI, CoreWeave buying Weights & Biases, the Agentic AI Foundation, and the renaming of UK AISI and US CAISI. I left the 2026 facts as they were, since they come from the freshness audits.

**Appendix E (Resources).** Clear and usable:
- The levels mirror Chapter 65's Stage 1 and Tracks A to E, and each table gives what a resource is, why it is worth it, what it costs and a stable address.
- The cost labels are defined up front.
- Each resource appears once, with later sections pointing back.

Acronyms were already in good shape: CS course codes, DAIR.AI, OWASP, IBEW, NECA, HVAC, EPRI, OECD, IAPP and AIGP are all expanded, and Discord, cohort course and PMs are glossed. The three fixes close the last gaps. Every technical term the tables use is defined in a chapter: shortcut learning, prompt injection, CUDA and Triton kernels, data, tensor and pipeline parallelism, Uptime Tier ratings, compute governance, moats, unit economics, customer concentration and startup accelerators. Book titles, authors and years match the standard publication record. The URL audit in freshness-appendices.md already covers E's links.

## Flagged, not edited

- Appendix C still has no row for Meta's Muse Spark Open (October 15, 2026); Appendix D is now consistent with Chapter 24. Adding a timeline row is outside this reader test.
- The Stargate row in Appendix D puts "up to $500 billion and 10 gigawatts" in quotation marks as one phrase. Chapter 42 quotes only "up to $500 billion" and gives 10 GW by 2029 separately. The substance is confirmed in freshness-part7.md. The verbatim wording could not be checked because OpenAI's announcement page returns HTTP 403 to automated clients. Consider moving the closing quotation mark to after "billion".
- `acronyms.py` counts only definition callouts and glossary headings, so it will keep listing the inline-glossed entries for Appendices D and E.

## Sources consulted

- Meta, "Muse Spark Open" (October 15, 2026; 816B total, 42B active; Muse Model License with limited commercial terms): https://research.meta.ai/blog/muse-spark-open
- Reflection AI home page (Beam: Reflection's first open-weight model, a 501B mixture-of-experts model "built for coding, reasoning, and agentic workloads"): https://reflection.ai/
- Stanford CS336 course page (Spring 2026; instructors Tatsunori Hashimoto and Percy Liang): https://cs336.stanford.edu
- Attempted, not relied on (HTTP 403): https://openai.com/index/announcing-the-stargate-project/
