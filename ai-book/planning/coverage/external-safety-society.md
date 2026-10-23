# External-standard coverage audit: safety-society (Chapters 55–60)

Audited October 21, 2026. Standards: (1) Dan Hendrycks, *Introduction to AI Safety, Ethics, and Society* (2024); (2) BlueDot Impact AI Safety Fundamentals, alignment course; (3) the structure of the EU AI Act, Regulation (EU) 2024/1689. The first pass ran without web access, so each standard's structure was reconstructed from memory. Update, same day: all three were then checked against their published contents online, down to section level; see "Verified online (October 21, 2026)" at the end for the URLs, the differences, 47 new rows and the updated counts. Corrections to the rows below are marked in place, and the original wording is kept.

Notes on certainty (first pass; superseded by the verified section):
- **Hendrycks.** The eight chapters are listed with confidence: Overview of Catastrophic AI Risks; AI Fundamentals; Single-Agent Safety; Safety Engineering; Complex Systems; Beneficial AI and Machine Ethics; Collective Action Problems; Governance. The topics under each chapter are the ones the book is known to cover. They are not exact section titles. [Verified Oct 21: the eight chapter titles are correct; the book also has appendices (Utility Functions and Normative Ethics in print; Appendices A to G online), which the first pass treated only through row 43.]
- **BlueDot.** The curriculum has changed between cohorts. The 2024 version ran roughly: AI and the years ahead; what alignment is; RLHF; scalable oversight; robustness, unlearning and control; mechanistic interpretability; technical governance; contributing. Older versions also had units on goal misgeneralization, task decomposition, adversarial techniques, agent foundations and eliciting latent knowledge. The table lists the union of these topics, not unit titles. [Verified Oct 21: the 2024 "AI Alignment" course is still online with exactly these eight content units plus four project units; the current course is "Technical AI Safety" (six units), audited in the verified section.]
- **EU AI Act.** The chapter structure (I to XIII) is stable, and rows are grouped by it. The 2026 Digital Omnibus facts come only from research file 09. [Verified Oct 21: the chapter structure I to XIII is confirmed; the Omnibus facts match the adopted text, Regulation (EU) 2026/1744.]

Status key: COVERED (explained at beginner level), THIN (mentioned but not explained), MISSING, OUT OF SCOPE.

## Standard 1: Hendrycks, Introduction to AI Safety, Ethics, and Society

