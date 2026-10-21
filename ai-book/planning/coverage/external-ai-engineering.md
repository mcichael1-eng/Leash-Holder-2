# External-standard coverage audit: AI engineering

Audit of the book against four external standards for building, shipping and running AI systems, October 21, 2026. Topic lists come from the auditor's own knowledge of each standard (web search was unavailable). Statuses describe the book **before** this audit's edits. COVERED = explained at beginner level; THIN = mentioned but not explained; MISSING = absent; OUT OF SCOPE = too specialized or code-level for this reader (reason given).

Notes on the standards' structure:
- **AI Engineering** (Huyen, 2025): the ten chapter titles are known with confidence (1 Introduction to Building AI Applications with Foundation Models; 2 Understanding Foundation Models; 3 Evaluation Methodology; 4 Evaluate AI Systems; 5 Prompt Engineering; 6 RAG and Agents; 7 Finetuning; 8 Dataset Engineering; 9 Inference Optimization; 10 AI Engineering Architecture and User Feedback). Rows below are the topics each chapter covers, paraphrased, not exact section titles.
- **Designing Machine Learning Systems** (Huyen, 2022): the eleven chapter titles are known with confidence (1 Overview of ML Systems; 2 Introduction to ML Systems Design; 3 Data Engineering Fundamentals; 4 Training Data; 5 Feature Engineering; 6 Model Development and Offline Evaluation; 7 Model Deployment and Prediction Service; 8 Data Distribution Shifts and Monitoring; 9 Continual Learning and Test in Production; 10 Infrastructure and Tooling for MLOps; 11 The Human Side of ML). Rows are paraphrased topics.
- **Hugging Face LLM Course and Agents Course**: chapter numbering of the LLM Course changed when it was renamed from the NLP Course and extended (fine-tuning LLMs, reasoning models), so rows are grouped by topic rather than by chapter number. The Agents Course rows follow its units (introduction, frameworks, agentic RAG, final project) and bonus units (function-calling fine-tuning, observability and evaluation, agents in games), as best recalled.
- **Full Stack Deep Learning 2022**: lecture titles are known with confidence (1 Course Vision and When to Use ML; 2 Development Infrastructure and Tooling; 3 Troubleshooting and Testing; 4 Data Management; 5 Deployment; 6 Continual Learning; 7 Foundation Models; 8 ML Teams and Project Management; 9 Ethics). Rows are paraphrased topics.

