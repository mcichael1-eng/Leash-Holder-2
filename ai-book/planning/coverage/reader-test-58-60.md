# Reader test: chapters 58 to 60

Tested by reading chapters 58 (Misuse, Security and Everyday Harms), 59 (AI Law and Policy Around the World) and 60 (AI, Work, the Economy and the Big Debates) in order, in full, as the intended reader: almost no computer-science background, a daily chatbot user for a year, and someone who has read chapters 1 to 57. Before treating a term as undefined I checked GLOSSARY.md and the earlier chapters. Every entry for these chapters in acronyms-by-chapter.json was worked through. All arithmetic in the three chapters was recomputed by hand (scam-message costs, the fairness table, prompt energy, compute thresholds, fines, incident clocks, the Dana task audit, growth rates, the build-out revenue, METR extrapolations); none was wrong. Fixes are small and surgical: a definition callout, an inline gloss, a bridging sentence or a clearer exercise step. Nothing was rewritten for style and no content was cut.

After editing, `validate.py` passes on all three files (7/7, 12/12 and 9/9 diagrams valid) and `check.py` reports `[OK]` for chapters 58, 59 and 60.

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 58 | Why this is now a society problem | "Perplexity's Comet": Perplexity appears in the glossary only as a statistics term | Glossed as "the AI search company Perplexity" |
| 58 | Same section, hijack arithmetic | "Attack surface" is security jargon | Added a one-clause gloss |
| 58 | Cyber, Mythos paragraph | "OpenBSD" is unexplained | Glossed as a free operating system known for its focus on security |
| 58 | Same paragraph | NVIDIA and AWS are used in 43 and 22 chapters with no definition anywhere | New definition callouts: NVIDIA; AWS (Amazon Web Services). Both added to Key terms |
| 58 | Grok image scandal | "X" given with no hint that it is Twitter | Added "(the social network formerly called Twitter)" |
| 58 | The law, EU bullet | Digital Omnibus and EU AI Act are used here but defined only in Chapter 59 | Glossed both in the sentence, with a pointer to Chapter 59 |
| 58 | Figure 58.5 | The figure says a camera "signs" a file and that a "re-encode" strips credentials; neither is explained | Added a two-sentence paragraph after the caption explaining both |
| 58 | Risk scores (COMPAS) | ProPublica is unexplained | Glossed as a US investigative newsroom |
| 58 | Equal false positive rates definition | "Equalized odds" named but not explained | Added that it also requires equal false negative rates, with a gloss of false negative |
| 58 | Can it be predicted at all? | "PNAS" unexplained | Spelled out and glossed as a leading US science journal |
| 58 | Same paragraph | "Explained only about a fifth of the variation" is statistics language | Linked to R² from Chapter 9 and restated it in plain words |
| 58 | ADMT definition | The label is "ADMT", but the T is never expanded | Added "ADMT is short for automated decision-making technology" |
| 58 | Privacy, legal demands | "Subpoena" unexplained | Glossed as a legal order to hand over evidence |
| 58 | Children and teens | Common Sense Media unexplained | Glossed as a US nonprofit that rates media and technology for families |
| 58 | OpenAI crisis figures | "Leaves thousands of people a week" skipped the step | Added "1% of 1.2 million is 12,000" |
| 58 | Lawsuits paragraph | Character.AI first appears with no gloss | Glossed as a popular companion app for chatting with AI characters |
| 58 | Rules list, SB 243 | "SB" (used in 13 chapters) unexplained | Added "(SB stands for Senate Bill...)" at first use |
| 58 | FTC inquiry bullet | Alphabet and Snap are not obviously Google's parent and Snapchat's maker | Glossed both |
| 58 | China bullet | "Anthropomorphic" unexplained | Added "(human-like)" |
| 58 | Environmental footprint | "CO2-equivalent" unexplained (CO2 is undefined anywhere in the book) | Glossed CO2-equivalent and CO2 |
| 58 | Table 58.3 | "Shadow libraries", "summary judgment", "legal headnotes", "survived dismissal", "cross-motions" are legal jargon | Short glosses inside the table cells |
| 58 | After Table 58.3 | "Collective licensing" unexplained | Added a one-clause gloss |
| 58 | Who owns chatbot output | Mistral given with no gloss | Glossed as a French AI company |
| 58 | Exercise 5 | "Enter Group A and Group B with the counts" gave no layout or formulas, and ÷ fails in a spreadsheet | Gave cell positions, the four formulas with /, check values (48% and 10%), and the new Group B counts for step 3 |
| 58 | Exercise 9 | "Third Circuit" unexplained | Glossed as a US federal appeals court |
| 59 | Why governing AI is hard | "Dan Hendrycks" and "Hendrycks's textbook" arrive with no reminder of who he is | Glossed with a pointer to Chapter 55, where his textbook is introduced |
| 59 | Six instruments, Standards | NIST, ISO and CEN-CENELEC are used ~430 lines before NIST is defined; ISO and CEN-CENELEC are never expanded | Spelled out all three at first use |
| 59 | After the Bill definition | SB, AB and Colorado's SB26-189 are used throughout with no explanation (SB is undefined in 13 chapters) | New definition callout: SB and AB (US state bill numbers), covering the Colorado year prefix. Added to Key terms |
| 59 | Executive order definition | "EO 14110" in Table 59.1 and later; EO never expanded | Added a sentence to the definition: US orders are numbered and abbreviated EO |
| 59 | How the instruments connect | New York's RAISE Act named with no hint of what it is | Added "(both described later in this chapter)" |
| 59 | Figure 59.2 | Figure uses GPAI and NCII before GPAI is defined | Added a sentence after the caption glossing both |
| 59 | Worked example 1 (GPT-3) | The powers-of-ten multiplication and the "30 times below" step are skipped | Showed multiply-the-numbers, add-the-exponents, and 10^25 ÷ 3.2 × 10^23 ≈ 31 |
| 59 | Banned list | "CCTV" unexplained | Added "(security-camera)" |
| 59 | Code of Practice signatories | IBM (used in 8 chapters) has no definition in this range | New definition callout: IBM (International Business Machines), labeled to match Chapters 8 and 54. Added to Key terms |
| 59 | Fines | "SME" unexplained | Spelled out as the EU's small or medium-sized enterprise definition |
| 59 | Older laws apply | FCC used later as an abbreviation that is never attached | Added "(FCC)" and a one-clause gloss |
| 59 | Figure 59.6 | The timeline uses DOJ, "House" and the FRONTIER Act before the text explains them | Added a sentence after the caption |
| 59 | EO 14365 bullets | "Broadband (BEAD) money" unexplained | Spelled out BEAD and said what it pays for |
| 59 | New York RAISE Act | Table 59.4 says "new DFS office"; DFS never introduced | Added "(DFS)" after Department of Financial Services |
| 59 | United Kingdom | "Horizontal AI law" and "white paper" unexplained | Short glosses for both |
| 59 | Other countries | "Ratify" unexplained | Glossed as formally approving a treaty through national procedures |
| 59 | Table 59.5 and Figure 59.11 | "CA" and "NY" abbreviations | Written out as California and New York |
| 59 | International AI Safety Report | IPCC used before it is spelled out | Spelled out and glossed at first use |
| 59 | United Nations | OECD unexplained | Spelled out and glossed |
| 59 | Export controls, looser-controls case | SMIC (3 chapters, no definition) and Huawei unexplained | New definition callout: SMIC, consistent with Chapter 36's "per reports" wording; Huawei glossed. Added to Key terms |
| 59 | Standards list | IEC and "JTC 21" unexplained | Spelled out both |
| 59 | Exercise 4 | No row layout, "175e9" notation unexplained, formulas only for row 2 and not filled down, no check value | Added header row and start row, explained e-notation, said to copy the formulas down, gave a check (GPT-3: about 3.2E23 FLOPs and roughly $440,000) |
| 59 | Areas of opportunity | IAPP (5 chapters) and CSET (7 chapters) have no definition in this range | New definition callouts after the list: IAPP; CSET. Added to Key terms |
| 60 | Exposure estimates | IMF unexplained | Spelled out and glossed |
| 60 | Same list | "Bing Copilot" unexplained | Glossed as Microsoft's AI assistant in Bing |
| 60 | Canaries study | "After controlling for company-level shocks" is statistics jargon | Explained as comparing workers inside the same companies |
| 60 | Null results | Yale Budget Lab unexplained | Glossed |
| 60 | Adoption is broad | "Pilots" is defined only in Chapter 61 | Glossed as small trial projects inside companies |
| 60 | Normal-transition case | "ATMs" unexplained | Spelled out |
| 60 | Growth worked example | 1.07^(1/10) appears with no explanation of a fractional power | Added what it means and how to compute it in a spreadsheet |
| 60 | Circular deals | AMD (22 chapters) has no definition in this range | New definition callout: AMD (Advanced Micro Devices), labeled to match the earlier chapters. Added to Key terms |
| 60 | Government-lab dispute | "Pentagon", "temporary injunction" and "First Amendment retaliation" unexplained | Glossed all three, with a pointer to Chapter 59's injunction definition |
| 60 | Manageable-concentration case | "Antitrust law" and "procurement rules" unexplained | Short glosses |
| 60 | METR paragraph | "AI R&D" unexplained | Added "(research and development)" |
| 60 | Extrapolation worked example | No way for the reader to compute log2 | Added the spreadsheet formula =LOG(2.3, 2) |
| 60 | Case for concern | Future of Life Institute and "CAIS" (used in Exercise 8) unexplained | Glossed FLI; tied CAIS to the Center for AI Safety from Chapter 55 |
| 60 | Model welfare | "NYU" unexplained | Spelled out |
| 60 | Areas of opportunity | "HR-data" unexplained; MATS and ARENA undefined in this range | Spelled out HR; pointed MATS and ARENA to their definitions in Chapter 55 |
| 60 | Exercise 4 | No row layout or fill-down instructions, and step 5 ("doubling time slows by 10% every doubling") had no formula a non-programmer could write | Gave the layout and fill-down, a check (months 6, 14 and 29), and a complete column-D formula with a plain-words explanation and a check (about month 41), verified by computation |
| 60 | Exercise 8 | "CAIS" unexplained | Spelled out |
| 60 | Exercise 10 | The scoring rule did not say to write probabilities as decimals or what ^2 means | Added both, two worked scores and the always-50% baseline of 0.25 |