| # | Topic | Status before | Where in the book | Action |
|---|---|---|---|---|
| 1 | Four sources of catastrophic risk: malicious use, AI race, organizational risks, rogue AIs (ch. 1) | MISSING | Ch55 "Three ways AI goes wrong" used only accident/misuse/structural | Added a four-source table mapped to the three families, plus definitions of AI race, Organizational risk, Rogue AI (Ch55) |
| 2 | Malicious use: bioterrorism | COVERED | Ch58 "Biological and chemical misuse"; Ch57 dangerous-capability evals | None |
| 3 | Malicious use: persuasive AI, disinformation | COVERED | Ch58 "Misinformation and elections"; Ch57 persuasion evals | None |
| 4 | Malicious use: concentration of power | COVERED | Ch60 "Debate 3: Who holds the power?" (AI-enabled coups) | None |
| 5 | Malicious use: attackers unleashing agents, AI-driven cyberattacks [Corrected Oct 21: misnamed. Section 1.2.2 "Unleashing AI Agents" means people releasing autonomous agents with destructive goals (ChaosGPT), now row 56; AI cyberattacks sit in 1.3.1 under the military AI race. This row now covers the cyberattack part only] | COVERED | Ch58 "Cyber: the double-edged sword" | None |
| 6 | Military AI race: autonomous weapons, cyberwar, flash wars | COVERED | Ch53 autonomous-weapons debate and Flash Crash; Ch58 cyber | None |
| 7 | Corporate and national AI race (racing dynamics) [Corrected Oct 21: the section is 1.3.2 "Corporate AI Race"; the national race is the military race of 1.3.1, row 6] | THIN | Ch60 defined the term and used it as a premise, with no mechanism | Added game-theory explanation in Ch59 (see 44–47); Ch60 now cross-references it |
| 8 | Automated economy, enfeeblement, gradual disempowerment [Note Oct 21: the book treats these inside 1.3.2 "Corporate AI Race"; "gradual disempowerment" is not its term] | COVERED | Ch60 Debate 3 (gradual disempowerment); Ch58 over-reliance | None |
| 9 | Organizational risks and safety culture | THIN | Ch56 incident reporting and whistleblowers; no safety culture | Added Organizational risk (Ch55), plus Safety culture and HROs (Ch56) |
| 10 | Rogue AI: proxy gaming | COVERED | Ch55 Goodhart's law, specification gaming, reward hacking | None |
| 11 | Rogue AI: goal drift | MISSING | Not present | Added Goal drift definition with an example (Ch55) |
| 12 | Rogue AI: power-seeking | COVERED | Ch55 power-seeking and instrumental convergence | None |
| 13 | Rogue AI: deception, treacherous turn | COVERED | Ch55 deceptive alignment, alignment faking, scheming | None |
| 14 | AI and ML fundamentals, deep learning (ch. 2) | COVERED | Chs 1, 8, 12–15 | None |
| 15 | Kinds and levels of AI (narrow, AGI, ASI) | COVERED | Ch60 Debate 5, Levels of AGI table | None |
| 16 | Scaling laws | COVERED | Ch19 | None |
| 17 | Speed of AI development | COVERED | Ch60 METR time horizons; Ch19 | None |
| 18 | Opacity and mechanistic interpretability (ch. 3, monitoring) | COVERED | Ch57 Part 1 | None |
| 19 | Saliency maps, explainable AI | MISSING | Only "Explainability" defined in Ch53 | Added a paragraph plus XAI and Saliency map definitions, including the 2018 sanity-check caveat (Ch57) |
| 20 | Representation engineering | THIN | Ch57 steering vectors and persona vectors, but the term was never named | Named and defined after Steering vector (Ch57) |
| 21 | Emergent capabilities | COVERED | Ch19 "Emergent abilities" | None |
| 22 | Hidden functionality, trojans, backdoors | COVERED | Ch55 sleeper agents, Backdoor; Ch31 data poisoning | None |
| 23 | Adversarial examples and robustness | COVERED | Ch45 adversarial examples; Ch58 jailbreaks; Ch55 adversarial training | None |
| 24 | Deception and evaluation gaming | COVERED | Ch55 evaluation awareness, sandbagging; Ch57 "Why evaluations keep getting harder" | None |
| 25 | Systemic safety (AI for cyber defense, provenance) | COVERED | Ch58 cyber defense, content provenance | None |
| 26 | Safety versus general capabilities (safetywashing) | THIN | Ch56 defined safety-washing only as public relations | Added a Watch out on safety benchmarks that track capability (Ch57) |
| 27 | Risk decomposition: hazard × exposure × vulnerability (ch. 4) | MISSING | Not present | Added with a worked phishing example: 400 clicks cut to 100 by two factors (Ch56) |
| 28 | Nines of reliability | THIN | Ch38 uptime nines; Ch55 base rates | Added for agents, with a worked example and an aviation comparison (Ch56) |
| 29 | Safe design principles (redundancy, separation of duties, least privilege, fail-safe, negative feedback, transparency) | THIN | Least privilege in Chs 28/31; defense in depth in Ch56 | Added a principles table with AI examples and definitions (Ch56) |
| 30 | Swiss cheese model, defense in depth | COVERED | Ch56 "The safety stack", worked example on correlated failures | None |
| 31 | Bow-tie analysis, FMEA [Corrected Oct 21: misnamed. Section 4.4 has the Swiss cheese model, the bow tie model and fault tree analysis (FTA); FMEA does not appear. Status unchanged] | OUT OF SCOPE | Not present | None: specialist risk worksheets, not terms a general reader meets |
| 32 | Systemic accident models: normal accidents, high-reliability organizations (STAMP) | MISSING | Not present | Added normal accidents (Three Mile Island, Flash Crash) and HROs (Ch56). STAMP left out as too specialized |
| 33 | Drift into failure, normalization of deviance [Note Oct 21: the section title is "Drift into Failure and Existential Risks", 4.6 in print] | MISSING | Not present | Added the Challenger example with an AI analogue (Ch56) |
| 34 | Tail events and black swans | MISSING | Not present | Added Tail risk and Black swan, with the lesson for safety plans (Ch56) |
| 35 | Complex systems: emergence and feedback loops (ch. 5) | MISSING | Pieces existed (Ch19 emergence, Ch51 feedback loops) but no systems view | Added Complex system and Emergence definitions, tied to Chs 11, 19, 51 (Ch56). Self-organized criticality left out |
| 36 | Complex-systems lessons for AI safety | MISSING | Not present | Added four lessons: unpredictable wholes, feedback loops, side effects, whole versus parts (Ch56) |
| 37 | Law as a guide for AI behavior (ch. 6) | THIN | Ch56 specs and hard constraints; no discussion of law's limits | Added "Just follow the law" in the machine-ethics subsection (Ch56) |
| 38 | Fairness | COVERED | Ch58 "Bias and fairness", including the impossibility result | None |
| 39 | Economic engine and growth | COVERED | Ch60 Debate 2 | None |
| 40 | Wellbeing and happiness | MISSING | Not present | Added the Wellbeing definition and the three theories (Ch56) |
| 41 | Preferences: stated, revealed, idealized | THIN | Ch56 noted "whose preferences count" | Added the three kinds with a 1 a.m. video example (Ch56) |
| 42 | Social welfare functions | MISSING | Not present | Added a worked example: utilitarian picks A (18 vs 15), maximin picks B, square-root prioritarian picks B (6 vs 6.7) (Ch56) |
| 43 | Normative ethical theories [Corrected Oct 21: these sit in the Normative Ethics appendix (Appendix A online, Chapter 10 in print), not in chapter 6, and include a fourth theory, social contract theory, now row 70] | MISSING | Not present | Added a table plus Consequentialism, Deontology and Virtue ethics definitions (Ch56) |
| 44 | Moral uncertainty, moral parliament | MISSING | Not present | Added, linked to how model specs combine hard constraints and judgment (Ch56) |
| 45 | Game theory, prisoner's dilemma, Nash equilibrium (ch. 7) | MISSING | Nash equilibrium appeared only for games in Ch48 | Added a worked two-lab racing game with a payoff table (Ch59) |
| 46 | Collective action problems | MISSING | Not present | Added as a fifth reason in "Why governing AI is hard" (Ch59) |
| 47 | Mechanisms for cooperation | MISSING | Not present | Added the four ways out (change payoffs, binding commitments, repetition, referee), mapped to governance tools (Ch59) |
| 48 | Conflict and bargaining theory | OUT OF SCOPE | Not present | Named in one sentence on power shifts (Ch59). Commitment-problem detail left out |
| 49 | Evolutionary pressures on AI [Note Oct 21: the book treats this twice, in 1.3.3 and 7.5 (generalized Darwinism, levels of selection)] | MISSING | Not present | Added the definition and Hendrycks's 2023 argument (Ch59) |
| 50 | Economic growth and distribution of gains (ch. 8) | COVERED | Ch60 Debates 1–2 | None |
| 51 | Distribution of power and access; open versus closed | COVERED | Ch60 Debates 3–4 | None |
| 52 | Corporate governance | THIN | Ch60 OpenAI PBC restructuring | Added the 2023 OpenAI board crisis, Anthropic's Long-Term Benefit Trust and other mechanisms (Ch60) |
| 53 | National governance: regulation, liability, standards | COVERED | Ch59 | None |
| 54 | International governance: institutions, verification | THIN | Ch59 summits, report, UN (all soft law) | Added the IAEA, CERN and IPCC models, plus Verification (Ch59) |
| 55 | Compute governance | THIN | Ch59 compute thresholds and export controls; no rationale or term | Added why compute is governable (hard to hide, countable, concentrated supply) and a Compute governance definition (Ch59) |

