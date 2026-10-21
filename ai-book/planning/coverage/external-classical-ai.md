# External-standard coverage audit: classical AI

Audited October 21, 2026 against `ai-book/chapters/` (66 chapters) and `ai-book/appendices/`. Each topic was searched
for by its key terms across the whole book, and every hit was read in context. COVERED means explained at beginner
level; THIN means mentioned but not explained; MISSING means absent; OUT OF SCOPE means too specialized or
mathematical for this reader (the reason is given in the Action column).

## Standards and how their structure was reconstructed

1. **Russell and Norvig, *Artificial Intelligence: A Modern Approach*, 4th edition (2020).** Topics were first listed
   by chapter from memory of the table of contents, because web search was unavailable during the first pass, and
   were then verified online against the published contents on October 21, 2026 (see "Verified online (October 21,
   2026)" at the end of this file, which lists the corrections and the topics added). Chapter numbers follow the US
   edition: 1 Introduction, 2 Intelligent Agents, 3 Search, 4 Search in Complex Environments, 5 Adversarial Search and
   Games, 6 Constraint Satisfaction Problems [corrected after verification: the first pass had 5 and 6 swapped, which
   is the Global Edition order], 7 Logical Agents, 8 First-Order Logic, 9 Inference in First-Order Logic,
   10 Knowledge Representation, 11 Automated Planning, 12 Quantifying Uncertainty, 13 Probabilistic Reasoning,
   14 Probabilistic Reasoning over Time, 15 Probabilistic Programming, 16 Making Simple Decisions, 17 Making Complex
   Decisions, 18 Multiagent Decision Making, 19 Learning from Examples, 20 Learning Probabilistic Models, 21 Deep
   Learning, 22 Reinforcement Learning, 23 Natural Language Processing, 24 Deep Learning for NLP, 25 Computer Vision,
   26 Robotics, 27 Philosophy, Ethics, and Safety of AI, 28 The Future of AI. **Uncertainty:** the Global Edition
   numbers the later chapters differently and includes a "Knowledge in Learning" chapter (explanation-based learning,
   relevance-based learning, inductive logic programming, carried over from the 3rd edition) while placing
   probabilistic programming online [corrected after verification: the Global Edition prints Probabilistic
   Programming as Chapter 18; it is not online-only]; both are listed below. Rows name topics, not exact section titles.
2. **ACM/IEEE-CS/AAAI Computer Science Curricula 2023 (CS2023), Artificial Intelligence knowledge area.** Listed by
   knowledge unit: AI-Introduction, AI-Search, AI-KRR, AI-ML and AI-SEP (CS Core), then AI-LRR, AI-Probability,
   AI-Planning, AI-Agents, AI-NLP, AI-Robo and AI-Vision (KA Core) [corrected after verification: these seven units
   are Non-core, with no CS Core or KA Core hours, and AI-Robo is named AI-Robotics]. **Uncertainty (first pass):** the
   unit names are as I recall them; the topic rows inside each unit summarize what the unit is known to cover rather
   than quoting its bullet list word for word. The lists were reconstructed this way and then verified online against
   the final CS2023 report on October 21, 2026; corrected rows are marked in the table and new rows are in the
   verification section at the end.

Topics already treated at length in the dedicated chapters (deep learning, LLMs, safety, law) are kept at one row
each, since earlier audits checked them in detail.