## 1. Chip Huyen, *AI Engineering* (O'Reilly, 2025)

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Ch1 From language models to foundation models; self-supervision | COVERED | Ch 8 self-supervised learning; Ch 18; Ch 19 | None |
| Ch1 Foundation-model use cases (coding, media, writing, education, bots, information aggregation, data organization, workflow automation) | COVERED | Ch 29; Ch 31 "How organizations adopt AI" (typical first wins); Ch 53 | None |
| Ch1 Planning an AI application (use-case evaluation, expectations, milestones, last mile, maintenance) | COVERED | Ch 31 "From demo to product"; Ch 64 eight-step method and worksheet | None |
| Ch1 The AI engineering stack; AI engineering vs ML engineering | COVERED | Ch 62 Levels 4 and 5, AI engineer definition; Ch 63 role table | None |
| Ch2 Training data: multilingual and domain-specific models | COVERED | Ch 18 "Other languages cost more"; Ch 19 data mixtures | None |
| Ch2 Modeling: architectures and model size | COVERED | Ch 15; Ch 17; Ch 19 | None |
| Ch2 Post-training: SFT and preference fine-tuning | COVERED | Ch 20 | None |
| Ch2 Sampling: temperature, top-k, top-p, stopping, test-time compute | COVERED | Ch 18; Ch 21; Ch 26 | None |
| Ch2 Structured outputs | COVERED | Ch 26 "Structured outputs" | None |
| Ch2 Probabilistic nature: inconsistency and hallucination | COVERED | Ch 18; Ch 31 "Outputs vary", nondeterministic | None |
| Ch3 Why evaluating foundation models is hard | COVERED | Ch 31 "Why vibes do not scale"; Ch 24 | None |
| Ch3 Language-modeling metrics: entropy, cross-entropy, perplexity | COVERED | Ch 6 cross-entropy and perplexity; Ch 19; Ch 21 entropy. Bits-per-byte not named (OUT OF SCOPE detail) | None |
| Ch3 Exact evaluation: functional correctness (pass@k) | COVERED | Ch 21; Ch 31 pass@k and pass^k; Ch 57 | None |
| Ch3 Similarity to reference data: exact match, lexical (BLEU, ROUGE), semantic similarity | THIN | Ch 54 BLEU; Ch 31 exact match inside code graders | Added "reference-based metrics" paragraph with a worked wording example to Ch 31 Step 3; definitions: Reference-based metric, ROUGE, Semantic similarity score |
| Ch3 AI as a judge: methods, biases, limits | COVERED | Ch 31 graders, judge biases, calibration | None |
| Ch3 Comparative evaluation (pairwise, Elo, Bradley–Terry) | COVERED | Ch 24 LMArena and Elo; Ch 20 reward models | None |
| Ch4 Evaluation criteria: domain capability, factual consistency, safety, instruction following, cost and latency | COVERED | Ch 31 Step 1 criteria, groundedness check, cost-latency triangle | None |
| Ch4 Model selection; build vs buy (open weights vs APIs) | COVERED | Ch 26 "Choosing a model"; Ch 30 "Why go local, and why not"; Ch 31 tiers | None |
| Ch4 Public benchmarks, leaderboards, contamination | COVERED | Ch 24; Ch 9 | None |
| Ch4 Designing an evaluation pipeline | COVERED | Ch 31 Steps 1–3, sample-size table, eval flywheel | None |
| Ch5 In-context learning; zero- and few-shot; system vs user prompt; context efficiency | COVERED | Ch 25; Ch 8; Ch 18 | None |
| Ch5 Prompting best practices | COVERED | Ch 25 Techniques 1–12 | None |
| Ch5 Prompt-engineering tools and automatic prompt optimization | MISSING | — | Added paragraph (DSPy, overfitting risk) to Ch 25 Technique 11; definition: Automatic prompt optimization |
| Ch5 Organizing and versioning prompts | COVERED | Ch 31 "Versioning: pin everything" | None |
| Ch5 Defensive prompt engineering: prompt extraction, jailbreaks, injection, defenses | COVERED | Ch 31 AI security, canary token; Ch 58 | None |
| Ch6 RAG architecture; term-based vs embedding retrieval; hybrid search | COVERED | Ch 27 | None |
| Ch6 Retrieval optimization: chunking, reranking, query rewriting, contextual retrieval | COVERED | Ch 27 | None |
| Ch6 RAG beyond text: tables (text-to-SQL) and multimodal RAG | MISSING | Ch 27 mentions parsing only | Added section "Beyond text: tables and images" to Ch 27 with a commented SQL example; definitions: Text-to-SQL, Multimodal RAG |
| Ch6 Agents: tools, planning, reflection, tool selection | COVERED | Ch 28 agent loop, planning, evaluator-optimizer, tool design | None |
| Ch6 Agent failure modes and evaluation | THIN | Ch 28 compounding errors; Ch 31 "Evaluating agents" | Added planning / tool / efficiency / safety failure families to Ch 31 "Evaluating agents"; definition: Agent failure modes |
| Ch6 Memory | COVERED | Ch 28 memory layers; Ch 25 | None |
| Ch7 When to fine-tune vs prompt vs RAG | COVERED | Ch 30 decision ladder | None |
| Ch7 Memory math, trainable parameters, numerical formats | COVERED | Ch 30 "Will it fit?", "Under the hood"; Ch 5; Ch 33 | None |
| Ch7 Quantization for inference and training | COVERED | Ch 23; Ch 30; Ch 53 | None |
| Ch7 PEFT: adapters and LoRA | COVERED | Ch 30 LoRA and QLoRA | None |
| Ch7 PEFT: soft prompts (prompt tuning) | MISSING | — | Added prompt-tuning paragraph with worked parameter count to Ch 30; definition: Prompt tuning (soft prompt) |
| Ch7 Model merging and multi-task fine-tuning | COVERED | Ch 20 "Model merging"; Ch 30 merging an adapter; Ch 51 multi-task learning | None |
| Ch7 Fine-tuning hyperparameters (learning rate, epochs, batch size, base model) | COVERED | Ch 30 definitions and LoRA settings | None |
| Ch8 Data curation: quality, coverage, quantity | COVERED | Ch 30 "Data: the part that decides the result"; Ch 11 data quality | None |
| Ch8 Data acquisition and annotation | COVERED | Ch 11 labeling and the labeling industry | None |
| Ch8 Data augmentation, AI-powered synthesis, verification | COVERED | Ch 11; Ch 19; Ch 20 synthetic data and self-play | None |
| Ch8 Model distillation | COVERED | Ch 20; Ch 30; Ch 53 | None |
| Ch8 Data processing: inspect, deduplicate, clean, format | COVERED | Ch 11; Ch 19 curation pipeline; Ch 30 JSONL | None |
| Ch9 Bottlenecks (compute- vs memory-bound); online vs batch APIs | COVERED | Ch 23; Ch 33; Ch 26 Batch API | None |
| Ch9 Metrics: latency, TTFT, TPOT, throughput, goodput, MFU | COVERED | Ch 23 metrics table; Ch 37 | None |
| Ch9 AI accelerators | COVERED | Ch 32–35 | None |
| Ch9 Model compression: quantization, distillation, pruning | COVERED | Ch 53 worked examples; Ch 23 | None |
| Ch9 Speculative and parallel decoding | COVERED | Ch 23 speculative decoding and multi-token prediction. "Inference with reference" not named (OUT OF SCOPE detail) | None |
| Ch9 Attention optimization, KV cache, kernels and compilers | COVERED | Ch 23; Ch 35 | None |
| Ch9 Service optimization: batching, prefill/decode split, prompt caching, parallelism | COVERED | Ch 23; Ch 37 | None |
| Ch10 Context enhancement (RAG, tools) | COVERED | Ch 27; Ch 28 | None |
| Ch10 Guardrails | COVERED | Ch 31 "Guardrails" | None |
| Ch10 Model router and gateway | COVERED | Ch 31 gateways and cascades; Ch 26 routing | None |
| Ch10 Caching: exact and semantic response caches | THIN | Ch 26 and Ch 31 cover prompt caching only | Added response and semantic cache paragraph with worked saving and a false-match example to Ch 31 "The levers"; definitions: Response cache, Semantic cache |
| Ch10 Agent patterns and write actions | COVERED | Ch 28; Ch 31 action checks | None |
| Ch10 Monitoring and observability: metrics, logs, traces | COVERED | Ch 31 tracing | None |
| Ch10 Drift detection for AI applications | THIN | Ch 31 versioning (model and prompt changes only) | Added subsection "Dashboards and drift" to Ch 31 LLMOps; definition: Percentile latency (p95, p99) |
| Ch10 AI pipeline orchestration | COVERED | Ch 28 agent SDKs and frameworks | None |
| Ch10 User feedback: extracting it and designing for it | THIN | Ch 31 online signals; Ch 51 implicit feedback | Added feedback-design paragraph to Ch 31 "Offline and online evaluation"; definition: Explicit and implicit feedback |
| Ch10 Feedback limitations: biases, degenerate feedback loops | COVERED | Ch 31 GPT-4o rollback; Ch 11 and Ch 51 feedback loops, position and popularity bias | None |