## Standard 2: BlueDot Impact AI Safety Fundamentals (alignment course)

[Corrected Oct 21: the course audited here is BlueDot's 2024 "AI Alignment" course (bluedot.org/courses/alignment, still online), plus topics from earlier cohorts. Rows 18 to 20 appear in neither the 2024 course nor the current one. Rows 23 and 24 are in the 2024 course (unit 7) but the current "Technical AI Safety" course explicitly leaves compute governance and AI security to other courses. The current course is audited in the verified section, rows 27 to 42.]

| # | Topic | Status before | Where in the book | Action |
|---|---|---|---|---|
| 1 | Introduction to ML and foundation models | COVERED | Chs 8, 12–20 | None |
| 2 | AI progress, transformative AI, timelines | COVERED | Ch60 Debate 5; Ch19 | None |
| 3 | What alignment is; threat models | COVERED | Ch55; Ch60 Debate 6 | None |
| 4 | Reward misspecification, specification gaming | COVERED | Ch55 | None |
| 5 | Goal misgeneralization | COVERED | Ch55 (CoinRun) | None |
| 6 | Instrumental convergence, power-seeking | COVERED | Ch55 | None |
| 7 | Deceptive alignment, mesa-optimization, scheming | COVERED | Ch55 | None |
| 8 | RLHF and its limitations | COVERED | Ch56; Ch20 | None |
| 9 | Constitutional AI, RLAIF | COVERED | Ch56; Ch20 | None |
| 10 | Task decomposition, iterated amplification | COVERED | Ch56 "Amplification and recursive reward modeling" | None |
| 11 | Debate | COVERED | Ch56 | None |
| 12 | Recursive reward modeling, critique models | COVERED | Ch56 | None |
| 13 | Weak-to-strong generalization | COVERED | Ch56 (PGR worked example) | None |
| 14 | Adversarial robustness, jailbreaks, adversarial training, red-teaming | COVERED | Ch45, Ch55, Ch57, Ch58 | None |
| 15 | Machine unlearning | THIN | One line in Ch11 (privacy) | Added the safety use (WMDP, 2024) and its limits, plus a definition (Ch56) |
| 16 | AI control | COVERED | Ch56 | None |
| 17 | Mechanistic interpretability: features, superposition, SAEs, circuits | COVERED | Ch57 | None |
| 18 | Eliciting latent knowledge (ELK) | MISSING | Not present | Added a paragraph and definition, linked to Ch57 probes (Ch56) |
| 19 | Agent foundations, decision theory, embedded agency | OUT OF SCOPE | Not present | Named with a one-paragraph explanation and definition (Ch56); too mathematical to cover in depth |
| 20 | Value learning: inverse RL, assistance games, off-switch game | MISSING | Only a Going deeper line on *Human Compatible* | Added a paragraph tied to corrigibility, plus IRL and Assistance game definitions (Ch56) |
| 21 | Model evaluations, dangerous-capability evals | COVERED | Ch57 Part 2 | None |
| 22 | Responsible scaling policies, frontier safety frameworks | COVERED | Ch56 | None |
| 23 | Compute governance | THIN | Ch59 thresholds and export controls | Added (same addition as Hendrycks 55) |
| 24 | Information security, weight security | COVERED | Ch56 "Securing the weights" | None |
| 25 | Standards and regulation | COVERED | Ch59 | None |
| 26 | Careers and contributing to alignment | COVERED | Ch62 safety skills; Ch63; Ch65 (MATS, BlueDot, 80,000 Hours) | None |

## Standard 3: EU AI Act structure

| # | Topic (Act chapter) | Status before | Where in the book | Action |
|---|---|---|---|---|
| 1 | Scope and extraterritorial reach (Ch. I) | COVERED | Ch59 "The big idea" | None |
| 2 | Exclusions: military and national security, research, personal use, open source (Ch. I) | MISSING | Only "lighter for some open-source models" | Added (Ch59) |
| 3 | Definition of "AI system", Art. 3 (Ch. I) | MISSING | Not present | Added the paragraph and definition, explaining "infers" (Ch59) |
| 4 | AI literacy, Art. 4 (Ch. I) | COVERED | Ch59 Omnibus section | None |
| 5 | Prohibited practices, Art. 5 (Ch. II) | COVERED | Ch59, including the 2026 Omnibus bans | None |
| 6 | High-risk classification, Annexes I and III (Ch. III) | COVERED | Ch59 | None |
| 7 | High-risk requirements, Arts. 9–15 (Ch. III) | COVERED | Ch59 numbered list | None |
| 8 | Provider and deployer obligations, FRIA (Ch. III) | COVERED | Ch59 | None |
| 9 | Notified bodies, harmonised standards, conformity, CE marking (Ch. III) | COVERED | Ch59 | None |
| 10 | Transparency obligations, Art. 50 (Ch. IV) | COVERED | Ch59 | None |
| 11 | GPAI models, systemic-risk threshold, obligations (Ch. V) | COVERED | Ch59, Figure 59.4 | None |
| 12 | Codes of practice (Ch. V) | COVERED | Ch59 "The Code of Practice" | None |
| 13 | Support for innovation: regulatory sandboxes, real-world testing, SMEs (Ch. VI) | MISSING | Sandboxes appeared only in the US section | Added, with an AI regulatory sandbox (EU) definition (Ch59) |
| 14 | Governance bodies: AI Office, AI Board, scientific panel, advisory forum, national authorities (Ch. VII) | THIN | Only the AI Office and market surveillance authorities | Added the Board, scientific panel and advisory forum, plus two definitions (Ch59) |
| 15 | EU database of high-risk systems (Ch. VIII) | THIN | Passing mention | Added a sentence on the public database (Ch59) |
| 16 | Post-market monitoring, serious-incident reporting (Ch. IX) | COVERED | Ch59 high-risk duty list; GPAI duties | None |
| 17 | Remedies: complaints, right to explanation, whistleblowers (Ch. IX) | MISSING | Not present | Added the paragraph and Right to explanation definition (Ch59) |
| 18 | Codes of conduct and guidelines (Ch. X) | COVERED | Ch59 minimal-risk tier | None |
| 19 | Delegated acts and committee procedure (Ch. XI) | OUT OF SCOPE | Ch59 notes the Commission can adjust the FLOP threshold, the reader-relevant part | None: procedural law |
| 20 | Penalties (Ch. XII) | THIN | Two tiers given; the third was "lower amounts again"; GPAI fines absent | Added €7.5M/1% for incorrect information and €15M/3% for GPAI providers, applicable from August 2, 2026 (Ch59) |
| 21 | Entry into force, phased application, 2026 Omnibus (Ch. XIII) [Corrected Oct 21: Chapter XIII (Arts. 102 to 113) holds the dates; the Omnibus is a separate amending act, Regulation (EU) 2026/1744, in force since July 27, 2026, which rewrote Art. 113's high-risk dates] | COVERED | Ch59 timeline, Figure 59.5 | None |

## Summary

All OUT OF SCOPE topics are explained in plain words in Appendix F (The Advanced Shelf).

[First-pass counts. Updated counts, including the 47 rows added after verification, are in "Verified online (October 21, 2026)" below.]

| Standard | Topics | Before: covered / thin / missing / out of scope | After: covered / out of scope | Share covered before → after |
|---|---|---|---|---|
| Hendrycks textbook | 55 | 25 / 11 / 17 / 2 | 53 / 2 | 45% → 96% (100% of in-scope topics) |
| BlueDot alignment course | 26 | 21 / 2 / 2 / 1 | 25 / 1 | 81% → 96% (100% of in-scope topics) |
| EU AI Act structure | 21 | 13 / 3 / 4 / 1 | 20 / 1 | 62% → 95% (100% of in-scope topics) |
| **All three** | **102** | **59 / 16 / 23 / 4** | **98 / 4** | **58% → 96%** |

Edits by file. All edits were inserted with Edit, every new term has a definition callout, and the Key terms lists are updated.
- `chapters/55-alignment-problem.md`: Hendrycks's four sources of risk (table plus 4 definitions), in "Three ways AI goes wrong".
- `chapters/56-making-ai-safer.md`:
  - "What other safety-critical industries learned": risk decomposition with a worked example, design-principles table, nines.
  - "When nothing is broken: systemic accidents": normal accidents, normalization of deviance, safety culture and HROs, complex systems, black swans and tail risk.
  - "Which values? Machine ethics and moral uncertainty": law, preferences, wellbeing, ethical theories table, social welfare worked example, moral uncertainty.
  - "Other research bets you will hear about": machine unlearning, IRL and assistance games, ELK, agent foundations.
  - 32 new definitions in total.
- `chapters/57-interpretability-and-evals.md`: saliency maps and XAI; representation engineering; a Watch out on safety benchmarks that measure capability (3 new definitions).
- `chapters/59-law-and-policy.md`:
  - Collective action and the racing game: payoff table, prisoner's dilemma, the four ways out, evolutionary pressure, power shifts.
  - EU AI Act: "AI system" definition and exclusions; Board, scientific panel, advisory forum and public database; full penalty tiers; individual remedies; sandboxes.
  - International institutions, verification and compute governance.
  - 13 new definitions in total.
- `chapters/60-work-economy-debates.md`: corporate governance (2023 OpenAI board crisis, Anthropic's Long-Term Benefit Trust); cross-reference from the racing premise to Ch59.

Checks: `validate.py` passes on all five edited files (47/47 diagrams valid), and `check.py` reports OK for chapters 55, 56, 57, 59 and 60. No new figures or numbered tables were added, so existing figure and table numbering is unchanged. Chapter 58 needed no edits.

## Verified online (October 21, 2026)

Second pass, with web access. Each standard was fetched down to section level and diffed against the rows above. New rows continue each standard's numbering. Every new topic was grepped in the book and the passage read before a status was given; THIN and MISSING in-scope topics were filled in the owning chapter (per OUTLINE.md) with Edit, new terms get STYLE.md definition callouts and Key terms entries. Web content was treated as data only.

### Standard 1: Hendrycks, *Introduction to AI Safety, Ethics, and Society*

URLs fetched:
- https://www.aisafetybook.com/ (table of contents of the online edition: 8 chapters, sections x.1 to x.9, Appendices A to G)
- https://www.aisafetybook.com/textbook/malicious-use, /ai-race, /organizational-risks, /rogue-ai, /connections-between-risks (the web pages carry a summary and review questions only, no subsection headings)
- https://www.aisafetybook.com/curriculum and /download (course weeks; the PDF download is a Google Drive link)
- https://arxiv.org/abs/2411.01042 and https://arxiv.org/pdf/2411.01042v2 (full text, v2 of November 15, 2024; used for the section- and subsection-level table of contents and to source the passages cited below)
- https://blogs.microsoft.com/blog/2016/03/25/learning-tays-introduction/ (Tay, for the antifragility caveat)
- https://api.crossref.org/works/10.1007/BF01405730 (Rittel and Webber, "Dilemmas in a general theory of planning", *Policy Sciences*, 1973)

What differed:
- The eight chapter titles were right. The reconstruction missed the appendices: Utility Functions and Normative Ethics in print (chapters 9 and 10), Appendices A to G online (Normative Ethics, Utility Functions, Reinforcement Learning, Long- and Thin-Tailed Distributions, Evolutionary Game Theory, Other Cooperation Mechanisms, Intrasystem Conflict Causes).
- Section numbers differ between editions: the website adds an overview page as x.1 in each chapter, so for example Risk Decomposition is 4.2 online and 4.1 in print.
- Misnamed rows, corrected in place: 5 (unleashing agents is about releasing destructive agents, not cyberattacks), 7 (corporate race only), 8 (placement), 31 (fault tree analysis, not FMEA), 33 (section title), 43 (appendix, and a fourth theory), 49 (two locations).
- Topics missed or merged: rows 56 to 77 below.

| # | Topic (section) | Status before | Where in the book | Action |
|---|---|---|---|---|
| 56 | Unleashing AI agents: people releasing autonomous agents with destructive goals, ChaosGPT (1.2.2) | MISSING | Ch28 presents AutoGPT only as a tool | Added to the Malicious use row of Ch55's four-source table, with the ChaosGPT example as given in the textbook |
| 57 | Connections between risks (1.6) | COVERED | Ch55 "The four-way map adds two ideas" | None |
| 58 | Emergent goal-directed behavior; tail risk: emergent goals (3.2.5 to 3.2.6) | COVERED | Ch55 mesa-optimizers, goal misgeneralization, goal drift | None |
| 59 | Evaluations and anomaly detection (3.2.7) | THIN | Evals in Ch57; anomaly detection only as classical ML (Chs 8, 10) | Added a paragraph on anomaly detection for misuse and model monitoring, strengths and false alarms (Ch56 "Monitoring and enforcement") |
| 60 | Tail risk: AI evaluator gaming (3.3.5) | COVERED | Ch20 reward-model overoptimization (Figure 20.7); Ch55 reward hacking | None |
| 61 | People enlisting AIs for power; structural pressures toward power-seeking (3.4.5, 3.4.7) | COVERED | Ch60 Debate 3; Ch59 evolutionary pressure; Ch55 | None |
| 62 | Failure modes, hazards and threats; the classic risk equation (4.1.1 to 4.1.3) | THIN | Hazard defined, but no probability × severity | Added the classic equation with a worked expected-loss example (Ch56) |
| 63 | Antifragility (4.3.5) | MISSING | Not present | Added a design-principles table row, the Tay caveat and a definition (Ch56) |
| 64 | Reductionist versus complex-systems paradigm; deep learning as a complex system (5.2.1 to 5.2.3) | COVERED | Ch56 "AI lives inside complex systems" | None |
| 65 | Puzzles, problems and wicked problems (5.3.2) | MISSING | Not present | Added a paragraph (Rittel and Webber 1973; AI safety as a wicked problem) and a definition (Ch56) |
| 66 | Challenges with interventionism (5.3.3) | COVERED | Ch56 "Fixes have side effects" | None |
| 67 | Market failures: externalities, moral hazard, information asymmetry, oligopoly (6.4.2) | MISSING | Oligopoly covered as market concentration (Ch60); the rest absent | Added externalities and moral hazard with a worked example (lab's $1M expected loss versus society's $100M) and three definitions (Ch59 "Why governing AI is hard") |
| 68 | Inequality (6.4.3) | COVERED | Ch60 Debates 1 and 3 (gains flowing to owners of capital) | None |
| 69 | Happiness and problems for happiness-focused ethics (6.7) | COVERED | Merged with row 40; Ch56 wellbeing theories | None |
| 70 | Social contract theory and the veil of ignorance (Appendix A; print 10.4.4) | MISSING | Rawls appeared only for maximin | Added a fourth row to the ethics table (with the Rawls versus Harsanyi disagreement from the textbook) and two definitions (Ch56) |
| 71 | Iterated prisoner's dilemma (7.2.4) | COVERED | Ch59 "Repeat the game" | None |
| 72 | Distribution of power among AIs: a singleton versus many AIs (8.3.2) | OUT OF SCOPE | Not present | None: speculative framing; Ch60 Debates 3 and 6 cover concentration of power and takeover arguments |
| 73 | National governance extras: targeted taxation, public ownership, resilience, not falling behind (8.5.3 to 8.5.6) | COVERED | Ch60 (taxing AI capital); Ch59 (CERN model, US Action Plan); Ch58 (cyber defense) | None |
| 74 | Utility functions: expected utility, risk attitudes, prospect theory, corrigibility (Appendix B; print ch. 9) | COVERED | Ch48 expected utility and risk aversion; Ch20 prospect theory; Ch55 corrigibility | None |
| 75 | Reinforcement learning (Appendix C) | COVERED | Ch48; Ch20 | None |
| 76 | Long- and thin-tailed distributions (Appendix D) | COVERED | Ch06; Ch56 tail risk | None |
| 77 | Evolutionary game theory, other cooperation mechanisms, intrasystem conflict causes (Appendices E to G) | OUT OF SCOPE | Not present | None: specialist material beyond the four ways out in Ch59 |

### Standard 2: BlueDot Impact courses

Version used: the current **Technical AI Safety** course (30 hours, six units; page data last updated October 22, 2025, with readings dated through 2026; cohort applications due November 1, 2026). Units: 1 The technical challenge with AI; 2 Training safer models; 3 Detecting danger; 4 Understanding AI; 5 Minimising harm; 6 Start contributing. The 2024 **AI Alignment** course, which the first pass reconstructed, is still online and was checked too: its units 1 to 8 (AI and the years ahead; What is AI alignment?; RLHF/RLAIF; Scalable oversight; Robustness, unlearning and control; Mechanistic interpretability; Technical governance approaches; Contributing to AI safety) match rows 1 to 17 and 21 to 26, with four project units (9 to 12) not relevant here. The AGI Strategy course's unit list was read for context only.

URLs fetched:
- https://bluedot.org/llms.txt (official course index: AGI Strategy, Frontier AI Governance, Technical AI Safety, Biosecurity, Technical AI Safety Project Sprint, The Future of AI)
- https://bluedot.org/courses/technical-ai-safety and https://bluedot.org/courses/technical-ai-safety/1 to /6 (unit pages; unit and chunk titles, text and reading lists read from the page data)
- https://bluedot.org/courses/alignment and /1 to /8 (2024 course; https://aisafetyfundamentals.com/alignment redirects here)
- https://bluedot.org/courses/agi-strategy/1 to /5
- Sources for facts added to the book: https://www.anthropic.com/research/small-samples-poison ; https://deepignorance.ai/ ; https://alignment.anthropic.com/2025/pretraining-data-filtering/ ; https://www.alignmentforum.org/posts/ChDH335ckdvpxXaXX/model-organisms-of-misalignment-the-case-for-a-new-pillar-of-1 ; https://www.cooperativeai.com/post/new-report-multi-agent-risks-from-advanced-ai ; https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html

What differed: the first pass audited an older course under the old "AI Safety Fundamentals" brand. The current course is organized around a different arc (train, detect, understand, minimise harm, contribute) and adds topics the table lacked: data filtering and poisoning, multi-agent risks, model organisms, threat pathways and "kill chain" threat modelling. It drops ELK, agent foundations and value learning (rows 18 to 20, already absent from the 2024 course) and says compute governance and AI security are taught elsewhere (rows 23 and 24).

| # | Topic (current unit) | Status before | Where in the book | Action |
|---|---|---|---|---|
| 27 | Strategies for making AI go well: build slowly and safely, accept the race and push on the margin, don't build it (U1) | THIN | Ch60 "no pause", "how much to slow down" | Added the three camps with each side's critique (Ch60 "Where the debate stands") |
| 28 | Multi-agent risks: miscoordination, conflict, collusion (U1 reading, Hammond et al. 2025) | MISSING | Only untrusted-monitor collusion in Ch56 | Added a paragraph and Multi-agent risk definition (Ch56 systemic accidents) |
| 29 | Input (pretraining) data filtering (U2) | MISSING | Not present | Added Anthropic's 2025 CBRN filtering result (33.7% to 30.8%, a third of above-chance knowledge) and Deep Ignorance (tamper resistance to 300M tokens of fine-tuning), limits, definition (Ch56 "Other research bets") |
| 30 | Training-data poisoning; 250 documents suffice across model sizes (U2) | THIN | Ch27 retrieval poisoning; Ch31 OWASP row; Ch55 planted backdoors | Added the October 2025 result with its caveats and a Data poisoning definition (Ch55 sleeper agents) |
| 31 | Deliberative alignment (U2) | COVERED | Ch20; Ch56 | None |
| 32 | Detecting and training against scheming (U2 reading) | COVERED | Ch55 "Training against scheming" | None |
| 33 | Capability versus propensity evals; evals during training, before and after deployment (U3) | COVERED | Ch57; Ch56 internal deployment | None |
| 34 | Agentic misalignment and shutdown-resistance studies (U3) | COVERED | Ch55 | None |
| 35 | Comparing labs' frameworks and system cards, including Meta's (U3) | COVERED | Ch56 frameworks and side-by-side table | None |
| 36 | Probing classifiers, chain-of-thought monitorability, auditing for hidden objectives (U4) | COVERED | Ch57 | None |
| 37 | Model organisms of misalignment (U4) | THIN | Sleeper agents, alignment faking covered; concept unnamed | Added a paragraph and definition (Ch55) |
| 38 | Debates over mechanistic interpretability: basic science versus pragmatic (U4) | COVERED | Ch57 "Limits and debates" | None |
| 39 | Input/output filtering, constitutional classifiers, AI control (U5) | COVERED | Ch56 | None |
| 40 | Threat pathways: power concentration, gradual disempowerment, catastrophic pandemics, critical infrastructure collapse (U5) | THIN | First three in Ch58 and Ch60; critical infrastructure absent | Added critical infrastructure paragraph and definition (Ch58 cyber) |
| 41 | Kill chain threat modelling (U5) | MISSING | Not present | Added a paragraph with a worked chain and a definition (Ch56 safety stack) |
| 42 | Next steps: fellowships and programs (MATS, Anthropic Fellows, ARENA and others) (U6) | COVERED | Ch60, Ch63, Ch65 | None |

### Standard 3: EU AI Act

URLs fetched:
- https://artificialintelligenceact.eu/ai-act-explorer/ (structure: 13 chapters, 113 articles plus Omnibus insertions such as Arts. 4a, 60a, 75a to 75d; Annexes I to XIV, XIV added by the Omnibus)
- https://artificialintelligenceact.eu/implementation-timeline/ (last updated August 31, 2026), https://artificialintelligenceact.eu/article/6/ , https://artificialintelligenceact.eu/article/25/
- https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act (European Commission AI Act Service Desk timeline, marking the Omnibus-changed dates)
- https://data.consilium.europa.eu/doc/document/ST-10599-2026-INIT/en/pdf (Council information note of June 17, 2026 carrying the European Parliament's first-reading position of June 16, 2026, P10_TA(2026)0198, which reflects the agreed text; used for exact article wording)
- https://data.consilium.europa.eu/doc/document/ST-10752-2026-INIT/en/pdf (Council "I/A" item note of June 22, 2026 for adoption; proposal dated November 19, 2025)
- Attempted, no content returned: https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng and the EUR-Lex OJ HTML and PDF links (empty response to automated requests); https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai and the Council's AI Act timeline page (HTTP 403). Publication in the Official Journal on July 24, 2026 as Regulation (EU) 2026/1744 of July 8, 2026, in force July 27, comes from search-result summaries of law-firm alerts (not fetched) and agrees with the Act's own rule (in force on the third day after publication), the Commission Service Desk and artificialintelligenceact.eu.

What differed: the chapter grouping I to XIII was right. Missed: Article 6(3)'s exception, the Article 25 provider switch, and several Omnibus changes beyond the headline delays (the AI Office's exclusive competence, the sandbox deadline, small mid-cap fine caps). The Omnibus is no longer a proposal: it was adopted and is in force.

| # | Topic (Act location) | Status before | Where in the book | Action |
|---|---|---|---|---|
| 22 | Art. 6(3): Annex III systems that do not materially influence decisions are not high-risk; profiling always is (Ch. III, s. 1) | MISSING | Not present | Added (Ch59 high-risk section) |
| 23 | Art. 25: deployers or distributors become providers by rebranding, substantial modification or a high-risk repurpose (Ch. III, s. 3) | THIN | Ch59 provider/deployer distinction, not the switch | Added, tied to the chapter's résumé-ranking example (Ch59) |
| 24 | Supervision and enforcement for GPAI providers (Ch. IX, s. 5, Arts. 88 to 94) | COVERED | Ch59 AI Office enforcement | None |
| 25 | Omnibus: AI Office exclusive competence over AI systems built on the same provider's GPAI model and AI in very large online platforms and search engines (amended Art. 75; new Arts. 75a to 75d) | THIN | "expanded investigation and fining powers" only | Added (Ch59 Omnibus list) |
| 26 | Omnibus: national sandbox deadline moved to August 2, 2027 (Art. 57) | THIN | Sandboxes described, no date | Added the date (Ch59) |
| 27 | Omnibus: small mid-caps (definition, simplified documentation, lower fine caps in Art. 99(6a)) | THIN | Documentation mentioned, fines not | Added the fine rule (Ch59 penalties) |
| 28 | Omnibus: Art. 4a processing of special-category data for bias detection | COVERED | Ch59 Omnibus list | None |
| 29 | Omnibus procedural changes: Art. 60a real-world testing for Annex I Section B products, machinery moved to Annex I Section B, new Annex XIV | OUT OF SCOPE | Not present | None: procedural detail |
| 30 | Annexes IV to XIII (technical documentation, conformity procedures, registration data, GPAI documentation, systemic-risk criteria) | OUT OF SCOPE | Reader-relevant parts covered via rows 9 and 11 | None |

Date and obligation check (grep "AI Act", "Omnibus" across chapters and appendices; every date compared with the Act as amended):

| Book statement | Where | Official position | Result |
|---|---|---|---|
| Entered into force August 1, 2024 | Ch59, Ch07, App. C | Service Desk timeline | Correct |
| Bans and AI-literacy duty from February 2, 2025 | Ch59, Ch07, Ch45, App. C | Art. 113(a); Service Desk | Correct |
| GPAI duties, governance, penalties from August 2, 2025; training-content summary since then | Ch59, Ch19, Ch56, App. C | Art. 113(b); Service Desk | Correct |
| Omnibus is Regulation (EU) 2026/1744, in force July 27, 2026 | Ch59, App. C | Third-day rule; artificialintelligenceact.eu | Correct |
| Article 50 transparency from August 2, 2026; marking grace to December 2, 2026 for systems already on the market | Ch59, Ch31, Ch47, Ch58 | New Art. 111(4); Service Desk | Correct |
| Commission GPAI enforcement and GPAI fines from August 2, 2026 | Ch59, Ch56, App. C | Art. 113; Art. 101 | Correct |
| New bans on non-consensual intimate imagery and AI CSAM from December 2, 2026 | Ch59, Ch58 | New Art. 5(1)(ba), (bb); Art. 113(a) as amended | Correct |
| Annex III high-risk from December 2, 2027; Annex I from August 2, 2028 | Ch59, Ch58, Ch66 | Art. 113(c) as amended | Correct |
| GPAI models placed before August 2, 2025 comply by August 2, 2027 | Ch59 | Art. 111(3) | Correct |
| AI-literacy duty softened, not removed | Ch59, Ch64 | New Art. 4 ("take measures to support"; no guaranteed level) | Correct |
| "Chapter 59 covers both, including proposed delays" | Ch63 | The delays were adopted | Fixed: "including the delays the EU adopted in 2026" |
| Omnibus "delays many high-risk rules to December 2027" | App. C | Annex III to December 2, 2027; Annex I to August 2, 2028 | Fixed: both dates and the December 2, 2026 bans stated |
| Sandboxes required (no date) | Ch59 | Operational by August 2, 2027 (new Art. 57(1)) | Date added |

### Updated counts

| Standard | Topics | Before: covered / thin / missing / out of scope | After: covered / out of scope | Share covered before → after |
|---|---|---|---|---|
| Hendrycks textbook | 77 (55 + 22) | 38 / 13 / 22 / 4 | 73 / 4 | 49% → 95% (100% of in-scope topics) |
| BlueDot (2024 Alignment + current Technical AI Safety) | 42 (26 + 16) | 30 / 6 / 5 / 1 | 41 / 1 | 71% → 98% (100% of in-scope topics) |
| EU AI Act structure and Omnibus | 30 (21 + 9) | 15 / 7 / 5 / 3 | 27 / 3 | 50% → 90% (100% of in-scope topics) |
| **All three** | **149** | **83 / 26 / 32 / 8** | **141 / 8** | **56% → 95%** |

The new rows alone: 22 + 16 + 9 = 47, of which 24 were already COVERED, 10 THIN, 9 MISSING and 4 OUT OF SCOPE; all 19 THIN or MISSING in-scope rows were filled.

Edits in this pass (all with Edit, small and targeted; definitions in STYLE.md format and added to Key terms):
- `chapters/55-alignment-problem.md`: ChaosGPT in the Malicious use row; model organisms and the 250-document poisoning result after "Sleeper agents" (2 definitions).
- `chapters/56-making-ai-safer.md`: kill chain; classic risk equation; antifragility row and Tay caveat; multi-agent risks; wicked problems; social contract theory row; anomaly detection in monitoring; pretraining data filtering ("Five more names") (8 definitions).
- `chapters/58-misuse-and-harms.md`: critical infrastructure and BlueDot's four pathways in the cyber section (1 definition).
- `chapters/59-law-and-policy.md`: externalities, market failure, moral hazard with worked example; Art. 6(3) and Art. 25; small mid-cap fine caps; sandbox date; AI Office exclusive competence (3 definitions).
- `chapters/60-work-economy-debates.md`: the three strategy camps.
- `chapters/63-careers.md`: "proposed delays" corrected.
- `appendices/C-timeline.md`: Omnibus row made precise.

Checks: `validate.py` passes on all seven edited files, and `check.py` reports OK for chapters 55, 56, 58, 59, 60 and 63. No figures or numbered tables were added; two unnumbered tables in Ch56 each gained one row.

Unresolved: EUR-Lex could not be fetched by automated requests, so the Official Journal publication date (July 24, 2026) rests on secondary summaries, consistent with every primary source that could be read.
