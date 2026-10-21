# External-standard coverage audit: classical AI

Audited October 21, 2026 against `ai-book/chapters/` (66 chapters) and `ai-book/appendices/`. Each topic was searched
for by its key terms across the whole book, and every hit was read in context. COVERED means explained at beginner
level; THIN means mentioned but not explained; MISSING means absent; OUT OF SCOPE means too specialized or
mathematical for this reader (the reason is given in the Action column).

## Standards and how their structure was reconstructed

1. **Russell and Norvig, *Artificial Intelligence: A Modern Approach*, 4th edition (2020).** Topics are listed by
   chapter from memory of the table of contents (web search was unavailable). Chapter numbers follow the US edition:
   1 Introduction, 2 Intelligent Agents, 3 Search, 4 Search in Complex Environments, 5 Constraint Satisfaction,
   6 Adversarial Search and Games, 7 Logical Agents, 8 First-Order Logic, 9 Inference in First-Order Logic,
   10 Knowledge Representation, 11 Automated Planning, 12 Quantifying Uncertainty, 13 Probabilistic Reasoning,
   14 Probabilistic Reasoning over Time, 15 Probabilistic Programming, 16 Making Simple Decisions, 17 Making Complex
   Decisions, 18 Multiagent Decision Making, 19 Learning from Examples, 20 Learning Probabilistic Models, 21 Deep
   Learning, 22 Reinforcement Learning, 23 Natural Language Processing, 24 Deep Learning for NLP, 25 Computer Vision,
   26 Robotics, 27 Philosophy, Ethics, and Safety of AI, 28 The Future of AI. **Uncertainty:** the Global Edition
   numbers the later chapters differently and includes a "Knowledge in Learning" chapter (explanation-based learning,
   relevance-based learning, inductive logic programming, carried over from the 3rd edition) while placing
   probabilistic programming online; both are listed below. Rows name topics, not exact section titles.