## 2. Chip Huyen, *Designing Machine Learning Systems* (O'Reilly, 2022)

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Ch1 When to use ML | COVERED | Ch 8 "Two ways to make a computer do something" (key idea) | None |
| Ch1 ML in research vs production; ML systems vs ordinary software | COVERED | Ch 31 "From demo to product" (five reasons); Ch 10 lifecycle | None |
| Ch2 Business objectives vs ML objectives | COVERED | Ch 10 "Frame the question"; Ch 31 success criteria | None |
| Ch2 Requirements: reliability, scalability, maintainability, adaptability | THIN | Scattered | Addressed by the new Ch 10 serving, rollout, retraining and platform subsections |
| Ch2 Iterative process | COVERED | Ch 10 Figure 10.11 | None |
| Ch2 Framing: regression vs classification; binary, multiclass, multilabel | COVERED | Ch 8 | None |
| Ch2 Objective functions; decoupling objectives | COVERED | Ch 8 loss; Ch 51 multi-task ranking with weights chosen afterward | None |
| Ch2 Mind vs data | COVERED | Ch 11 "Why data matters"; Ch 13 Bitter Lesson | None |
| Ch3 Data sources | COVERED | Ch 11 "Where data comes from" | None |
| Ch3 Data formats: JSON, CSV, row vs column (Parquet), text vs binary | COVERED | Ch 3; Ch 11 | None |
| Ch3 Data models: relational, NoSQL, structured vs unstructured | COVERED | Ch 11; Ch 54 knowledge graphs | None |
| Ch3 Transactional vs analytical processing; ETL; warehouses and lakes | COVERED | Ch 11 pipelines, warehouses, lakehouses | None |
| Ch3 Batch vs stream processing; modes of dataflow | COVERED | Ch 11 batch and streaming. Message brokers such as Kafka not named (OUT OF SCOPE detail) | None |
| Ch4 Sampling: random and stratified | COVERED | Ch 9 stratified sampling | None |
| Ch4 Sampling: reservoir, weighted, importance sampling | OUT OF SCOPE | — | None: statistical techniques a non-programmer will not meet |
| Ch4 Hand labels: multiplicity, agreement, lineage | COVERED | Ch 11 labeling, Cohen's kappa, lineage | None |
| Ch4 Natural labels and feedback-loop length | MISSING | — | Added natural-label paragraph to Ch 11 (definition: Natural label); feedback delay defined in Ch 10 |
| Ch4 Lack of labels: weak supervision, semi-supervision, transfer, active learning | THIN | Ch 8 (semi-supervised, transfer, active); Ch 46 weak supervision as noisy web labels | Added programmatic labeling (labeling functions, Snorkel) to Ch 11; definition: Programmatic labeling |
| Ch4 Class imbalance: choosing metrics | COVERED | Ch 9 confusion matrix, precision–recall curves | None |
| Ch4 Class imbalance: resampling and class-weighted losses | MISSING | — | Added rebalancing paragraph with worked weight (9,800 ÷ 200 = 49) to Ch 9; definitions: Oversampling and undersampling, Class weights. Focal loss left out as too specialized |
| Ch4 Data augmentation | COVERED | Ch 9; Ch 13; Ch 14; Ch 11 synthetic data | None |
| Ch5 Learned vs engineered features | COVERED | Ch 11; Ch 14 | None |
| Ch5 Missing values, scaling, discretization, encoding, feature crossing | COVERED | Ch 11 cleaning and feature engineering. Hashing trick not named (OUT OF SCOPE detail) | None |
| Ch5 Data leakage | COVERED | Ch 9 "Data leakage" | None |
| Ch5 Feature importance, selection, generalization | COVERED | Ch 10 feature importance; Ch 11 feature selection | None |
| Ch6 Model selection tips; start with baselines | COVERED | Ch 10 cheat sheet; Ch 9 baselines | None |
| Ch6 Ensembles: bagging, boosting, stacking | COVERED | Ch 10 | None |
| Ch6 Experiment tracking and versioning | THIN | Ch 10 one paragraph, no definition or tools | Added to new Ch 10 "The ML platform" (MLflow, Weights & Biases, DVC); definitions: Experiment tracking, Data versioning |
| Ch6 Distributed training | COVERED | Ch 37 | None |
| Ch6 AutoML: hyperparameter search and architecture search | COVERED (search); NAS absent | Ch 9 grid, random, Bayesian, successive halving; Ch 10 AutoML mention | Added one-paragraph neural architecture search mention to Ch 9; definition: Neural architecture search (NAS) |
| Ch6 Offline evaluation: baselines, calibration, confidence | COVERED | Ch 9; Ch 8 calibration | None |
| Ch6 Perturbation, invariance and directional-expectation tests | MISSING | — | Added section "Beyond one number: slices and behavioral tests" to Ch 9 (CheckList); definitions: Invariance test, Directional expectation test |
| Ch6 Slice-based evaluation | MISSING | Ch 58 fairness case studies only | Added in the same Ch 9 section with worked Table 9.14; definition: Slice-based evaluation |
| Ch7 Deployment basics; model as a web service | THIN | Ch 10 "Deploy, perhaps as a nightly scoring job" | Added Ch 10 "Serving a model: batch or real time" |
| Ch7 Batch vs online prediction | MISSING | — | Added in Ch 10; definitions: Batch prediction, Online prediction |
| Ch7 Unifying batch and streaming features; training-serving skew | MISSING | — | Added in Ch 10 with feature store as the cure; definition: Training-serving skew |
| Ch7 Model compression (quantization, distillation, pruning, low-rank) | COVERED | Ch 53; Ch 23; Ch 30 LoRA | None |
| Ch7 Cloud vs edge; compiling for devices; ML in browsers | THIN | Ch 53 trade-offs, one line on compilers | Added on-device runtimes (Core ML, LiteRT, ExecuTorch, ONNX Runtime incl. browsers) to Ch 53; definition: On-device runtime |
| Ch8 Causes of failure: software failures, edge cases, degenerate feedback loops | THIN | Ch 11 and Ch 51 feedback loops; Ch 31 edge cases | Added Ch 10 Watch out on pipeline-caused failures (Google outage review) and alert fatigue |
| Ch8 Shift types: covariate, label, concept | THIN | Ch 9 distribution shift; Ch 10 data vs concept drift | Added to Ch 10 with how each should be handled; definitions: Covariate shift, Label shift |
| Ch8 Detecting shifts: statistical tests and distances | MISSING | — | Added PSI worked example and Kolmogorov–Smirnov mention to Ch 10; definition: Population stability index (PSI) |
| Ch8 Monitoring: what to measure, logs, dashboards, alerts | THIN | Ch 10 Figure 10.12 | Added four-layer monitoring table to Ch 10; definition: Feedback delay |
| Ch9 Continual learning: stateless vs stateful, stages, how often to update | MISSING | Ch 8 online learning only | Added "Retraining: how often, and how" with worked freshness experiment to Ch 10; definitions: Stateless retraining, Stateful training |
| Ch9 Test in production: shadow, canary, A/B, interleaving | MISSING | Ch 31 A/B test only | Added "Rolling out a new model safely" with Figure 10.13 and worked numbers to Ch 10; definitions: Shadow deployment, Canary release, Rollback |
| Ch9 Bandits for exploration | COVERED | Ch 51 multi-armed bandits (contextual bandits OUT OF SCOPE detail) | Pointer added from Ch 10 |
| Ch10 Storage and compute; cloud vs own data centers | COVERED | Ch 4; Ch 38; Ch 43 | None |
| Ch10 Standardized environments and containers | MISSING | — | Added to Ch 10; definition: Container |
| Ch10 Schedulers and orchestrators | COVERED | Ch 11 orchestration; Ch 62 Kubernetes and Slurm | None |
| Ch10 ML platform: deployment, model store, feature store | MISSING | Named only in Ch 62 and Ch 63 role descriptions | Added Ch 10 "The ML platform"; definitions: ML platform, Model registry, Feature store |
| Ch10 Build vs buy | COVERED | Ch 31 "Buy or build?" | Pointer added from Ch 10 |
| Ch11 User experience: consistency, mostly-correct predictions, smooth failing | COVERED | Ch 31 design patterns, graceful failure | None |
| Ch11 Team structure: cross-functional teams, end-to-end vs specialists | THIN | Ch 63 roles only | Added Ch 31 "Who builds it: team shapes" and Ch 10 roles paragraph |
| Ch11 Responsible AI: bias sources, model cards, trade-offs | COVERED | Ch 11 bias; Ch 58 fairness; Ch 24 and Ch 30 model cards | None |