## Standard 1: Russell and Norvig, AIMA 4th edition

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| **Part I** | | | |
| Ch 1. What is AI: the four approaches (thinking/acting, humanly/rationally) | THIN | Ch 1 "What is AI?" (goal definition only); Turing test in Ch 7 | Added a 2x2 table, the rational-agent view and a Rational agent definition to Ch 1 "What is AI?" |
| Ch 1. Foundations of AI (philosophy, mathematics, economics, neuroscience, psychology, control theory, linguistics) | THIN | Scattered: Ch 7 history, Ch 54 brains, Ch 6 math | Added a one-paragraph map of the source disciplines to Ch 1 |
| Ch 1. History of AI | COVERED | Ch 7 (all eras); Appendix C | None |
| Ch 1. State of the art | COVERED | Ch 7 Eras 9-10; Ch 24 | None |
| Ch 1. Risks and benefits of AI | COVERED | Part IX (Ch 55-60) | None |
| Ch 2. Agents and environments; PEAS task description | MISSING | "Agent" defined (Ch 1, Ch 48) but not the agent-environment framing or PEAS | Added Ch 48 "What kind of world is the agent in?" with PEAS worked for a robot vacuum |
| Ch 2. Rationality and performance measures | THIN | Ch 8 mentions performance measures for learning | Rational agent defined in Ch 1 and Ch 48 |
| Ch 2. Properties of task environments (observable, deterministic, episodic, static, discrete, multiagent) | THIN | Ch 48 Figure on hidden information vs number of players only | Added Table 48.1 and three definitions (observable, deterministic/stochastic, episodic/sequential) |
| Ch 2. Agent structures (simple reflex, model-based, goal-based, utility-based, learning) | MISSING | None | Added the agent ladder with four definitions and everyday examples in Ch 48 |
| Ch 2. Atomic, factored and structured representations | OUT OF SCOPE | Implicit in CSPs and planning | None (technical vocabulary; the ideas appear in the new CSP and planning sections) [Re-audited after verification: CS2023 AI-Search lists "factoring states into representations" in its CS Core, so factored representation was added to Ch 48 "States, actions and goals" with a definition; now COVERED] |
| **Part II** | | | |
| Ch 3. Problem formulation: states, actions, goals, state space | COVERED | Ch 48 "States, actions and goals" | None |
| Ch 3. Breadth-first and depth-first search | COVERED | Ch 48 "Blind search" | None |
| Ch 3. Uniform-cost search (Dijkstra) | MISSING | Only a resource link in Ch 48 Going deeper | Added explanation and definition to Ch 48 "Blind search" |
| Ch 3. Depth-limited search and iterative deepening | MISSING | None | Added explanation and definition to Ch 48 |
| Ch 3. Bidirectional search | OUT OF SCOPE | None | None (a refinement the reader does not need) [Re-audited after verification: CS2023 lists bidirectional search in the AI-Search KA Core, so it was added to Ch 48 "Blind search" with a worked count and a definition; now COVERED] |
| Ch 3. Greedy best-first search | MISSING | None | Added to Ch 48 A* section with definition |
| Ch 3. A* search and admissible heuristics | COVERED | Ch 48 A* worked on a grid | None |
| Ch 3. Designing heuristics (relaxed problems, pattern databases, learned heuristics) | THIN | Manhattan distance only | Added relaxed-problem heuristics in the Ch 48 planning section (Manhattan distance as a relaxed maze); pattern databases left out |
| Ch 4. Local search: hill climbing, local maxima, random restarts | MISSING | Gradient descent in Ch 6 only | Added Ch 48 "Local search" with a worked trail example |
| Ch 4. Simulated annealing | MISSING | None | Added to Ch 48 with definition |
| Ch 4. Local beam search | MISSING | None anywhere in the book | Added beam search to Ch 48 (with translation decoding link to Ch 18) |
| Ch 4. Evolutionary algorithms | COVERED | Ch 54 "Evolution as an algorithm" (one generation by hand) | None |
| Ch 4. Optimization in continuous spaces | COVERED | Ch 6 gradients and gradient descent | None |
| Ch 4. Nondeterministic actions (AND-OR search, contingency plans) | OUT OF SCOPE | None | None (replanning is named in the new Ch 48 planning section) |
| Ch 4. Partially observable search and belief states | MISSING | None | Belief state defined in the new Ch 48 MDP section |
| Ch 4. Online search in unknown environments | OUT OF SCOPE | Exploration covered under RL in Ch 48 | None |
| Ch 6 [corrected: was Ch 5]. Defining CSPs (variables, domains, constraints) | MISSING | None | Added Ch 48 "Constraint satisfaction" with a meeting-schedule example solved by hand |
| Ch 6 [corrected: was Ch 5]. Constraint propagation | MISSING | None | Added with definition |
| Ch 6 [corrected: was Ch 5]. Backtracking search and variable ordering (most-constrained first) | MISSING | None | Added with definition and worked steps |
| Ch 6 [corrected: was Ch 5]. Local search for CSPs (min-conflicts) | MISSING | None | Added one sentence in the CSP section |
| Ch 6 [corrected: was Ch 5]. Problem structure (tree-structured CSPs, decomposition) | OUT OF SCOPE | None | None |
| Ch 5 [corrected: was Ch 6]. Two-player zero-sum games | COVERED | Ch 48 zero-sum game definition, game trees | None |
| Ch 5 [corrected: was Ch 6]. Minimax | COVERED | Ch 48 minimax worked on tic-tac-toe | None |
| Ch 5 [corrected: was Ch 6]. Alpha-beta pruning | COVERED | Ch 48 | None |
| Ch 5 [corrected: was Ch 6]. Evaluation functions and cutoff search | COVERED | Ch 48 (Deep Blue, Stockfish) | None |
| Ch 5 [corrected: was Ch 6]. Monte Carlo tree search | COVERED | Ch 48 (UCB worked) | None |
| Ch 5 [corrected: was Ch 6]. Stochastic games (expectiminimax) | THIN | Backgammon named, method absent | Added Ch 48 "Games with dice: chance nodes" with a worked dice example |
| Ch 5 [corrected: was Ch 6]. Partially observable games (card games) | COVERED | Ch 48 poker, imperfect information, CFR | None |
| Ch 5 [corrected: was Ch 6]. Limitations of game search | COVERED | Ch 48 Watch out on narrowness and adversarial Go strategies | None |
| **Part III** | | | |
| Ch 7. Knowledge-based agents | COVERED | Ch 54 knowledge base and inference engine | None |
| Ch 7. Propositional logic and entailment | MISSING | None | Added Ch 54 "Logic: the mathematics underneath the rules" with a worked truth-table example |
| Ch 7. Inference rules and resolution | MISSING | None | Added resolution worked step by step, with definition |
| Ch 7. Horn clauses, forward and backward chaining | COVERED | Ch 54 expert system worked by hand (forward and backward chaining) | None (Horn clauses not named; not needed) |
| Ch 7. Propositional model checking (DPLL, WalkSAT, SAT) | MISSING | None | Added SAT solvers with real uses (chip verification, package managers, scheduling); DPLL/WalkSAT not named |
| Ch 7. The wumpus world | OUT OF SCOPE | None | None (a textbook teaching device) |
| Ch 8. First-order logic (objects, relations, quantifiers) | MISSING | None | Added with an insurance example and definition |
| Ch 8. Knowledge engineering | COVERED | Ch 54 knowledge engineers, knowledge-acquisition bottleneck | None |
| Ch 9. Unification and lifted inference | OUT OF SCOPE | None | None |
| Ch 9. Logic programming (Prolog) | THIN | Prolog only in Appendix C | Added Prolog with definition |
| Ch 9. Resolution theorem provers | THIN | Lean and formal proofs in Ch 54 neuro-symbolic | Covered by the new resolution passage |
| Ch 10. Ontological engineering and ontologies | COVERED | Ch 54 Ontology, Wikidata, Google Knowledge Graph | None |
| Ch 10. Categories, inheritance, semantic networks and description logics | MISSING | None | Added Ch 54 "Ancestors, defaults and the frame problem" (semantic networks, inheritance, OWL/description logics) |
| Ch 10. Frames [not a heading in the published contents; 10.5 lists semantic networks and description logics] | MISSING | None | Added Minsky's frames with definition |
| Ch 10. Events, situation calculus and the frame problem [published heading: 10.3 Events, with Time and Fluents; situation calculus is not a heading] | MISSING | None | Added the frame problem; situation calculus left out |
| Ch 10. Mental objects and modal logic | OUT OF SCOPE | None | None |
| Ch 10. Default (non-monotonic) reasoning; truth maintenance | MISSING | None | Added default reasoning (the penguin example); truth maintenance left out |
| Ch 11. Classical planning representation (STRIPS, PDDL, preconditions and effects) | MISSING | Shakey named in Ch 7 and Ch 48; STRIPS absent | Added Ch 48 "Planning with actions: from Shakey to PDDL" with a worked tea-making domain (Table 48.3) |
| Ch 11. Planning algorithms (forward and backward state-space search) | MISSING | None | Backward search worked in the tea example; forward search described |
| Ch 11. Planning heuristics (relaxation, ignoring delete effects) | MISSING | None | Added |
| Ch 11. Hierarchical planning (HTN) | MISSING | None | Added with definition |
| Ch 11. Partial-order planning [not a heading; falls under 11.2.4 Other classical planning approaches] | MISSING | None | Named and explained in the tea example |
| Ch 11. Planning and acting in nondeterministic domains (monitoring, replanning) | THIN | Ch 28 agents revise plans | Added execution monitoring and replanning, linked to Ch 28 agents |
| Ch 11. Time, schedules and resources | THIN | Scheduling uses mentioned in Ch 54 | Added (scheduling as a constraint problem; NASA Remote Agent) |
| **Part IV** | | | |
| Ch 12. Acting under uncertainty; probability basics | COVERED | Ch 6 probability rules | None |
| Ch 12. Full joint distributions and inference by enumeration | THIN | Implicit in Ch 54 "The compression" | Added Full joint distribution definition in Ch 54 |
| Ch 12. Independence | COVERED | Ch 6 | None |
| Ch 12. Bayes' rule | COVERED | Ch 6 medical test with natural frequencies | None |
| Ch 12. Naive Bayes | COVERED | Ch 10 spam filter worked | None |
| Ch 13. Bayesian networks and conditional probability tables | COVERED | Ch 54 worked network, explaining away | None |
| Ch 13. Conditional independence (semantics of networks) | THIN | Implicit | Added definition with the two-neighbors example in Ch 54 |
| Ch 13. Exact inference | COVERED | Ch 54 natural-frequency enumeration | None (variable elimination not named) |
| Ch 13. Approximate inference by sampling (MCMC, Gibbs) | MISSING | None | Added sampling estimate of the wet-grass answer and MCMC definition in Ch 54 |
| Ch 13. Causal networks | COVERED | Ch 54 causality, do-notation, ladder of causation | None |
| Ch 14. Time and uncertainty; Markov chains and the Markov assumption | MISSING | None | Added Ch 54 "Reasoning over time" (Markov chain) and Markov property in Ch 48 |
| Ch 14. Filtering, prediction, smoothing, most likely sequence (Viterbi) | MISSING | None | Added the worked umbrella-detective filter over two days; smoothing and Viterbi named |
| Ch 14. Hidden Markov models | THIN | Defined in Ch 46 speech history only | Added HMM in Ch 54 with the worked example |
| Ch 14. Kalman filters | MISSING | None | Added with definition (GPS, Apollo) |
| Ch 14. Dynamic Bayesian networks and particle filtering | MISSING | None | Added particle filter (robot localization); DBN described, not named |
| Ch 15 (US ed.; Ch 18 in the Global ed.). Probabilistic programming | THIN | Named once in Ch 54 | Added definition (Stan, PyMC) |
| Ch 15 (US ed.; Ch 18 in the Global ed.). Relational and open-universe probability models | OUT OF SCOPE | None | None |
| Ch 16. Utility theory and the maximum expected utility principle | MISSING | Only expected value (Ch 6) | Added Ch 48 "Deciding when you are not sure" with a worked umbrella decision |
| Ch 16. Utility of money and risk aversion | MISSING | None | Added with definition |
| Ch 16. Human judgment and irrationality | OUT OF SCOPE | Kahneman's System 1 and 2 in Ch 54 | None |
| Ch 16. Multiattribute utility; decision networks | OUT OF SCOPE | None | None |
| Ch 16. Value of information | MISSING | None | Added worked example (94 vs 80) and definition |
| Ch 16. Unknown preferences and deference to humans | COVERED | Ch 55 shutdown resistance, Ch 56 oversight | None |
| Ch 17. Sequential decision problems and MDPs | THIN | Bellman equation defined; MDP never named | Added Ch 48 "Markov decision processes" with MDP and Markov property definitions |
| Ch 17. Value iteration and policy iteration | MISSING | None | Added value iteration worked on the corridor world (three sweeps), policy iteration named |
| Ch 17. Bandit problems | COVERED | Ch 48 multi-armed bandit, epsilon-greedy, UCB | None |
| Ch 17. Partially observable MDPs | MISSING | None | Added POMDP and belief state definitions |
| Ch 18. Properties of multiagent environments | COVERED | Ch 28 multi-agent systems; Ch 48 multiplayer games | None |
| Ch 18. Non-cooperative game theory (dominant strategies, Nash equilibrium, prisoner's dilemma) | THIN | Nash equilibrium in Ch 48 poker only | Added Ch 48 "A short course in game theory" with a worked prisoner's dilemma (Table 48.8) |
| Ch 18. Mixed strategies and repeated games | MISSING | None | Added (rock-paper-scissors; Axelrod's tit-for-tat) |
| Ch 18. Cooperative game theory (Shapley value) | MISSING | None | Added with a worked two-player split and the link to SHAP explanations |
| Ch 18. Auctions | COVERED | Ch 51 second-price and first-price ad auctions | None |
| Ch 18. Mechanism design [not a heading; the published section is 18.4 Making Collective Decisions: contract net, auctions, voting, bargaining] | MISSING | None | Added with the truthful second-price auction |
| Ch 18. Voting, bargaining, contract net | OUT OF SCOPE | None | None (mechanism design definition mentions voting systems) |
| **Part V** | | | |
| Ch 19. Forms of learning; supervised learning | COVERED | Ch 8 | None |
| Ch 19. Decision trees | COVERED | Ch 10 (Gini worked) | None |
| Ch 19. Model selection, cross-validation, regularization | COVERED | Ch 9 | None |
| Ch 19. Learning theory (PAC learning, VC dimension) [published: 19.5 The Theory of Learning with a PAC example; VC dimension is not a heading] | OUT OF SCOPE | Bias-variance intuition in Ch 9 | None (mathematical; not a term this reader will meet) |
| Ch 19. Linear and logistic regression, perceptron | COVERED | Ch 8, Ch 10 | None |
| Ch 19. Nonparametric models (kNN, SVMs, kernels) | COVERED | Ch 10 | None |
| Ch 19. Ensembles (bagging, random forests, boosting) | COVERED | Ch 10 | None |
| Ch 19. Developing machine learning systems | COVERED | Ch 10 lifecycle and MLOps; Ch 11 | None |
| Global ed. Ch 20 [corrected: chapter number confirmed]. Knowledge in learning (published sections: a logical formulation of learning, knowledge in learning, explanation-based learning, learning using relevance information, inductive logic programming) | OUT OF SCOPE | None | None (research niche; the reader will not meet these terms) |
| Ch 20. Maximum likelihood estimation | MISSING | None when this audit began | Added to Ch 6 by a parallel audit during this round; no action needed |
| Ch 20. Bayesian parameter learning (priors and posteriors) | COVERED | Ch 6 prior and posterior; Ch 10 Laplace smoothing | None |
| Ch 23 [corrected: was Ch 20; the published section is 23.1.4 Smoothing n-gram models]. Smoothing of count estimates | THIN | Ch 10 Laplace smoothing for naive Bayes only | Added add-one smoothing worked on the Ch 6 n-gram model, with definition |
| Ch 20. Bayesian network structure learning; density estimation | OUT OF SCOPE | None | None |
| Ch 20. EM algorithm and mixtures of Gaussians | MISSING | None when this audit began | Added to Ch 10 by a parallel audit during this round; no action needed |
| Ch 21. Feedforward networks, computation graphs, backpropagation | COVERED | Ch 12, Ch 13; Ch 6 chain rule | None |
| Ch 21. Convolutional networks | COVERED | Ch 14 | None |
| Ch 21. Learning algorithms and generalization | COVERED | Ch 13 | None |
| Ch 21. Recurrent networks | COVERED | Ch 14 | None |
| Ch 21. Unsupervised and transfer learning | COVERED | Ch 14 transfer learning; Ch 16 | None |
| Ch 22. Learning from rewards | COVERED | Ch 48 | None |
| Ch 22. Passive RL (TD learning; direct estimation, adaptive dynamic programming) | COVERED | Ch 48 TD learning and Q-learning worked | None (direct estimation and ADP not named) |
| Ch 22. Active RL: exploration and Q-learning | COVERED | Ch 48 | None |
| Ch 22. Safe exploration | COVERED | Ch 48 Watch out and At the frontier | None |
| Ch 22. Function approximation and deep RL | COVERED | Ch 48 DQN | None |
| Ch 22. Policy search | COVERED | Ch 48 policy gradients, actor-critic, PPO | None |
| Ch 22. Apprenticeship learning and inverse RL | MISSING | Imitation learning only in Ch 49 and Ch 50 | Added imitation learning and inverse RL to Ch 48, linked to reward models in Ch 20 |
| Ch 22. Applications of RL | COVERED | Ch 48 "Reinforcement learning leaves the arcade"; Ch 20-21 | None |
| **Part VI** | | | |
| Ch 23. N-gram language models | COVERED | Ch 6 counting model | None |
| Ch 23. Bag-of-words models | THIN | Ch 10 naive Bayes counts words without naming the idea | Added bag of words to Ch 10 with definition |
| Ch 23. Part-of-speech tagging | MISSING | None | Added Ch 54 "Grammar, parsing and ambiguity" |
| Ch 23. Grammars (context-free, probabilistic) | MISSING | None | Added formal grammar definition; probabilistic grammars and treebanks described |
| Ch 23. Parsing (constituency and dependency) | MISSING | None | Added two parse trees as an ASCII figure (Figure 54.11) and dependency parsing |
| Ch 23. Augmented grammars and semantic interpretation | OUT OF SCOPE | None | None |
| Ch 23. Complications of real language (ambiguity) | THIN | "Ambiguity" mentioned in passing | Added definition and the telescope example |
| Ch 23. Natural language tasks | COVERED | Ch 54 classic NLP tasks table, machine translation, BLEU | None |
| Ch 24. Word embeddings | COVERED | Ch 14 | None |
| Ch 24. RNNs, sequence-to-sequence models and attention | COVERED | Ch 14 | None |
| Ch 24. The Transformer | COVERED | Ch 15 | None |
| Ch 24. Pretraining and transfer (masked and causal language models) | COVERED | Ch 7, Ch 15, Ch 19 | None |
| Ch 24. State of the art | COVERED | Part IV | None |
| Ch 25. Image formation (cameras, lenses, light) | OUT OF SCOPE | Ch 3 images as pixels | None (optics; the book needs only pixels) |
| Ch 25. Simple features: edges | COVERED | Ch 14 edge filter worked by hand | None |
| Ch 25. Texture | OUT OF SCOPE | None | None |
| Ch 25. Optical flow | MISSING | None | Added to Ch 45 tracking section with definition |
| Ch 25. Segmentation | COVERED | Ch 45 | None |
| Ch 25. Image classification and object detection | COVERED | Ch 45, Ch 14 | None |
| Ch 25. The 3D world (stereo, depth, motion) | COVERED | Ch 45 "Seeing in 3D" | None |
| Ch 25. Using vision (activity recognition, captioning, reconstruction, generation) | COVERED | Ch 45, Ch 22, Ch 47 | None |
| Ch 26. Robot hardware (sensors, actuators) | COVERED | Ch 49 sense-plan-act | None |
| Ch 26. What robotics solves; sense-plan-act | COVERED | Ch 49 | None |
| Ch 26. Localization and mapping (Monte Carlo localization, SLAM) | COVERED | Ch 45 SLAM; Ch 50 localization | Particle-filter localization added in Ch 54 |
| Ch 26. Configuration space and motion planning (RRT, roadmaps) | MISSING | "Motion planning" defined for cars in Ch 50 only | Added Ch 49 "From go there to motor commands" (configuration space, RRT) |
| Ch 26. Forward and inverse kinematics [not a separate heading; sits inside 26.5 Planning and Control; CS2023 AI-Robotics lists it explicitly] | MISSING | None | Added with definition |
| Ch 26. Trajectory-tracking control (PID) | MISSING | "Controller" defined without any method | Added PID with a worked example |
| Ch 26. Planning uncertain movements | OUT OF SCOPE | None | None |
| Ch 26. Reinforcement learning in robotics | COVERED | Ch 49 learning to walk, sim-to-real | None |
| Ch 26. Humans and robots | COVERED | Ch 49 safety, teleoperation, learning from demonstrations | None |
| Ch 26. Alternative frameworks (reactive control, subsumption) | MISSING | None | Added Brooks's subsumption architecture and the Roomba link |
| Ch 26. Application domains | COVERED | Ch 49, Ch 50, Ch 53 | None |
| **Part VII** | | | |
| Ch 27. Limits of AI: argument from informality (Dreyfus) | MISSING | None | Added to Ch 60 "The classic arguments about machine minds" |
| Ch 27. Argument from disability (Lady Lovelace's objection) | COVERED | Ch 7 | None |
| Ch 27. The mathematical objection (Godel, Lucas, Penrose) | MISSING | None | Added with Godel's theorem definition and the standard reply |
| Ch 27. Measuring AI: the Turing test | COVERED | Ch 7 | None |
| Ch 27. Can machines really think? Chinese room, strong vs weak AI | THIN | Appendix C timeline row only | Added the Chinese room, the systems reply and strong/weak AI definitions to Ch 60 |
| Ch 27. Consciousness and qualia | COVERED | Ch 60 Debate 7 | None |
| Ch 27. Lethal autonomous weapons | COVERED | Ch 53 military and defense | None |
| Ch 27. Surveillance, security and privacy | COVERED | Ch 45 faces; Ch 58 privacy | None |
| Ch 27. Fairness and bias | COVERED | Ch 58 | None |
| Ch 27. Trust and transparency | COVERED | Ch 57; Ch 53 explainability | None |
| Ch 27. The future of work | COVERED | Ch 60 Debate 1 | None |
| Ch 27. Robot rights and moral status | COVERED | Ch 60 Debate 7 (model welfare) | None |
| Ch 27. AI safety | COVERED | Ch 55-57 | None |
| Ch 28. AI components (perception, representation, learning, reasoning) and their open problems | COVERED | Ch 66 technical open problems | None |
| Ch 28. AI architectures (hybrid, neuro-symbolic, general-purpose) | COVERED | Ch 66; Ch 54 neuro-symbolic; Ch 17 | None |

## Standard 2: CS2023 Artificial Intelligence knowledge area

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| **AI-Introduction: Fundamental Issues (CS Core)** | | | |
| Overview of AI problems and successful applications | COVERED | Ch 1; Part VIII | None |
| Definitions of agents, reactive vs deliberative | THIN | Ch 1, Ch 28 (LLM agents) | Added the agent ladder in Ch 48 |
| What is intelligent behavior: the Turing test and its flaws | COVERED | Ch 7 | None |
| Rational vs human-like behavior | THIN | Implicit | Added the four approaches and rational agent to Ch 1 |
| Problem characteristics: observability, determinism, static/dynamic, discrete/continuous, single/multiagent | MISSING | None | Added Table 48.1 |
| Autonomy levels: autonomous, semi-autonomous, human in the loop | COVERED | Ch 28 humans in the loop; Ch 50 SAE levels | None |
| Philosophical issues [published as a Non-core item] | THIN | Ch 60 Debate 7 (consciousness) | Added classic arguments to Ch 60 |
| Symbolic vs sub-symbolic; rules vs learning [not an AI-Introduction item; the preamble and AI-KRR item 1 (types of representations) cover it, so it duplicates the AI-KRR row; excluded from the verified count] | COVERED | Ch 1 three ways; Ch 54 five tribes | None |
| History of AI [published as a Non-core item] | COVERED | Ch 7 | None |
| **AI-Search: Search (CS Core and KA Core)** | | | |
| State spaces and problem formulation | COVERED | Ch 48 | None |
| Uninformed search (BFS, DFS, iterative deepening, uniform cost) | THIN | BFS and DFS only | Added uniform-cost and iterative deepening |
| Heuristic search (greedy best-first, A*, admissibility) | THIN | A* only | Added greedy best-first |
| Space and time efficiency of search | COVERED | Ch 7 combinatorial explosion; Ch 48 BFS vs A* counts | None |
| Local search (hill climbing, simulated annealing, beam search) [tiers differ: hill climbing CS Core, beam search KA Core, local search and simulated annealing Non-core] | MISSING | None | Added Ch 48 local search |
| Population-based search (genetic algorithms) [Non-core item 17b] | COVERED | Ch 54 | None |
| Constraint satisfaction (backtracking, propagation, local search) | MISSING | None | Added Ch 48 CSP section |
| Two-player games: minimax and alpha-beta | COVERED | Ch 48 | None |
| Games with chance (expectimax) [Non-core item 16] | THIN | Backgammon named only | Added chance nodes |
| Monte Carlo tree search | COVERED | Ch 48 | None |
| **AI-KRR: Fundamental Knowledge Representation and Reasoning (CS Core)** | | | |
| Types of representation: symbolic, logical, probabilistic, neural | COVERED | Ch 1; Ch 54 | None |
| Propositional and predicate (first-order) logic [published under AI-LRR item 1, Non-core, not AI-KRR] | MISSING | None | Added Ch 54 logic section |
| Resolution and theorem proving [published under AI-LRR item 2, propositional only] | MISSING | None | Added |
| Forward and backward chaining [published under AI-LRR item 2a] | COVERED | Ch 54 | None |
| Ontologies, semantic networks, knowledge graphs [published under AI-LRR items 3b (ontology engineering) and 11 (semantic networks); knowledge graphs are not named] | THIN | Knowledge graphs and ontologies only | Added semantic networks and frames |
| Probability review, Bayes' theorem, Bayesian inference | COVERED | Ch 6 | None |
| Random variables, joint distributions, conditional independence | THIN | Ch 6 independence only | Added full joint distribution and conditional independence |
| Decision-theoretic agents: utility and expected utility [published as AI-KRR KA Core item 8, Utility and decision making] | MISSING | None | Added Ch 48 expected utility |
| Value of information [not in the published list; excluded from the verified count] | MISSING | None | Added |
| **AI-ML: Machine Learning (CS Core and KA Core)** | | | |
| Definitions and examples: classification, regression, clustering | COVERED | Ch 8, Ch 10 | None |
| Supervised learning: features, labels, training and test data | COVERED | Ch 8, Ch 9 | None |
| Linear and logistic regression, decision trees, naive Bayes, kNN | COVERED | Ch 8, Ch 10 | None |
| Overfitting, regularization, cross-validation, evaluation metrics | COVERED | Ch 9 | None |
| Unsupervised learning: k-means, hierarchical clustering, dimensionality reduction [published: clustering (CS Core) and k-means (Non-core); hierarchical clustering and dimensionality reduction are not named] | COVERED | Ch 10 | None |
| EM and Gaussian mixtures [Non-core item 24] | MISSING | None when this audit began | Added to Ch 10 by a parallel audit; no action needed |
| Ensembles | COVERED | Ch 10 | None |
| Neural networks and deep learning (backpropagation, CNNs, RNNs, Transformers) | COVERED | Part III | None |
| Generative models | COVERED | Ch 16 | None |
| Reinforcement learning: MDPs, value and policy iteration, Q-learning, policy gradients [Non-core item 30; the KA Core lists only an overview] | THIN | Q-learning and policy gradients only | Added MDPs, value iteration, POMDPs |
| Explainability (feature importance, SHAP) [published names LIME and Shapley values; LIME added on verification, see new rows] | THIN | Ch 10 feature importance; Ch 53, Ch 57 | Added Shapley value and SHAP |
| Fairness, bias and privacy in ML | COVERED | Ch 11, Ch 58 | None |
| Data collection and preparation | COVERED | Ch 11 | None |
| **AI-SEP: Applications and Societal Impact (CS Core)** | | | |
| Societal and economic impact | COVERED | Ch 60 | None |
| Ethics and fairness | COVERED | Ch 58 | None |
| Privacy and surveillance | COVERED | Ch 45, Ch 58 | None |
| Safety, robustness and alignment [not in the published list; excluded from the verified count] | COVERED | Ch 55-57 | None |
| Misinformation and deepfakes [not an AI-SEP item; the preamble mentions fake photos and videos; excluded from the verified count] | COVERED | Ch 58 | None |
| Environmental impact | COVERED | Part VII; Ch 58 | None |
| Law, regulation and governance | COVERED | Ch 59 | None |
| Dual use and military applications [not an AI-SEP item; autonomous weapons are AI-Robotics item 15d, counted in the new rows; excluded from the verified count] | COVERED | Ch 53, Ch 58 | None |
| Accountability and transparency [published as trust/explainability and human autonomy, oversight, regulations and legal requirements] | COVERED | Ch 57, Ch 59 | None |
| **AI-LRR: Logical Representation and Reasoning (Non-core) [corrected: was KA Core]** | | | |
| Non-monotonic and default reasoning | MISSING | None | Added Ch 54 |
| Argumentation | OUT OF SCOPE | None | None |
| Reasoning about action and change (situation calculus, frame problem) [published: situation and event calculus] | MISSING | None | Added the frame problem; situation calculus left out |
| Temporal and spatial reasoning (formal calculi) | OUT OF SCOPE | None | None |
| Rule-based expert systems | COVERED | Ch 54 | None |
| Semantic networks, frames, description logics [frames are not named in the published list] | MISSING | None | Added Ch 54 |
| Model-based and case-based reasoning | THIN | Ch 54 analogizers | Added case-based reasoning definition |
| Logic programming (Prolog) and answer set programming | THIN | Prolog in Appendix C only | Added Prolog; answer set programming left out |
| SAT and SMT solvers [not in the published list; excluded from the verified count] | MISSING | None | Added SAT solvers |
| **AI-Probability: Probabilistic Representation and Reasoning (Non-core) [corrected: was KA Core]** | | | |
| Bayesian networks | COVERED | Ch 54 | None |
| Exact inference | COVERED | Ch 54 enumeration with natural frequencies | None |
| Approximate inference (sampling, MCMC) | MISSING | None | Added |
| Markov networks (undirected models) | OUT OF SCOPE | None | None |
| Probabilistic programming and relational models [corrected: the published item 2c is relational probability models only; consistent with the AIMA row this is OUT OF SCOPE; the probabilistic programming definition added earlier stays] | THIN | Named once | Added probabilistic programming definition |
| Temporal models: Markov chains and HMMs [published: HMMs here; Markov chains are AI-KRR KA Core item 7, counted in the new rows] | THIN | HMM in Ch 46 only | Added Ch 54 reasoning over time |
| Filtering: Kalman and particle filters [not in the published list; excluded from the verified count] | MISSING | None | Added |
| Decision networks / influence diagrams [not in the published list; the unit lists Decision Theory instead (new rows); excluded from the verified count] | OUT OF SCOPE | None | None |
| **AI-Planning: Planning (Non-core) [corrected: was KA Core]** | | | |
| Planning representations (STRIPS, PDDL) | MISSING | None | Added Ch 48 planning section |
| State-space planning and planning heuristics [published: total order planning; heuristics are not named] | MISSING | None | Added |
| Partial-order planning | MISSING | None | Added |
| Planning graphs (GraphPlan) and planning as SAT [published: plan graphs and GraphPlan; planning as SAT is not named] | OUT OF SCOPE | None | None |
| Hierarchical planning | MISSING | None | Added |
| Plan execution, monitoring and replanning | THIN | Ch 28 agents revise plans | Added |
| Scheduling with time and resources [not in the published list; excluded from the verified count] | THIN | Uses named only | Added |
| Probabilistic planning: MDPs and POMDPs [published: MDP-based planning and probabilistic planning; POMDPs are not named] | MISSING | None | Added Ch 48 |
| Multi-agent planning | OUT OF SCOPE | None | None |
| Planning with language models [not in the published list; excluded from the verified count] | COVERED | Ch 28 planning; Ch 21 | None |
| **AI-Agents: Agents and Cognitive Systems (Non-core) [corrected: was KA Core]** | | | |
| Agent architectures (reactive, deliberative, layered) | THIN | Ch 49 layered control loops | Added agent ladder (Ch 48) and subsumption (Ch 49) |
| Belief-desire-intention (BDI) agents [not an AI-Agents item; "beliefs, desires, and intentions" appears under AI-NLP item 3d, counted in the new rows; excluded from the verified count] | OUT OF SCOPE | None | None |
| Cognitive architectures (Soar, ACT-R) | MISSING | None | Added to Ch 28 memory section |
| Multi-agent systems: coordination and communication | COVERED | Ch 28 multi-agent systems, A2A | None |
| Game theory and Nash equilibria [published: Rationality, Game Theory (decision-theoretic agents, MDPs, bandit algorithms)] | THIN | Nash equilibrium only | Added game theory section |
| Mechanism design, auctions, voting [published: competitive agents (auctions, voting); mechanism design is not named] | THIN | Auctions in Ch 51 | Added mechanism design |
| LLM-based agents and tool use [corrected: the published item 4 is software agents, personal assistants and information access (collaborative and information-gathering agents)] | COVERED | Ch 28, Ch 29 | None |
| Human-agent interaction | COVERED | Ch 28 humans in the loop; Ch 31 product design | None |
| **AI-NLP: Natural Language Processing (Non-core) [corrected: was KA Core]** | | | |
| Deterministic and stochastic grammars; parsing | MISSING | None | Added Ch 54 grammar and parsing |
| Representing meaning | COVERED | Ch 14 embeddings; Ch 54 knowledge graphs | None |
| N-gram models and smoothing | THIN | N-grams in Ch 6; smoothing only in Ch 10 | Added n-gram smoothing to Ch 6 |
| Part-of-speech tagging and morphology | MISSING | None | Added POS tagging; morphology left out [Verified online: morphology is part of the published item 7, so it was added to Ch 54 with stemming and lemmatization on October 21] |
| Information retrieval (vector space, TF-IDF, BM25, precision and recall) [BM25 is not named] | COVERED | Ch 27, Ch 9 | None |
| Information extraction and named entities | COVERED | Ch 54 | None |
| Machine translation | COVERED | Ch 54 | None |
| Text classification and sentiment | COVERED | Ch 54, Ch 10 | None |
| Word embeddings, Transformers and large language models | COVERED | Ch 14, Ch 15, Part IV | None |
| Evaluation (BLEU, perplexity) [not in the published list; excluded from the verified count] | COVERED | Ch 54, Ch 6 | None |
| **AI-Robotics: Robotics (Non-core) [corrected: was "AI-Robo", KA Core]** | | | |
| Sensors and actuators | COVERED | Ch 49 | None |
| Configuration space and motion planning | MISSING | None | Added Ch 49 |
| Kinematics | MISSING | None | Added Ch 49 |
| Localization and mapping | COVERED | Ch 45, Ch 50 | Filters added in Ch 54 |
| Navigation and control (PID) [PID is not named] | THIN | Controller defined without method | Added PID |
| Robot learning (RL, imitation, foundation models) [not in the published list; excluded from the verified count] | COVERED | Ch 49 | None |
| Multi-robot systems [published: multiple-robot coordination and collaboration] | OUT OF SCOPE | None | None |
| Human-robot interaction, safety and ethics | COVERED | Ch 49 | None |
| **AI-Vision: Perception and Computer Vision (Non-core) [corrected: was KA Core]** | | | |
| Image acquisition and representation | COVERED | Ch 3, Ch 45 | None |
| Feature extraction and edges [a learning outcome (edge or corner detector), not a topic item] | COVERED | Ch 14 | None |
| Segmentation, recognition and detection | COVERED | Ch 45 | None |
| Motion analysis, tracking, optical flow | THIN | Tracking only | Added optical flow |
| 3D vision [not an AI-Vision item; depth and stereo appear only as robot sensors (AI-Robotics item 2a); excluded from the verified count] | COVERED | Ch 45 | None |
| Speech and audio recognition | COVERED | Ch 46 | None |
| Deep learning for vision | COVERED | Ch 14, Ch 45 | None |

## Summary

**AIMA 4th edition:** 171 topics. Before: 80 COVERED, 20 THIN, 52 MISSING, 19 OUT OF SCOPE (80 of 152 in-scope topics covered, 53%). After: 152 of 152 in-scope topics covered (100%); 152 of 171 topics overall (89%), the rest judged out of scope.

**CS2023 AI knowledge area:** 110 topics. Before: 56 COVERED, 22 THIN, 24 MISSING, 8 OUT OF SCOPE (56 of 102 in-scope topics covered, 55%). After: 102 of 102 in-scope topics covered (100%); 102 of 110 topics overall (93%), the rest judged out of scope.

Every THIN or MISSING topic is now explained at beginner level. Two of them (maximum likelihood in Ch 6, EM with
Gaussian mixtures in Ch 10) were added by parallel audits while this one ran; this audit checked them and left them
alone.

### What was added, by chapter

- **Ch 1:** the four textbook approaches to defining AI (2x2 table), the rational-agent view, and the disciplines AI
  grew from. 1 new definition.
- **Ch 6:** add-one smoothing worked on the chapter's own n-gram model. 1 new definition.
- **Ch 10:** the bag-of-words idea under naive Bayes. 1 new definition.
- **Ch 28:** cognitive architectures (Soar, ACT-R) as the origin of the agent-memory vocabulary. 1 new definition.
- **Ch 45:** optical flow. 1 new definition.
- **Ch 48 (largest change):** PEAS and environment types (Table 48.1); the agent ladder; expected utility, value of
  information and risk aversion (worked umbrella decision); uniform-cost search, iterative deepening and greedy
  best-first; local search (hill climbing, simulated annealing, beam search); constraint satisfaction (meeting
  schedule solved by propagation and backtracking, min-conflicts); classical planning (STRIPS, tea-making domain in
  Table 48.3, PDDL, relaxed heuristics, partial-order and hierarchical planning, replanning); chance nodes and
  expectiminimax (worked dice example); MDPs, the Markov property, value iteration (worked on the corridor world),
  POMDPs and belief states; imitation learning and inverse RL; a short course in game theory (prisoner's dilemma in
  Table 48.8, dominant and mixed strategies, tit-for-tat, mechanism design, Shapley value with SHAP). 41 new
  definitions; tables renumbered 48.1 to 48.9 in order.
- **Ch 49:** forward and inverse kinematics, configuration space, RRT, PID control (worked) and Brooks's subsumption
  architecture. 5 new definitions.
- **Ch 54:** case-based reasoning; propositional and first-order logic, entailment, resolution (worked), Prolog and
  SAT solvers; semantic networks, frames, default reasoning and the frame problem; full joint distribution,
  conditional independence and sampling/MCMC; probabilistic programming; reasoning over time (Markov chains, HMMs,
  the umbrella filter worked over two days, Kalman and particle filters, smoothing, Viterbi); part-of-speech tagging,
  formal grammar, parsing (two parse trees, Figure 54.11) and ambiguity. 24 new definitions; figures renumbered.
- **Ch 60:** the classic arguments about machine minds (Chinese room and the systems reply, strong vs weak AI,
  Dreyfus's argument from informality, the Godel argument and its standard reply). 4 new definitions.

All edited files pass `validate.py` and `check.py`; every new definition is in its chapter's Key terms list. No
2025-2026 facts were added; all new material is stable textbook knowledge.

### Judged out of scope

Atomic/factored/structured representations, bidirectional search, AND-OR and online search, CSP structure, the
wumpus world, unification, modal logic, situation calculus and truth maintenance, relational and open-universe
probability models, multiattribute utility and decision networks, voting theory and bargaining, PAC/VC learning
theory, the "Knowledge in Learning" chapter (EBL, ILP), Bayesian-network structure learning, augmented grammars,
image formation optics and texture, planning under motion uncertainty, BDI agents, argumentation, formal temporal
and spatial calculi, Markov networks, GraphPlan and SAT planning, multi-agent planning and multi-robot systems.
These are research or graduate-level detail that this reader will rarely meet by name; where an idea underneath
them matters (replanning, exploration, belief states, behavioral biases), the book now explains that idea.

## Verified online (October 21, 2026)

The first pass above reconstructed both topic lists from memory because web search was unavailable. On October 21,
2026 both were checked against the published contents. Each difference is marked in the tables above (chapter
numbers, tiers, misnamed rows, rows not in the published list), and nothing was deleted. Every topic the
reconstruction missed or merged into another row was then audited the same way as in the first pass: grep the whole
book, read each hit in context, assign COVERED / THIN / MISSING / OUT OF SCOPE, and fill in-scope THIN or MISSING
topics in the chapter that owns them per OUTLINE.md. All edited chapters pass `validate.py` and `check.py`.

### Standard 1: AIMA 4th edition

**URLs fetched (October 21, 2026):**
- https://aima.cs.berkeley.edu/ (US edition contents, chapter level, with page numbers)
- https://aima.cs.berkeley.edu/contents.html ("Full Table of Contents", US edition, down to subsection level)
- https://aima.cs.berkeley.edu/global-index.html (Global Edition contents, chapter level)
- https://aima.cs.berkeley.edu/global-Contents.pdf (Global Edition "Contents with subsections", section level)

**What differed from the reconstruction:**
- **Chapter numbering (US edition).** Chapter 5 is Adversarial Search and Games and Chapter 6 is Constraint
  Satisfaction Problems. The first pass had them swapped (the Global Edition order); 13 rows were relabelled.
- **Global Edition.** It has 29 chapters: 1-4 as in the US edition, 5 Constraint Satisfaction Problems,
  6 Adversarial Search and Games, 7-14 as in the US edition, 15 Making Simple Decisions, 16 Making Complex Decisions,
  17 Multiagent Decision Making, 18 Probabilistic Programming, 19 Learning from Examples, 20 Knowledge in Learning,
  21 Learning Probabilistic Models, 22 Deep Learning, 23 Reinforcement Learning, 24 Natural Language Processing,
  25 Deep Learning for Natural Language Processing, 26 Robotics, 27 Computer Vision, 28 Philosophy, Ethics, and Safety
  of AI, 29 The Future of AI. The first pass was right that the Global Edition adds "Knowledge in Learning" but wrong
  that it moves probabilistic programming online: it is printed as Chapter 18. The Knowledge in Learning row now lists
  the five published sections.
- **Misnamed rows.** Smoothing of count estimates is section 23.1.4, not Chapter 20. Frames, mechanism design,
  partial-order planning, forward and inverse kinematics, situation calculus and the VC dimension are not headings in
  the published contents; they are topics inside sections (10.5, 18.4, 11.2.4, 26.5, 10.3 and 19.5). The rows were
  kept and annotated.
- **Re-audited rows.** Bidirectional search and atomic/factored representations had been judged out of scope.
  CS2023 lists both in its core tiers (KA Core and CS Core), so both were added to Ch 48 and now count as covered.
- **Merged or missed topics.** The subsection-level contents show 52 topics the reconstruction missed or folded into a
  broader row. They are below. Subsections that are only worked examples (map coloring, the spare tire, the kinship
  domain, the wumpus world revisited) or that a first-pass row already names were not given rows.

**New rows (topics from the published contents):**

| Topic (published section) | Status before | Where in the book | Action |
|---|---|---|---|
| 1.1.5 Beneficial machines (the "standard model" and machines uncertain about our objectives) | COVERED | Ch 56 "Learning values by watching" (*Human Compatible*, off-switch game, assistance games) | None |
| 1.2.6 Computer engineering as a foundation of AI | THIN | Ch 2 and Part VI in depth, but missing from the Ch 1 list of source disciplines | Added to the Ch 1 list |
| 2.2.3 Omniscience, learning and autonomy | COVERED | Ch 48 rational agent ("given everything it has perceived so far"); learning agent | None |
| 3.2 Example problems: standardized puzzles and real-world problems (route finding, touring, layout) | COVERED | Ch 48 mazes, Rubik's cube, map apps; chip placement by simulated annealing | None |
| 3.3.3 Redundant paths (graph search versus tree search) | MISSING | None | Added to Ch 48 "Blind search" |
| 3.3.4 Measuring problem-solving performance (completeness, cost optimality, time and space) | THIN | BFS and DFS compared informally | Added the four criteria; Complete and optimal (search) defined |
| 3.5.4 Satisficing search: inadmissible heuristics and weighted A* | MISSING | None | Added weighted A* with its cost bound; definition |
| 3.5.5 Memory-bounded search (IDA*, RBFS, SMA*) | MISSING | None | Added IDA* with a definition; RBFS and SMA* not named |
| 5.2.2 Optimal decisions in multiplayer games | OUT OF SCOPE | Multiplayer poker and Diplomacy told as stories (Pluribus, CICERO) | None (vector-valued minimax is a refinement) |
| 5.2.4 Move ordering | MISSING | None | Added to Ch 48 "Alpha-beta pruning and evaluation functions" |
| 5.3.3 Forward pruning | OUT OF SCOPE | None | None (engine detail; beam search conveys the idea) |
| 5.3.4 Search versus lookup (opening books, endgame tablebases) | MISSING | Checkers solved (Table 48.4) only | Added opening books, endgame tablebases (all seven-piece positions, 2018) and the horizon effect; three definitions |
| 6.2 Levels of consistency (node, arc, path, k-consistency; global constraints) | THIN | Propagation worked by hand; arc consistency unnamed | Added arc consistency with a definition |
| 6.3.3-6.3.4 Intelligent backtracking (backjumping) and constraint learning | OUT OF SCOPE | None | None (named only as "learning from dead ends") |
| 7.5.2 Conjunctive normal form | COVERED | Ch 54 resolution "rewrites every fact as an OR statement" | None (the name is not used) |
| 7.6.3 The landscape of random SAT problems | OUT OF SCOPE | None | None (research detail on where SAT problems get hard) |
| 7.7 Agents based on propositional logic (logical state estimation, planning by propositional inference) | OUT OF SCOPE | None | None (consistent with planning as SAT) |
| 9.1-9.3 Propositionalization, indexing and efficient forward chaining (Rete) | OUT OF SCOPE | None | None (implementation detail of logic engines) |
| 9.4.5 Constraint logic programming | OUT OF SCOPE | None | None (niche paradigm; Prolog and constraint solvers are covered) |
| 10.2 Physical composition, measurements, things and stuff | OUT OF SCOPE | None | None (formal ontology detail) |
| 11.5 Sensorless, contingent and online planning | THIN | Ch 48 replanning only | Added contingent (conditional) plans and continuous planning; definition |
| 12.2.3 Probability axioms and their reasonableness | COVERED | Ch 6 "The three rules you need"; distributions sum to 1 | None |
| 13.2.2-13.2.3 Compact conditional distributions (noisy-OR) and continuous variables | OUT OF SCOPE | None | None (modeling detail for Bayesian networks) |
| 13.3.3 The complexity of exact inference | THIN | Ch 54 "even clever exact methods can be too slow" | Added the 1990 NP-hardness result, linked to NP-completeness in Ch 48 |
| 13.5.2 The back-door criterion | COVERED | Ch 54 "Adjusting for the confounder", worked | None (the name is not used) |
| 15.3 Keeping track of a complex world (multitarget tracking, data association) | OUT OF SCOPE | None | None (research-level probabilistic modeling) |
| 16.2 The basis of utility theory (axioms of rational preferences) | MISSING | None | Added transitivity, a worked money pump and the von Neumann-Morgenstern result |
| 16.3.3 Expected utility and post-decision disappointment (optimizer's curse) | MISSING | None | Added with the benchmark example; definition |
| 16.6.6 Sensitivity analysis and robust decisions | THIN | Umbrella break-even point computed but not named | Named, with a definition |
| 17.1.1 Utilities over time (discounting) | COVERED | Ch 48 "Rewards, returns and discounting" | None |
| 17.2.3-17.2.4 Linear programming and online algorithms for MDPs | COVERED | Ch 48 MCTS as online planning | None (linear programming not named) |
| 18.1.3-18.1.4 Multiagent planning, cooperation and coordination | OUT OF SCOPE | Ch 28 multi-agent LLM systems | None (matches the CS2023 multi-agent planning row) |
| 18.2.2 Social welfare (Pareto optimality) | THIN | Prisoner's dilemma "better for both" | Added Pareto optimal and social welfare; definition |
| 18.2.4 Sequential games in extensive form; imperfect information | COVERED | Ch 48 game trees and poker | None |
| 18.2.5 Uncertain payoffs and assistance games | COVERED | Ch 56 assistance game definition, off-switch game | None |
| 18.4.2 Common goods (tragedy of the commons) | THIN | "Overfishing" in the prisoner's dilemma paragraph | Named, with a definition |
| 19.3.3 Choosing attribute tests (entropy, information gain) | COVERED | Ch 10 Gini impurity worked | None (information gain not named) |
| 19.7.2-19.7.3 Fast nearest-neighbor lookup (k-d trees, locality-sensitive hashing) | COVERED | Ch 27 approximate nearest neighbor search and HNSW | None |
| 19.8.3 Stacking | MISSING | None | Added to Ch 10; definition |
| 19.8.6 Online learning | COVERED | Ch 8, Ch 10 | None |
| 20.2.3 Generative and discriminative models | COVERED | Ch 16 opening section | None |
| 21.3-21.7 Residual networks, batch normalization, neural architecture search, weight decay, dropout, LSTMs, autoencoders, GANs, multitask learning | COVERED | Ch 9, 13, 14, 16 | None |
| 22.4.4 Reward shaping | COVERED | Ch 48 | None |
| 22.4.5 Hierarchical reinforcement learning | OUT OF SCOPE | None | None (research topic beyond this reader's needs) |
| 23.1.7 Comparing language models (perplexity) | COVERED | Ch 6 | None |
| 24.3.2 Decoding (greedy and beam search) | COVERED | Ch 18 sampling; Ch 48 beam search | None |
| 26.2.1 Types of robots | COVERED | Ch 49 "A field guide to robot bodies" | None |
| 26.5.2 Other motion planners (visibility graphs, Voronoi diagrams, cell decomposition, probabilistic roadmaps) | OUT OF SCOPE | RRT only | None (RRT stands for the sampling family) |
| 26.5.2 and 26.5.4 Trajectory optimization and optimal control | MISSING | PID only | Added dynamics, model predictive control and trajectory optimization to Ch 49 |
| 26.8.1 Coordination with humans: predicting human action | COVERED | Ch 50 prediction stage | None |
| Appendix A.1 Complexity analysis, O() notation, NP-hard problems | THIN | Ch 17 quadratic cost only | Added NP-completeness (Cook 1971, Karp 1972) to Ch 48 |
| Appendix B Backus-Naur form and pseudocode | OUT OF SCOPE | None | None (notation for programmers) |

New rows: 52 (20 COVERED, 9 THIN, 9 MISSING, 14 OUT OF SCOPE).

**Updated counts, AIMA:** 223 topics (171 reconstructed, all matched to published content after the label fixes,
plus 52 new). In scope: 192 (the 152 of the first pass, the 2 re-audited rows and 38 new). Before this verification
pass, 172 of the 192 were covered (90%); after it, 192 of 192 (100%), which is 192 of 223 topics overall (86%). Out
of scope: 31.

### Standard 2: CS2023 Artificial Intelligence knowledge area

**URLs fetched (October 21, 2026):**
- https://csed.acm.org/ (CS2023 home)
- https://csed.acm.org/final-report/ (links to the final report sections, April 2024)
- https://csed.acm.org/knowledge-areas/ and https://csed.acm.org/artificial-intelligence/ (AI knowledge area page,
  with the alpha, beta and gamma drafts)
- https://csed.acm.org/wp-content/uploads/2024/04/3.1-Body-of-Knowledge-1.pdf (final report, Body of Knowledge; the
  AI knowledge area is its first section, with core hours, knowledge units and illustrative learning outcomes)

**What differed from the reconstruction:**
- **Tiers.** Only five units have core hours: AI-Introduction (2 CS Core, 1 KA Core), AI-Search (2 CS Core plus 3
  shared with Algorithmic Foundations, 6 KA Core), AI-KRR (1 plus 1 shared with Mathematical Foundations, 2 KA Core),
  AI-ML (4 and 6) and AI-SEP (3 and 3), for 12 CS Core and 18 KA Core hours. AI-LRR, AI-Probability, AI-Planning,
  AI-Agents, AI-NLP, AI-Robotics and AI-Vision are Non-core, not KA Core. Inside units, items carry their own tiers;
  for example, philosophical issues and the history of AI are Non-core items of AI-Introduction.
- **Names.** The unit is AI-Robotics, not AI-Robo. The other unit names were right.
- **Rows in the wrong unit.** Propositional and predicate logic, resolution, forward and backward chaining and
  ontologies belong to AI-LRR, not AI-KRR. Markov chains are in AI-KRR (KA Core), not AI-Probability. Beliefs,
  desires and intentions appear in AI-NLP (representing meaning), not AI-Agents. Autonomous weapons appear in
  AI-Robotics, not AI-SEP. The rows were annotated, not moved.
- **Rows not in the published list (14, excluded from the verified counts but kept above as history):** value of
  information; safety, robustness and alignment; misinformation and deepfakes; dual use and military applications
  (as an AI-SEP item); SAT and SMT solvers; Kalman and particle filters; decision networks; scheduling with time and
  resources; planning with language models; BDI agents (as an AI-Agents item); BLEU and perplexity; robot learning;
  3D vision; symbolic versus sub-symbolic (a duplicate of AI-KRR item 1). The book material added for them stays,
  since AIMA covers most of them.
- **One row re-scoped.** "Probabilistic programming and relational models" is published only as relational
  probability models, which the AIMA audit judged out of scope; it now counts as out of scope.
- **Partly invented details inside real rows.** BM25, PID, frames, POMDPs, hierarchical clustering and
  dimensionality reduction are not named in the published items; the rows are annotated.
- **Missed topics.** 85 published items or sub-items had no row. They are below, with the item number from the
  report.

**New rows (topics from the published knowledge units):**

| Topic (published item) | Status before | Where in the book | Action |
|---|---|---|---|
| **AI-Introduction** | | | |
| Multimodal input and output (CS Core 3b) | COVERED | Ch 22 | None |
| Simulation of intelligent behavior (3c) | COVERED | Ch 7 ELIZA; Ch 54 | None |
| Nature of agents: reflexive, goal-based, utility-based (5b) | COVERED | Ch 48 agent ladder | None |
| Mixed-initiative autonomy (5a) | MISSING | Ch 28 human-in-the-loop; Ch 50 SAE levels | Added mixed-initiative interaction to Ch 28; definition |
| Decision making under uncertainty and with incomplete information (5c) | COVERED | Ch 48 expected utility, POMDPs | None |
| Perception, environmental interaction and embodied agents: sensors, dynamics, effectors (5d, 5f) | THIN | Ch 49 sensors and actuators; dynamics unexplained | Added robot dynamics to Ch 49 |
| Learning-based agents (5e) | COVERED | Ch 48 learning agent | None |
| **AI-Search** | | | |
| Factoring states into representations (CS Core 1b) | MISSING | Implicit in CSPs and planning | Added factored representation to Ch 48; definition |
| Dynamic construction of the search graph (1c) | THIN | Implicit | Added: states are generated on demand |
| Local minima and the search landscape; ridges, plateaus, saddle points (3c, Non-core 10d) | THIN | Ch 48 local maxima; Ch 13 saddle points and plateaus | Added plateaus and ridges to Ch 48 |
| Bidirectional search (KA Core 5) | MISSING | None | Added to Ch 48 with a worked count; definition |
| Ply cutoff (KA Core 7b) | COVERED | Ch 48 evaluation functions | None |
| Tabu search (Non-core 12) | MISSING | None | Added to Ch 48; definition |
| Variations on A*: IDA*, SMA*, RBFS (Non-core 13) | MISSING | None | Added IDA* |
| The horizon effect (Non-core 14a) | MISSING | None | Added; definition |
| Opening playbooks and endgame solutions (Non-core 14b) | MISSING | None | Added opening books and endgame tablebases; definitions |
| What it means to "solve" a game (Non-core 14c) | COVERED | Table 48.4 (checkers solved in 2007) | One sentence added on what "solved" means |
| **AI-KRR** | | | |
| Creating a symbolic or logical representation from a natural-language problem statement (CS Core 1a) | COVERED | Ch 54 alarm-and-guard example; Ch 48 meeting-schedule CSP | None |
| Learned subsymbolic representations (1b) | COVERED | Ch 14 embeddings | None |
| Graphical models: naive Bayes, Bayesian networks (1c) | COVERED | Ch 10, Ch 54 | None |
| Axioms of probability (KA Core 4a) | COVERED | Ch 6 three rules | None |
| Markov chains and Markov models (KA Core 7) | COVERED | Ch 54 (added in the first pass) | None |
| **AI-ML** | | | |
| No free lunch theorem (CS Core 2a) | COVERED | Ch 10 | None |
| Sources of error in machine learning (2b) | COVERED | Ch 9 noise, bias and variance | None |
| Working with data: preprocessing, missing values, encoding, standardization (5) | COVERED | Ch 11 | None |
| Hypothesis spaces and complexity (6a) | THIN | Ch 9 model complexity | Added hypothesis space to Ch 8; definition |
| Simple basis feature expansion (6b) | THIN | Ch 9 polynomial fits | Added a worked x-squared example to Ch 8; definition |
| Learned feature representations and their visualization (6c, 12c) | COVERED | Ch 14 | None |
| Regression metrics and the confusion matrix (13b, 13c) | COVERED | Ch 9 | None |
| Parameter tuning by grid and random search (13d) | COVERED | Ch 9 | None |
| Intellectual property (16d) | COVERED | Ch 11, Ch 58, Ch 59 | None |
| Parameter estimation by maximum likelihood (Non-core 17) | COVERED | Ch 6 (added by a parallel audit) | None |
| SVMs and kernels; multi-layer perceptrons (18c, 18f) | COVERED | Ch 10, Ch 12 | None |
| Gaussian processes (18g) | COVERED | Ch 10 | None |
| Curse of dimensionality (19a) | COVERED | Ch 10 | None |
| L1 and L2 regularization (19b) | COVERED | Ch 9 | None |
| Stratification; ROC curve and AUC (20d, 20f) | COVERED | Ch 9 | None |
| Naive Bayes and its relationship to linear models (21a) | OUT OF SCOPE | Ch 10 naive Bayes | None (mathematical relationship) |
| Autoencoders, GANs and adversarial training, attention (22d, 22g, 22h) | COVERED | Ch 15, Ch 16 | None |
| Neural tangent kernel (22b) | OUT OF SCOPE | None | None (advanced theory) |
| Self-organizing maps (24d) | OUT OF SCOPE | None | None (historical niche method) |
| Graph analysis (PageRank) (25) | COVERED | Ch 51 | None |
| Semi-supervised learning (26) | COVERED | Ch 8 | None |
| Gated ensembles (28d) | COVERED | Ch 17 mixture of experts | None |
| Learning theory: VC dimension, generalization bounds (29) | OUT OF SCOPE | Ch 9 intuition only | None (as the AIMA row) |
| LIME (31a) | MISSING | SHAP only (Ch 48) | Added LIME to Ch 10; definition |
| Recommender systems (32) | COVERED | Ch 51 | None |
| Hardware for machine learning: GPUs and TPUs (33) | COVERED | Part VI | None |
| **AI-SEP** | | | |
| Formulating an application as an AI problem; ill-posed problems (CS Core 1a) | COVERED | Ch 10 project lifecycle ("framing the question") | None |
| Evaluation bias (1d) | THIN | Figure 11.8 label only | Added to Ch 11 with the Gender Shades benchmark figures; definition |
| Deployed deep generative models and foundation models (2, 5) | COVERED | Ch 16, Ch 18-19, Ch 47 | None |
| **AI-LRR** | | | |
| Ontology engineering (3b) | COVERED | Ch 54 | None |
| Semantic web (4) | THIN | OWL named only | Added RDF and the Semantic Web to Ch 54; definition |
| **AI-Probability** | | | |
| Exact inference and its complexity (2a) | THIN | "Too slow" only | Added the NP-hardness result to Ch 54 |
| Markov blankets and d-separation (2a) | OUT OF SCOPE | None | None (formal graph theory of Bayesian networks) |
| Decision theory: preferences, utility functions, maximizing expected utility, game theory (3) | COVERED | Ch 48 | Utility axioms added (AIMA 16.2 row) |
| **AI-Planning** | | | |
| Total order planning (3) | COVERED | Ch 48 tea-making example | None |
| Conditional and continuous planning (10a, 10b) | MISSING | Replanning only | Added contingent plans and continuous planning to Ch 48 |
| **AI-Agents** | | | |
| Agent theory, including mathematical formalisms (2) | OUT OF SCOPE | None | None (mathematical formalisms) |
| Bandit algorithms (3c) | COVERED | Ch 48 | None |
| Believable agents: synthetic characters, modeling emotions (4c) | MISSING | None | Added to Ch 28 with the 2023 Generative Agents study; definition |
| Learning agents (5) | COVERED | Ch 48 | None |
| Swarm systems and biologically inspired models (7d) | COVERED | Ch 54 "Swarms" | None |
| Multi-agent learning (7e) | COVERED | Ch 48 self-play, AlphaStar | None |
| Trading agents and supply chain management (8c) | COVERED | Ch 53 | None |
| **AI-NLP** | | | |
| Chart parsers (CYK) and weighted CYK for probabilistic grammars (2) | OUT OF SCOPE | Ch 54 probabilistic parsing described | None (parsing-algorithm detail) |
| Semantic roles (3b) | MISSING | None | Added semantic role labeling to Ch 54; definition |
| Temporal representations; beliefs, desires and intentions (3c, 3d) | OUT OF SCOPE | None | None (formal semantics detail) |
| Corpus-based methods (4) | COVERED | Ch 54 treebanks; Ch 11 | None |
| Backoff (6, "Smoothing and backoff") | MISSING | Smoothing only | Added backoff to Ch 6; definition |
| Multi-modal embeddings (12c) | COVERED | Ch 22 CLIP | None |
| **AI-Robotics** | | | |
| Control architectures: deliberative versus reactive, Braitenberg vehicles (1b) | THIN | Ch 49 subsumption | Added Braitenberg vehicles; reactive and deliberative control defined |
| World modeling; inherent uncertainty in sensing and control (1c, 1d) | COVERED | Ch 49 world models; Ch 54 filters | None |
| Coordinate frames, translation and rotation (3) | MISSING | Degrees of freedom only | Added coordinate frames and pose, with a worked calibration error, to Ch 49 |
| Manipulation and grasping (10) | COVERED | Ch 49 | None |
| Joint control and dynamics (11) | THIN | PID only | Added dynamics and model predictive control |
| Trajectory optimization (9) | MISSING | RRT only | Added to Ch 49 |
| Vision-based control (12) | COVERED | Ch 49 vision-language-action models; Ch 50 | None |
| Applications and societal issues: right-to-work, liability, autonomous weapons, oversight (15) | COVERED | Ch 50, 53, 59, 60 | None |
| **AI-Vision** | | | |
| Shape representation and contour-based recognition (1b) | OUT OF SCOPE | None | None (pre-deep-learning recognition technique) |
| Generative models (1d) | COVERED | Ch 16, Ch 47 | None |
| Touch and proprioception (3) | COVERED | Ch 49 | None |
| Other modalities: olfaction (4) | MISSING | None | Added the 2023 principal odor map to Ch 52; definition |
| Modularity in recognition (5) | OUT OF SCOPE | None | None (too vague to teach as a topic; recognition pipelines are covered in Ch 45) |
| Approaches to pattern recognition (6) | COVERED | Ch 10, 14, 45 | None |

New rows: 85 (50 COVERED, 10 THIN, 15 MISSING, 10 OUT OF SCOPE).

**Updated counts, CS2023:** 181 topics (96 first-pass rows that match the published list, plus 85 new). In scope:
164 (89 first-pass rows and 75 new). Before this verification pass, 139 of the 164 were covered (85%); after it, 164
of 164 (100%), which is 164 of 181 topics overall (91%). Out of scope: 17.

### Book changes in this verification pass

- **Ch 1:** computer engineering added to the map of fields AI grew from.
- **Ch 6:** backoff in n-gram models. 1 new definition.
- **Ch 8:** hypothesis space and feature (basis) expansion, worked with an x-squared feature. 2 new definitions.
- **Ch 10:** LIME (alongside SHAP) and stacking. 2 new definitions.
- **Ch 11:** evaluation bias, with the Gender Shades benchmark composition. 1 new definition.
- **Ch 28:** mixed-initiative interaction; believable agents and the 2023 Generative Agents study. 2 new definitions.
- **Ch 48:** factored representations and on-demand state generation; completeness and optimality; graph search;
  bidirectional search (worked count); weighted A* and IDA*; plateaus, ridges and tabu search; arc consistency;
  NP-completeness (Cook 1971, Karp 1972); contingent and continuous planning; move ordering, the horizon effect,
  opening books and endgame tablebases; utility axioms and the money pump (worked), sensitivity analysis and the
  optimizer's curse; Pareto optimality, social welfare and the tragedy of the commons. 17 new definitions.
- **Ch 49:** coordinate frames and pose (worked calibration error); dynamics, model predictive control and
  trajectory optimization; Braitenberg vehicles; reactive versus deliberative control. 6 new definitions.
- **Ch 52:** the 2023 principal odor map (machine olfaction). 1 new definition.
- **Ch 54:** NP-hardness of exact Bayesian-network inference; RDF and the Semantic Web; morphology (stemming,
  lemmatization) and semantic role labeling. 3 new definitions.

In all, 35 new definitions, each in its chapter's Key terms list.

### Sources for the facts added to the book

- LIME (Ribeiro, Singh and Guestrin, 2016): https://arxiv.org/abs/1602.04938
- Generative Agents (Park et al., 2023; 25 agents, the Valentine's Day party): https://arxiv.org/abs/2304.03442
- Braitenberg, *Vehicles* (1984) and the "fear" and "aggression" wirings: https://en.wikipedia.org/wiki/Braitenberg_vehicle
  (the MIT Press page returned 403)
- Cook 1971 and Karp's 1972 list of 21 NP-complete problems: https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem
  and https://en.wikipedia.org/wiki/Karp%27s_21_NP-complete_problems (the ACM Digital Library returned 403)
- Seven-piece endgame tablebases completed in 2018; Stockfish uses Syzygy tablebases:
  https://en.wikipedia.org/wiki/Endgame_tablebase
- Gender Shades benchmark composition (79.6% and 86.2% lighter-skinned):
  https://proceedings.mlr.press/v81/buolamwini18a.html
- Principal odor map (Lee, ..., Wiltschko, *Science* 381, 2023; 400 unseen molecules, better than the median
  panelist): Crossref record https://api.crossref.org/works/10.1126/science.ade4401 (science.org returned 403)
- Model predictive control, receding horizon, chemical plants and refineries since the 1980s:
  https://en.wikipedia.org/wiki/Model_predictive_control
- Exact inference in Bayesian networks is NP-hard (Cooper, 1990): https://en.wikipedia.org/wiki/Bayesian_network
- OWL as a W3C Semantic Web language alongside RDF: https://www.w3.org/OWL/

**Limits of this check.** The web-search budget for the session ran out partway through. All sources above were
fetched directly from known URLs; where a publisher page refused access, a reference page was used instead (marked
above). Two candidate details were left out because they could not be verified: the use of IDA* with pattern
databases for optimal Rubik's cube solutions, and Deep Blue's opening-book and endgame-database sizes. The Global
Edition contents PDF stops at section level, so Global Edition subsections were not compared; its sections match the
US edition's apart from the chapter order and Chapter 20.