2. **ACM/IEEE-CS/AAAI Computer Science Curricula 2023 (CS2023), Artificial Intelligence knowledge area.** Listed by
   knowledge unit: AI-Introduction, AI-Search, AI-KRR, AI-ML and AI-SEP (CS Core), then AI-LRR, AI-Probability,
   AI-Planning, AI-Agents, AI-NLP, AI-Robo and AI-Vision (KA Core). **Uncertainty:** the unit names are as I recall
   them; the topic rows inside each unit summarize what the unit is known to cover rather than quoting its bullet
   list word for word.

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
| Ch 2. Atomic, factored and structured representations | OUT OF SCOPE | Implicit in CSPs and planning | None (technical vocabulary; the ideas appear in the new CSP and planning sections) |
| **Part II** | | | |
| Ch 3. Problem formulation: states, actions, goals, state space | COVERED | Ch 48 "States, actions and goals" | None |
| Ch 3. Breadth-first and depth-first search | COVERED | Ch 48 "Blind search" | None |
| Ch 3. Uniform-cost search (Dijkstra) | MISSING | Only a resource link in Ch 48 Going deeper | Added explanation and definition to Ch 48 "Blind search" |
| Ch 3. Depth-limited search and iterative deepening | MISSING | None | Added explanation and definition to Ch 48 |
| Ch 3. Bidirectional search | OUT OF SCOPE | None | None (a refinement the reader does not need) |
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
| Ch 5. Defining CSPs (variables, domains, constraints) | MISSING | None | Added Ch 48 "Constraint satisfaction" with a meeting-schedule example solved by hand |
| Ch 5. Constraint propagation | MISSING | None | Added with definition |
| Ch 5. Backtracking search and variable ordering (most-constrained first) | MISSING | None | Added with definition and worked steps |
| Ch 5. Local search for CSPs (min-conflicts) | MISSING | None | Added one sentence in the CSP section |
| Ch 5. Problem structure (tree-structured CSPs, decomposition) | OUT OF SCOPE | None | None |
| Ch 6. Two-player zero-sum games | COVERED | Ch 48 zero-sum game definition, game trees | None |
| Ch 6. Minimax | COVERED | Ch 48 minimax worked on tic-tac-toe | None |
| Ch 6. Alpha-beta pruning | COVERED | Ch 48 | None |
| Ch 6. Evaluation functions and cutoff search | COVERED | Ch 48 (Deep Blue, Stockfish) | None |
| Ch 6. Monte Carlo tree search | COVERED | Ch 48 (UCB worked) | None |
| Ch 6. Stochastic games (expectiminimax) | THIN | Backgammon named, method absent | Added Ch 48 "Games with dice: chance nodes" with a worked dice example |
| Ch 6. Partially observable games (card games) | COVERED | Ch 48 poker, imperfect information, CFR | None |
| Ch 6. Limitations of game search | COVERED | Ch 48 Watch out on narrowness and adversarial Go strategies | None |
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
| Ch 10. Frames | MISSING | None | Added Minsky's frames with definition |
| Ch 10. Events, situation calculus and the frame problem | MISSING | None | Added the frame problem; situation calculus left out |
| Ch 10. Mental objects and modal logic | OUT OF SCOPE | None | None |
| Ch 10. Default (non-monotonic) reasoning; truth maintenance | MISSING | None | Added default reasoning (the penguin example); truth maintenance left out |
| Ch 11. Classical planning representation (STRIPS, PDDL, preconditions and effects) | MISSING | Shakey named in Ch 7 and Ch 48; STRIPS absent | Added Ch 48 "Planning with actions: from Shakey to PDDL" with a worked tea-making domain (Table 48.3) |
| Ch 11. Planning algorithms (forward and backward state-space search) | MISSING | None | Backward search worked in the tea example; forward search described |
| Ch 11. Planning heuristics (relaxation, ignoring delete effects) | MISSING | None | Added |
| Ch 11. Hierarchical planning (HTN) | MISSING | None | Added with definition |
| Ch 11. Partial-order planning | MISSING | None | Named and explained in the tea example |
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
| Ch 15 (US ed.). Probabilistic programming | THIN | Named once in Ch 54 | Added definition (Stan, PyMC) |
| Ch 15 (US ed.). Relational and open-universe probability models | OUT OF SCOPE | None | None |
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
| Ch 18. Mechanism design | MISSING | None | Added with the truthful second-price auction |
| Ch 18. Voting, bargaining, contract net | OUT OF SCOPE | None | None (mechanism design definition mentions voting systems) |
| **Part V** | | | |
| Ch 19. Forms of learning; supervised learning | COVERED | Ch 8 | None |
| Ch 19. Decision trees | COVERED | Ch 10 (Gini worked) | None |
| Ch 19. Model selection, cross-validation, regularization | COVERED | Ch 9 | None |
| Ch 19. Learning theory (PAC learning, VC dimension) | OUT OF SCOPE | Bias-variance intuition in Ch 9 | None (mathematical; not a term this reader will meet) |
| Ch 19. Linear and logistic regression, perceptron | COVERED | Ch 8, Ch 10 | None |
| Ch 19. Nonparametric models (kNN, SVMs, kernels) | COVERED | Ch 10 | None |
| Ch 19. Ensembles (bagging, random forests, boosting) | COVERED | Ch 10 | None |
| Ch 19. Developing machine learning systems | COVERED | Ch 10 lifecycle and MLOps; Ch 11 | None |
| Global ed. / 3rd ed. Knowledge in learning (explanation-based, relevance-based, inductive logic programming) | OUT OF SCOPE | None | None (research niche; the reader will not meet these terms) |
| Ch 20. Maximum likelihood estimation | MISSING | None when this audit began | Added to Ch 6 by a parallel audit during this round; no action needed |
| Ch 20. Bayesian parameter learning (priors and posteriors) | COVERED | Ch 6 prior and posterior; Ch 10 Laplace smoothing | None |
| Ch 20. Smoothing of count estimates | THIN | Ch 10 Laplace smoothing for naive Bayes only | Added add-one smoothing worked on the Ch 6 n-gram model, with definition |
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
| Ch 26. Forward and inverse kinematics | MISSING | None | Added with definition |
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
| Philosophical issues | THIN | Ch 60 Debate 7 (consciousness) | Added classic arguments to Ch 60 |
| Symbolic vs sub-symbolic; rules vs learning | COVERED | Ch 1 three ways; Ch 54 five tribes | None |
| History of AI | COVERED | Ch 7 | None |
| **AI-Search: Search (CS Core and KA Core)** | | | |
| State spaces and problem formulation | COVERED | Ch 48 | None |
| Uninformed search (BFS, DFS, iterative deepening, uniform cost) | THIN | BFS and DFS only | Added uniform-cost and iterative deepening |
| Heuristic search (greedy best-first, A*, admissibility) | THIN | A* only | Added greedy best-first |
| Space and time efficiency of search | COVERED | Ch 7 combinatorial explosion; Ch 48 BFS vs A* counts | None |
| Local search (hill climbing, simulated annealing, beam search) | MISSING | None | Added Ch 48 local search |
| Population-based search (genetic algorithms) | COVERED | Ch 54 | None |
| Constraint satisfaction (backtracking, propagation, local search) | MISSING | None | Added Ch 48 CSP section |
| Two-player games: minimax and alpha-beta | COVERED | Ch 48 | None |
| Games with chance (expectimax) | THIN | Backgammon named only | Added chance nodes |
| Monte Carlo tree search | COVERED | Ch 48 | None |
| **AI-KRR: Fundamental Knowledge Representation and Reasoning (CS Core)** | | | |
| Types of representation: symbolic, logical, probabilistic, neural | COVERED | Ch 1; Ch 54 | None |
| Propositional and predicate (first-order) logic | MISSING | None | Added Ch 54 logic section |
| Resolution and theorem proving | MISSING | None | Added |
| Forward and backward chaining | COVERED | Ch 54 | None |
| Ontologies, semantic networks, knowledge graphs | THIN | Knowledge graphs and ontologies only | Added semantic networks and frames |
| Probability review, Bayes' theorem, Bayesian inference | COVERED | Ch 6 | None |
| Random variables, joint distributions, conditional independence | THIN | Ch 6 independence only | Added full joint distribution and conditional independence |
| Decision-theoretic agents: utility and expected utility | MISSING | None | Added Ch 48 expected utility |
| Value of information | MISSING | None | Added |
| **AI-ML: Machine Learning (CS Core and KA Core)** | | | |
| Definitions and examples: classification, regression, clustering | COVERED | Ch 8, Ch 10 | None |
| Supervised learning: features, labels, training and test data | COVERED | Ch 8, Ch 9 | None |
| Linear and logistic regression, decision trees, naive Bayes, kNN | COVERED | Ch 8, Ch 10 | None |
| Overfitting, regularization, cross-validation, evaluation metrics | COVERED | Ch 9 | None |
| Unsupervised learning: k-means, hierarchical clustering, dimensionality reduction | COVERED | Ch 10 | None |
| EM and Gaussian mixtures | MISSING | None when this audit began | Added to Ch 10 by a parallel audit; no action needed |
| Ensembles | COVERED | Ch 10 | None |
| Neural networks and deep learning (backpropagation, CNNs, RNNs, Transformers) | COVERED | Part III | None |
| Generative models | COVERED | Ch 16 | None |
| Reinforcement learning: MDPs, value and policy iteration, Q-learning, policy gradients | THIN | Q-learning and policy gradients only | Added MDPs, value iteration, POMDPs |
| Explainability (feature importance, SHAP) | THIN | Ch 10 feature importance; Ch 53, Ch 57 | Added Shapley value and SHAP |
| Fairness, bias and privacy in ML | COVERED | Ch 11, Ch 58 | None |
| Data collection and preparation | COVERED | Ch 11 | None |
| **AI-SEP: Applications and Societal Impact (CS Core)** | | | |
| Societal and economic impact | COVERED | Ch 60 | None |
| Ethics and fairness | COVERED | Ch 58 | None |
| Privacy and surveillance | COVERED | Ch 45, Ch 58 | None |
| Safety, robustness and alignment | COVERED | Ch 55-57 | None |
| Misinformation and deepfakes | COVERED | Ch 58 | None |
| Environmental impact | COVERED | Part VII; Ch 58 | None |
| Law, regulation and governance | COVERED | Ch 59 | None |
| Dual use and military applications | COVERED | Ch 53, Ch 58 | None |
| Accountability and transparency | COVERED | Ch 57, Ch 59 | None |
| **AI-LRR: Logical Representation and Reasoning (KA Core)** | | | |
| Non-monotonic and default reasoning | MISSING | None | Added Ch 54 |
| Argumentation | OUT OF SCOPE | None | None |
| Reasoning about action and change (situation calculus, frame problem) | MISSING | None | Added the frame problem; situation calculus left out |
| Temporal and spatial reasoning (formal calculi) | OUT OF SCOPE | None | None |
| Rule-based expert systems | COVERED | Ch 54 | None |
| Semantic networks, frames, description logics | MISSING | None | Added Ch 54 |
| Model-based and case-based reasoning | THIN | Ch 54 analogizers | Added case-based reasoning definition |
| Logic programming (Prolog) and answer set programming | THIN | Prolog in Appendix C only | Added Prolog; answer set programming left out |
| SAT and SMT solvers | MISSING | None | Added SAT solvers |
| **AI-Probability: Probabilistic Representation and Reasoning (KA Core)** | | | |
| Bayesian networks | COVERED | Ch 54 | None |
| Exact inference | COVERED | Ch 54 enumeration with natural frequencies | None |
| Approximate inference (sampling, MCMC) | MISSING | None | Added |
| Markov networks (undirected models) | OUT OF SCOPE | None | None |
| Probabilistic programming and relational models | THIN | Named once | Added probabilistic programming definition |
| Temporal models: Markov chains and HMMs | THIN | HMM in Ch 46 only | Added Ch 54 reasoning over time |
| Filtering: Kalman and particle filters | MISSING | None | Added |
| Decision networks / influence diagrams | OUT OF SCOPE | None | None |
| **AI-Planning: Planning (KA Core)** | | | |
| Planning representations (STRIPS, PDDL) | MISSING | None | Added Ch 48 planning section |
| State-space planning and planning heuristics | MISSING | None | Added |
| Partial-order planning | MISSING | None | Added |
| Planning graphs (GraphPlan) and planning as SAT | OUT OF SCOPE | None | None |
| Hierarchical planning | MISSING | None | Added |
| Plan execution, monitoring and replanning | THIN | Ch 28 agents revise plans | Added |
| Scheduling with time and resources | THIN | Uses named only | Added |
| Probabilistic planning: MDPs and POMDPs | MISSING | None | Added Ch 48 |
| Multi-agent planning | OUT OF SCOPE | None | None |
| Planning with language models | COVERED | Ch 28 planning; Ch 21 | None |
| **AI-Agents: Agents and Cognitive Systems (KA Core)** | | | |
| Agent architectures (reactive, deliberative, layered) | THIN | Ch 49 layered control loops | Added agent ladder (Ch 48) and subsumption (Ch 49) |
| Belief-desire-intention (BDI) agents | OUT OF SCOPE | None | None |
| Cognitive architectures (Soar, ACT-R) | MISSING | None | Added to Ch 28 memory section |
| Multi-agent systems: coordination and communication | COVERED | Ch 28 multi-agent systems, A2A | None |
| Game theory and Nash equilibria | THIN | Nash equilibrium only | Added game theory section |
| Mechanism design, auctions, voting | THIN | Auctions in Ch 51 | Added mechanism design |
| LLM-based agents and tool use | COVERED | Ch 28, Ch 29 | None |
| Human-agent interaction | COVERED | Ch 28 humans in the loop; Ch 31 product design | None |
| **AI-NLP: Natural Language Processing (KA Core)** | | | |
| Deterministic and stochastic grammars; parsing | MISSING | None | Added Ch 54 grammar and parsing |
| Representing meaning | COVERED | Ch 14 embeddings; Ch 54 knowledge graphs | None |
| N-gram models and smoothing | THIN | N-grams in Ch 6; smoothing only in Ch 10 | Added n-gram smoothing to Ch 6 |
| Part-of-speech tagging and morphology | MISSING | None | Added POS tagging; morphology left out |
| Information retrieval (vector space, TF-IDF, BM25, precision and recall) | COVERED | Ch 27, Ch 9 | None |
| Information extraction and named entities | COVERED | Ch 54 | None |
| Machine translation | COVERED | Ch 54 | None |
| Text classification and sentiment | COVERED | Ch 54, Ch 10 | None |
| Word embeddings, Transformers and large language models | COVERED | Ch 14, Ch 15, Part IV | None |
| Evaluation (BLEU, perplexity) | COVERED | Ch 54, Ch 6 | None |
| **AI-Robo: Robotics (KA Core)** | | | |
| Sensors and actuators | COVERED | Ch 49 | None |
| Configuration space and motion planning | MISSING | None | Added Ch 49 |
| Kinematics | MISSING | None | Added Ch 49 |
| Localization and mapping | COVERED | Ch 45, Ch 50 | Filters added in Ch 54 |
| Navigation and control (PID) | THIN | Controller defined without method | Added PID |
| Robot learning (RL, imitation, foundation models) | COVERED | Ch 49 | None |
| Multi-robot systems | OUT OF SCOPE | None | None |
| Human-robot interaction, safety and ethics | COVERED | Ch 49 | None |
| **AI-Vision: Perception and Computer Vision (KA Core)** | | | |
| Image acquisition and representation | COVERED | Ch 3, Ch 45 | None |
| Feature extraction and edges | COVERED | Ch 14 | None |
| Segmentation, recognition and detection | COVERED | Ch 45 | None |
| Motion analysis, tracking, optical flow | THIN | Tracking only | Added optical flow |
| 3D vision | COVERED | Ch 45 | None |
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
