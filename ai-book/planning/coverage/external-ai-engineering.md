# External-standard coverage audit: AI engineering

Audit of the book against four external standards for building, shipping and running AI systems, October 21, 2026. Topic lists were first reconstructed from the auditor's own knowledge of each standard (web search was unavailable at the time) and then verified online on October 21, 2026 against the publishers' and authors' contents pages and the live course pages; corrections are marked in place and the new rows, URLs and revised counts are in the final section, "Verified online (October 21, 2026)". Statuses describe the book **before** this audit's edits. COVERED = explained at beginner level; THIN = mentioned but not explained; MISSING = absent; OUT OF SCOPE = too specialized or code-level for this reader (reason given).

Notes on the standards' structure:
- **AI Engineering** (Huyen, 2025): the ten chapter titles are known with confidence (1 Introduction to Building AI Applications with Foundation Models; 2 Understanding Foundation Models; 3 Evaluation Methodology; 4 Evaluate AI Systems; 5 Prompt Engineering; 6 RAG and Agents; 7 Finetuning; 8 Dataset Engineering; 9 Inference Optimization; 10 AI Engineering Architecture and User Feedback). Rows below are the topics each chapter covers, paraphrased, not exact section titles. [Verified Oct 21: all ten titles and their order match the author's published contents.]
- **Designing Machine Learning Systems** (Huyen, 2022): the eleven chapter titles are known with confidence (1 Overview of ML Systems; 2 Introduction to ML Systems Design; 3 Data Engineering Fundamentals; 4 Training Data; 5 Feature Engineering; 6 Model Development and Offline Evaluation; 7 Model Deployment and Prediction Service; 8 Data Distribution Shifts and Monitoring; 9 Continual Learning and Test in Production; 10 Infrastructure and Tooling for MLOps; 11 The Human Side of ML). Rows are paraphrased topics. [Verified Oct 21: all eleven titles match the published contents.]
- **Hugging Face LLM Course and Agents Course**: chapter numbering of the LLM Course changed when it was renamed from the NLP Course and extended (fine-tuning LLMs, reasoning models), so rows are grouped by topic rather than by chapter number. The Agents Course rows follow its units (introduction, frameworks, agentic RAG, final project) and bonus units (function-calling fine-tuning, observability and evaluation, agents in games), as best recalled. [Verified Oct 21: the LLM Course runs from Chapter 0 (Setup) to Chapter 12 (Build Reasoning Models); the Agents Course structure was recalled correctly and has no new units. Chapter numbers are mapped in the final section.]
- **Full Stack Deep Learning 2022**: lecture titles are known with confidence (1 Course Vision and When to Use ML; 2 Development Infrastructure and Tooling; 3 Troubleshooting and Testing; 4 Data Management; 5 Deployment; 6 Continual Learning; 7 Foundation Models; 8 ML Teams and Project Management; 9 Ethics). Rows are paraphrased topics. [Verified Oct 21: the nine titles are correct, but two rows below were not 2022 topics, and the site's newest offering is the LLM Bootcamp (Spring 2023), audited in the final section.]

## 1. Chip Huyen, *AI Engineering* (O'Reilly, 2025)

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Ch1 From language models to foundation models; self-supervision | COVERED | Ch 8 self-supervised learning; Ch 18; Ch 19 | None |
| Ch1 Foundation-model use cases (coding, media, writing, education, bots, information aggregation, data organization, workflow automation) | COVERED | Ch 29; Ch 31 "How organizations adopt AI" (typical first wins); Ch 53 | None |
| Ch1 Planning an AI application (use-case evaluation, expectations, milestones, last mile, maintenance) | COVERED | Ch 31 "From demo to product"; Ch 64 eight-step method and worksheet | None |
| Ch1 The AI engineering stack; AI engineering vs ML engineering [verified Oct 21: the section also compares AI engineering with full-stack engineering, now a separate row in the final section] | COVERED | Ch 62 Levels 4 and 5, AI engineer definition; Ch 63 role table | None |
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
| Ch4 Evaluation criteria: domain capability, factual consistency, safety, instruction following, cost and latency [corrected Oct 21: the published sections are Domain-Specific Capability, Generation Capability (which holds factual consistency and safety), Instruction-Following Capability, and Cost and Latency] | COVERED | Ch 31 Step 1 criteria, groundedness check, cost-latency triangle | None |
| Ch4 Model selection; build vs buy (open weights vs APIs) | COVERED | Ch 26 "Choosing a model"; Ch 30 "Why go local, and why not"; Ch 31 tiers | None |
| Ch4 Public benchmarks, leaderboards, contamination | COVERED | Ch 24; Ch 9 | None |
| Ch4 Designing an evaluation pipeline | COVERED | Ch 31 Steps 1–3, sample-size table, eval flywheel | None |
| Ch5 In-context learning; zero- and few-shot; system vs user prompt; context efficiency | COVERED | Ch 25; Ch 8; Ch 18 | None |
| Ch5 Prompting best practices | COVERED | Ch 25 Techniques 1–12 | None |
| Ch5 Prompt-engineering tools and automatic prompt optimization | MISSING | — | Added paragraph (DSPy, overfitting risk) to Ch 25 Technique 11; definition: Automatic prompt optimization |
| Ch5 Organizing and versioning prompts | COVERED | Ch 31 "Versioning: pin everything" | None |
| Ch5 Defensive prompt engineering: prompt extraction, jailbreaks, injection, defenses [verified Oct 21: published sections are Proprietary Prompts and Reverse Prompt Engineering, Jailbreaking and Prompt Injection, Information Extraction, Defenses; Information Extraction was merged here and is now its own row in the final section] | COVERED | Ch 31 AI security, canary token; Ch 58 | None |
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
| Ch10 Drift detection for AI applications [verified Oct 21: not a heading in the published two-level contents; treated as part of Monitoring and Observability] | THIN | Ch 31 versioning (model and prompt changes only) | Added subsection "Dashboards and drift" to Ch 31 LLMOps; definition: Percentile latency (p95, p99) |
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
| L1 Metrics and baselines [corrected Oct 21: not a section of the 2022 Lecture 1, whose sections are Course Vision, When to Use Machine Learning (with ML product archetypes and data flywheels) and Lifecycle; dropped from the verified count] | COVERED | Ch 9 | None |
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
| L3 Shadow tests in production [renamed Oct 21: the lecture's section is "Test in Production, But Don't YOLO"] | MISSING | — | Added in Ch 10 rollout subsection |
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
| L6 The data flywheel [verified Oct 21: introduced in Lecture 1 "Data Flywheels" and revisited in Lecture 6 "The Continual Improvement Workflow"] | COVERED | Ch 31 eval flywheel; Ch 10 Figure 10.12 | None |
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
| L9 Interpretability [corrected Oct 21: not a section of the 2022 Lecture 9, which mentions interpretability only in passing; the topic belonged to the 2021 course's "Testing & Explainability" lecture; dropped from the verified count] | COVERED | Ch 57; Ch 10 | None |
| L9 Alignment, power, existential risk [verified Oct 21: published as the themes "Alignment, Trade-Offs, Humility" and "Frontiers: AI Rights and X-Risk"; AI rights is now its own row in the final section] | COVERED | Ch 55; Ch 56; Ch 60 | None |
| L9 ML in medicine | COVERED | Ch 52 | None |

## Summary

All OUT OF SCOPE topics are explained in plain words in Appendix F (The Advanced Shelf).

| Standard | Topics | COVERED before | THIN | MISSING | OUT OF SCOPE | Covered after (in scope) |
|---|---|---|---|---|---|---|
| AI Engineering (2025) | 60 | 52 (87%) | 5 | 3 | 0 | 60 of 60 (100%) |
| Designing ML Systems (2022) | 53 | 32 (62% of 52 in scope) | 9 | 11 | 1 | 52 of 52 (100%) |
| Hugging Face LLM and Agents courses | 32 | 23 (82% of 28 in scope) | 2 | 3 | 4 | 28 of 28 (100%) |
| Full Stack Deep Learning (2022) | 48 | 30 (63%) | 8 | 10 | 0 | 48 of 48 (100%) |
| All four | 193 | 137 (73% of 188 in scope) | 24 | 27 | 5 | 188 of 188 (100%) |

These are the counts from the reconstructed lists. Counts revised after online verification are at the end of the final section.

The book was already strong on the LLM-application side (prompting, RAG, agents, evals, inference, fine-tuning). The gaps clustered in classical production ML, the "MLOps" material of *Designing Machine Learning Systems* chapters 7–10 and FSDL lectures 3, 5 and 6, which Ch 10 had compressed into one short section. That cluster is now a set of six Ch 10 subsections (serving, staged rollout with Figure 10.13, monitoring and drift detection with a PSI worked example, retraining, testing, the ML platform), plus supporting additions in Ch 9 (rare classes, slices and behavioral tests, neural architecture search), Ch 11 (natural and programmatic labels) and Ch 31 (reference-based metrics, feedback design, agent failure modes and GAIA, dashboards and drift, semantic caching, team shapes). Smaller additions: Ch 18 (WordPiece and Unigram), Ch 25 (automatic prompt optimization), Ch 27 (text-to-SQL and multimodal RAG), Ch 28 (code agents; how models learn tool calls), Ch 30 (prompt tuning; Gradio and Streamlit), Ch 53 (on-device runtimes). In total, 51 new definition callouts, one new mermaid diagram (Figure 10.13) and three new tables (Table 9.14 and two in Ch 10); every new term was added to its chapter's Key terms list.

Out of scope, with reasons: reservoir, weighted and importance sampling (statistical techniques this reader will not meet); padding and attention masks for batched sequences, and streaming or memory-mapping datasets (library-level code detail); the Hugging Face course's "how to ask for help" chapter (course logistics); the Agents Course games bonus unit (a hands-on project; game-playing AI is covered in Ch 48). Sub-details judged too specialized to name: bits-per-byte, inference with reference, Kafka-style message brokers, the hashing trick, focal loss, contextual bandits and serverless hosting.

Checks: `validate.py` reports all mermaid diagrams valid and `check.py` reports OK for every edited chapter (9, 10, 11, 18, 25, 27, 28, 30, 31, 53).

## Verified online (October 21, 2026)

Each standard's real contents were fetched from primary sources (author repositories, publisher and course pages) and diffed against the rows above. Web search itself was not used (the shared search budget was exhausted), so every page below was opened directly by its URL. Statuses for new rows follow the same rules as the original audit: the book was grepped and the passage read before a status was given. Status before = the book before this round's edits.

### 1. AI Engineering (Huyen, 2025)

URLs: https://github.com/chiphuyen/aie-book/blob/main/ToC.md (read as https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md, the author's full two-level contents with page numbers). The O'Reilly page https://www.oreilly.com/library/view/ai-engineering/9781098166298/ refused the request (HTTP 403).

What differed: the reconstruction was accurate. All ten chapter titles and their order match, and nearly every row maps to a published section. Missed or merged: "AI Engineering Versus Full-Stack Engineering" (Ch1), "Introduction to Embedding" (Ch3, inside Exact Evaluation) and "Information Extraction" (Ch5). Misnamed: the Ch4 evaluation-criteria row (corrected in place). Not verifiable: "Drift detection" (Ch10) is not a heading at the two levels published. Merged without a new row because the existing row already covers them: "What Models Can Act as Judges?" (Ch3), "Data Quantity" and "Traditional Data Synthesis Techniques" (Ch8), "Finetuning Tactics" (Ch7). Numbering: identical.

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Ch1 AI engineering versus full-stack engineering | COVERED | Ch 62 Level 4 (the AI engineer as a software engineer building on top of models); Ch 63 role table; Ch 31 "From demo to product" | None |
| Ch3 Introduction to embedding (embeddings as an evaluation tool) | COVERED | Ch 5 embeddings preview; Ch 14; Ch 27 cosine similarity; Ch 31 semantic similarity score | None |
| Ch5 Information extraction (training-data, personal-data and copyright extraction) | COVERED | Ch 58 "Models can memorize" (2021 GPT-2 and 2023 ChatGPT extraction results); Ch 31 system-prompt extraction (OWASP LLM07); Ch 30 | None |

### 2. Designing Machine Learning Systems (Huyen, 2022)

URLs: https://github.com/chiphuyen/dmls-book (README), https://raw.githubusercontent.com/chiphuyen/dmls-book/main/ToC.pdf (the full contents, read as text), https://raw.githubusercontent.com/chiphuyen/dmls-book/main/summary.md (chapter summaries).

What differed: all eleven chapter titles match, and the reconstruction found most sections. Missed: Ch1 "Machine Learning Use Cases"; Ch4 "Nonprobability Sampling" and "Perturbation" (under Data Augmentation); Ch5 "Discrete and Continuous Positional Embeddings"; Ch7 "Machine Learning Deployment Myths"; Ch8 "General Data Distribution Shifts"; Ch10 "Development Environment" and "Data Science Workflow Management"; Ch11 "Irresponsible AI: Case Studies". Merged without a new row: Ch3 "Modes of Dataflow" (databases, services, real-time transport) sits in the batch-versus-stream row; Ch6 "Evaluating ML Models" (model-selection tips) sits in the baselines row. Minor naming: the Ch3 data-formats row lists CSV and Parquet, which are examples; the headings are JSON, Row-Major Versus Column-Major Format, and Text Versus Binary Format. No invented rows. Numbering: identical.

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Ch1 Machine-learning use cases | COVERED | Ch 1 invisible AI; Ch 51; Ch 53 | None |
| Ch4 Nonprobability sampling (convenience, snowball, judgment, quota) | THIN | Ch 11 sampling bias only; Ch 9 stratified sampling | Added paragraph to Ch 11 "Bias in data" (convenience, snowball and quota sampling; web text as a convenience sample); definitions: Nonprobability sampling, Convenience sampling |
| Ch4 Perturbation: noisy and adversarial training examples | COVERED | Ch 9 data augmentation; Ch 45 adversarial example and robust training; Ch 55 adversarial training | None |
| Ch5 Discrete and continuous positional embeddings | COVERED | Ch 15 position (sinusoidal, learned, RoPE) | None |
| Ch7 Deployment myths (one or two models, performance stays the same, rare updates, scale) | COVERED | Ch 10 MLOps, retraining and ML platform subsections | None |
| Ch8 General distribution shifts: feature change and label schema change | THIN | Ch 10 Watch out (renamed column, dollars switched to cents); label schema change absent | Added paragraph to Ch 10 "Monitoring" covering feature change and label schema change; definition: Label schema change |
| Ch10 Development environment: setup, notebooks, standardization | COVERED | Ch 3 Colab; Ch 10 toolbox table and containers; Ch 29 | None |
| Ch10 Data science workflow management (Airflow and similar) | COVERED | Ch 11 orchestration; Ch 10 ML platform "Pipelines and compute". Kubeflow and Metaflow not named (OUT OF SCOPE detail) | None |
| Ch11 Irresponsible AI: case studies | COVERED | Ch 11 and Ch 58 case studies (COMPAS, Gender Shades, Amazon's recruiting model); the book's own case studies differ | None |

### 3. Hugging Face LLM Course and AI Agents Course

URLs: https://huggingface.co/learn/llm-course/chapter1/1 and https://raw.githubusercontent.com/huggingface/course/main/chapters/en/_toctree.yml (the course's own table of contents); https://huggingface.co/learn/agents-course/unit0/introduction and https://raw.githubusercontent.com/huggingface/agents-course/main/units/en/_toctree.yml; https://raw.githubusercontent.com/huggingface/mcp-course/main/units/en/_toctree.yml (the separate MCP Course).

Numbering of the LLM Course, for the rows above: 0 Setup; 1 Transformer models (including Inference with LLMs, and Bias and limitations); 2 Using Transformers (including Optimized Inference Deployment); 3 Fine-tuning a pretrained model (including Understanding Learning Curves); 4 Sharing models and tokenizers; 5 The Datasets library (including Semantic search with FAISS); 6 The Tokenizers library (normalization, BPE, WordPiece, Unigram); 7 Classical NLP tasks; 8 How to ask for help; 9 Building and sharing demos (Gradio); 10 Curate high-quality datasets (Argilla); 11 Fine-tune large language models (chat templates, SFTTrainer, LoRA, evaluation); 12 Build reasoning models (RL on LLMs, the DeepSeek-R1 "aha moment", GRPO).

What differed: the LLM Course rows were recalled correctly; missed were Ch1 "How Transformers solve tasks" and the tokenizer-library sections of Ch6 (training a new tokenizer, fast tokenizers, building one block by block). The Agents Course structure (Units 0 to 4, bonus Units 1 to 3) was recalled correctly; missed was Unit 1 "Dummy Agent Library", and the LlamaIndex (LlamaHub, components, agentic workflows) and LangGraph (building blocks, a document-analysis graph) sections were merged into the frameworks row. The live page labels Unit 3 "Use Cases" while the repository calls it "Use Case for Agentic RAG". Neither course has added units since the reconstruction: there is no MCP or other new unit in the Agents Course on the live page or in its repository. What Hugging Face added instead is a separate MCP Course (Units 0 to 3 plus 3.1), audited below as a related course and counted on its own line.

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| LLM Ch1 How Transformers solve tasks (text, speech and vision with one architecture) | COVERED | Ch 15 Transformers beyond text; Ch 22; Ch 46 | None |
| LLM Ch6 Training a tokenizer and fast-tokenizer mechanics (offset mapping, building a tokenizer block by block) | OUT OF SCOPE | Ch 18 tokenization concepts | None: library mechanics for programmers |
| Agents Unit 1 Dummy agent library (an agent built from a raw prompt, no framework) | COVERED | Ch 28 "The whole agent is a loop" | None |
| MCP Course Unit 1 Concepts and architecture: hosts, clients, servers; JSON-RPC and transports; tools, resources, prompts and sampling | COVERED | Ch 28 MCP section (which notes sampling being phased out in the 2026 specification) | None |
| MCP Course Unit 1 SDKs, clients, the Hugging Face MCP server and Gradio integration | COVERED | Ch 28 connectors and registries; Ch 30 Gradio. SDK code is OUT OF SCOPE detail | None |
| MCP Course Unit 2 An end-to-end MCP application, MCP in coding assistants, Tiny Agents | COVERED | Ch 28; Ch 29 | None |
| MCP Course Units 3 and 3.1 Workflow servers for a coding agent (GitHub Actions, Slack) and a pull-request agent driven by webhooks | COVERED | Ch 29 tests, CI, webhooks and no-code automation; Ch 28 | None |

### 4. Full Stack Deep Learning

URLs: https://fullstackdeeplearning.com/ ; https://fullstackdeeplearning.com/course/2022/ and its nine lecture pages (https://fullstackdeeplearning.com/course/2022/lecture-1-course-vision-and-when-to-use-ml/, .../lecture-2-development-infrastructure-and-tooling/, .../lecture-3-troubleshooting-and-testing/, .../lecture-4-data-management/, .../lecture-5-deployment/, .../lecture-6-continual-learning/, .../lecture-7-foundation-models/, .../lecture-8-teams-and-pm/, .../lecture-9-ethics/); https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ and its eleven pages (launch-an-llm-app-in-one-hour, llm-foundations, prompt-engineering, augmented-language-models, ux-for-luis, llmops, askfsdl-walkthrough, whats-next, shabani-train-your-own, chase-agents, welinder-fireside-chat); https://fullstackdeeplearning.com/working-with-ai-agents/ (a manifesto page, not a course).

Latest offering: the site's newest course is the LLM Bootcamp (Spring 2023). FSDL 2022 remains the newest edition of the deep-learning course, and nothing newer than the Bootcamp is offered. Both are audited.

What differed for FSDL 2022: the nine lecture titles are correct. Two rows were not 2022 topics: "L1 Metrics and baselines" and "L9 Interpretability" (both corrected in place and dropped from the verified count). One row was renamed: "L3 Shadow tests in production" is the section "Test in Production, But Don't YOLO". Missed sections: L1 "ML-Powered Products vs MLOps"; L2 "Meta-Frameworks and Model Zoos"; L3 "ML Test Score"; L6 "Types of Distribution Drift" (sudden, gradual, periodic, temporary) and the retraining-strategy steps "Logging", "Curation" and "Dataset Formation"; L7 "Other Applications" (code, semantic search, going cross-modal); L9 "Tracking Carbon Emissions", "Deceptive Design and Dark Patterns", "AI Snake Oils" and "Frontiers: AI Rights and X-Risk". Merged without a new row: L1 "What's Hard in ML?" and "ML Feasibility Assessment" (prioritizing row), L2 TPUs (compute row), L3 "Adapt Regression Testing for Models" (evaluation-tests row), L6 proxy and data-quality metrics (monitoring row), L8 "Types of User Feedback" and "What is Agile for ML?" (product-design and managing rows). The labs are hands-on versions of the lecture topics and add no rows.

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| L1 ML-powered products versus MLOps | COVERED | Ch 10 MLOps; Ch 31 "From demo to product" | None |
| L2 Meta-frameworks and model zoos (PyTorch Lightning, Hugging Face) | COVERED | Ch 13 frameworks table (including Keras); Ch 30 Hugging Face tour. PyTorch Lightning not named (OUT OF SCOPE detail) | None |
| L3 ML Test Score (Google's 28-test production-readiness rubric) | MISSING | — | Added paragraph to Ch 10 "Testing a machine-learning system" (four areas of seven tests, half and full points, score = weakest area, 36 Google teams); definition: ML Test Score |
| L6 Drift patterns over time (sudden, gradual, periodic, temporary) | THIN | Ch 10 pandemic example only | Added to the Ch 10 monitoring paragraph, with the same-week-last-year rule for periodic drift; definition: Periodic drift (seasonal drift) |
| L6 Logging, curation and dataset formation for retraining | THIN | Ch 10 automated retraining; Ch 8 active learning | Added paragraph to Ch 10 "Retraining" (what to log, which examples to label, training window, the continual improvement workflow); definition: Prediction logging |
| L7 Other applications: code, semantic search, going cross-modal | COVERED | Ch 29; Ch 27; Ch 16 and Ch 22 | None |
| L9 Tracking carbon emissions | COVERED | Ch 40; Ch 41; Ch 58 per-prompt footprint | None |
| L9 Deceptive design and dark patterns | MISSING | Ch 58 engagement optimization only | Added subsection "Dark patterns: designs that work against the user" to Ch 31 (Brignull's 2010 catalogue, the FTC's September 2022 report and its four groups, AI versions, A/B tests that select manipulative designs); definition: Dark pattern (deceptive pattern) |
| L9 AI snake oil (perception versus judgment versus predicting social outcomes) | THIN | *AI Snake Oil* cited in reading lists only | Added subsection "A prior question: can it be predicted at all?" to Ch 58 with the 2020 Fragile Families Challenge numbers; definition: AI snake oil |
| L9 Frontiers: AI rights | COVERED | Ch 60 model welfare | None |

FSDL LLM Bootcamp (Spring 2023), the latest offering:

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Launch an LLM app in one hour (playground, notebook, deployed MVP) | COVERED | Ch 26 first API call in Colab; Ch 29 app builders; Ch 30 Gradio | None |
| LLM foundations: the Transformer decoder (embeddings, masked attention, positional encoding, residuals, layer norm, feed-forward) | COVERED | Ch 12 to Ch 15 | None |
| Notable LLMs (BERT, T5, GPT, Chinchilla, LLaMA, RETRO), code in training data, instruction tuning | COVERED | Ch 15; Ch 19 data mixtures and Chinchilla; Ch 20. RETRO not named (OUT OF SCOPE detail) | None |
| Prompt engineering: base models as simulators, limits of few-shot, character-level weakness, reasoning, reflection and ensembling | COVERED | Ch 19 base model; Ch 25; Ch 18 letter counting; Ch 21 self-consistency; Ch 28 evaluator-optimizer | None |
| Augmented LMs: retrieval (classic search, embeddings, indexes, vector databases, beyond naive embeddings) | COVERED | Ch 27 (BM25, HNSW, HyDE) | None |
| Augmented LMs: chains, tool use and plugins | COVERED | Ch 28 workflow patterns, tool use, plugins | None |
| UX for language user interfaces: interface principles, patterns (click-to-complete, autocomplete, command palette, chat), Copilot and Bing Chat case studies | COVERED | Ch 31 "Designing AI products people trust" and "When chat is the wrong interface"; Ch 29 autocomplete. The Bing Chat case is not named (example-level detail) | None |
| LLMOps: choosing proprietary or open models, prompt management, testing, evaluation metrics, deployment and monitoring, test-driven development | COVERED | Ch 26; Ch 30; Ch 31 evals, versioning, tracing, eval-driven development | None |
| Project walkthrough askFSDL (a retrieval bot: cleaning, ETL, embeddings, Gradio and Discord front ends, monitoring) | COVERED | Ch 27 Colab mini-RAG; Ch 30 Gradio; Ch 31 tracing | None |
| What's next: multimodality and robots, limits of scale, the data bottleneck, small models, AGI, safety | COVERED | Ch 49; Ch 19; Ch 53; Ch 60; Ch 55 and Ch 56; Ch 66 | None |
| Invited talk: training your own LLM (data pipelines, tokenizer training, training runs, evaluation, deployment) | COVERED | Ch 19; Ch 18; Ch 24. HumanEval not named (OUT OF SCOPE detail) | None |
| Invited talk: agents (ReAct, controlling tool use, parsing tool calls, memory, evaluation) | COVERED | Ch 28; Ch 31 "Evaluating agents" | None |
| Invited talk: early autonomous agents (AutoGPT, BabyAGI, CAMEL, Generative Agents) | MISSING | — | Added two paragraphs to Ch 28 (AutoGPT and BabyAGI in "Planning", with Harrison Chase's list of open problems; the 2023 Generative Agents town in "Memory"); definition: Generative agents. CAMEL not named |
| Fireside chat: from GPT research to the API and ChatGPT | COVERED | Ch 7 | None |

### Sources for the facts added to the book

- ML Test Score: Breck, Cai, Nielsen, Salib and Sculley, IEEE Big Data 2017, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ and the paper PDF https://storage.googleapis.com/gweb-research2023-media/pubtools/4156.pdf (28 tests, four sections, scoring rules, 36 teams, Table V wording).
- Generative Agents: https://arxiv.org/abs/2304.03442 (Park et al., April 2023; 25 agents; Valentine's Day party; observation, planning and reflection ablations).
- BabyAGI: https://raw.githubusercontent.com/yoheinakajima/babyagi/main/README.md ("The original BabyAGI from March 2023 introduced task planning..."). AutoGPT: https://raw.githubusercontent.com/Significant-Gravitas/AutoGPT/master/classic/README.md ("an experimental project to demonstrate autonomous GPT-4 operation", "one of the first implementations of autonomous AI agents"). Harrison Chase's challenge list: https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/chase-agents/.
- Dark patterns: https://www.ftc.gov/reports/bringing-dark-patterns-light (September 2022) and https://www.ftc.gov/news-events/news/press-releases/2022/09/ftc-report-shows-rise-sophisticated-dark-patterns-designed-trick-trap-consumers (September 15, 2022; the four groups); https://www.deceptive.design/about-us (site started in 2010 as darkpatterns.org, founded by Harry Brignull); A/B-testing point from the FSDL Lecture 9 page.
- AI snake oil: the perception, judgment and social-prediction split as presented on the FSDL Lecture 9 page; Fragile Families Challenge, Salganik et al., PNAS 117(15):8398-8403 (2020), https://pmc.ncbi.nlm.nih.gov/articles/PMC7165437/ (160 teams, 4,242 families, 12,942 variables, waves from birth to age 9 predicting age-15 outcomes, holdout R² about 0.2 for GPA and material hardship and about 0.05 for the rest, a four-variable expert benchmark). The PNAS page itself refused the request (HTTP 403).
- Drift shapes, logging, curation and dataset formation: FSDL Lecture 6 page; feature change and label schema change: DMLS Ch8 section title "General Data Distribution Shifts"; nonprobability sampling: DMLS Ch4 section title (the paragraph uses standard statistics definitions only).

Edits this round: Ch 10 (three paragraphs; definitions Periodic drift (seasonal drift), Label schema change, Prediction logging, ML Test Score), Ch 11 (one paragraph; Nonprobability sampling, Convenience sampling), Ch 28 (two paragraphs; Generative agents), Ch 31 (new subsection; Dark pattern (deceptive pattern)), Ch 58 (new subsection; AI snake oil). Nine new definitions, each added to its chapter's Key terms list. `validate.py` and `check.py` report OK for chapters 10, 11, 28, 31 and 58.

### Updated counts

Verified topic counts = original rows, minus rows found not to belong to the standard, plus the new rows above. Status columns describe the book before any edits of either round.

| Standard | Topics | COVERED before | THIN | MISSING | OUT OF SCOPE | Covered after (in scope) |
|---|---|---|---|---|---|---|
| AI Engineering (2025) | 63 (60 + 3) | 55 (87%) | 5 | 3 | 0 | 63 of 63 (100%) |
| Designing ML Systems (2022) | 62 (53 + 9) | 39 (64% of 61 in scope) | 11 | 11 | 1 | 61 of 61 (100%) |
| Hugging Face LLM and Agents courses | 35 (32 + 3) | 25 (83% of 30 in scope) | 2 | 3 | 5 | 30 of 30 (100%) |
| Hugging Face MCP Course (related, added since) | 4 | 4 (100%) | 0 | 0 | 0 | 4 of 4 (100%) |
| Full Stack Deep Learning 2022 | 56 (48 − 2 + 10) | 33 (59%) | 11 | 12 | 0 | 56 of 56 (100%) |
| FSDL LLM Bootcamp (Spring 2023, latest offering) | 14 | 13 (93%) | 0 | 1 | 0 | 14 of 14 (100%) |
| All | 234 | 169 (74% of 228 in scope) | 29 | 30 | 6 | 228 of 228 (100%) |

Net effect of verification: the reconstructions of the two Huyen books and the Hugging Face courses were close (no invented rows; 15 sections missed or merged, all but three already covered: two THIN, one out of scope). The Full Stack Deep Learning list was the weakest: two rows were not 2022 topics (interpretability belonged to the 2021 course), and the 2022 ethics lecture's tech-ethics material (dark patterns, AI snake oil) and the continual-learning lecture's drift shapes and data curation had been skipped. The latest FSDL offering, the 2023 LLM Bootcamp, was already almost entirely covered, apart from the early-agent history now added to Chapter 28.