Fixes per chapter (66 in total):

- **Chapter 58 (25 rows, 29 individual fixes):** 24 undefined terms (2 new definition callouts: NVIDIA and AWS), 3 beginner jumps and 2 exercises.
- **Chapter 59 (25 fixes):** 21 undefined terms (6 new definition callouts: SB and AB, IBM, SMIC, IAPP and CSET, plus the EO sentence added to an existing definition), 3 beginner jumps and 1 exercise.
- **Chapter 60 (20 fixes):** 14 undefined terms (1 new definition callout: AMD), 3 beginner jumps and 3 exercises.

Every new definition was added to its chapter's Key terms list.

## Noticed but not changed

- **Duplicate definitions from parallel passes.** Other reader passes running at the same time added definition callouts for the same organizations in their own chapters. NVIDIA is now defined in 8 chapters, AMD and AWS in about 6 each, IBM in 3, and IAPP and CSET also in Chapter 62. Chapter 56 now defines SB 53 and the RAISE Act. So I removed the RAISE Act callout I had first added to Chapter 59 and kept only a pointer, and I matched my IBM and AMD labels to the earlier ones so the glossary merges them. Whoever builds the glossary may want to pick one wording for each organization.
- **Capitalization.** Chapters 59 and 60 write "Nvidia" in running text, while definitions and most chapters use "NVIDIA". This was left alone because it is a style question.
- **Chapter 60, Exercise 2.** The exercise cites an OpenAI run-rate of "about $20 billion at the end of 2025" that does not appear in the chapter text. It is a sourced 2025 figure, so it is flagged here and not changed.
- **Placement of new callouts.** IAPP and CSET first appear in Chapter 59's Areas of opportunity list, so their callouts sit at the end of that list. Chapter 55's pass placed MATS and ARENA the same way.

