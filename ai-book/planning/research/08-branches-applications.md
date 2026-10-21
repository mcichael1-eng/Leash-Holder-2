# 08 — The Branches and Application Areas of AI Beyond Chatbots

Research notes for *Everything About AI: From Zero to the Frontier*. Prepared October 21, 2026.

**How to read these notes.** The reader has used chatbots daily but knows almost no computer science. This domain is where the book shows them that chatbots are one branch of a large tree. AI also sees, hears, draws, plays games, drives cars, folds proteins, picks their next video and moves robot arms. Every section is written so the author can lift material straight into chapters.

**Verification status.** Time-sensitive facts in Section 4 were checked against web sources in October 2026, with URLs given. Partway through the research, the shared web-search budget for this session ran out. A few items could therefore only be checked through direct fetches of primary pages or not at all. These are labelled **[company claim]**, **[secondary source]** or **[unverified]**. Historical milestones before 2025 are long-established facts; for those I give canonical sources from memory where useful.

---

## 1. Topic map (teaching order)

The order goes from things the reader already touches (phone camera, feeds, voice assistants) to things they only hear about (robots, protein folding, AGI). Each module notes what must be explained and how to teach it.

### Part A — Orientation: the whole tree, not just the chatbot branch

- **A1. What "AI" covers.** Present AI as a family tree with two old trunks. One is *symbolic AI*: hand-written rules and logic. The other is *machine learning*: learning patterns from examples. Deep learning grows out of machine learning, generative AI grows out of deep learning, and LLMs (the reader's chatbots) are one twig of generative AI. Use the "map of all AI branches" diagram (Section 5, D1) as the chapter opener.
- **A2. The five verbs of AI.** Organize all branches by what they do: **perceive** (see, hear, read), **understand/predict** (classify, forecast, recommend), **create** (generate text, images, audio, video, 3D), **decide** (plan, play, search), and **act** (robots, cars). A chatbot mostly reads and creates text. Every later chapter is tagged with its verbs.
- **A3. The invisible AI you used this morning.** Make an inventory: face unlock, the photo app's search ("dog"), spam filter, autocorrect, map arrival times, the bank's fraud check, the feed on TikTok, YouTube or Instagram, and ad targeting. Say plainly that recommendation and ranking systems are the AI most people meet most often, far more than chatbots.

### Part B — Classic and symbolic AI (the old toolbox that never went away)

- **B1. Search and planning.** Explain search as "trying possibilities in your head before acting," using a maze and GPS routing (A* search). Then cover game trees and minimax with tic-tac-toe, then Monte Carlo tree search. This lays the groundwork for AlphaGo.
- **B2. Rules, expert systems and knowledge representation.** Cover IF-THEN rules, the expert systems of the 1970s–80s (MYCIN for infections, XCON for configuring computers) and why they were brittle. Then knowledge graphs (Google's Knowledge Graph, Wikidata) as facts stored as subject–relation–object triples.
- **B3. Reasoning under uncertainty.** Cover probability and Bayes' rule, using the medical-test example. Then Bayesian networks (Judea Pearl) and fuzzy logic (degrees of truth, such as "somewhat warm"; Lotfi Zadeh, 1965), with real uses in washing machines and train braking.
- **B4. Evolutionary algorithms.** Explain "breed the best solutions and mutate" with a genetic algorithm, using NASA's evolved spacecraft antenna (2006) as the example. Mention swarm intelligence briefly.
- **B5. Causal inference.** Correlation is not causation. Explain confounders (ice cream and drowning), randomized experiments and A/B tests, and Pearl's "ladder of causation": seeing, doing, imagining. Explain why prediction models fail when the world changes.
- **B6. Neuro-symbolic AI.** Combine neural intuition with symbolic rigor. AlphaGeometry pairs a neural model with a symbolic deduction engine, and AlphaProof pairs an AI model with the Lean proof checker. Present this as one of the frontier's live debates.

### Part C — Language processing beyond chatbots (NLP)

- **C1. The four eras of language AI.** Rules (1950s–80s), statistics (1990s–2000s), neural networks (2010s), transformers and LLMs (2017–now). Translation is the thread that runs through all four.
- **C2. Classic NLP tasks.** Tokenization, text classification (spam), sentiment analysis (reviews), named entity recognition (people, places, companies), information extraction (turn a contract into a table), summarization, question answering. Show each task as "text in → structured thing out." Note that LLMs now do most of these with a single prompt, but specialized small models still run at massive scale because they are cheap and fast.
- **C3. Machine translation history.** The Georgetown–IBM demo (1954), the ALPAC report that killed funding (1966), statistical MT (IBM, then Google Translate in 2006), neural MT (Google's GNMT, 2016), the Transformer (2017, invented *for translation*), Meta's NLLB-200 (200 languages, 2022) and speech-to-speech translation.
- **C4. Embeddings and semantic search.** Words and documents become points in a "meaning space." Use this to explain search, recommendations and RAG later.

### Part D — Computer vision (how machines see)

- **D1. An image is a grid of numbers.** Pixels and RGB values. Show a 5×5 zoom of a real photo.
- **D2. Image classification.** "What is in this picture?" Cover ImageNet, AlexNet (2012) as the deep-learning "big bang," convolutional neural networks (CNNs: small filters that detect edges, then shapes, then objects) and vision transformers.
- **D3. Object detection.** "What is where?" Bounding boxes, YOLO-style real-time detectors, and uses in cars, retail and security.
- **D4. Segmentation.** Pixel-level outlines. Distinguish semantic, instance and panoptic segmentation. Then Meta's Segment Anything (SAM 2023 → SAM 2 for video 2024 → SAM 3 with text "concept" prompts, Nov 2025).
- **D5. OCR and document AI.** From reading digits on checks (LeNet, 1990s) to today's document understanding of tables, forms and handwriting.
- **D6. Faces.** Face detection, face verification (is this the phone's owner?) and face identification (who is this stranger?). Cover accuracy gaps across demographics, surveillance, consent and the legal landscape.
- **D7. Pose estimation and tracking.** Skeleton keypoints, used in fitness apps, sports analytics and robot learning from human video.
- **D8. Video understanding.** Action recognition, temporal reasoning and long-video question answering by multimodal models.
- **D9. 3D vision.** Depth estimation, stereo, SLAM (how robot vacuums map rooms), photogrammetry, NeRFs (2020), Gaussian splatting (2023) and single-image 3D reconstruction (SAM 3D, 2025).
- **D10. Vision-language models.** CLIP (2021) linked images and text in one meaning space, and multimodal chatbots grew from that. This module bridges back to the reader's chatbot experience ("when you upload a photo to ChatGPT…").

### Part E — Speech and audio

- **E1. Sound as numbers.** Waveforms and spectrograms. A spectrogram turns audio into an image, so vision tricks work on sound.
- **E2. Speech recognition (ASR).** From Dragon NaturallySpeaking to Siri (2011) to deep-learning ASR to Whisper (2022, trained on 680,000 hours of audio). Cover word error rate, accents, noise and speaker diarization ("who spoke when").
- **E3. Text-to-speech and voice cloning.** WaveNet (2016) made synthetic voices natural, and modern systems clone a voice from seconds of audio. Cover ethics, scams and the 2024 US FCC ruling on AI voices in robocalls.
- **E4. Real-time voice agents.** Contrast the cascade (ASR → LLM → TTS) with native speech-to-speech models. Explain latency budgets, turn-taking, barge-in (interrupting) and why sub-second response matters. Uses include call centers, receptionists and language tutors.
- **E5. Music and sound generation.** Suno and Udio, the 2024 label lawsuits and the 2025–26 settlements and licensing pivot. Sound effects for video, and stem separation.
- **E6. Audio understanding.** Sound-event detection (glass breaking, coughs), bioacoustics (whale and bird calls), hearing aids with AI noise reduction.

### Part F — Generative media (images, video, 3D, worlds)

- **F1. How generators work, intuitively.** GANs (forger vs detective, 2014), diffusion (start from static and "un-blur" step by step toward the prompt), autoregressive generation (predict the next patch or token) and latent space.
- **F2. Image generation and editing.** DALL·E, Midjourney, Stable Diffusion, Google's Nano Banana models and GPT image models. Cover inpainting and outpainting, style and character consistency, and text rendering.
- **F3. Video generation.** Sora (2024 preview) → Sora 2 with a social app (Sept 2025) → app shut down (announced March 2026). Then Veo 3/3.1 with native sound, Kling, Runway and Seedance. Explain why physics and consistency are hard, and the clip-length limits.
- **F4. 3D and avatars.** Text-to-3D, image-to-3D, digital humans and lip-sync.
- **F5. World models.** Models that generate interactive, explorable environments frame by frame in response to your actions: Genie 2 (2024), Genie 3 (2025), Project Genie (2026), NVIDIA Cosmos, World Labs. Explain why labs think these matter for training robots and agents.
- **F6. Provenance and deepfakes.** Watermarks (SynthID), C2PA Content Credentials, why detection is an arms race, non-consensual imagery, elections and copyright.

### Part G — Reinforcement learning, games and planning

- **G1. RL from scratch.** Teach the loop of agent, environment, action, reward and policy with a dog-training analogy. Cover exploration vs exploitation and delayed reward (credit assignment).
- **G2. The game milestones as a story.** TD-Gammon (1992), Deep Blue (1997), Watson on Jeopardy! (2011), DQN on Atari (2013/2015), AlphaGo vs Lee Sedol (2016, "Move 37"), AlphaGo Zero and AlphaZero (2017, no human games), MuZero (2020, not even told the rules), OpenAI Five in Dota 2 (2019), AlphaStar in StarCraft II (2019), Libratus and Pluribus in poker (2017, 2019), CICERO in Diplomacy (2022, negotiation in natural language).
- **G3. Why games matter.** They are cheap, safe, scorable worlds. Self-play is how a program can surpass every human teacher.
- **G4. RL leaves the arcade.** Data-center cooling, chip floorplanning, plasma control in fusion reactors, drone racing, robot locomotion, RLHF for chatbots, and RL for "reasoning" models. This links back to the reader's chatbots, which were partly shaped by RL.
- **G5. Planning and search today.** Monte Carlo tree search, test-time search ("thinking longer"), and agents that plan multi-step tasks.

### Part H — Robotics (AI with a body)

- **H1. Why robots are hard.** Moravec's paradox: chess is easy for computers, folding laundry is hard. The sense–plan–act loop, noisy sensors, and the real cost of mistakes.
- **H2. Robot types.** Industrial arms (mostly not "AI"), warehouse mobile robots, drones, quadrupeds, humanoids, surgical robots, robot vacuums.
- **H3. Locomotion.** Walking learned in simulation with RL, domain randomization and sim-to-real transfer. Unitree and Boston Dynamics videos as examples.
- **H4. Manipulation.** Grasping, dexterous hands, tactile sensing, deformable objects (cloth, cables).
- **H5. The data problem.** There is no "internet of robot actions." Sources are teleoperation rigs (ALOHA, VR suits), handheld grippers (UMI), pooled datasets (Open X-Embodiment), human videos, simulation and synthetic data. Fleet learning.
- **H6. Robot foundation models and VLAs.** A vision-language-action model takes in camera images plus a sentence ("put the dishes in the sink") and outputs motor commands. Lineage: RT-1/RT-2 (Google, 2022–23) → π0 (2024) → π0.5 → π*0.6 → π0.7 (Physical Intelligence) → Gemini Robotics (2025) → Gemini Robotics 1.5 → Gemini Robotics 2 (2026); NVIDIA GR00T; Figure's Helix.
- **H7. The humanoid industry.** Figure, Tesla Optimus, 1X NEO, Agility Digit, Boston Dynamics Atlas, Apptronik Apollo, Unitree, AgiBot. China's lead in units shipped. Hype vs deployments: count real hours worked, not demo videos.
- **H8. Teleoperation honesty and safety.** Many demos are partly remote-controlled. Cover how to tell the difference, safety standards, and robots in homes.

### Part I — Autonomous vehicles

- **I1. Levels of autonomy (SAE J3016, Levels 0–5).** Focus on who is responsible at each level, not how clever the car is. Level 2 (your hands-on driver assist, including Tesla FSD Supervised) vs Level 4 (Waymo: no driver, limited area).
- **I2. The driving stack.** Perception → prediction → planning → control, plus localization and HD maps. The newer end-to-end approach is a single big network from pixels to steering.
- **I3. Sensors.** Cameras, radar, lidar and ultrasonic sensors, plus sensor fusion. The Waymo (many sensors) vs Tesla (cameras only) debate.
- **I4. History.** The DARPA Grand Challenges (2004 failure, 2005 Stanford win, 2007 urban), the Google project (2009) → Waymo (2016), the Uber test-vehicle fatality (2018) and the Cruise incident and shutdown (2023–24).
- **I5. The 2026 landscape.** Waymo, Tesla Robotaxi, Zoox, Baidu Apollo Go, Pony.ai, WeRide, robotrucks (Aurora) and sidewalk delivery robots.
- **I6. Safety evidence and regulation.** How to read "X% fewer crashes" claims, the operational design domain, and federal vs state rules.

### Part J — Recommenders, ads and search (the AI most people meet daily)

- **J1. The feed is an AI.** Every swipe is a training signal. The feed picks a few items from billions in milliseconds.
- **J2. How recommenders work.** Collaborative filtering ("people like you liked…"), content-based filtering, embeddings and the "two-tower" model, the candidate → ranking → re-ranking funnel, and the Netflix Prize (2006–09).
- **J3. What they optimize.** Watch time, engagement and retention. Cover side effects (filter bubbles, polarization debates, compulsive use), the evidence and its limits, and user controls.
- **J4. Advertising.** Click-through-rate prediction, auctions held in about 100 ms, lookalike audiences, automated campaigns (Meta Advantage+, Google Performance Max), the privacy changes (Apple's tracking prompt) and generative ad creative.
- **J5. Search.** Crawling, indexing and ranking (PageRank, 1998) → learning to rank → BERT in Google Search (2019) → AI Overviews and answer engines, with retrieval-augmented generation explained. What changes for websites when search engines answer directly.

### Part K — AI for science

- **K1. Protein structure.** Amino-acid strings fold into 3D machines. AlphaFold 2 at CASP14 (2020), the AlphaFold Database (200+ million predictions), AlphaFold 3 (2024: proteins plus DNA, RNA and drug-like molecules) and the 2024 Nobel Prize in Chemistry.
- **K2. Protein design.** Running the problem in reverse: design new proteins (David Baker's lab, RFdiffusion; ESM3).
- **K3. Genomics.** DNA language models (Evo 2), variant-effect prediction (AlphaMissense), regulatory-code models (AlphaGenome).
- **K4. Drug discovery.** Target finding, molecule generation, the clinical-trial phases, and why "AI-discovered drug" takes a decade. Insilico's rentosertib Phase IIa (2025) and Isomorphic Labs.
- **K5. Materials.** GNoME's 2.2 million predicted crystals, self-driving labs, batteries and catalysts.
- **K6. Weather and climate.** Physics simulation on supercomputers vs learned forecasting (GraphCast, GenCast, WeatherNext 2, ECMWF AIFS). Ensembles and probability.
- **K7. Mathematics.** Formal proofs (Lean), AlphaGeometry, AlphaProof (IMO silver 2024), Gemini Deep Think and OpenAI (IMO gold level, 2025), the 2026 perfect-score claims, AlphaEvolve finding new algorithms.
- **K8. AI co-scientists and autonomous labs.** Hypothesis-generating agents (Google's AI co-scientist, FutureHouse, Sakana's AI Scientist), robot labs, and what "discovery" really requires: an experiment.
- **K9. Physics, astronomy, fusion.** Plasma control, particle physics triggers, gravitational lensing. Brief.

### Part L — AI by industry (application tour)

For each industry, cover: the tasks AI does, the data it uses, the main risks, and one real example.

- **L1. Healthcare.** Imaging (radiology is about three-quarters of FDA AI devices), pathology slides, diabetic eye screening (IDx-DR, 2018, the first autonomous AI diagnostic cleared by the FDA), ambient scribes, triage, sepsis prediction (and its failures), patient-facing chat.
- **L2. Finance.** Card fraud scoring in milliseconds, anti-money-laundering, credit scoring and fair lending law, algorithmic and high-frequency trading, document processing, robo-advisors.
- **L3. Law.** E-discovery, contract review, legal research assistants, and fake-citation sanctions (Mata v. Avianca, 2023).
- **L4. Education.** AI tutors, feedback, accessibility, cheating and assessment redesign, the evidence on learning.
- **L5. Customer service.** Chat and voice bots, agent-assist, the Klarna story (big claims in 2024, partial walk-back in 2025).
- **L6. Marketing.** Personalization, generative ad creative, and the shift from SEO to "generative engine optimization."
- **L7. Manufacturing and logistics.** Visual inspection, predictive maintenance, digital twins, warehouse robots, route optimization.
- **L8. Agriculture.** Camera-guided precision spraying (John Deere See & Spray), yield prediction, drone and satellite crop monitoring, livestock monitoring.
- **L9. Military and defense.** Drones with autonomous terminal guidance (Ukraine), intelligence analysis, targeting-support systems, swarms, the "human in/on the loop" debate, UN talks on lethal autonomous weapons.
- **L10. Cybersecurity.** Anomaly detection, AI that finds software vulnerabilities (Google Big Sleep, DARPA's AI Cyber Challenge), AI-assisted attacks, phishing and voice-clone fraud.
- **L11. Others, briefly.** Energy grids, insurance, real estate, HR screening (bias risks), government services, journalism, sports analytics.

### Part M — Edge AI and the Internet of Things

- **M1. Cloud vs edge.** Running AI on the device (phone, car, camera, watch) vs in a data center. Tradeoffs: latency, privacy, cost, battery, connectivity.
- **M2. Hardware.** NPUs (neural processing units) and TOPS as a marketing metric; Apple's Neural Engine (2017), "AI PCs."
- **M3. Making models small.** Quantization, distillation, pruning; TinyML on microcontrollers; federated learning (keyboard prediction trained across phones without uploading what you type).
- **M4. IoT examples.** Smart cameras, predictive maintenance sensors, wearables (fall detection, AFib alerts), smart speakers' wake-word detection.

### Part N — Brains and machines

- **N1. Biological vs artificial neurons.** McCulloch & Pitts (1943), the perceptron (1958). Emphasize that artificial neurons are a loose cartoon of real ones.
- **N2. Neuroscience-inspired AI.** CNNs inspired by the visual cortex (Hubel & Wiesel), RL's link to dopamine reward-prediction errors, neuromorphic chips and spiking networks.
- **N3. Brain-computer interfaces.** Electrodes read neural signals and AI decoders turn them into cursor movement, text or speech. Invasive (BrainGate, Neuralink, Paradromics), minimally invasive (Synchron's stent electrode), non-invasive (EEG). Speech neuroprostheses (2023–24 breakthroughs), Neuralink's trials. Ethics: neural data privacy.
- **N4. Decoding thoughts with scanners.** fMRI-based semantic decoders (2023): what they can and cannot do, consent.

### Part O — AGI and ASI: definitions and the timelines debate

- **O1. Definitions.** Narrow AI vs AGI vs ASI. OpenAI's charter definition ("highly autonomous systems that outperform humans at most economically valuable work"), DeepMind's "Levels of AGI" grid (2023), and practical "can it do a remote job?" tests.
- **O2. How people measure progress.** Benchmarks and saturation, ARC-AGI, METR's task "time horizon," Humanity's Last Exam, real-world deployments.
- **O3. The timelines debate.** Short-timeline views (AI 2027 scenario, some lab leaders), longer views (skeptics who see missing ingredients such as world models, continual learning and reliability), and forecasters' shifting medians. Teach the reader to ask "AGI by what definition, measured how?"
- **O4. What would change the picture.** Robots that work in arbitrary homes, AI doing original science end to end, reliable autonomy over weeks of work.

---

## 2. Glossary candidates (plain-English definitions)

Grouped by topic; alphabetize in the book's final glossary.

### General
1. **Artificial intelligence (AI)**: Computer systems that do tasks we normally associate with human intelligence, such as recognizing images, understanding language, making decisions or controlling machines.
2. **Narrow AI**: AI built for one task or domain, like a chess engine or a spam filter. Nearly all deployed AI is narrow.
3. **Artificial general intelligence (AGI)**: A hypothetical AI that can learn and perform most intellectual tasks a human can, across domains. There is no single agreed definition.
4. **Artificial superintelligence (ASI)**: A hypothetical AI that greatly exceeds the best humans at virtually every cognitive task.
5. **Machine learning (ML)**: Building programs that learn patterns from examples instead of following rules a programmer wrote by hand.
6. **Deep learning**: Machine learning using large neural networks with many layers. It has powered most AI progress since about 2012.
7. **Neural network**: A program made of many simple connected units ("neurons") whose connection strengths are adjusted during training so the network maps inputs to useful outputs.
8. **Model**: The trained artifact, a file full of learned numbers (parameters), that takes an input and produces an output.
9. **Training**: The process of adjusting a model's parameters using data until it performs well.
10. **Inference**: Using an already-trained model to produce answers. This is what happens each time you use an AI app.
11. **Dataset**: The collection of examples used to train or test a model.
12. **Label**: The "right answer" attached to a training example, such as "cat" on a cat photo.
13. **Supervised learning**: Learning from examples that come with labels.
14. **Unsupervised learning**: Finding structure, such as groups or clusters, in data without labels.
15. **Self-supervised learning**: Learning by hiding part of the data and predicting it, for example the next word or a masked patch of an image. It lets models learn from huge unlabeled datasets.
16. **Benchmark**: A standard test set used to compare AI systems' performance.
17. **Generalization**: How well a model performs on new examples it never saw in training.
18. **Overfitting**: When a model memorizes its training examples instead of learning the general pattern, so it fails on new data.
19. **Bias (in data/models)**: Systematic skew in a model's behavior, often inherited from unrepresentative training data, that makes it perform worse for some groups or situations.
20. **False positive / false negative**: A false positive is an alarm when nothing is there (a legitimate payment flagged as fraud). A false negative is a miss (fraud that slips through).
21. **Precision and recall**: Precision is the share of a model's "yes" answers that were correct. Recall is the share of real "yes" cases the model caught. Improving one usually costs the other.
22. **Multimodal**: Able to handle more than one kind of data, such as text, images, audio and video, in a single model.

### Classic and symbolic AI
23. **Symbolic AI ("GOFAI")**: "Good old-fashioned AI" that represents knowledge as explicit symbols and rules and reasons with logic.
24. **Expert system**: A 1970s–80s style program that encoded a human expert's knowledge as hundreds or thousands of IF-THEN rules.
25. **Knowledge graph**: A database of facts stored as connected triples, such as "Paris — capital of — France," that computers can traverse and query.
26. **Ontology**: A formal vocabulary that defines the types of things in a domain and how they relate (a "drug" treats a "disease").
27. **Search (AI sense)**: Systematically exploring possible sequences of actions to find one that reaches a goal.
28. **Heuristic**: A rule of thumb that guides search toward promising options without guaranteeing the best answer.
29. **A\* search**: A classic algorithm for finding the shortest path that combines distance traveled so far with an estimate of the distance remaining. It is used in maps and games.
30. **Game tree**: A branching diagram of all possible moves and counter-moves in a game.
31. **Minimax**: A game strategy that picks the move that is best for you, assuming your opponent always replies with the move that is worst for you.
32. **Monte Carlo tree search (MCTS)**: A search method that explores a game tree by playing out many sampled continuations and focusing effort on the moves that look best. It was central to AlphaGo.
33. **Fuzzy logic**: Logic in which statements can be partly true, such as "70% hot," useful for smooth control of appliances and machines.
34. **Bayes' theorem**: A formula for updating a belief when new evidence arrives. It combines how likely something was beforehand with how well it explains the evidence.
35. **Bayesian network**: A diagram of variables (like "smoker," "cough," "cancer") connected by arrows that encode probabilistic dependencies, used to reason under uncertainty.
36. **Causal inference**: Methods for figuring out whether X actually causes Y, not just whether they move together.
37. **Confounder**: A hidden third factor that causes two things and makes them look related. Hot weather drives both ice-cream sales and drownings.
38. **Counterfactual**: A "what would have happened if…" question, the hardest rung on the ladder of causal reasoning.
39. **A/B test**: An experiment that randomly shows users version A or B to measure which causes a better outcome. It is the workhorse of causal evidence in tech.
40. **Evolutionary algorithm**: An optimization method inspired by natural selection: generate many candidate solutions, keep the fittest, mutate and combine them, and repeat.
41. **Genetic algorithm**: A type of evolutionary algorithm that represents solutions as strings, like DNA, and uses crossover and mutation.
42. **Fitness function**: The score that tells an evolutionary algorithm how good a candidate solution is.
43. **Neuro-symbolic AI**: Systems that combine neural networks (pattern intuition) with symbolic components (logic, rules, proof checkers) to get both flexibility and rigor.

### Language (NLP)
44. **Natural language processing (NLP)**: The branch of AI that deals with human language: reading, writing, translating and extracting meaning.
45. **Token / tokenization**: Splitting text into pieces (words or word fragments) that a model processes as units.
46. **Text classification**: Assigning a category to a piece of text, such as spam vs not spam, or topic.
47. **Sentiment analysis**: Detecting the emotional tone of text, such as positive, negative or neutral.
48. **Named entity recognition (NER)**: Finding and labeling names of people, organizations, places, dates and so on in text.
49. **Information extraction**: Pulling structured facts (fields, tables, relationships) out of unstructured text such as contracts or medical notes.
50. **Machine translation (MT)**: Automatically translating text or speech between languages.
51. **Statistical machine translation**: The 1990s–2016 approach that translated using probabilities learned from huge collections of human-translated sentence pairs.
52. **Neural machine translation**: Translation done by neural networks end to end, the approach since about 2016.
53. **Transformer**: The neural-network design introduced in 2017 (originally for translation) that processes whole sequences using attention. It underlies modern chatbots, many vision models and robot models.
54. **Attention**: A mechanism that lets a model weigh which parts of its input matter most for each part of its output.
55. **Embedding**: A list of numbers that represents the meaning of a word, image, song or user, so that similar things have nearby numbers.
56. **Semantic search**: Search by meaning, using embeddings, rather than by exact keyword match.

### Computer vision
57. **Computer vision**: The branch of AI that extracts information from images and video.
58. **Pixel**: The smallest dot in a digital image, stored as numbers for red, green and blue brightness.
59. **Image classification**: Assigning one label to a whole image ("this is a golden retriever").
60. **Convolutional neural network (CNN)**: A neural network that slides small pattern detectors (filters) across an image, building up from edges to textures to objects.
61. **Vision transformer (ViT)**: A transformer applied to images by cutting them into small patches treated like words.
62. **ImageNet**: A dataset of over 14 million labeled images whose annual competition (2010–2017) drove the deep-learning revolution in vision.
63. **Object detection**: Finding each object in an image and drawing a box around it with a label.
64. **Bounding box**: The rectangle a detector draws around an object it found.
65. **Segmentation**: Labeling every pixel. *Semantic* segmentation says what class each pixel belongs to (road, car, sky). *Instance* segmentation separates individual objects (car #1, car #2). *Panoptic* does both.
66. **Mask**: The pixel-exact outline of an object produced by segmentation.
67. **Segment Anything Model (SAM)**: Meta's family of models that can outline any object in an image or video from a click, a box or (in SAM 3) a short text phrase.
68. **Optical character recognition (OCR)**: Turning images of printed or handwritten text into machine-readable text.
69. **Document AI**: Systems that understand whole documents (layout, tables, forms, signatures), not just the characters.
70. **Face detection vs face recognition**: Detection finds *that* there is a face. Recognition determines *whose* face it is, either by verification (one-to-one: are you the phone's owner?) or identification (one-to-many: who is this, out of millions?).
71. **Biometrics**: Identifying people from body characteristics such as face, fingerprint, iris, voice or gait.
72. **Pose estimation**: Detecting the positions of body joints (keypoints) to form a stick-figure skeleton of a person.
73. **Object tracking**: Following the same object across video frames.
74. **Action recognition**: Identifying what is happening in a video, such as "person falling" or "goal scored."
75. **Depth estimation**: Predicting how far away each point in an image is, even from a single camera.
76. **SLAM (simultaneous localization and mapping)**: Building a map of an unknown space while tracking your own position in it. Robot vacuums and AR headsets use it.
77. **Photogrammetry**: Reconstructing 3D shapes from many overlapping photos.
78. **Point cloud**: A 3D scene represented as millions of dots with x, y, z positions, the typical output of a lidar sensor.
79. **NeRF (neural radiance field)**: A 2020 technique that trains a neural network to represent a 3D scene from photos, so you can render it from new viewpoints.
80. **Gaussian splatting**: A 2023 technique that represents a 3D scene as millions of tiny colored, semi-transparent blobs. It renders photorealistic views in real time and is faster than NeRFs.
81. **Vision-language model (VLM)**: A model that takes images and text together and can describe, answer questions about, or reason over images.
82. **CLIP**: A 2021 OpenAI model trained on hundreds of millions of image–caption pairs to place pictures and words in the same meaning space. It is a foundation of image search and image generation.

### Speech and audio
83. **Waveform**: The raw wiggle of air pressure over time that a microphone records.
84. **Spectrogram**: A picture of sound showing which frequencies are loud at each moment. Many audio models "look" at spectrograms.
85. **Automatic speech recognition (ASR)**: Converting spoken audio into text (speech-to-text).
86. **Word error rate (WER)**: The standard ASR accuracy measure: the percentage of words wrongly substituted, deleted or inserted.
87. **Speaker diarization**: Figuring out "who spoke when" in a recording with several voices.
88. **Text-to-speech (TTS)**: Generating spoken audio from text.
89. **Voice cloning**: Making a TTS system speak in a specific person's voice from a sample recording, sometimes only seconds long.
90. **Speech-to-speech model**: A model that listens to audio and replies in audio directly, without converting to text in between. This makes conversation faster and more expressive.
91. **Latency**: The delay between input and response. In voice agents, delays over about a second feel unnatural.
92. **Turn-taking / barge-in**: Turn-taking is a voice agent's ability to know when you have finished speaking. Barge-in is your ability to interrupt it mid-sentence.
93. **Wake word**: A trigger phrase ("Hey Siri") detected by a tiny always-on model on the device.

### Generative media
94. **Generative AI**: AI that creates new content (text, images, audio, video, 3D, code) rather than only classifying or predicting.
95. **GAN (generative adversarial network)**: Two networks trained against each other: a generator makes fakes and a discriminator tries to spot them, until the fakes become convincing.
96. **Diffusion model**: A generator trained to remove noise. To create an image it starts from pure static and denoises step by step, guided by a prompt.
97. **Latent space**: A compressed internal "map" of possibilities inside a model, where nearby points correspond to similar content.
98. **Prompt**: The instruction or description you give a generative model.
99. **Inpainting / outpainting**: Inpainting regenerates a selected region inside an image. Outpainting extends the image beyond its borders.
100. **Text-to-video / image-to-video**: Generating a video clip from a written description, or animating a starting still image.
101. **World model**: A model that predicts how an environment will change in response to actions. Some generate interactive worlds you can walk through, and robots and agents can use them to "imagine" before acting.
102. **Deepfake**: Realistic synthetic media that depicts a real person saying or doing something they did not.
103. **Watermark (AI)**: A hidden signal embedded in generated content (for example Google's SynthID) so software can later detect that it was AI-made.
104. **Content Credentials (C2PA)**: An industry standard for attaching tamper-evident "nutrition labels" to media that record how it was created and edited.

### Reinforcement learning and games
105. **Reinforcement learning (RL)**: Learning by trial and error: an agent takes actions, receives rewards or penalties, and gradually learns which behavior maximizes reward.
106. **Agent (RL sense)**: The learner or decision-maker that acts in an environment. Note that "AI agent" in chatbot products means something related but broader.
107. **Environment**: The world, simulated or real, that the agent acts in and that responds to its actions.
108. **Reward**: The numeric score signal that tells an RL agent how well it is doing.
109. **Policy**: The agent's strategy: a rule (often a neural network) that maps what it observes to what it does.
110. **Value function**: An estimate of how much future reward the agent can expect from a given situation, its "sense of how good this position is."
111. **Exploration vs exploitation**: The trade-off between trying new things to learn (explore) and doing what is known to work (exploit).
112. **Self-play**: Training an agent by having it play against copies of itself, so it keeps facing an opponent at its own level.
113. **Deep Q-Network (DQN)**: DeepMind's 2013–15 system that learned to play dozens of Atari games from raw screen pixels and the score alone.
114. **Imperfect-information game**: A game where players cannot see everything, such as poker's hidden cards, which requires bluffing and probabilistic reasoning.
115. **RLHF (reinforcement learning from human feedback)**: Fine-tuning a model with rewards derived from human preference ratings. It helped turn raw language models into helpful chatbots.

### Robotics
116. **Robot**: A machine that senses its environment and physically acts on it, with some degree of autonomy.
117. **Sensor**: A device that measures the world, such as a camera, microphone, touch sensor or joint encoder.
118. **Actuator**: A motor or other device that makes a robot move.
119. **Degrees of freedom (DoF)**: The number of independent ways a robot can move. A human arm and hand have dozens.
120. **End effector / gripper**: The "hand" at the end of a robot arm: a pinch gripper, suction cup or multi-fingered hand.
121. **Manipulation**: Using hands or grippers to grasp, move and change objects.
122. **Locomotion**: Moving the robot's whole body around: walking, rolling, climbing.
123. **Humanoid robot**: A robot with a roughly human body shape (two arms, often two legs), designed to work in spaces built for people.
124. **Moravec's paradox**: The observation that tasks hard for humans (chess, calculus) are often easy for computers, while tasks easy for toddlers (walking, grasping) are very hard for robots.
125. **Simulation / sim-to-real gap**: Training robots in a virtual physics world is cheap and fast. The "gap" is the mismatch between simulation and reality that makes some skills fail when moved to a real robot.
126. **Domain randomization**: Training in simulations with randomly varied friction, lighting, weights and so on, so the robot copes with the real world as "just another variation."
127. **Teleoperation**: A human remotely controlling a robot, often to collect demonstration data or to rescue it when it gets stuck.
128. **Imitation learning / behavior cloning**: Teaching a robot by having it copy recorded human demonstrations.
129. **Vision-language-action model (VLA)**: A robot foundation model that takes camera images and a language instruction and outputs motor actions.
130. **Robot foundation model**: A large, general model pretrained on diverse robot (and web) data that can be adapted to many robots and tasks.
131. **Cross-embodiment**: Training one model on data from many different robot bodies so that skills transfer between them.
132. **Action chunking**: Having a robot policy predict a short sequence of future motions at once, which makes movement smoother and faster.
133. **Fleet learning**: Improving all robots or cars by pooling experience collected by every unit in the field.

### Autonomous vehicles
134. **Autonomous vehicle (AV)**: A vehicle that can drive itself for some or all of a trip.
135. **SAE levels of automation**: A 0–5 scale from the Society of Automotive Engineers. Levels 0–2 mean a human drives and supervises, Level 3 means the car drives but a human must take over when asked, Level 4 means no human is needed within a limited area or conditions, and Level 5 means anywhere a human could drive.
136. **Operational design domain (ODD)**: The specific conditions (area, roads, weather, speeds, times) in which an automated system is designed to work.
137. **Lidar**: A sensor that fires laser pulses and times their reflections to measure distance, producing a precise 3D point cloud.
138. **Radar**: A sensor that uses radio waves to measure distance and speed. It works in rain and fog but has coarse detail.
139. **Sensor fusion**: Combining several sensors' readings into one more reliable picture of the world.
140. **HD map**: A centimeter-accurate map of lanes, signs and curbs that some AVs use as prior knowledge.
141. **Perception–prediction–planning stack**: The classic AV pipeline: perceive what is around (perception), forecast what others will do (prediction), choose a path (planning), then steer and brake (control).
142. **End-to-end driving**: Replacing the hand-built pipeline with one large neural network trained to map sensor input directly to driving actions.
143. **Robotaxi**: A self-driving taxi with no human driver, booked through an app.
144. **Safety driver / safety monitor**: A human employee who sits in a test vehicle ready to intervene. "Monitor" usually means a passenger-seat observer with a stop button.
145. **Disengagement**: When the automated system hands control back to a human or a human takes over.

### Recommenders, ads and search
146. **Recommender system**: Software that predicts which items (videos, products, posts, songs) you will like and ranks them for you.
147. **Collaborative filtering**: Recommending things liked by people whose past behavior resembles yours.
148. **Content-based filtering**: Recommending items similar in content (genre, topic, features) to items you liked.
149. **Cold start**: The problem of recommending to brand-new users or new items with no history.
150. **Engagement**: Measurable user interaction (watch time, likes, shares, return visits) that platforms often optimize.
151. **Click-through rate (CTR)**: The fraction of people shown an item or ad who click on it. Predicting CTR is the core of ad AI.
152. **Ranking**: Ordering candidate items by predicted value, the heart of feeds and search engines.
153. **Filter bubble**: The concern that personalization shows people only what fits their existing views. The research evidence on its size is mixed.
154. **Ad auction / real-time bidding**: Advertisers' software bids for each individual ad slot in fractions of a second as a page or feed loads.
155. **Search index**: A giant pre-built lookup table of which web pages contain which words and concepts, so search can answer in milliseconds.
156. **PageRank**: Google's original algorithm (1998) that ranked pages by how many important pages linked to them.
157. **Retrieval-augmented generation (RAG)**: Having an AI model search a document collection first and then write its answer using what it found.

### AI for science
158. **Protein**: A molecular machine in living things, built from a chain of amino acids that folds into a precise 3D shape.
159. **Amino acid**: One of 20 building blocks that make up proteins, like letters in a word.
160. **Protein folding problem**: The 50-year challenge of predicting a protein's 3D shape from its amino-acid sequence, largely solved by AlphaFold 2 in 2020.
161. **AlphaFold**: Google DeepMind's protein-structure prediction system. AlphaFold 2 (2020) predicted single proteins, and AlphaFold 3 (2024) extended this to complexes with DNA, RNA and small molecules.
162. **pLDDT**: AlphaFold's per-residue confidence score (0–100), shown as colors on predicted structures.
163. **Protein design**: Creating new protein sequences that fold into desired shapes or perform new functions.
164. **Drug discovery pipeline**: Find a biological target → find or design a molecule → test in cells and animals → Phase I (safety), Phase II (does it work?) and Phase III (large confirmation) trials → approval. It typically takes 10+ years.
165. **Density functional theory (DFT)**: A physics-based computer method for calculating materials' properties. It is accurate but slow, and AI models now approximate it quickly.
166. **Numerical weather prediction (NWP)**: Traditional forecasting by simulating the atmosphere's physics equations on supercomputers.
167. **Ensemble forecast**: Running many slightly different forecasts to estimate the range and probability of outcomes.
168. **Reanalysis (ERA5)**: A decades-long, consistent reconstruction of past global weather. It is the main training data for AI weather models.
169. **Formal proof / Lean**: A proof written in a precise computer language (Lean is the most popular) that software can check step by step with no room for error.
170. **Automated theorem proving**: Getting computers to find proofs of mathematical statements.
171. **AI co-scientist**: An AI system (usually several cooperating LLM agents) that reads literature, generates hypotheses, debates them and proposes experiments.
172. **Self-driving (autonomous) lab**: A laboratory where robots run experiments chosen by AI, feeding results back to choose the next experiment.

### Industry, edge and BCI
173. **FDA clearance / 510(k)**: The US Food and Drug Administration's most common pathway for authorizing a medical device by showing it is substantially equivalent to an existing one. Most AI medical devices go this route.
174. **Computer-aided detection (CAD)**: Software that flags suspicious areas on medical images for a clinician to review.
175. **Ambient AI scribe**: Software that listens to a doctor–patient conversation and drafts the clinical note automatically.
176. **Fraud detection / anomaly detection**: Spotting unusual patterns, such as a card suddenly used abroad, that may signal fraud, faults or attacks.
177. **Credit scoring**: Predicting the likelihood that a borrower repays, which is regulated to prevent discrimination.
178. **Algorithmic / high-frequency trading**: Computer programs that trade automatically, sometimes thousands of times per second.
179. **Predictive maintenance**: Using sensor data to predict when a machine will fail so it can be fixed beforehand.
180. **Digital twin**: A live virtual replica of a physical system (factory, engine, city) used for monitoring and simulation.
181. **Precision agriculture**: Using sensors, cameras and AI to treat each plant or patch of field individually instead of the whole field uniformly.
182. **Lethal autonomous weapon system (LAWS)**: A weapon that can select and engage targets without further human intervention. Its regulation is debated at the UN.
183. **Human-in-the-loop / on-the-loop**: "In the loop" means a human must approve each decision. "On the loop" means the system acts by itself while a human supervises and can intervene.
184. **Vulnerability**: A flaw in software that an attacker could exploit. AI is increasingly used both to find and to exploit them.
185. **Edge AI**: Running AI models directly on local devices (phones, cars, cameras, sensors) instead of in remote data centers.
186. **NPU (neural processing unit)**: A chip, or part of a chip, specialized for running neural networks efficiently, now standard in phones and laptops.
187. **TOPS**: "Trillions of operations per second," a rough and often marketing-driven measure of an AI chip's speed.
188. **Quantization**: Storing a model's numbers with fewer bits (for example 4 instead of 16) so it runs faster and fits on smaller devices, at a small accuracy cost.
189. **TinyML**: Machine learning on tiny, low-power microcontrollers, such as a sensor that detects a machine's abnormal vibration.
190. **Internet of Things (IoT)**: Everyday physical objects (thermostats, cameras, meters, machines) connected to the internet and exchanging data.
191. **Federated learning**: Training a shared model across many devices by sending model updates, not raw personal data, to a central server.
192. **Brain-computer interface (BCI)**: A system that records brain activity and translates it, using AI decoders, into commands for a computer, speech or prosthetic.
193. **EEG**: Electroencephalography: recording brain electrical activity through sensors on the scalp. It is non-invasive but blurry.
194. **Neuroprosthesis**: A device that replaces or restores a lost function, such as speech or movement, by connecting to the nervous system.
195. **Neuromorphic computing / spiking neural network**: Hardware and models that imitate the brain's event-driven "spikes," aiming for much lower power use.

### AGI debate
196. **ARC-AGI**: A benchmark of visual grid puzzles (created by François Chollet in 2019) designed to test the ability to learn new skills from a few examples rather than recall knowledge.
197. **Task time horizon (METR)**: A measure of how long a task (in human-expert time) an AI agent can complete with 50% reliability. Its rapid growth is a key input to timelines debates.
198. **Benchmark saturation**: When top models score near the maximum on a test, so it no longer distinguishes them.
199. **Recursive self-improvement**: The hypothetical scenario where AI systems substantially speed up AI research itself, accelerating progress.
200. **Levels of AGI**: Google DeepMind's 2023 framework that rates AI by *performance* (Emerging, Competent, Expert, Virtuoso, Superhuman) and *generality* (narrow vs general) instead of a single AGI yes/no line.

---

## 3. Prerequisites and dependencies

What must be taught before what. Arrows read "must come before."

**Foundations shared with other chapters (assume these are taught earlier in the book):**
- "Data → model → prediction" and training vs inference → *everything here*.
- Neural networks as adjustable dials → CNNs, transformers, diffusion, VLAs.
- Embeddings → semantic search, recommenders, CLIP, RAG, image generation.
- Transformers and LLMs (from the chatbot chapters) → VLMs, VLAs, speech-to-speech models, AI co-scientists, Gemini Deep Think math.

**Within this domain:**
1. **Orientation map (A1–A3)** → all parts. Gives the reader a mental hook for each branch.
2. **Search and game trees (B1)** → MCTS → AlphaGo/AlphaZero (G2) → AlphaProof and test-time search (K7, G5).
3. **Probability and Bayes (B3)** → Bayesian networks → causal inference (B5) → reading safety statistics (I6), A/B tests in recommenders (J3), medical AI accuracy (L1).
4. **Symbolic AI (B2) + neural nets** → neuro-symbolic (B6) → AlphaGeometry and AlphaProof (K7).
5. **Evolutionary algorithms (B4)** → AlphaEvolve (K7) (LLM + evolution).
6. **Pixels as numbers (D1)** → classification (D2) → detection (D3) → segmentation (D4) → 3D vision (D9) → robot perception (H) and AV perception (I2).
7. **Spectrograms (E1)** → ASR (E2) and TTS (E3) → voice agents (E4); the latency concept (E4) → edge AI (M1).
8. **Classification and embeddings** → CLIP (D10) → text-to-image (F2) → video (F3) → world models (F5).
9. **Diffusion intuition (F1)** → image, video and music generation → diffusion-based robot action heads ("flow matching" in π0) (H6).
10. **RL loop (G1)** → game milestones (G2) → sim-to-real locomotion (H3) → RLHF and reasoning models (G4) → π*0.6 learning from experience (H6).
11. **Moravec's paradox (H1)** → why robotics lagged chatbots → the data problem (H5) → VLAs (H6) → humanoid hype check (H7).
12. **SAE levels (I1)** → AV stack (I2) → sensors (I3) → deployments and safety evidence (I5–I6).
13. **Ranking and embeddings** → recommenders (J2) → ads (J4) → search (J5) → RAG and AI answer engines.
14. **Proteins and amino acids (K1 intro)** → AlphaFold → protein design → drug discovery (K4). The basic drug pipeline must precede any "AI-designed drug" claims.
15. **NWP vs ML (K6)** requires ensembles and probability (B3).
16. **Formal proof / Lean (K7)** before AlphaProof; IMO context before IMO results.
17. **All branches** → industry tour (L), since the industry tour is applications of earlier tools.
18. **Model compression concepts** (quantization, from the compute chapters) → edge AI (M).
19. **Artificial neurons (N1)** → BCIs (N3), which need decoders = classification/regression.
20. **Everything** → AGI definitions and timelines (O). Teach last, after the reader has seen how uneven progress is across branches. That unevenness ("jagged frontier") is the key insight for judging AGI claims.

---

## 4. Current state and key facts (2025–2026)

### 4.1 Autonomous vehicles

**Waymo (Alphabet)**
- Safety data hub (data through June 2026): **271.3 million rider-only miles**. Compared with human drivers in the same cities: **~95% (94.82%) fewer crashes causing serious injury or worse**, 82% fewer injury-reported crashes, 93% fewer pedestrian-injury crashes, 82% fewer airbag-deployment crashes. These are company-computed comparisons against a human benchmark. — https://waymo.com/safety/impact/
- Independent and peer-reviewed context: a peer-reviewed paper (Kusano et al., *Traffic Injury Prevention*, ~56.7M miles through January 2025, authored by Waymo staff) found large reductions. The IIHS estimated somewhat smaller reductions (e.g., ~81% fewer injury crashes). Caveat: Waymo avoids heavy snow and most highway driving, so its conditions differ from typical human driving. — https://www.eweek.com/news/waymo-safety-stats/
- Scale: Waymo reported **~500,000 paid rides per week** in spring 2026 (after 250,000 in April 2025) and targets **1 million per week by end of 2026**. Fleet is ~3,500 vehicles, with 20M+ cumulative trips. — https://insideevs.com/news/791245/waymo-rides-per-week-2026-doubled/ ; https://www.automotiveworld.com/news/waymos-metric-for-2026-success-one-million-weekly-rides/
- Cities: a March 2026 expansion brought driverless service to 10 metros (Phoenix, SF Bay Area, Los Angeles, Austin, Atlanta, Miami, Dallas, Houston, San Antonio, Orlando). **Las Vegas went fully driverless July 8, 2026**, and Denver, San Diego and Tampa are next. — https://electrek.co/2026/07/08/waymo-driverless-las-vegas-four-new-cities/
- International: London service targeted for 2026 (testing underway). Tokyo commercial driverless service now targeted for 2027. As of mid-2026, no paid driverless rides abroad. — https://www.automotiveworld.com/articles/waymo-expands-into-europe-with-2026-london-robotaxi-debut/
- A forecasting analysis mentions a May 2026 software recall that paused freeway rides in some markets **[secondary source, unverified]**. — https://futuresearch.ai/app/p/a/waymo-weekly-paid-rides-q4-2026

**Tesla**
- Robotaxi launched in Austin in June 2025 with safety monitors aboard. By April 2026, rides with no employee onboard were running in Austin, Dallas and Houston. Later reports add Miami and other Florida cities. One September 2026 report says the fleet passed 1 million unsupervised miles with ~200+ unsupervised vehicles **[secondary source]**. The Bay Area service still uses safety drivers. — https://driveteslacanada.ca/news/tesla-robotaxi-expands-to-dallas-and-houston-with-fully-autonomous-rides/ ; https://cryptobriefing.com/tesla-million-unsupervised-robotaxi-miles/
- Consumer FSD (Supervised) remains a **Level 2** system: the driver must supervise. Musk called unsupervised FSD for customer cars in **Q4 2026** "a guess" (Electrek notes repeated missed targets). Tesla reported cumulative supervised FSD miles approaching **12 billion** on its Q2 2026 call. — https://electrek.co/2026/04/22/tesla-elon-musk-unsupervised-fsd-consumer-cars-q4-delay-again/ ; https://notateslaapp.com/news/4481/summary-of-teslas-2026-q2-earnings-call-cybercab-fsd-ai4-and-more
- Teaching point: Tesla uses cameras only and relies on end-to-end neural networks and fleet data. Waymo uses lidar, radar, cameras and HD maps. Both now use large learned models; the debate is about sensors, validation and scale.

**Zoox (Amazon)**
- Purpose-built vehicle with no steering wheel or pedals. By March 2026 it had ~2 million autonomous miles and 350,000+ riders on free rides (Las Vegas, San Francisco early-rider program), with Austin and Miami coming. — https://techcrunch.com/2026/03/24/zoox-brings-its-robotaxis-to-austin-and-miami
- On July 30, 2026, Zoox received NHTSA's first commercial exemption for a purpose-built robotaxi (capped at 2,500 vehicles/year). **Paid rides began in Las Vegas on August 10, 2026.** — https://lasvegassun.com/news/2026/aug/06/free-rides-no-more-zoox-robotaxi-service-to-begin/

**China and the Middle East**
- Baidu Apollo Go: **20M+ cumulative rides by February 2026** (weekly peak 300,000+ in Q4 2025) and ~3.2 million fully driverless rides in Q1 2026. Driverless commercial service in Dubai and Abu Dhabi, and London road tests in 2026 with public rides planned for 2027. — https://cnevpost.com/2026/07/28/baidu-apollo-go-robotaxi-road-tests-london/ ; https://www.nasdaq.com/press-release/baidus-apollo-go-commences-fully-driverless-commercial-ride-hailing-dubai-partners
- Pony.ai: global robotaxi fleet of **1,975 vehicles as of June 30, 2026**, targeting 3,500+ by year-end. — https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm
- WeRide operates robotaxis in China and Abu Dhabi (fleet counts not broken out in sources found).

**Historical anchors (well established):** DARPA Grand Challenge 2004 (no finisher) and 2005 (Stanford's "Stanley" won). The Google self-driving project started in 2009 and became Waymo in 2016, with fully driverless public rides in Phoenix in 2020. An Uber test vehicle killed a pedestrian in Tempe in March 2018. A Cruise robotaxi dragged a pedestrian in October 2023, California suspended its permit, and GM ended Cruise's robotaxi program in December 2024. Mercedes Drive Pilot became the first SAE Level 3 system certified in the US (Nevada 2023, California 2023).

### 4.2 Robotics and humanoids

**Robot foundation models (VLAs)**
- Physical Intelligence (π) timeline from its site: π0 (Oct 31, 2024), open-sourced π0 (Feb 4, 2025), π0.5 "open-world generalization" (Apr 22, 2025), real-time action chunking (Jun 2025), **π\*0.6 "a VLA that learns from experience"** using RL (Nov 17, 2025), human-to-robot transfer (Dec 2025), MEM long/short-term memory for 10+ minute tasks (Mar 3, 2026), RL Token for precise manipulation (Mar 19, 2026), **π0.7 "a steerable model with emergent capabilities" (Apr 16, 2026)**, and **Pi API beta "Frontier Models for Every Robot" (Oct 13, 2026)**. — https://www.pi.website/
- Google DeepMind Gemini Robotics: first models March 12, 2025 (Gemini Robotics and Gemini Robotics-ER), On-Device (June 2025). **Gemini Robotics 1.5 and ER 1.5 arrived Sept 25, 2025**: the model "thinks before acting," skills transfer across robot bodies (ALOHA 2, Apptronik Apollo, Franka), and ER 1.5 was offered to developers via the Gemini API. — https://deepmind.google/discover/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/
- **Gemini Robotics 2, ER 2 and On-Device 2 (announced July 30, 2026)** add whole-body humanoid control (walk, crouch, manipulate), dexterous tasks (screwing in a light bulb, tying knots) and multi-robot collaboration. ER 2 is in preview in Google AI Studio. Partners named include Apptronik, Agile Robots and Boston Dynamics, plus 100+ trusted testers. — https://deepmind.google/models/gemini-robotics/ ; https://en.wikipedia.org/wiki/Gemini_Robotics
- NVIDIA: Project GR00T was announced March 2024, followed by **GR00T N1, described as the first open humanoid foundation model (March 2025)**. In June 2026 NVIDIA announced the **Isaac GR00T reference humanoid** for academic research: a Unitree H2 Plus body, Sharpa tactile hands and Jetson Thor compute, available from Unitree in late 2026. Named users are Ai2, ETH Zurich, Stanford and UC San Diego. — https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-NVIDIA-Isaac-GR00T-Reference-Humanoid-Robot-for-Academic-Research
- Lineage to teach: Google RT-1 (2022) and RT-2 (2023, first widely known VLA built from a vision-language model), the Open X-Embodiment pooled dataset (2023, many robot types), and Stanford's ALOHA low-cost teleoperation rig (2023).

**Humanoid deployments and industry**
- Units shipped, 2025: Omdia estimates **13,318 humanoids shipped globally**, with AgiBot (5,168) ahead of Unitree (4,200). Unitree itself claims 5,500+. Counterpoint estimates ~16,000 installations with China >80%. — https://technode.com/2026/01/09/chinas-agibot-leads-global-humanoid-robot-shipments-in-2025-omdia-says/ ; https://www.scmp.com/tech/tech-trends/article/3340446/chinas-unitree-ships-more-5500-humanoid-robots-2025-surpassing-us-peers
- Figure AI: the Figure 02 pilot at BMW Spartanburg ran 10-hour shifts for 11 months, loading 90,000+ parts over 1,250+ runtime hours **[company claim]**. **Figure 03 began work at BMW in 2026** on parts sequencing, using the Helix 02 model to coordinate hands, arms, torso and feet. — https://figure.ai/news/f-03-at-bmw ; https://www.automotivelogistics.media/news-and-features/figuring-out-humanoid-logistics-at-spartanburg/2725217
- Agility (Digit): deployed or committed at nine customer sites with 65,000+ operating hours. GXO reached 100,000 totes moved in November 2025. Customers include Schaeffler, Toyota Canada and Mercado Libre **[company claims in SEC filing]**. — https://www.sec.gov/Archives/edgar/data/0002074973/000121390026097764/ea0297114-04.htm
- Boston Dynamics: production electric Atlas unveiled at CES on Jan 5, 2026. 2026 units go to Hyundai's robotics application center and Google DeepMind, and factory work at Hyundai's Georgia EV plant is planned from 2028. — https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/
- Tesla Optimus: V3 production was slated to begin at Fremont (converted Model S/X line) in late July/August 2026. One report says output rose to "several hundred" per week by August, mostly for internal use **[single secondary report]**. A Giga Texas Optimus factory is targeted for 2027. — https://driveteslacanada.ca/news/tesla-delaying-optimus-v3-reveal-fears-copycats/ ; https://www.basenor.com/blogs/news/tesla-optimus-production-ramp-6-details-that-matter
- 1X NEO (home humanoid): pre-orders opened Oct 28, 2025 at **$20,000 or $499/month**, with US deliveries planned in 2026. Tasks it cannot do autonomously can be done by a remote 1X operator (an "expert mode" that raises privacy questions). A Hayward, CA factory targets 100,000+/year by end-2027 **[company claim]**. I could not confirm whether consumer deliveries had begun by October 2026. — https://heise.de/-11287205 ; https://hoodline.com/2026/05/hayward-robot-plant-gears-up-to-crank-out-100-000-home-helpers/

### 4.3 Generative media, vision and audio

- **Video**: OpenAI launched Sora 2 with a social app on Sept 30, 2025, then **announced the Sora app's shutdown on March 24, 2026**, amid declining usage and a pivot to business tools. — https://engadget.com/ai/openai-is-shutting-down-its-sora-video-generation-app-211023358.html ; https://mynews13.com/fl/orlando/ap-top-news/2026/03/24/openai-pulls-the-plug-on-sora-the-viral-ai-video-app-that-sparked-deepfake-concerns
- Leading video models in mid-2026 per comparison guides **[secondary sources, rankings shift monthly]**: Google **Veo 3.1** (native audio, up to 4K, short clips extendable), Kuaishou **Kling 3.0** (multi-shot, multilingual audio), **Runway Gen-4.5** (creative control), ByteDance **Seedance 2.0**. Google's Veo 3 (May 2025) was the first major model to generate synchronized sound and dialogue with video. — https://upsampler.com/blog/best-ai-video-generators-sora-veo-kling-runway-2026
- **World models**: Genie 3 (Aug 2025) generates interactive 3D worlds at 720p/24fps that stay consistent for minutes. **Project Genie** opened to US Google AI Ultra subscribers on Jan 29, 2026, with ~60-second sessions. — https://techcrunch.com/2025/08/05/deepmind-reveals-genie-3-a-world-model-that-could-be-the-key-to-reaching-agi ; https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/
- **Segmentation and 3D**: Meta released **SAM 3** (segment and track objects from text "concept" prompts like "red baseball cap") and **SAM 3D** (Objects and Body reconstruction from a single image), both open, on Nov 19, 2025. — https://about.fb.com/news/2025/11/new-sam-models-detect-objects-create-3d-reconstructions/
- **Music**: Universal settled with Udio (Oct 2025) and Warner settled with Udio (Nov 2025). Warner settled with Suno, which is to launch licensed models in 2026. Udio signed Merlin (Jan 2026) and Kobalt (Apr 2026). Sony was still litigating in the reports found. — https://www.musicbusinessworldwide.com/universal-music-settles-udio-lawsuit-strikes-deal-for-licensed-ai-music-platform ; https://uk.marketscreener.com/news/warner-music-group-settles-copyright-case-with-suno-for-licensed-ai-music-ce7d5ed2db8bff22 ; https://www.musicbusinessworldwide.com/after-universal-warner-and-merlin-deals-now-udio-inks-licensing-agreement-with-kobalt
- Anchors (well established): Whisper (OpenAI, Sept 2022, 680,000 hours of training audio, open-source). WaveNet (2016). The US FCC ruled in Feb 2024 that AI-generated voices in robocalls fall under the TCPA robocall restrictions, after a fake-Biden robocall. NeRF (2020). 3D Gaussian Splatting (SIGGRAPH 2023). SAM 1 (April 2023, 1.1 billion masks) and SAM 2 (July 2024, video).

### 4.4 AI for science

- **Nobel Prizes 2024**: Physics to John Hopfield and Geoffrey Hinton for foundational work enabling machine learning with artificial neural networks. Chemistry to David Baker (computational protein design) and Demis Hassabis & John Jumper (protein structure prediction, AlphaFold). — https://www.nobelprize.org/prizes/physics/2024/summary/ ; https://www.nobelprize.org/prizes/chemistry/2024/summary/
- **AlphaFold DB** now describes **over 260 million structure predictions** (its background text still says "over 200 million"). In October 2026 it added AI-mined literature annotations linking residues and mutations to papers. — https://alphafold.ebi.ac.uk/
- **AI-designed drugs**: Insilico Medicine's rentosertib (AI-identified target TNIK plus AI-generated molecule) published Phase IIa results in *Nature Medicine* (June 2025): 71 patients with idiopathic pulmonary fibrosis, +98.4 mL lung capacity (FVC) at 60 mg vs −20.3 mL on placebo over 12 weeks. The trial was small, and larger trials are needed. — https://www.biospace.com/press-releases/insilico-medicine-announces-nature-medicine-publication-of-phase-iia-results-evaluating-rentosertib-the-novel-tnik-inhibitor-for-idiopathic-pulmonary-fibrosis-ipf-discovered-and-designed-with-a-pioneering-ai-approach
- Isomorphic Labs (DeepMind spin-out) had not dosed a human by May 2026 per secondary reporting, with first-in-human trials expected by end-2026 after slipping from 2025 **[secondary source]**. — https://www.layer3labs.io/guides/isomorphic-labs-explained
- **Materials**: GNoME (Nature, Nov 2023) predicted **2.2 million new crystal structures, ~380,000 of them stable**, and contributed them to the Materials Project. — https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/
- **Weather**: GraphCast (*Science*, 2023) and GenCast (*Nature*, Dec 2024, probabilistic ensembles) from Google DeepMind. ECMWF made its AI model AIFS operational in Feb 2025. **WeatherNext 2 (Nov 2025)** generates hundreds of scenarios in under a minute on one TPU, 8× faster than its predecessor, and powers Google Search, Gemini and Pixel Weather forecasts. — https://9to5google.com/2025/11/17/google-weathernext-2/ ; https://deepmind.google/discover/blog/gencast-predicts-weather-and-the-risks-of-extreme-conditions-with-sota-accuracy/
- **Mathematics**:
  - IMO 2024: AlphaProof + AlphaGeometry 2 reached silver standard (28/42), working in the formal language Lean and needing days of computation.
  - **IMO 2025: an advanced Gemini Deep Think scored 35/42 (gold standard), solving 5 of 6 problems in natural language within the 4.5-hour limit, officially graded by IMO coordinators** (announced July 21, 2025). OpenAI's experimental model also scored 35/42, graded by former medalists rather than official coordinators. — https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/
  - **IMO 2026 (Shanghai, July 2026)**: the *South China Morning Post* reported that RedNote's **dots-note-3.0** scored a perfect 42/42. Similar claims circulated for Huawei's "Celia" and, on social media, for models from OpenAI and others. **I could not verify official certification of any 2026 AI result.** The book should say "multiple labs reported perfect scores" only if confirmed closer to publication. — https://www.scmp.com/tech/article/3361482/worlds-first-ai-model-earn-perfect-score-maths-olympiad-comes-chinas-rednote
  - AlphaEvolve (May 2025): an LLM-guided evolutionary coding agent that found a 4×4 complex matrix multiplication using 48 multiplications (first improvement over Strassen's approach in that setting since 1969) and slightly improved bounds on open problems. An August 2026 preprint used it to nudge the matrix multiplication exponent bound to ~2.371177. — https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/ ; https://www.alphaxiv.org/abs/2608.16884
- **AI co-scientist** (Google, Feb 2025): a multi-agent Gemini system. Its proposed drug repurposing candidates for acute myeloid leukemia inhibited cancer cells in lab tests, it proposed liver-fibrosis candidates, and it independently re-derived an unpublished bacterial gene-transfer hypothesis. — https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/

### 4.5 Healthcare

- FDA's AI-Enabled Medical Device List: ~1,451 authorizations through end-2025. A secondary analysis counts **1,614 as of June 29, 2026**, with ~3/4 in radiology. The FDA notes the list is not exhaustive. — https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices ; https://www.complizen.ai/post/fda-has-cleared-1614-ai-medical-devices
- Ambient scribes are among the fastest-spreading clinical AI tools. Abridge (Best in KLAS for ambient speech in 2025 and 2026) and Microsoft Dragon Copilot (formed March 2025 from DAX Copilot and Dragon Medical One) lead, while Epic's built-in tool adds pressure. Reported outcomes include Intermountain Health's 27% reduction in time-in-notes per appointment. — https://www.aha.org/aha-center-health-innovation-market-scan/2026-04-14-6-health-systems-enhancing-care-delivery-ambient-ai-scribes ; https://medcitynews.com/2026/02/mount-sinai-microsoft-clinical-documentation/
- Anchor: IDx-DR (2018) was the first FDA-authorized autonomous AI diagnostic, for diabetic retinopathy screening without a specialist reading the image.

### 4.6 Brain-computer interfaces

- Neuralink: first human implant January 2024. A February 2026 article cites **21+ participants** using its "Telepathy" implant **[secondary source]**. As of mid-2026 reports, the vision implant "Blindsight" was still awaiting its first human implant. — https://aish.com/neuralinks-next-frontier-can-a-brain-implant-give-sight-to-those-born-blind/
- Anchors: BrainGate cursor control (2006). In 2023–24, speech neuroprostheses decoded attempted speech from people with paralysis or ALS at high accuracy (UCSF/Berkeley avatar study 2023; UC Davis study in *NEJM*, 2024, ~97% word accuracy). Synchron's stent-based electrode is inserted through a blood vessel without open-brain surgery.

### 4.7 AGI timelines

- Forecasters' views moved later during 2025 (including the authors of the "AI 2027" scenario) and then earlier again in early 2026, according to one tally of public updates **[commentary source]**. The AI Futures Project describes its updated forecasts for automated AI research and superintelligence on its blog. — https://blog.aifutures.org/p/clarifying-how-our-ai-timelines-forecasts ; https://www.lesswrong.com/posts/Tc5AbEpbFFdNx5nkP/a-visualization-of-changing-agi-timelines
- Useful stable references: DeepMind's "Levels of AGI" paper (Morris et al., 2023, arXiv:2311.02462). METR's "Measuring AI Ability to Complete Long Tasks" (2025, arXiv:2503.14499) found the task length AI agents can complete doubling roughly every 7 months since 2019. ARC Prize benchmarks: https://arcprize.org/
- Teaching stance: present the positions (short, medium and long timelines; "AGI is the wrong frame") with their reasons, not a verdict.

### 4.8 Other industries (stable anchors from training knowledge; verify before print)

- Recommenders: Netflix's own researchers wrote (2015) that about 80% of hours streamed came from recommendations. YouTube's product chief said in 2018 that over 70% of watch time came from recommendations. The Netflix Prize ($1M, 2006–2009) popularized collaborative filtering.
- Customer service: Klarna said in Feb 2024 that its AI assistant handled 2.3 million conversations in its first month (the work of ~700 agents). In 2025 the CEO said the company would again invest in human service quality. This makes a good "both sides" case study.
- Law: in *Mata v. Avianca* (S.D.N.Y. 2023), lawyers were sanctioned for filing ChatGPT-invented case citations.
- Cybersecurity: Google's Big Sleep agent found an exploitable SQLite bug (Nov 2024). DARPA's AI Cyber Challenge finals were at DEF CON in Aug 2025. In Nov 2025 Anthropic reported disrupting a largely AI-orchestrated cyber-espionage campaign.
- Agriculture: John Deere's See & Spray (from its 2017 Blue River acquisition) uses cameras to spray individual weeds, cutting herbicide use (company-reported).
- Edge: Microsoft's Copilot+ PC spec (2024) required an NPU of 40+ TOPS. Apple's Neural Engine debuted in 2017.
- Games anchors: Deep Blue (1997). AlphaGo 4–1 vs Lee Sedol (March 2016). AlphaZero (*Science*, 2018). MuZero (*Nature*, 2020). OpenAI Five beat Dota 2 world champions OG (April 2019). AlphaStar reached Grandmaster (*Nature*, Oct 2019). Pluribus beat pros at six-player no-limit poker (*Science*, 2019). CICERO reached human-level Diplomacy (*Science*, 2022).

---

## 5. Diagram ideas (24)

**D1. "Map of all AI branches" (chapter-opening fold-out).** A tree or subway map. Root: "Artificial Intelligence." Two trunks: **Symbolic AI** (branches: Search & Planning, Logic & Rules/Expert Systems, Knowledge Graphs, Fuzzy Logic, Bayesian Networks, Evolutionary Algorithms) and **Machine Learning** (branches: Supervised, Unsupervised, Reinforcement Learning). From ML grows **Deep Learning**, which splits into application limbs: Computer Vision (classification, detection, segmentation, OCR, faces, pose, 3D), Speech & Audio (ASR, TTS, music), Language/NLP (translation, extraction, LLMs/chatbots highlighted as "You are here"), Generative Media (image, video, 3D, world models), Robotics (locomotion, manipulation, VLAs), Autonomous Vehicles, Recommenders/Ads/Search, AI for Science (proteins, materials, weather, math). Dotted "bridge" lines show hybrids: Neuro-symbolic (Logic ↔ Deep Learning), AlphaGo (Search ↔ RL ↔ Deep Learning), AlphaEvolve (Evolution ↔ LLMs). Color-code by the five verbs (perceive/understand/create/decide/act). A side legend shows "Where you meet it daily" icons.

**D2. The five verbs of AI.** Five columns: PERCEIVE (eye, ear, page icons) → UNDERSTAND/PREDICT (brain) → CREATE (paintbrush) → DECIDE (chess knight) → ACT (robot arm/car). Under each, 3–4 example systems. A chatbot is shown spanning only "perceive text → create text," and a robot spans all five.

**D3. Milestone timeline 1950–2026 (beyond chatbots).** Horizontal line with stacked lanes for Games, Vision, Speech, Robotics/AVs, Science and Generative. Key dots: 1954 Georgetown MT, 1997 Deep Blue, 2005 DARPA Stanley, 2011 Watson/Siri, 2012 AlexNet, 2015 DQN, 2016 AlphaGo, 2018 Waymo One, 2019 AlphaStar/Pluribus, 2020 AlphaFold 2/NeRF, 2022 Whisper/Stable Diffusion, 2023 SAM/RT-2/Gaussian splatting, 2024 Nobel prizes/Sora preview/π0, 2025 IMO gold/Veo 3/Genie 3/π*0.6/Figure 03, 2026 Waymo ~500k rides/week, Gemini Robotics 2, Zoox paid rides.

**D4. How a computer sees.** Left: photo of a cat. Middle: zoomed 8×8 grid of numbers (RGB triplets). Right: CNN layers drawn as stacked panels labeled "edges → textures → parts (ears, eyes) → 'cat' 97%." Arrow labeled "learned filters, not programmed."

**D5. The four vision tasks on one photo.** A 2×2 grid using the same street photo. (a) Classification: one label "street scene." (b) Detection: boxes labeled car, person, bike. (c) Semantic segmentation: road purple, sidewalk pink, all people red. (d) Instance segmentation: each person a different color. Caption: "What? / What and where? / Which pixels? / Which pixels belong to which object?"

**D6. From photos to 3D: photogrammetry vs NeRF vs Gaussian splatting.** Three rows starting from the same ring of 30 phone photos around a statue. Row 1 → mesh of triangles. Row 2 → a neural network box queried per ray ("color & density at point x,y,z?"). Row 3 → a cloud of colored ellipsoid blobs rendered in real time. Columns: speed to train, rendering speed, quality, editability.

**D7. Sound → spectrogram → text, and back.** Top lane (ASR): microphone → waveform → spectrogram (time on x, pitch on y, brightness = loudness) → model → "Hello, how are you?" Bottom lane (TTS) reversed: text → model → spectrogram → vocoder → waveform → speaker. Side callout: "voice cloning = TTS conditioned on a 5-second voice sample."

**D8. Voice agent architectures and the latency budget.** Two pipelines. Cascade: ASR (300 ms) → LLM (500 ms) → TTS (300 ms), with a stacked bar showing total ~1.1 s. Speech-to-speech: a single model with a bar of ~0.3–0.6 s. Annotations show where barge-in detection and voice activity detection sit. Illustrative numbers only; label them as such.

**D9. Diffusion in six frames.** Frame 1 pure static → frames 2–5 progressively clearer → frame 6 "a red fox in snow, watercolor." Above, the prompt feeds into every step via an arrow labeled "guidance." Below, the training direction is reversed: real image → add noise → model learns to predict the noise.

**D10. The reinforcement learning loop.** Circle: Agent (robot/dog icon) → action → Environment (game/world) → new state + reward → back to Agent. Inside the agent, a box labeled "policy (what to do)" and "value (how good is this?)." Callouts: exploration vs exploitation; "reward can be delayed (win at move 200)."

**D11. The AlphaGo family tree.** Boxes left to right: AlphaGo (2016: human games + self-play + MCTS) → AlphaGo Zero (2017: no human games) → AlphaZero (chess, shogi, Go; one algorithm) → MuZero (2020: not told the rules; learns its own model) → offshoots: AlphaTensor/AlphaDev (algorithms), AlphaProof (math in Lean), AlphaEvolve (LLM + evolution). Each arrow is labeled with "what was removed or added."

**D12. Monte Carlo tree search in four steps.** A small tree drawn four times: Select (follow promising branch), Expand (add a new move), Simulate/Evaluate (neural network estimates the win chance), Backpropagate (update counts up the tree). Final panel: "most-visited move is played."

**D13. Robot control: the old way vs the VLA way.** Left: modular pipeline: Cameras → object detector → pose estimator → task planner (rules) → motion planner → controller → motors. Right: a VLA: camera images + "fold the towel" → [vision-language backbone pretrained on the web] → [action expert / diffusion or flow head] → action chunk (next ~1 s of joint targets at 50 Hz) → motors, with a feedback loop of new camera frames.

**D14. The robot data pyramid.** Bottom layer (widest): internet text, images and videos (billions, cheap, no actions). Next: human videos (egocentric cooking, assembly). Next: simulation and synthetic data (unlimited, sim-to-real gap). Next: cross-robot datasets (Open X-Embodiment). Top (narrowest, most valuable): teleoperated demonstrations on the target robot plus autonomous practice with RL (π*0.6). Arrows show cost per hour rising toward the top.

**D15. SAE levels as a ladder of responsibility.** Six rungs, 0–5. For each: "Who drives?", "Who watches the road?", "Who is the fallback?", plus an example. L2: Tesla FSD (Supervised), GM Super Cruise. L3: Mercedes Drive Pilot. L4: Waymo, Zoox, Apollo Go within a mapped city area. L5: none exists. A bold line between L2 and L3 is labeled "the human stops being responsible here."

**D16. The robotaxi sensor suite (top-down car).** A car seen from above with overlapping coverage cones: long-range lidar (360° circle), short-range lidars at the corners, radar cones (front/back), camera cones (13–29 cameras for Waymo-style), ultrasonic close range. A side panel compares a "camera-only" Tesla approach (8 cameras) with a table of strengths and weaknesses: cost, night, fog, depth precision, scalability.

**D17. The self-driving software stack vs end-to-end.** Top: Sensors → Perception ("there's a cyclist at 12 m") → Prediction ("she will turn left in 2 s, 70%") → Planning ("slow down, wait") → Control ("brake 20%"), with HD map and localization feeding in. Bottom: Sensors → [one big neural network] → steering/brake, with a "shadow" safety layer. Caption on the tradeoff between interpretability and scaling with data.

**D18. The recommendation funnel.** A funnel: "Billions of videos" → candidate generation (embeddings, "people like you," follows) → "~1,000 candidates" → ranking model (predicts watch time, like, share, skip) → "~100" → re-ranking (diversity, freshness, policy filters, ads inserted) → "your next 10 videos." A loop arrow from "your swipe/watch time" back into the models, labeled "every action is training data." Clock: "all within ~100–200 ms."

**D19. The ad auction in a blink.** Timeline from 0 ms to ~100 ms: page/feed loads → ad request with context and user signals → many advertiser bids computed by models (predicted click × value) → auction picks winner → ad displayed → click/conversion feeds back to training. A privacy sidebar covers cookies, device IDs, Apple tracking prompt, and on-platform data.

**D20. AlphaFold: from string to shape.** Left: amino-acid letter string "MKTAYIAK…". Middle: "evolutionary relatives" alignment and a neural network box. Right: folded ribbon structure colored by pLDDT (blue confident → orange low). Bottom strip: "Before: months to years per structure in the lab. After: minutes on a computer; 200M+ predictions free online." An inset shows AlphaFold 3 adding a drug molecule docked in a pocket.

**D21. The AI-for-science discovery loop.** A cycle: Literature & data → AI hypothesis generator (co-scientist) → AI model / simulation (AlphaFold, GNoME, weather model) → Robot lab experiment (self-driving lab) → New data → back. A human scientist icon in the center is labeled "sets goals, judges, interprets." A red note marks "the experiment is the bottleneck."

**D22. Weather forecasting: physics vs learned.** Two side-by-side pipelines. Traditional: observations → data assimilation → physics equations on a supercomputer (hours, thousands of CPUs) → forecast. AI: the same observations and analysis → neural network trained on 40+ years of ERA5 reanalysis → forecast in about a minute on one chip. Below: an ensemble "spaghetti plot" of 50 hurricane tracks showing how probability is communicated.

**D23. Edge vs cloud AI.** Left: phone/car/camera with an NPU chip icon: "fast, private, works offline, limited size, battery." Right: data center: "huge models, latest knowledge, costs per use, needs connection, data leaves device." Middle: a hybrid router arrow ("simple requests stay on-device; hard ones go to the cloud"). Examples are placed on a spectrum: wake word, face unlock, keyboard prediction → photo search → voice assistant → frontier chatbot.

**D24. Brain-computer interface pipeline.** Brain (motor/speech cortex) → electrode array (Utah array, Neuralink threads, stentrode in vessel, EEG cap: invasiveness vs signal quality scale) → amplifier/wireless → AI decoder (maps firing patterns to intended movement/phonemes) → output (cursor, text, synthesized voice, robotic arm) → visual/audio feedback to the user (closed loop).

**D25 (bonus). Levels of AGI grid.** A matrix with performance levels (Emerging, Competent, Expert, Virtuoso, Superhuman) as rows and Narrow vs General as columns. Narrow cells hold examples (spell-checker = Competent narrow, AlphaFold = Superhuman narrow, Stockfish = Superhuman narrow). General column: "Emerging AGI = early chatbots (per 2023 paper)"; higher cells are empty with question marks. Caption: "AGI is a region, not a line."

---

## 6. Practical exercises (easy → hard; no programming required)

Each exercise lists what to do and what the reader should learn. Tools change; the author should re-check URLs before print.

**E1. The invisible-AI audit (15 min, no tools).** For one day, write down every moment software makes a guess or a choice for you: unlock, autocorrect, photo search, maps ETA, spam folder, feed order, ad, card payment approval, streaming suggestion, smart-speaker wake word. Tag each with a verb (perceive/predict/create/decide/act).
*Learn:* AI is mostly invisible, narrow and embedded. Recommenders and classifiers outnumber chatbots in daily life.

**E2. Your phone as a vision lab (15 min).** Use Google Lens or Apple Visual Look Up/Live Text. (1) Point at a plant or dog breed. (2) Photograph a printed page and copy the text (OCR). (3) Translate a foreign menu live. (4) Search your photo library for "beach" or "receipt."
*Learn:* classification, OCR and translation run in seconds, partly on-device. Note failures (blurry text, rare objects) and connect them to training data.

**E3. Quick, Draw! (10 min).** At https://quickdraw.withgoogle.com draw six doodles and watch the network guess. Then browse the public doodle dataset for one category.
*Learn:* models learn from millions of examples, and "average" drawings are recognized best. This shows how datasets encode culture (e.g., how different countries draw a "chair").

**E4. Train your first image classifier with Teachable Machine (30 min).** At https://teachablemachine.withgoogle.com create an Image project with 3 classes (e.g., thumbs-up, thumbs-down, nothing). Capture ~50 webcam images each, train, and test. Then sabotage it: train "thumbs-up" only with a red shirt and test in a blue shirt.
*Learn:* training data, labels, generalization, overfitting and bias, all demonstrated hands-on.

**E5. Teachable Machine: sound and pose (30 min).** Make an Audio project (clap vs snap vs background noise) and a Pose project (standing vs squatting).
*Learn:* sound becomes a picture (spectrogram), and pose estimation turns a body into keypoints. The same "learn from examples" recipe works across senses.

**E6. Speech recognition stress test (30 min).** Use a Whisper demo on Hugging Face Spaces (search "whisper" at https://huggingface.co/spaces) or your chatbot's voice input. Record the same paragraph four ways: quiet room, noisy café, fast speech, a strong accent or second language. Count wrong words and compute word error rate = errors ÷ total words.
*Learn:* ASR is good but not equally good for everyone; noise and accents matter. Introduces WER and the idea of measuring a model.

**E7. Listen like an engineer: TTS and the ethics of cloning (20 min).** Try a TTS demo (built into most phones' accessibility settings, or free tiers of commercial voice tools). Compare an old robotic voice with a neural one, listening for pauses, emphasis and emotion. Do **not** clone anyone's voice without consent. Instead, discuss with family a "safe word" for phone calls claiming emergencies.
*Learn:* how natural TTS has become, why voice-clone scams work, and practical defenses.

**E8. Segment Anything playground (20 min).** Open Meta's Segment Anything demo (https://aidemos.meta.com, the SAM 3 playground) or a SAM Space on Hugging Face. Upload a cluttered photo. Click objects, then type concepts like "shoes" or "yellow things." Try a short video to track an object.
*Learn:* segmentation vs detection, promptable vision, and how text prompts now reach into vision models.

**E9. Image generation, the controlled experiment (30 min).** Pick one prompt ("a cozy reading nook at dusk, rain on the window, film photo"). Generate it in two different tools. Change one word at a time (style, lighting, lens). Then use inpainting to replace one object. Finally upload a result to https://contentcredentials.org/verify to see whether provenance data is attached.
*Learn:* prompts as specifications, the randomness of each generation, editing vs generating, provenance and watermark limits.

**E10. Make an 8-second video and audit its physics (30–45 min).** Using any available video model (e.g., Veo in the Gemini app or Flow, Kling, Runway), generate "a glass of water knocked off a table in slow motion" and "a person tying shoelaces." Watch frame by frame for impossible physics, morphing hands and object permanence errors.
*Learn:* video models learn appearance statistics, not physics engines. This is why "world models" are an active research area.

**E11. Reverse-engineer your feed (3 days, 10 min/day).** Create a fresh account on a short-video app or YouTube (or use a private window). Day 1: watch only woodworking videos to the end and skip everything else in under 2 seconds. Record the topics of the first 20 recommendations each day. Then visit your ad settings (Google "My Ad Center," Meta "Ad preferences," "Why am I seeing this ad?").
*Learn:* recommenders learn fast from implicit signals (watch time, skips). Introduces engagement optimization, cold start and the user controls that exist.

**E12. Wikidata: walk a knowledge graph (30 min).** Go to https://www.wikidata.org, look up "Marie Curie," and inspect statements (occupation, award received, spouse). Then open https://query.wikidata.org and run a built-in example query (e.g., "Cats"), changing one item.
*Learn:* knowledge as triples. This is how search engines answer "How tall is the Eiffel Tower?" without reading pages, and where symbolic AI lives today.

**E13. Bayes with your hands (20 min, paper).** A disease affects 1 in 100 people. A test catches 90% of sick people but wrongly flags 9% of healthy people. Draw 1,000 dots: 10 sick (9 test positive), 990 healthy (~89 test positive). What fraction of positives are actually sick? (About 9/98 ≈ 9%.)
*Learn:* base rates, false positives, and why medical AI, fraud AI and face recognition at scale produce many false alarms.

**E14. Correlation is not causation (30 min).** Use Gapminder (https://www.gapminder.org/tools) to plot two variables that correlate (e.g., number of TVs per person vs life expectancy). Write down three possible confounders.
*Learn:* prediction models find correlations, and decisions need causal thinking. Introduces confounders and A/B tests.

**E15. Watch evolution solve a problem (20 min).** Run a browser genetic-algorithm car or walker simulator (e.g., "BoxCar2D"-style demos such as https://rednuht.org/genetic_cars_2/). Watch the generations, then change the mutation rate.
*Learn:* fitness functions, mutation and selection, and how optimization without understanding can still find clever (sometimes weird) solutions.

**E16. Play against superhuman search (30 min).** On https://lichess.org play a game, then open "Analysis board" with the engine on. Watch the evaluation bar and the engine's top lines. Find your biggest mistake.
*Learn:* search plus learned evaluation (Stockfish now uses a neural net). Gives a feel for game trees, and for what "superhuman narrow AI" means.

**E17. Explore a protein in the AlphaFold Database (30 min).** At https://alphafold.ebi.ac.uk search "hemoglobin" (human) and "green fluorescent protein." Rotate the structure, read the color-coded confidence (pLDDT), and find regions of low confidence (often floppy, disordered parts). Compare with the experimental structure at https://www.rcsb.org.
*Learn:* sequence → structure, what a confidence score means, why this earned a Nobel, and its limits (disorder, complexes, dynamics).

**E18. AI vs physics weather forecasts (15 min/day for a week).** On ECMWF's open charts (https://charts.ecmwf.int) compare the AI model (AIFS) with the physics model (IFS) for your region, or track a tropical storm's ensemble. Keep a log of which was closer.
*Learn:* ML forecasting is now operational, ensembles express uncertainty, and how to judge a forecast fairly.

**E19. Read a safety claim like a scientist (30 min).** Open Waymo's safety hub (https://waymo.com/safety/impact/). Write down the headline percentages, the miles, the comparison group (human benchmark in the same cities) and what is excluded (snow, many highways). Then find one independent analysis (e.g., IIHS).
*Learn:* operational design domain, benchmarks, base rates and conflicts of interest. These skills transfer to every "AI is X% better" claim.

**E20. Scan an object into 3D with your phone (30 min).** Use a free 3D-capture app that supports Gaussian splats (e.g., Scaniverse, Polycam or Luma). Walk slowly around a plant or shoe and view the result. Try a shiny or transparent object.
*Learn:* photogrammetry vs Gaussian splatting, why reflective and transparent surfaces fail, and how robots and AR "see" in 3D.

**E21. Robot-demo detective (30 min).** Watch three robot videos (e.g., a Physical Intelligence π0.5/π0.7 demo, a Figure or 1X home demo, a Unitree acrobatics clip). For each, answer: Is it autonomous or teleoperated (check the caption)? Is it sped up? How many attempts? Is the task new to the robot or rehearsed? Then list five household tasks you think are hardest for robots and explain why using Moravec's paradox.
*Learn:* critical viewing of hype, the data problem, and why folding laundry is a frontier problem.

**E22. Ask an embodied-reasoning model to "point" (45 min, free account needed).** In Google AI Studio, select a Gemini Robotics-ER model (preview availability may vary) or any multimodal model. Upload a photo of your kitchen counter and ask: "Point to the objects I'd need to make tea, return coordinates, and give a step-by-step plan for a robot arm."
*Learn:* how VLMs ground language in pixels (the "brain" layer of a VLA) and where spatial reasoning breaks.

**E23. Build a no-code voice receptionist (60–90 min).** Use a free tier of a voice-agent builder (several platforms offer drag-and-drop phone agents). Give it a script for a fictional bakery (hours, menu, take a pickup order). Call it and test interruptions, mumbling, off-script questions and silence. Time the response delay with a stopwatch.
*Learn:* the voice stack (ASR → LLM → TTS or speech-to-speech), latency, barge-in, guardrails, and a real small-business opportunity.

**E24. Prove 2 + 2 = 4 the way AlphaProof does (60+ min).** Play the first levels of the Natural Number Game in Lean (https://adam.math.hhu.de, choose "Natural Number Game").
*Learn:* what a formal proof is, why a computer can check it perfectly, and why math became a reinforcement-learning playground (verifiable reward).

**E25. Mini-project: map AI opportunities in your own job (2 hours).** List 20 recurring tasks you do. For each, tag which AI branch could help (vision, speech, extraction, recommendation, forecasting, robotics, generation), the data needed, the risk if wrong, and whether a human must stay in the loop. Pick one and pilot it with an off-the-shelf tool.
*Learn:* translating branches into real value, and judging when AI is (and is not) appropriate.

---

## 7. Areas of opportunity (careers, businesses, open problems)

### Computer vision
- **Careers:** data annotation leads and labeling-quality managers, vision QA for manufacturing, retail analytics, medical imaging specialists, drone and satellite image analysts, AR/3D capture (real estate, insurance claims, heritage preservation via Gaussian splats).
- **Businesses:** visual inspection for small manufacturers (now cheap with off-the-shelf models plus SAM-style annotation), document automation for SMEs (invoices, forms), 3D product capture for e-commerce, sports video analytics for amateur leagues, accessibility tools for the blind and low-vision.
- **Open problems:** robustness to unusual conditions, small-object and long-tail recognition, real 3D/physical understanding from video, fair performance across demographics, privacy-preserving vision.

### Speech and audio
- **Careers:** voice-agent designers ("conversation designers"), voice QA testers, localization and dubbing producers, audio forensics (deepfake detection), clinical documentation specialists.
- **Businesses:** voice receptionists for clinics, restaurants and trades; dubbing and localization of creator content; low-resource-language ASR and TTS; hearing and speech accessibility; call analytics for compliance.
- **Open problems:** natural turn-taking and emotion, robust performance across accents and low-resource languages, reliable voice-clone detection, consent and licensing frameworks for voices, on-device real-time translation.

### Generative media and world models
- **Careers:** AI-assisted video producers, previsualization artists, brand-safety and provenance specialists, synthetic-data engineers (generating training data for robots and AVs), game designers using world models.
- **Businesses:** ad creative at scale for small brands, personalized education video, licensed-music generation for creators (post-settlement licensing models), virtual production for indie film, synthetic training environments.
- **Open problems:** long-form consistency (characters, physics), controllability, copyright and compensation models, reliable provenance, real-time interactive world generation, using world models to train robots.

### Reinforcement learning, games, planning
- **Careers:** RL environment designers (building the "gyms" that train AI agents is a growth area), simulation engineers, operations-research/optimization specialists.
- **Businesses:** scheduling and logistics optimization, energy and HVAC control, pricing, game AI and testing bots.
- **Open problems:** sample efficiency (learning from few trials), reward design without loopholes ("reward hacking"), safe exploration in the real world, transferring game-style success to messy domains.

### Robotics
- **Careers:** teleoperators and robot data collectors (a new job category), robot fleet technicians, field deployment engineers, safety certification specialists, simulation artists.
- **Businesses:** robots-as-a-service for warehouses and factories, robot data collection services, specialized grippers and tactile sensors, robot training environments, integration consultants for small factories, eldercare assistance (long-term).
- **Open problems:** dexterous manipulation of deformable objects, reliability (99.9%+ success over long shifts), safety around people, cost per hour vs human labor, battery life, generalization to new homes, learning from human video at scale, standards for teleoperation transparency and privacy.

### Autonomous vehicles and mobility
- **Careers:** remote assistance operators, fleet operations managers, AV safety analysts, mapping specialists, policy and regulatory roles in cities.
- **Businesses:** depots, charging and cleaning for robotaxi fleets; insurance products for AVs; autonomous trucking corridors; delivery robots for campuses; accessibility services for elderly and disabled riders.
- **Open problems:** bad weather, highway speeds at scale, interacting with police and emergency scenes, validation and statistically convincing safety cases, mixed traffic in dense developing-world cities, economics of sensors and vehicles.

### Recommenders, ads and search
- **Careers:** recommendation and ranking engineers, experimentation (A/B test) analysts, trust and safety specialists, "generative engine optimization" for brands, privacy engineers.
- **Businesses:** recommendation engines for niche e-commerce and media, retail media networks, AI-search visibility consulting, tools that give users control over their own feeds.
- **Open problems:** optimizing for long-term well-being rather than short-term engagement, measuring societal effects, privacy-preserving ad measurement, fair compensation for publishers when AI answers directly.

### AI for science
- **Careers:** computational biologists, "AI + wet lab" scientists, lab automation engineers, materials informatics specialists, research software engineers, science communicators.
- **Businesses:** AI-native biotech and drug discovery, protein design for enzymes (industrial, food, plastic recycling), materials for batteries and carbon capture, climate and weather risk analytics for insurers and farmers, contract self-driving labs.
- **Open problems:** experimental validation bottlenecks, models of dynamic (moving) proteins and cells, data quality and negative results, AI-generated hypotheses that are new rather than recombined, formal verification of math beyond competitions, trusted AI forecasts of extreme weather.

### Industry applications
- **Healthcare:** ambient documentation, prior-authorization automation, imaging triage, AI for low-resource clinics. *Open problems:* prospective evidence of patient benefit, bias, liability, monitoring model drift after deployment.
- **Finance:** real-time fraud with deepfake-resistant identity verification, compliance (AML) automation, explainable credit decisions. *Open problems:* adversarial fraudsters using AI, fairness law compliance.
- **Law:** contract analysis, e-discovery, access-to-justice tools for people who can't afford lawyers. *Open problems:* hallucinated citations, confidentiality, unauthorized practice of law rules.
- **Education:** tutoring that improves learning rather than giving answers, teacher planning and feedback tools, assessment redesign.
- **Customer service and marketing:** hybrid human+AI service desks, multilingual support, creative testing.
- **Manufacturing and agriculture:** visual inspection, predictive maintenance retrofits, precision spraying, robotic harvesting (still hard), livestock health monitoring.
- **Defense and security:** counter-drone systems, AI red-teaming, vulnerability discovery services, AI-incident response. *Open problems:* meaningful human control, escalation risks, international norms.
- **Cybersecurity:** AI-assisted patching, phishing and voice-fraud defense for small businesses and families.

### Edge AI and IoT
- **Careers:** embedded ML engineers, model compression specialists, hardware–software co-designers.
- **Businesses:** private on-device assistants, smart cameras that never upload video, industrial sensors with on-device anomaly detection, wearables for health.
- **Open problems:** fitting capable models in limited memory and power, updating models securely in the field, battery life.

### Brain-computer interfaces
- **Careers:** neural engineers, clinical trial coordinators, neuroethicists.
- **Opportunities:** communication restoration for ALS and stroke, rehabilitation, non-invasive wellness (with caution).
- **Open problems:** implant longevity, wireless bandwidth, decoder recalibration, neural data privacy law.

### AGI-adjacent
- **Careers:** AI evaluation and benchmark design, AI safety and alignment research, AI policy, forecasting.
- **Open problems:** measuring general capability, continual learning, reliability over long tasks, deciding what "AGI" should mean for law and contracts.

---

## 8. Common misconceptions to correct

1. **"AI = chatbots."** Chatbots are one branch. Most AI the reader encounters daily (feeds, spam filters, fraud checks, photo search, maps) is not a chatbot and has been around for over a decade.
2. **"AI understands images like we do."** Vision models find statistical patterns in pixels. They can be fooled by small changes and fail on unusual angles or lighting, even while beating humans on benchmarks.
3. **"Face recognition is either perfect or useless."** Accuracy depends on image quality, demographics and the decision threshold. At population scale even 99.9% accuracy produces many false matches (the base-rate problem).
4. **"AI-generated video simulates physics."** Video models imitate how things *look* when they move. They do not compute forces, which is why liquids, hands and collisions often go wrong.
5. **"Deepfake detectors will save us."** Detection is an arms race. Provenance (signing real media at capture and labeling AI media) plus media literacy and verification habits are more reliable.
6. **"Self-driving cars are always 5 years away."** Driverless robotaxis already give hundreds of thousands of paid rides per week (Waymo), and more in China. They operate in limited areas and conditions, though, not everywhere (Level 4, not Level 5).
7. **"Tesla FSD is a self-driving car."** Consumer FSD (Supervised) is Level 2: the human is legally the driver and must watch the road at all times. Tesla's robotaxi service in some cities is a separate, limited operation.
8. **"Humanoid robots are about to be in every home."** Shipments are in the tens of thousands per year globally. Many impressive demos are teleoperated, sped up or rehearsed, and home robots that work reliably in any home remain an unsolved problem.
9. **"Robots are hard because of the mechanics."** Hardware matters, but the bigger bottleneck is *data and generalization*. There is no internet-scale dataset of robot actions (Moravec's paradox).
10. **"AlphaFold solved biology / cured diseases."** AlphaFold predicts static structures very well. Proteins move, interact in cells and need testing, and drugs still take ~10 years and mostly fail in trials. By late 2026, AI-designed drugs had reached mid-stage trials but none had been approved.
11. **"AI weather models don't need physics data."** They are trained on decades of physics-based reanalysis and still depend on traditional observation and data-assimilation systems to start each forecast.
12. **"An AI got IMO gold, so it's a better mathematician than mathematicians."** Competition problems are hard but have known answers and fit in a few pages. Research math involves choosing questions, building theories and working over years. AI is starting to contribute (AlphaEvolve bounds, formal proofs) but is not a replacement.
13. **"The algorithm is a neutral mirror of what I like."** Recommenders optimize targets the platform chooses (often engagement), and what they show shapes what you come to like.
14. **"Recommenders and ads 'listen through your microphone'."** There is no credible evidence of mass covert audio eavesdropping for ads. Behavioral data, location, purchases, contacts and lookalike modeling explain the eerie accuracy.
15. **"Old-fashioned symbolic AI is dead."** Search, planning, rules, knowledge graphs and formal verification run in maps, airline scheduling, chip design, tax software and math proof checkers, and they are being combined with neural networks.
16. **"More data always fixes it."** Biased, unrepresentative or mislabeled data scales up the bias. Distribution shift (the world changing) can break any model.
17. **"Correlation found by AI is a discovery."** Without causal reasoning or experiments, predictive patterns can be confounded and fail when acted upon.
18. **"Edge AI is just weaker cloud AI."** On-device AI is chosen for latency, privacy, offline use and cost, not only because of limitations. Many tasks (face unlock, wake words) *must* run locally.
19. **"Brain implants read your thoughts."** Current BCIs decode specific trained signals (intended movement, attempted speech) from specific brain areas, with the user's cooperation. They are not general mind-readers, though neural privacy is a real future concern.
20. **"AGI has a precise definition and a date."** There are many definitions and forecasts disagree widely. Progress is "jagged": superhuman at some tasks while failing at simple ones.
21. **"RL means robots learning by themselves in the real world."** Most RL happens in simulation or games because real-world trial and error is slow, costly and risky. Real-world RL (e.g., π*0.6) is a recent frontier.
22. **"Music/image AI is legally settled."** Lawsuits and licensing deals were still evolving in 2025–26 (label settlements with Udio and Suno, ongoing cases elsewhere). Rules vary by country.

---

## 9. Analogies that work for beginners

- **The AI tree / family reunion.** AI is a big family. Grandparents are "rules" (symbolic AI) and "learning" (machine learning). Chatbots are the famous grandchild everyone talks about, but the cousins (vision, speech, robotics, recommenders) have been working quietly for years.
- **Pixels as a paint-by-numbers grid.** A photo is a paint-by-numbers board with millions of tiny numbered squares. The computer only sees the numbers.
- **CNN as a team of detectives with magnifying glasses.** The first detectives spot only edges, the next team combines edges into shapes, the next into eyes and ears, and the last one says "cat."
- **Detection vs segmentation: highlighter vs scissors.** Detection draws a box around something with a highlighter. Segmentation cuts it out precisely with scissors.
- **Spectrogram as sheet music for any sound.** A spectrogram is like a piano roll showing which notes (frequencies) play when, for speech, birdsong or engines.
- **Diffusion as a sculptor revealing a statue in marble.** It starts from a noisy block and chips away the noise, guided by your description.
- **GAN as forger vs art detective.** Each gets better by trying to beat the other.
- **RL as training a dog with treats.** No instructions, only rewards; the dog figures out what earns treats, sometimes in unexpected ways (reward hacking = the dog learns to look sad to get treats).
- **Exploration vs exploitation as choosing restaurants.** Go back to your favorite (exploit) or try the new place (explore)?
- **MCTS as imagining several futures in your head before a chess move,** spending more imagination on the most promising lines.
- **Self-play as practicing tennis against a perfect clone of yourself** who improves exactly as fast as you do.
- **Moravec's paradox: the toddler and the chess master.** A toddler easily picks up a sock; a chess grandmaster computer can't. What's easy for us is hard for machines, and vice versa.
- **Teleoperation data as a driving instructor's dual pedals.** A human controls the robot while it watches and records, so it can later imitate.
- **VLA as an apprentice who's read every cookbook but never cooked.** It knows what "dice an onion" means from the web, but must learn the knife work from demonstrations and practice.
- **Sim-to-real as a flight simulator.** Pilots train in simulators, but the first real landing still feels different. Domain randomization is training in every kind of simulated weather so the real one isn't a surprise.
- **SAE levels as who holds the steering wheel and who is to blame.** At Level 2 you are a supervisor with your hands near the wheel. At Level 4 you are a passenger in the back seat, but only within the neighborhood the car knows.
- **Lidar as a bat's echolocation with light; radar as echolocation with radio** (sees through fog but blurry); **cameras as eyes** (rich detail but no direct distance).
- **Recommender as a shopkeeper who remembers everything you ever lingered on,** and everyone else's habits too, rearranging the store's front table each time you walk in.
- **Collaborative filtering as "people who bought this also bought…" at planetary scale.**
- **Embeddings as GPS coordinates for meaning.** Similar songs, words or people have nearby coordinates.
- **Search index as the index at the back of a book,** but for the entire web, built before you ask.
- **Protein folding as origami from a string of beads,** where the bead sequence determines the final shape, and the shape determines the job (key-and-lock).
- **AlphaFold DB as a free library of 3D origami instructions** for nearly every known protein.
- **AI weather model as an experienced forecaster who has studied 40 years of weather maps** and recognizes patterns, versus a physicist solving equations from scratch every time.
- **Formal proof checker as a merciless spell-checker for logic.** It accepts nothing that isn't fully justified, which makes it a perfect referee for AI training.
- **AI co-scientist as a tireless research assistant who has read every paper,** brainstorms many hypotheses and argues about them, but can't run the experiment.
- **Edge vs cloud: a calculator in your pocket vs calling an expert on the phone.** The pocket one is instant and private; the expert knows more but needs a connection and costs per call.
- **Quantization as compressing a high-resolution photo into a smaller JPEG.** You lose a little detail and gain a lot of speed and space.
- **BCI as a very smart translator listening to a crowd's murmur in one stadium section** (neurons) and learning to infer what the crowd wants.
- **Bayesian updating as a detective revising suspicion as each clue arrives.**
- **Evolutionary algorithm as dog breeding for solutions.** Keep the best, cross them, add random variation, repeat for many generations.
- **AGI debate as arguing over when a child "becomes an adult".** People mean different things (voting age, independence, maturity). Ask which definition before arguing about the date.
- **The jagged frontier as a coastline.** AI capability isn't a smooth wall rising evenly; it juts far out in some places (protein folding, Go) and is far inland in others (folding laundry, reliable long tasks).

---

### Source list (primary URLs used above)

Waymo safety: https://waymo.com/safety/impact/ · Waymo scale: https://electrek.co/2026/07/08/waymo-driverless-las-vegas-four-new-cities/ , https://insideevs.com/news/791245/waymo-rides-per-week-2026-doubled/ , https://www.automotiveworld.com/news/waymos-metric-for-2026-success-one-million-weekly-rides/ · Waymo international: https://www.automotiveworld.com/articles/waymo-expands-into-europe-with-2026-london-robotaxi-debut/ · Waymo safety context: https://www.eweek.com/news/waymo-safety-stats/ · Tesla: https://driveteslacanada.ca/news/tesla-robotaxi-expands-to-dallas-and-houston-with-fully-autonomous-rides/ , https://electrek.co/2026/04/22/tesla-elon-musk-unsupervised-fsd-consumer-cars-q4-delay-again/ , https://notateslaapp.com/news/4481/summary-of-teslas-2026-q2-earnings-call-cybercab-fsd-ai4-and-more , https://cryptobriefing.com/tesla-million-unsupervised-robotaxi-miles/ · Zoox: https://techcrunch.com/2026/03/24/zoox-brings-its-robotaxis-to-austin-and-miami , https://lasvegassun.com/news/2026/aug/06/free-rides-no-more-zoox-robotaxi-service-to-begin/ · Apollo Go: https://cnevpost.com/2026/07/28/baidu-apollo-go-robotaxi-road-tests-london/ , https://www.nasdaq.com/press-release/baidus-apollo-go-commences-fully-driverless-commercial-ride-hailing-dubai-partners · Pony.ai: https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm · Physical Intelligence: https://www.pi.website/ · Gemini Robotics: https://deepmind.google/models/gemini-robotics/ , https://deepmind.google/discover/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/ , https://en.wikipedia.org/wiki/Gemini_Robotics · NVIDIA: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-NVIDIA-Isaac-GR00T-Reference-Humanoid-Robot-for-Academic-Research · Humanoid shipments: https://technode.com/2026/01/09/chinas-agibot-leads-global-humanoid-robot-shipments-in-2025-omdia-says/ , https://www.scmp.com/tech/tech-trends/article/3340446/chinas-unitree-ships-more-5500-humanoid-robots-2025-surpassing-us-peers · Figure: https://figure.ai/news/f-03-at-bmw , https://www.automotivelogistics.media/news-and-features/figuring-out-humanoid-logistics-at-spartanburg/2725217 · Agility: https://www.sec.gov/Archives/edgar/data/0002074973/000121390026097764/ea0297114-04.htm · Boston Dynamics: https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/ · Tesla Optimus: https://driveteslacanada.ca/news/tesla-delaying-optimus-v3-reveal-fears-copycats/ , https://www.basenor.com/blogs/news/tesla-optimus-production-ramp-6-details-that-matter · 1X: https://heise.de/-11287205 , https://hoodline.com/2026/05/hayward-robot-plant-gears-up-to-crank-out-100-000-home-helpers/ · Sora: https://engadget.com/ai/openai-is-shutting-down-its-sora-video-generation-app-211023358.html · Video models: https://upsampler.com/blog/best-ai-video-generators-sora-veo-kling-runway-2026 · Genie: https://techcrunch.com/2025/08/05/deepmind-reveals-genie-3-a-world-model-that-could-be-the-key-to-reaching-agi , https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/ · SAM 3: https://about.fb.com/news/2025/11/new-sam-models-detect-objects-create-3d-reconstructions/ · Music: https://www.musicbusinessworldwide.com/universal-music-settles-udio-lawsuit-strikes-deal-for-licensed-ai-music-platform , https://uk.marketscreener.com/news/warner-music-group-settles-copyright-case-with-suno-for-licensed-ai-music-ce7d5ed2db8bff22 , https://www.musicbusinessworldwide.com/after-universal-warner-and-merlin-deals-now-udio-inks-licensing-agreement-with-kobalt · Nobel: https://www.nobelprize.org/prizes/chemistry/2024/summary/ , https://www.nobelprize.org/prizes/physics/2024/summary/ · AlphaFold DB: https://alphafold.ebi.ac.uk/ · Insilico: https://www.biospace.com/press-releases/insilico-medicine-announces-nature-medicine-publication-of-phase-iia-results-evaluating-rentosertib-the-novel-tnik-inhibitor-for-idiopathic-pulmonary-fibrosis-ipf-discovered-and-designed-with-a-pioneering-ai-approach · Isomorphic: https://www.layer3labs.io/guides/isomorphic-labs-explained · GNoME: https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/ · Weather: https://9to5google.com/2025/11/17/google-weathernext-2/ , https://deepmind.google/discover/blog/gencast-predicts-weather-and-the-risks-of-extreme-conditions-with-sota-accuracy/ · IMO: https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/ , https://www.scmp.com/tech/article/3361482/worlds-first-ai-model-earn-perfect-score-maths-olympiad-comes-chinas-rednote · AlphaEvolve: https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/ , https://www.alphaxiv.org/abs/2608.16884 · Co-scientist: https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/ · FDA: https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices , https://www.complizen.ai/post/fda-has-cleared-1614-ai-medical-devices · Scribes: https://www.aha.org/aha-center-health-innovation-market-scan/2026-04-14-6-health-systems-enhancing-care-delivery-ambient-ai-scribes , https://medcitynews.com/2026/02/mount-sinai-microsoft-clinical-documentation/ · Neuralink: https://aish.com/neuralinks-next-frontier-can-a-brain-implant-give-sight-to-those-born-blind/ · AGI timelines: https://blog.aifutures.org/p/clarifying-how-our-ai-timelines-forecasts , https://www.lesswrong.com/posts/Tc5AbEpbFFdNx5nkP/a-visualization-of-changing-agi-timelines , https://arcprize.org/

**Open items to re-verify before publication:** official IMO 2026 AI results; Tesla's unsupervised robotaxi city list and fleet size; 1X NEO consumer delivery status; Optimus production numbers; Isomorphic first-in-human dosing; current FDA AI device count; Neuralink participant count and Blindsight first implant; Sora API retirement date; latest video-model leaderboard; whether Waymo reached 1M weekly rides by year-end 2026.
