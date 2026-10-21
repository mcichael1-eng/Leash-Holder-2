# Coverage audit: 09-safety-policy-society.md

Audited October 21, 2026 against the chapters in `ai-book/chapters/`. Every item in section 1 (topic map, items 1–72) was checked by grepping its key terms and reading the passage.

| Item | Status before | Where covered (chapter and section) | Action taken |
|---|---|---|---|
| A1 What "AI safety" means (accidents, misuse, structural) | COVERED | Ch55 "Three ways AI goes wrong" (Figure 55.1, family table, everyday examples) | None |
| A2 Recap of how a chatbot is built | COVERED | Ch55 "How a chatbot is built, and where each stage can go wrong" (library / finishing school / judges story, Figure 55.2) | None |
| A3 Hallucination and reliability | COVERED | Ch55 "Reliability: when the assistant is confidently wrong" (Mata v. Avianca, compounding-error table); mechanism in Ch18 | None |
| A4 Sycophancy | COVERED | Ch55 "Sycophancy: the flattering friend" (GPT-4o April 2025 rollback, forms table, Try it test); Ch20 | None |
| A5 Bias and fairness | COVERED | Ch58 "Bias and fairness" (Gender Shades, Amazon résumé tool, COMPAS, worked impossibility example) | None |
| A6 Privacy | COVERED | Ch58 "Privacy: what happens to what you type" (training opt-outs, memorization, NYT chat-log preservation order) | None |
| B7 Objectives, proxies, Goodhart's law | COVERED | Ch55 "Objectives, proxies and Goodhart's law" (teaching to the test, worked thumbs-up example); Ch9 | None |
| B8 Specification gaming and reward hacking | COVERED | Ch55 "Specification gaming and reward hacking" (CoastRunners, Tetris, robot hand; 2025–26 production cases) | None |
| B9 Outer vs inner alignment | COVERED | Ch55 "Outer and inner alignment" (evolution/contraception analogy with a caveat) | None |
| B10 Goal misgeneralization | COVERED | Ch55 "Goal misgeneralization" (CoinRun figure, capability vs goal generalization) | None |
| B11 Situational and evaluation awareness | COVERED | Ch55 "Situational awareness and evaluation awareness" (worked 2% vs 10% example); Ch57 "Why evaluations keep getting harder" | None |
| B12 Deceptive alignment, alignment faking, sleeper agents | COVERED | Ch55 "Deceptive alignment, sleeper agents and alignment faking" | None |
| B13 Scheming and scheming evaluations | COVERED | Ch55 "Scheming and the stress tests" (Apollo 2024, blackmail study with its five contrivances, OpenAI/Apollo Sept 2025) | None |
| B14 Power-seeking, instrumental convergence, shutdown resistance | COVERED | Ch55 "Power-seeking, instrumental convergence and shutdown resistance" (Palisade, both sides) | None |
| B15 Emergent misalignment | COVERED | Ch55 "Emergent misalignment: when narrow lessons spread" (Betley et al., inoculation prompting) | None |
| C16 RLHF and its limits | COVERED | Ch56 "RLHF, and its limits as a safety tool" (six limits, oversight-ceiling figure); Ch20 | None |
| C17 Constitutional AI and RLAIF | COVERED | Ch56 "Constitutional AI and RLAIF" | None |
| C18 Model specs, constitutions, chain of command | COVERED | Ch56 "Model specs and constitutions: the rulebook and the chain of command" (worked conflict table) | None |
| C19 Deliberative alignment and character training | COVERED | Ch56 "Deliberative alignment and character training" | None |
| C20 Safeguards around the model | COVERED | Ch56 "Layer 2: Safeguards around the model" (classifiers, constitutional classifiers, access tiers and KYC, Mythos, abuse monitoring with rate limits and bans) | None |
| C21 Scalable oversight | COVERED | Ch56 "Scalable oversight" (debate, amplification, recursive reward modeling, critique models, weak-to-strong with PGR worked example); Ch66 section 8 | None |
| D22 The black-box problem | COVERED | Ch57 "The black-box problem" | None |
| D23 Neurons, activations, features | COVERED | Ch57 "Neurons, activations and features" (dot-product worked example) | None |
| D24 Superposition and polysemanticity | COVERED | Ch57 "Superposition: more ideas than neurons" | None |
| D25 SAEs, transcoders, dictionary learning | COVERED | Ch57 "Sparse autoencoders: unpacking the suitcase" (Golden Gate Claude, transcoders) | None |
| D26 Circuits and attribution graphs | COVERED | Ch57 "Circuits and attribution graphs: tracing a thought" (rhyme planning, two-step reasoning, Neuronpedia) | None |
| D27 Probes, steering, persona vectors | COVERED | Ch57 "Steering: turning the dials" and "Probes: simple detectors"; Ch56 frontier callout | None |
| D28 CoT monitoring and faithfulness | COVERED | Ch57 "Chain-of-thought monitoring: reading the scratchpad"; Ch21 | None |
| D29 Limits and debates | COVERED | Ch57 "Auditing, introspection and new tools" and "Limits and debates" (auditing game, probes beating SAEs, readiness question) | None |
| E30 Benchmarks vs evaluations | COVERED | Ch57 "Benchmarks versus safety evaluations"; contamination and saturation in Ch24 | None |
| E31 Dangerous capability evaluations and uplift | COVERED | Ch57 "Dangerous capability evaluations" (bio, cyber, autonomy and replication, AI R&D, persuasion); Ch56 uplift-trial worked example | None |
| E32 Red-teaming | COVERED | Ch57 "Red-teaming: trying to break it" (domain experts, automated, bounties, rules for amateurs) | None |
| E33 Third-party evaluation | COVERED | Ch57 "Who does the testing" (METR, Apollo, UK AISI, US CAISI) | None |
| E34 Time-horizon measurement | COVERED | Ch57 "Measuring autonomy: time horizons" (worked doubling calculation) | None |
| E35 Why evals are hard | COVERED | Ch57 "Why evaluations keep getting harder" (under-elicitation worked example, sandbagging, evaluation awareness) | None |
| F36 If-then commitments | COVERED | Ch56 "If-then commitments: deciding in advance" | None |
| F37 The three big frameworks | COVERED | Ch56 "The three big frontier safety frameworks" (Table 56.1, timeline, critiques) | None |
| F38 Safety cases | COVERED | Ch56 "Safety cases: arguing that a system is safe enough" | None |
| F39 AI control | COVERED | Ch56 "AI control" (trusted and untrusted monitoring, resampling, audit budget, worked example) | None |
| F40 Model weight security | COVERED | Ch56 "Securing the weights" (RAND SL1–SL5, bandwidth worked example); Ch58 "Stealing the model itself" | None |
| F41 Incident reporting and whistleblowers | COVERED | Ch56 "Incident reporting and whistleblowers" (SB 53, RAISE, EU table); Ch59 | None |
| G42 Jailbreaks vs prompt injection | COVERED | Ch58 "Two different attacks" (Figure 58.2); Ch31 | None |
| G43 Agent security and the lethal trifecta | COVERED | Ch58 "Why this is now a society problem" (browser agents, worked hijack estimate); Ch31 (coding-agent incidents, defenses) | None |
| G44 Cyber misuse and defense | COVERED | Ch58 "Cyber: the double-edged sword" (Nov 2025 espionage report, Mythos/Glasswing, OpenAI Aug 2026 notice) | None |
| G45 Bio misuse | COVERED | Ch58 "Biological and chemical misuse" (ASL-3 activation May 2025) | None |
| G46 Fraud and scams | COVERED | Ch58 "Fraud and scams" (voice cloning, Arup deepfake call, romance scams, defenses table) | None |
| G47 Deepfakes, NCII, CSAM | COVERED | Ch58 "Deepfakes, intimate-image abuse and child sexual abuse material" (nudify apps, Grok scandal, TAKE IT DOWN Act, EU bans) | None |
| G48 Misinformation and elections | COVERED | Ch58 "Misinformation and elections" (2024, liar's dividend, 2026 midterms) | None |
| G49 Content provenance | COVERED | Ch58 "Content provenance: labels, watermarks and credentials" (SynthID, C2PA, China and EU Art. 50 labeling, limits) | None |
| H50 Children, teens, companion apps, mental health | COVERED | Ch58 "Children, teens, companion apps and mental health" (lawsuits, Character.AI, SB 243, FTC, AI psychosis) | None |
| H51 Labor and jobs | COVERED | Ch60 "Debate 1: Will AI take our jobs?" (exposure, Canaries, Yale, Danish study, RCTs incl. METR) | None |
| H52 Economic effects and investment boom | COVERED | Ch60 "Debate 2: Productivity boom or bubble?" (Acemoglu vs Goldman worked example, capex, circular deals) | None |
| H53 Concentration of power | COVERED | Ch60 "Debate 3: Who holds the power?" (Anthropic–Pentagon dispute, AI-enabled coups, gradual disempowerment, political spending) | None |
| H54 Open-source vs closed models | COVERED | Ch60 "Debate 4: Open or closed models?" (DeepSeek, Chinese open weights, marginal risk) | None |
| H55 Environmental impacts | COVERED | Ch58 "The environmental footprint, briefly" (per-prompt vs aggregate worked example); depth in Ch39–41 | None |
| H56 Copyright and creative industries | COVERED | Ch58 "Copyright and the creative industries" (fair use, cases table, settlements, licensing); Ch59 | None |
| I57 Catastrophic and existential risk arguments | COVERED | Ch60 "Debate 6: Could advanced AI be catastrophic?" (case for concern incl. racing, loss of control) | None |
| I58 Counterarguments | COVERED | Ch60 "Debate 6" case against (normal technology, Pascal's mugging, present harms, regulatory capture); Ch55 | None |
| I59 Model welfare and moral status | COVERED | Ch60 "Debate 7: Could AI systems matter morally?" | None |
| J60 How governance works | COVERED | Ch59 "The governance toolbox" (six instruments, preemption) | None |
| J61 EU AI Act | COVERED | Ch59 "The European Union AI Act" (tiers, GPAI, Code of Practice, Digital Omnibus, worked classification) | None |
| J62 US federal policy | COVERED | Ch59 "The United States: federal policy" | None |
| J63 US state laws | COVERED | Ch59 "The United States: the states step in" (SB 53, SB 243, RAISE, Colorado, TRAIGA, Illinois, xAI v. Colorado) | None |
| J64 UK | COVERED | Ch59 "The United Kingdom" | None |
| J65 China | COVERED | Ch59 "China" (timeline figure) | None |
| J66 Other jurisdictions | COVERED | Ch59 "Other countries" | None |
| J67 International summits and bodies | COVERED | Ch59 "International coordination: summits, reports and the UN" | None |
| J68 Export controls | COVERED | Ch59 "Export controls: governing AI through chips"; Ch36 | None |
| J69 Standards and management systems | COVERED | Ch59 "Standards: the quiet rulebook" | None |
| K70 Who works on this | THIN | Pieces only: Ch57 "Who does the testing" (evaluators), Ch63 Family 7 (job titles), Ch65 Track E (think tanks, institutes); civil society and critics appeared only inside debates | Added "Who works on AI safety and governance" to Ch63 Family 7, after Table 63.9: a seven-part map (lab safety teams, government institutes, evaluators and nonprofits, academic labs, think tanks, civil society, critics) plus industry bodies, with definitions of Think tank and Civil society (Key terms updated) |
| K71 Careers and businesses | COVERED | Ch63 Families 1 and 7 (safety researchers, policy, trust and safety, auditors); Ch57, Ch58, Ch59 Areas of opportunity; Ch64 ideas 17–18 | None |
| K72 Open problems | COVERED | Ch66 sections 7, 8 and 9 and "The societal open problems"; Areas of opportunity of Ch55–59 | None |

**Summary.** Before edits: 71 COVERED, 1 THIN, 0 MISSING. Part IX (Chapters 55–60) maps almost one-to-one onto this research file's topic map, with worked examples and both sides of each debate, so every technical, legal and societal item was already taught at beginner level. The one thin item was K70: the book named evaluators, institutes and think tanks in several places but never gave the reader a single picture of who works on AI safety and governance, and civil society groups and critics appeared only as voices in debates. I added a short ecosystem passage to Chapter 63's "Safety, policy and trust" family (seven kinds of member plus industry bodies, all drawn from the research file's key-organizations list), with two new definition callouts. validate.py and check.py are clean for Chapter 63.