## Verdicts

**Chapter 58.** The ramp works. The chapter opens with a map, then a cheap-versus-expensive worked example the reader can follow with school arithmetic. It moves through security, cyber, bio, fraud, abuse, elections, provenance, fairness, privacy, teens, energy and copyright, and each section is self-contained. The fairness section is the hardest part and the best taught: the two-group table reconciles exactly, and the screening-test analogy carries the impossibility result. Every core concept already had a callout. The gaps were names (companies, organizations, journals, platforms), a run of legal jargon in the copyright table, and two terms (EU AI Act, Digital Omnibus) borrowed from the next chapter. With the glosses added, every term is now defined or glossed where it first appears.

**Chapter 59.** This is the densest chapter of the three. It has 106 definitions and a new institution every few paragraphs, but the structure carries the reader: six instruments, grip points, then jurisdiction by jurisdiction, ending with a five-question checklist. The game-theory and externality worked examples are clear, and the compute-threshold examples are correct. The one place a beginner would stall was multiplying powers of ten, which is now shown. The main friction was abbreviations used as if already known: SB and AB, EO, NIST, ISO, CEN-CENELEC, IEC, JTC, SME, BEAD, FCC, DFS, IPCC, OECD and CA/NY, plus two figures whose labels came before the text. All are now expanded or glossed at first use. The difficulty ramp holds, although a reader should expect to go slowly.

**Chapter 60.** The ramp works well. It opens with thinking tools (steelman, crux, calibration), and each of the seven debates then starts from a concrete worked example: Dana's week, the growth comparison, the build-out revenue, the METR extrapolation and the 5% airline example. Every number checks. The beginner jumps were mathematical: a fractional power (1.07^(1/10)), log base 2 with no way to compute it, and a regression phrase ("controlling for"). Each now has a plain-words explanation or a spreadsheet formula. The exercises were the weakest part, because the spreadsheet extrapolation asked for a slowing-doubling column that no non-programmer could build. That exercise now has a complete, verified formula and check values. Every term is defined in this chapter or an earlier one, or glossed where it is used.