## 3. Hugging Face LLM Course and Agents Course

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| LLM: What Transformers can do (tasks, pipelines) | COVERED | Ch 18; Ch 54 classic NLP tasks | None |
| LLM: How Transformers work; encoder, decoder, encoder–decoder | COVERED | Ch 15 | None |
| LLM: Bias and limitations | COVERED | Ch 18; Ch 58 | None |
| LLM: Inference and optimized deployment (TGI, vLLM, llama.cpp) | COVERED | Ch 23 serving engines; Ch 30 local toolkit | None |
| LLM: Behind the pipeline (tokenizer, model, logits, softmax) | COVERED | Ch 18 | None |
| LLM: Batching sequences: padding, attention masks, truncation | OUT OF SCOPE | Ch 15 causal mask | None: code-level detail for programmers |
| LLM: Fine-tuning a pretrained model (Trainer, training loop) | COVERED | Ch 30 and its QLoRA walkthrough; Ch 13 PyTorch loop | None |
| LLM: Reading learning curves | COVERED | Ch 9; Ch 13; Ch 30 validation loss | None |
| LLM: Sharing on the Hub; model cards | COVERED | Ch 30 "A tour of Hugging Face" | None |
| LLM: Loading and preparing datasets | COVERED | Ch 11; Ch 30 JSONL | None |
| LLM: Streaming and memory-mapping huge datasets | OUT OF SCOPE | — | None: library mechanics |
| LLM: Semantic search with FAISS | COVERED | Ch 27 vector databases and ANN search | None |
| LLM: BPE tokenization | COVERED | Ch 15; Ch 18 worked example | None |
| LLM: WordPiece, Unigram, SentencePiece; normalization and pre-tokenization | MISSING | — | Added paragraph to Ch 18; definitions: WordPiece, Unigram tokenizer (SentencePiece) |
| LLM: Classic NLP tasks (NER, masked LM, translation, summarization, QA) | COVERED | Ch 54; Ch 15 masked language modeling | None |
| LLM: Training a causal LM from scratch | COVERED | Ch 19 | None |
| LLM: Debugging and asking for help | OUT OF SCOPE | — | None: course logistics; the training-debugging check (overfit one batch) is now in Ch 10 |
| LLM: Building demos (Gradio, Spaces) | THIN | Ch 30 Space definition only | Added Gradio/Streamlit paragraph to Ch 30; definition: Gradio and Streamlit |
| LLM: Curating datasets and annotation tools | COVERED | Ch 11 labeling | None |
| LLM: Fine-tuning LLMs (chat templates, SFT with TRL, LoRA, evaluation) | COVERED | Ch 18 chat templates; Ch 30 TRL and PEFT, LoRA | None |
| LLM: Building reasoning models (RL, DeepSeek-R1, GRPO) | COVERED | Ch 21 | None |
| Agents: What an agent is; LLMs; messages and special tokens | COVERED | Ch 28; Ch 18 chat templates | None |
| Agents: Tools and function calling | COVERED | Ch 28 | None |
| Agents: Thought–Action–Observation cycle; ReAct | COVERED | Ch 28 agent loop and worked trace | None |
| Agents: Code agents vs JSON tool calls (smolagents) | MISSING | — | Added subsection "Actions written as code" with commented example to Ch 28; definition: Code agent (code actions) |
| Agents: Frameworks (smolagents, LlamaIndex, LangGraph) | COVERED | Ch 28 framework table | smolagents now named in Ch 28 |
| Agents: Multi-agent, vision and browser agents | COVERED | Ch 28 | None |
| Agents: Agentic RAG | COVERED | Ch 27 | None |
| Agents (bonus): Fine-tuning a model for function calling | THIN | Ch 20 SFT mentions tool use | Added explanation of how models learn tool calls to Ch 28 "The tool definition" |
| Agents (bonus): Observability and evaluation (OpenTelemetry, Langfuse) | COVERED | Ch 31 tracing and agent evals | None |
| Agents (bonus): Agents in games | OUT OF SCOPE | Ch 48 covers game-playing AI | None: hands-on course project |
| Agents: Final project and the GAIA benchmark | MISSING (GAIA) | — | Added GAIA with launch scores to Ch 31 "Evaluating agents"; definition: GAIA |

