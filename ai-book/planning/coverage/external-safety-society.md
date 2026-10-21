# External-standard coverage audit: safety-society (Chapters 55–60)

Audited October 21, 2026. Standards: (1) Dan Hendrycks, *Introduction to AI Safety, Ethics, and Society* (2024); (2) BlueDot Impact AI Safety Fundamentals, alignment course; (3) the structure of the EU AI Act, Regulation (EU) 2024/1689. Web search was unavailable, so each standard's structure is reconstructed from memory.

Notes on certainty:
- **Hendrycks.** The eight chapters are listed with confidence: Overview of Catastrophic AI Risks; AI Fundamentals; Single-Agent Safety; Safety Engineering; Complex Systems; Beneficial AI and Machine Ethics; Collective Action Problems; Governance. The topics under each chapter are the ones the book is known to cover. They are not exact section titles.
- **BlueDot.** The curriculum has changed between cohorts. The 2024 version ran roughly: AI and the years ahead; what alignment is; RLHF; scalable oversight; robustness, unlearning and control; mechanistic interpretability; technical governance; contributing. Older versions also had units on goal misgeneralization, task decomposition, adversarial techniques, agent foundations and eliciting latent knowledge. The table lists the union of these topics, not unit titles.
- **EU AI Act.** The chapter structure (I to XIII) is stable, and rows are grouped by it. The 2026 Digital Omnibus facts come only from research file 09.

Status key: COVERED (explained at beginner level), THIN (mentioned but not explained), MISSING, OUT OF SCOPE.

## Standard 1: Hendrycks, Introduction to AI Safety, Ethics, and Society

| # | Topic | Status before | Where in the book | Action |
|---|---|---|---|---|
| 1 | Four sources of catastrophic risk: malicious use, AI race, organizational risks, rogue AIs (ch. 1) | MISSING | Ch55 "Three ways AI goes wrong" used only accident/misuse/structural | Added a four-source table mapped to the three families, plus definitions of AI race, Organizational risk, Rogue AI (Ch55) |
| 2 | Malicious use: bioterrorism | COVERED | Ch58 "Biological and chemical misuse"; Ch57 dangerous-capability evals | None |
| 3 | Malicious use: persuasive AI, disinformation | COVERED | Ch58 "Misinformation and elections"; Ch57 persuasion evals | None |
| 4 | Malicious use: concentration of power | COVERED | Ch60 "Debate 3: Who holds the power?" (AI-enabled coups) | None |
| 5 | Malicious use: attackers unleashing agents, AI-driven cyberattacks | COVERED | Ch58 "Cyber: the double-edged sword" | None |
| 6 | Military AI race: autonomous weapons, cyberwar, flash wars | COVERED | Ch53 autonomous-weapons debate and Flash Crash; Ch58 cyber | None |
| 7 | Corporate and national AI race (racing dynamics) | THIN | Ch60 defined the term and used it as a premise, with no mechanism | Added game-theory explanation in Ch59 (see 44–47); Ch60 now cross-references it |
| 8 | Automated economy, enfeeblement, gradual disempowerment | COVERED | Ch60 Debate 3 (gradual disempowerment); Ch58 over-reliance | None |
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
| 31 | Bow-tie analysis, FMEA | OUT OF SCOPE | Not present | None: specialist risk worksheets, not terms a general reader meets |
| 32 | Systemic accident models: normal accidents, high-reliability organizations (STAMP) | MISSING | Not present | Added normal accidents (Three Mile Island, Flash Crash) and HROs (Ch56). STAMP left out as too specialized |
| 33 | Drift into failure, normalization of deviance | MISSING | Not present | Added the Challenger example with an AI analogue (Ch56) |
| 34 | Tail events and black swans | MISSING | Not present | Added Tail risk and Black swan, with the lesson for safety plans (Ch56) |
| 35 | Complex systems: emergence and feedback loops (ch. 5) | MISSING | Pieces existed (Ch19 emergence, Ch51 feedback loops) but no systems view | Added Complex system and Emergence definitions, tied to Chs 11, 19, 51 (Ch56). Self-organized criticality left out |
| 36 | Complex-systems lessons for AI safety | MISSING | Not present | Added four lessons: unpredictable wholes, feedback loops, side effects, whole versus parts (Ch56) |
| 37 | Law as a guide for AI behavior (ch. 6) | THIN | Ch56 specs and hard constraints; no discussion of law's limits | Added "Just follow the law" in the machine-ethics subsection (Ch56) |
| 38 | Fairness | COVERED | Ch58 "Bias and fairness", including the impossibility result | None |
| 39 | Economic engine and growth | COVERED | Ch60 Debate 2 | None |
| 40 | Wellbeing and happiness | MISSING | Not present | Added the Wellbeing definition and the three theories (Ch56) |
| 41 | Preferences: stated, revealed, idealized | THIN | Ch56 noted "whose preferences count" | Added the three kinds with a 1 a.m. video example (Ch56) |
| 42 | Social welfare functions | MISSING | Not present | Added a worked example: utilitarian picks A (18 vs 15), maximin picks B, square-root prioritarian picks B (6 vs 6.7) (Ch56) |
| 43 | Normative ethical theories | MISSING | Not present | Added a table plus Consequentialism, Deontology and Virtue ethics definitions (Ch56) |
| 44 | Moral uncertainty, moral parliament | MISSING | Not present | Added, linked to how model specs combine hard constraints and judgment (Ch56) |
| 45 | Game theory, prisoner's dilemma, Nash equilibrium (ch. 7) | MISSING | Nash equilibrium appeared only for games in Ch48 | Added a worked two-lab racing game with a payoff table (Ch59) |
| 46 | Collective action problems | MISSING | Not present | Added as a fifth reason in "Why governing AI is hard" (Ch59) |
| 47 | Mechanisms for cooperation | MISSING | Not present | Added the four ways out (change payoffs, binding commitments, repetition, referee), mapped to governance tools (Ch59) |
| 48 | Conflict and bargaining theory | OUT OF SCOPE | Not present | Named in one sentence on power shifts (Ch59). Commitment-problem detail left out |
| 49 | Evolutionary pressures on AI | MISSING | Not present | Added the definition and Hendrycks's 2023 argument (Ch59) |
| 50 | Economic growth and distribution of gains (ch. 8) | COVERED | Ch60 Debates 1–2 | None |
| 51 | Distribution of power and access; open versus closed | COVERED | Ch60 Debates 3–4 | None |
| 52 | Corporate governance | THIN | Ch60 OpenAI PBC restructuring | Added the 2023 OpenAI board crisis, Anthropic's Long-Term Benefit Trust and other mechanisms (Ch60) |
| 53 | National governance: regulation, liability, standards | COVERED | Ch59 | None |
| 54 | International governance: institutions, verification | THIN | Ch59 summits, report, UN (all soft law) | Added the IAEA, CERN and IPCC models, plus Verification (Ch59) |
| 55 | Compute governance | THIN | Ch59 compute thresholds and export controls; no rationale or term | Added why compute is governable (hard to hide, countable, concentrated supply) and a Compute governance definition (Ch59) |

## Standard 2: BlueDot Impact AI Safety Fundamentals (alignment course)

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
| 21 | Entry into force, phased application, 2026 Omnibus (Ch. XIII) | COVERED | Ch59 timeline, Figure 59.5 | None |

## Summary

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