## 4. Full Stack Deep Learning (2022 course)

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| L1 When to use ML | COVERED | Ch 8 | None |
| L1 Project lifecycle | COVERED | Ch 10 Figure 10.11 | None |
| L1 Prioritizing projects: impact vs feasibility | COVERED | Ch 64 eight-step method and worksheet | None |
| L1 Product archetypes (software 2.0, human-in-the-loop, autonomous) | COVERED | Ch 31 copilot vs autopilot, autonomy quadrant | None |
| L1 Metrics and baselines | COVERED | Ch 9 | None |
| L2 Python, notebooks, editors | COVERED | Ch 3; Ch 26; Ch 29 | None |
| L2 Deep learning frameworks | COVERED | Ch 13 | None |
| L2 Distributed training | COVERED | Ch 37 | None |
| L2 Compute: GPUs, cloud vs on-premises, cost | COVERED | Ch 32; Ch 43 | None |
| L2 Resource management (Slurm, Kubernetes) | COVERED | Ch 62 | None |
| L2 Experiment management | THIN | Ch 10 one paragraph | Added Ch 10 "The ML platform" |
| L2 Hyperparameter optimization | COVERED | Ch 9 | None |
| L2 All-in-one ML platforms (SageMaker, Vertex AI and others) | MISSING | — | Added to Ch 10 "The ML platform" |
| L3 Software testing, linting, CI | COVERED | Ch 29 tests and CI | None |
| L3 Testing ML systems: data tests, training tests, evaluation tests | MISSING | — | Added Ch 10 "Testing a machine-learning system"; definitions: Data validation, Overfitting a single batch, Evaluation gate. Behavioral tests in Ch 9 |
| L3 Shadow tests in production | MISSING | — | Added in Ch 10 rollout subsection |
| L3 Troubleshooting models (make it run, fast, right; overfit one batch) | THIN | Ch 13 loss spikes and NaN | Added the overfit-a-single-batch check to Ch 10 |
| L4 Storage: files, object storage, databases, warehouses, lakes | COVERED | Ch 11 | None |
| L4 Exploration (EDA) | COVERED | Ch 10 | None |
| L4 Processing and workflow orchestration | COVERED | Ch 11; Ch 62 | None |
| L4 Feature stores | MISSING | — | Added to Ch 10 |
| L4 Datasets and labeling | COVERED | Ch 11; Ch 8 | None |
| L4 Data versioning | THIN | Ch 11 one clause on keeping versions | Added to Ch 10 with DVC |
| L4 Privacy: federated learning, differential privacy | COVERED | Ch 11; Ch 53 | None |
| L5 Prototypes and demo apps (Gradio, Streamlit) | MISSING | Ch 30 Spaces | Added to Ch 30 |
| L5 Model-in-service vs model-as-a-service; REST APIs | THIN | Ch 26 (API consumer side) | Added Ch 10 "Serving a model" |
| L5 Dependencies and containers (Docker) | MISSING | — | Added to Ch 10 |
| L5 Performance: GPU vs CPU, batching, caching, distillation, quantization | COVERED | Ch 23; Ch 53 | None |
| L5 Horizontal scaling (Kubernetes) | THIN | Ch 62 definition only | Added autoscaling sentence to Ch 10 (serverless not named: OUT OF SCOPE detail) |
| L5 Rollouts: gradual, instant rollback, split traffic, shadow | MISSING | — | Added Ch 10 rollout subsection and Figure 10.13 |
| L5 Edge deployment frameworks and efficiency | THIN | Ch 53 compression | Added on-device runtimes to Ch 53 |
| L6 The data flywheel | COVERED | Ch 31 eval flywheel; Ch 10 Figure 10.12 | None |
| L6 Retraining strategy and triggers | MISSING | — | Added Ch 10 "Retraining: how often, and how" |
| L6 What to monitor, and setting alerts | THIN | Ch 10 Figure 10.12 | Added monitoring table and alert advice to Ch 10 |
| L6 Drift types and how to measure them | THIN | Ch 9; Ch 10 two definitions | Added shift types and PSI worked example to Ch 10 |
| L7 Transfer learning and fine-tuning | COVERED | Ch 8; Ch 30 | None |
| L7 Transformers and LLMs | COVERED | Ch 15; Ch 18–21 | None |
| L7 Prompt engineering | COVERED | Ch 25 | None |
| L7 CLIP and image generation | COVERED | Ch 16; Ch 47 | None |
| L8 ML roles | COVERED | Ch 63 role catalog; Ch 62 | None |
| L8 Hiring and job search | COVERED | Ch 63 | None |
| L8 Organization archetypes | MISSING | — | Added Ch 31 "Who builds it: team shapes"; definitions: Centralized AI team, Embedded AI team, Hub-and-spoke model (center of excellence) |
| L8 Managing ML projects under uncertainty | MISSING | — | Added staged-planning paragraph to Ch 10 lifecycle; definition: Proof of concept |
| L8 ML product design; human–AI interaction | COVERED | Ch 31 "Designing AI products people trust" | None |
| L9 Fairness, representation, accountability | COVERED | Ch 58; Ch 11 | None |
| L9 Interpretability | COVERED | Ch 57; Ch 10 | None |
| L9 Alignment, power, existential risk | COVERED | Ch 55; Ch 56; Ch 60 | None |
| L9 ML in medicine | COVERED | Ch 52 | None |

## Summary

| Standard | Topics | COVERED before | THIN | MISSING | OUT OF SCOPE | Covered after (in scope) |
|---|---|---|---|---|---|---|
| AI Engineering (2025) | 60 | 52 (87%) | 5 | 3 | 0 | 60 of 60 (100%) |
| Designing ML Systems (2022) | 53 | 32 (62% of 52 in scope) | 9 | 11 | 1 | 52 of 52 (100%) |
| Hugging Face LLM and Agents courses | 32 | 23 (82% of 28 in scope) | 2 | 3 | 4 | 28 of 28 (100%) |
| Full Stack Deep Learning (2022) | 48 | 30 (63%) | 8 | 10 | 0 | 48 of 48 (100%) |
| All four | 193 | 137 (73% of 188 in scope) | 24 | 27 | 5 | 188 of 188 (100%) |

The book was already strong on the LLM-application side (prompting, RAG, agents, evals, inference, fine-tuning). The gaps clustered in classical production ML, the "MLOps" material of *Designing Machine Learning Systems* chapters 7–10 and FSDL lectures 3, 5 and 6, which Ch 10 had compressed into one short section. That cluster is now a set of six Ch 10 subsections (serving, staged rollout with Figure 10.13, monitoring and drift detection with a PSI worked example, retraining, testing, the ML platform), plus supporting additions in Ch 9 (rare classes, slices and behavioral tests, neural architecture search), Ch 11 (natural and programmatic labels) and Ch 31 (reference-based metrics, feedback design, agent failure modes and GAIA, dashboards and drift, semantic caching, team shapes). Smaller additions: Ch 18 (WordPiece and Unigram), Ch 25 (automatic prompt optimization), Ch 27 (text-to-SQL and multimodal RAG), Ch 28 (code agents; how models learn tool calls), Ch 30 (prompt tuning; Gradio and Streamlit), Ch 53 (on-device runtimes). In total, 51 new definition callouts, one new mermaid diagram (Figure 10.13) and three new tables (Table 9.14 and two in Ch 10); every new term was added to its chapter's Key terms list.

Out of scope, with reasons: reservoir, weighted and importance sampling (statistical techniques this reader will not meet); padding and attention masks for batched sequences, and streaming or memory-mapping datasets (library-level code detail); the Hugging Face course's "how to ask for help" chapter (course logistics); the Agents Course games bonus unit (a hands-on project; game-playing AI is covered in Ch 48). Sub-details judged too specialized to name: bits-per-byte, inference with reference, Kafka-style message brokers, the hashing trick, focal loss, contextual bandits and serverless hosting.

Checks: `validate.py` reports all mermaid diagrams valid and `check.py` reports OK for every edited chapter (9, 10, 11, 18, 25, 27, 28, 30, 31, 53).
