# Coverage audit: real questions from learners and builders

Audited October 21, 2026. The test: collect questions that real people learning AI, building with AI or moving into AI careers actually ask in public, then check whether a beginner could find and understand the answer in this book. Every edit followed STYLE.md; all ten edited chapters (25, 26, 27, 28, 29, 30, 31, 63, 64, 65) pass `validate.py` and `check.py`.

## How the questions were collected

- **Hacker News "Ask HN" threads** (2,125 threads pulled through the public HN Algolia API for 60 topic queries, then filtered to relevant questions by points and wording).
- **Stack Exchange** (989 questions from AI Stack Exchange, Data Science Stack Exchange and Cross Validated through the public Stack Exchange API, ranked by views).
- **Developer and course forums** (759 topics from the OpenAI Developer Community, the DeepLearning.AI community and the Hugging Face forums through their public Discourse search).
- **FAQs:** the Ollama FAQ (docs.ollama.com/faq) and the fast.ai course page ("Is this course for me?").
- **Reddit:** reddit.com refuses automated access from this environment (HTTP 403 for search and pages), so subreddit threads could not be read directly. Three Reddit threads seen through search-engine mirrors are included with their canonical URLs (A4, B1, C21). The Reddit-style questions in scope (local hardware, RAG versus fine-tuning, career switching, wrapper startups) are well represented by the HN, Stack Exchange and forum threads above, which ask the same things. The session's web-search budget ran out during collection, so no further Reddit mirrors were searched.

Duplicates were merged (several source URLs in one row); wording is kept close to the original title. 205 distinct questions remain. Classification used grep across all 66 chapters and the appendices, then reading the passage: **ANSWERED** means a beginner could find and understand the answer; **PARTLY** means the pieces exist but the question is not really answered, or the answer is scattered; **NOT ANSWERED** means the book is silent.

## Summary

| | ANSWERED | PARTLY | NOT ANSWERED | Total |
|---|---|---|---|---|
| Before | 175 | 23 | 7 | 205 |
| After | 201 | 4 | 0 | 205 |

In addition, 4 questions that were answered but hard to find, or answered with a gap worth closing, got a cross-reference or a short addition where the reader looks first (D22, I14, K2, M10).

Left as PARTLY on purpose (C20, G20, I11, M8): a personal career choice the book already frames (C20), a speculative question (G20), a niche server setting (I11) and a question with no reliable data to cite (M8).

Where the gaps were: careers and job-hunting mechanics (interviews, where jobs are posted, age), running models on modest or non-NVIDIA hardware, the context cost of tools and MCP versus the command line, skill atrophy and invented packages in AI coding, embedding-model choice and local or agentic retrieval, and early-stage founder questions (first customers, funding). The core how-it-works and how-to-build material was already strong: 175 of 205 questions were fully answered before any edit.

## Edits made

- **Ch25:** The context window: 'Why is there a limit at all?' paragraph plus a KV cache definition (D22); Custom assistants: one sentence on no training versus fine-tuning (F8).
- **Ch26:** API keys: rule 6, keep the key on a server and never in a frontend (L3, M10); pricing: cross-reference to Chapter 61 on whether prices are subsidized (K2).
- **Ch27:** Why any embedding model pairs with any chat model (E8); 'Choosing an embedding model' with an MTEB definition (E7); agentic search without a vector database (E19).
- **Ch28:** New subsection 'Where agents pay off today, and where they do not' (G1); new subsection 'Every connected tool costs context: MCP or the command line?' (G9).
- **Ch29:** Hosting paragraph for beginners' projects (L3); Watch out on what coding agents send to the provider (M15); new subsection on skill atrophy with Anthropic's January 2026 trial (M11).
- **Ch30:** 'What about training your own model from scratch?' (F2); 'No GPU, a small GPU, or a non-NVIDIA one?' with a Layer offloading definition and the short-default-context trap (I7, I8, I13, I14, I15); pruning paragraph and definition (I10); fully private local RAG (E12); Ollama cloud models in the frontier box (I16).
- **Ch31:** Package hallucination (slopsquatting) paragraph and definition (M14).
- **Ch63:** 'Am I too old, or is it too late?' paragraph (A26); new subsection 'Finding openings and getting through interviews' with definitions of Coding interview, System-design interview and Take-home assignment (A24, C12, C13).
- **Ch64:** New subsection 'After the pilot: first customers and funding' with definitions of Bootstrapping, Angel investor and Accelerator (N4, N8, N10).
- **Ch65:** 'Python or R?' paragraph (A14).

New terms were added to each chapter's Key terms list.

## Sources relied on for new facts

- Anthropic, "How AI assistance impacts the formation of coding skills" (January 29, 2026): <https://www.anthropic.com/research/AI-assistance-coding-skills> (52 engineers; quiz 50% with AI versus 67% by hand; about two minutes faster, not significant).
- Spracklen et al., "We Have a Package for You!" (USENIX Security 2025): <https://arxiv.org/abs/2406.10279> (at least 5.2% of packages from commercial models and 21.7% from open models invented; 205,474 unique names).
- Anthropic Engineering, "Introducing advanced tool use" (November 24, 2025): <https://www.anthropic.com/engineering/advanced-tool-use> (five MCP servers, 58 tools, about 55K tokens; wrong-tool selection as a common failure).
- Muennighoff et al., "MTEB: Massive Text Embedding Benchmark" (2022): <https://arxiv.org/abs/2210.07316> (8 tasks, 58 datasets, 112 languages); leaderboard <https://huggingface.co/spaces/mteb/leaderboard>.
- "LLM Pruning and Distillation in Practice: The Minitron Approach" (2024): <https://arxiv.org/abs/2408.11796> (Llama 3.1 8B to 4B; Mistral NeMo 12B to 8B).
- Ollama FAQ <https://docs.ollama.com/faq> (`ollama ps`; default context 4,096 tokens; local prompts not seen; local-only mode), Ollama GPU docs <https://docs.ollama.com/gpu> (NVIDIA CUDA, AMD ROCm v7, Apple Metal, Vulkan), Ollama embeddings <https://docs.ollama.com/capabilities/embeddings> (`/api/embed`).
- Hugging Face, Spaces overview <https://huggingface.co/docs/hub/spaces-overview> (static Spaces free; Gradio and Docker Spaces need a paid plan, except up to 2 Gradio Spaces on ZeroGPU for free personal accounts; secrets settings).
- Y Combinator, "The YC Deal" <https://www.ycombinator.com/deal> ($500,000: $125,000 post-money SAFE for 7% plus $375,000 uncapped MFN SAFE).
- Hacker News "Ask HN: Who is hiring? (October 2026)" <https://news.ycombinator.com/item?id=49922569> and "Who wants to be hired?" <https://news.ycombinator.com/item?id=49922568> (monthly threads by the whoishiring account).
- Figures reused from the book itself (no new sourcing): Chapter 19 (70B on 15T tokens, about 4.4 million GPU-hours and $11 million), Chapter 65 (nanochat about $48), Chapter 61 (Sierra about $200M ARR; MIT NANDA 5%; Cursor acquisition; OpenAI gross-margin estimate).

## The questions

### A. Getting started and learning paths

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| A1 | How to learn AI from first principles? | <https://news.ycombinator.com/item?id=42827913> | ANSWERED | Ch65 Track C 1–3 years (Zero to Hero, nanochat, UDL, d2l, CS336); Ch12–19 build from first principles | None |
| A2 | How to seriously start with machine learning and AI? / What is the structured way to learn AI? | <https://news.ycombinator.com/item?id=16167620>; <https://community.deeplearning.ai/t/what-is-the-structured-way-to-learn-ai/893987> | ANSWERED | Ch65 Why you need a roadmap; Stage 1; Choosing your track (Figures 65.1, 65.2) | None |
| A3 | What is the roadmap for someone from a non-technical background with zero coding experience to enter applied AI engineering? | <https://community.deeplearning.ai/t/what-is-the-roadmap-for-someone-from-a-non-technical-background-with-zero-coding-experience-to-enter-applied-ai-engineering-ai-ml/870183> | ANSWERED | Ch65 Stage 1 and Track B (0–3 months: AI Python for Beginners, Colab); Ch63 Table 63.12 | None |
| A4 | I'm not a CS student: where do I start, when beginner videos jump straight into hard concepts? | <https://www.reddit.com/r/learnmachinelearning/comments/1j68n0q/> | ANSWERED | Ch65 Rule 1 (build first, understand as you go) and Stage 1; the book itself starts at Ch1 | None |
| A5 | Is this course for me? (What background do I need: how much coding and math?) | <https://course.fast.ai/> | ANSWERED | Ch65 Track C 3–12 months (fast.ai assumes about a year of coding; do Python first); course-length table | None |
| A6 | What should I learn first? | <https://discuss.huggingface.co/t/what-should-i-learn-first/190448> | ANSWERED | Ch65 Stage 1 (everyone starts here) and Figure 65.2 | None |
| A7 | What are the foundational texts for learning about AI/ML/NN? | <https://news.ycombinator.com/item?id=34312248> | ANSWERED | Ch65 Block 4 (two books) and Track C resource table; every chapter's Going deeper | None |
| A8 | Best introductory video courses on ML and deep learning? | <https://news.ycombinator.com/item?id=16138353> | ANSWERED | Ch65 course table and Track C (3Blue1Brown, fast.ai, Zero to Hero, CS224N/CS231n/6.S191) | None |
| A9 | What are the best resources today for learning AI/LLMs? | <https://news.ycombinator.com/item?id=41105348> | ANSWERED | Ch65 Track B core-stack table; Staying current | None |
| A10 | Go deep into AI/LLMs or just use them as tools? | <https://news.ycombinator.com/item?id=44079303> | ANSWERED | Ch65 Choosing your track and T-shape; Ch62 Choosing your path through the tree | None |
| A11 | How can a front-end developer dive into machine learning? | <https://news.ycombinator.com/item?id=14322953> | ANSWERED | Ch65 Track B; Ch63 Figure 63.4 (software engineer to AI engineer) | None |
| A12 | Where should an experienced developer start learning AI development? | <https://news.ycombinator.com/item?id=45685702>; <https://news.ycombinator.com/item?id=35543774> | ANSWERED | Ch65 Track B 0–12 months; Ch63 Table 63.12 | None |
| A13 | Which programming language should I learn for ML? | <https://community.deeplearning.ai/t/which-programming-should-i-learn-for-ml/399173> | ANSWERED | Ch65 Track B, Definition of Python | None |
| A14 | Python vs R for machine learning? | <https://datascience.stackexchange.com/questions/326> | PARTLY | Ch65 Track B says Python is the main AI language; R never mentioned | Added a short 'Python or R?' paragraph after the Python definition (Ch65 Track B) |
| A15 | Best way to learn basic Python? | <https://community.deeplearning.ai/t/best-way-to-learn-basic-python/714> | ANSWERED | Ch65 Track B core-stack table (CS50P, Kaggle Learn, AI Python for Beginners) | None |
| A16 | TensorFlow vs PyTorch? What is the path ahead? | <https://community.deeplearning.ai/t/tensorflow-vs-pytorch-what-is-the-path-ahead/809073> | ANSWERED | Ch13 Frameworks: PyTorch, JAX and TensorFlow/Keras; Ch65 Track C (PyTorch most widely used) | None |
| A17 | How much of ML is needed before deep learning? | <https://community.deeplearning.ai/t/how-much-of-ml-is-needed-before-deep-learning/814930> | ANSWERED | Ch65 Track C 3–12 months (classical ML specialization before fast.ai) | None |
| A18 | Does deep learning always outperform 'standard' ML models? | <https://community.deeplearning.ai/t/does-deep-learning-always-outperform-standard-ml-models/203467> | ANSWERED | Ch10 (boosted trees still win on tabular data; Watch out on 'deep learning made classical ML obsolete') | None |
| A19 | Can machine learning be self-taught? | <https://news.ycombinator.com/item?id=6334586> | ANSWERED | Ch65 whole chapter; Ch63 Credentials versus portfolios; Track C 'Do you need a PhD?' | None |
| A20 | How to approach ML research papers? | <https://community.deeplearning.ai/t/how-to-approach-ml-research-papers/717528> | ANSWERED | Ch65 Research skills (Keshav three-pass method, replication) | None |
| A21 | How do you cope with the latest updates in the AI space? / How to keep up with LLMs? | <https://community.deeplearning.ai/t/how-do-you-cope-up-with-latest-updates-in-ai-space/892486>; <https://news.ycombinator.com/item?id=36992439> | ANSWERED | Ch65 Staying current without drowning; ten-point hype checklist | None |
| A22 | I've taken the Coursera course (AI for Everyone / Andrew Ng). Now what? | <https://community.deeplearning.ai/t/ive-taken-the-coursera-course-now-what/99748>; <https://news.ycombinator.com/item?id=34716543> | ANSWERED | Ch65 stage progression and Track tables (next course after each stage) | None |
| A23 | Where to learn the cutting edge of prompt engineering? | <https://news.ycombinator.com/item?id=38588127> | ANSWERED | Ch25 Prompting techniques and context engineering; Ch65 resources | None |
| A24 | Are data structures and algorithms (DSA) required for ML? | <https://community.deeplearning.ai/t/dsa-required-for-ml/883044> | NOT ANSWERED | Not covered (only 'DSA' in the book is domain-specific architecture, Ch32) | Added 'Finding openings and getting through interviews' to Ch63 with a Coding interview definition covering data structures and algorithms |
| A25 | How does an LLM 'parameter' relate to a 'weight'? (What do the 175 billion parameters mean?) | <https://datascience.stackexchange.com/questions/120764>; <https://ai.stackexchange.com/questions/22673> | ANSWERED | Ch30 Definition of Weights (parameters); Ch12; Ch18 | None |
| A26 | Getting started with machine learning later in career: is it too late? | <https://news.ycombinator.com/item?id=5975362> | NOT ANSWERED | Not addressed directly (Ch63 transitions imply it) | Added a paragraph 'Am I too old, or is it too late?' to Ch63 Career paths and transitions |

### B. Math

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| B1 | Is entry-level calculus enough math for ML, or do I need linear algebra and more? | <https://www.reddit.com/r/learnmachinelearning/comments/1hp0k50/why_ml/> | ANSWERED | Ch65 Rule 1 (math needed at Level 5, not for building apps); Ch62 Math for machine learning; Ch5–6 | None |
| B2 | What math should I know well to be able to learn ML? | <https://news.ycombinator.com/item?id=13621892>; <https://news.ycombinator.com/item?id=10986002> | ANSWERED | Ch62 Math for machine learning (vectors and matrices, derivatives and gradients, probability); Ch5–6 | None |
| B3 | How to learn math from zero for adults? | <https://news.ycombinator.com/item?id=31539549> | ANSWERED | Ch65 Track C 0–3 months (3Blue1Brown, Khan Academy); Ch5–6 written for adults with no math background | None |
| B4 | What is the roadmap to self-taught probability and statistics for AI? | <https://stats.stackexchange.com/questions/609570> | ANSWERED | Ch6; Ch65 Track C (Khan Academy probability and statistics; DeepLearning.AI math course) | None |
| B5 | How much math do I need if I only build with AI rather than invent new methods? | <https://community.deeplearning.ai/t/maths-need-for-ai-and-machine-learning/708464> | ANSWERED | Ch65 Rule 1; Ch62 'much less needed to build apps' | None |
| B6 | Is there really a market for deep learning skills without a PhD? | <https://news.ycombinator.com/item?id=13472331> | ANSWERED | Ch65 'Do you need a PhD?'; Ch63 Family 1 Research | None |

### C. Skills, roles, portfolios and jobs

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| C1 | SWEs, how do you future-proof your career in light of LLMs? | <https://news.ycombinator.com/item?id=42431103>; <https://news.ycombinator.com/item?id=46386783> | ANSWERED | Ch63 A playbook for adapting your career (Figure 63.7, Table 63.14) | None |
| C2 | Has anyone successfully pivoted from web dev to AI/ML development? | <https://news.ycombinator.com/item?id=40866311> | ANSWERED | Ch63 Figure 63.4 and Table 63.12 (software engineer to AI engineer, 3–12 months) | None |
| C3 | How to break into AI engineering? | <https://news.ycombinator.com/item?id=36432598>; <https://community.deeplearning.ai/t/how-to-build-a-career-in-ai/189916> | ANSWERED | Ch65 Track B; Ch63 Family 2 Engineering | None |
| C4 | What is an 'AI engineer'? | <https://news.ycombinator.com/item?id=48312377>; <https://news.ycombinator.com/item?id=39990845> | ANSWERED | Ch65 Definition of AI engineer; Ch63 Family 2 table | None |
| C5 | What does an ML engineer do? | <https://news.ycombinator.com/item?id=27555013> | ANSWERED | Ch65 Definition of ML engineer; Ch63 Family 2 | None |
| C6 | Data scientist vs machine learning engineer: what is the difference? | <https://datascience.stackexchange.com/questions/28006> | ANSWERED | Ch63 Family 5 Data (Definition of Data scientist) and Family 2 (ML engineer) | None |
| C7 | Is making a self-taught transition to AI/ML related fields possible? | <https://news.ycombinator.com/item?id=37151555> | ANSWERED | Ch63 Career paths and transitions; Credentials versus portfolios; Ch65 | None |
| C8 | How to transition from software engineer to AI/ML engineer? | <https://news.ycombinator.com/item?id=40797858>; <https://news.ycombinator.com/item?id=39992764> | ANSWERED | Ch63 Table 63.12 (AI engineer to ML or research engineer); Ch65 Track C | None |
| C9 | Can I build a career as a prompt engineer without knowing how to code? | <https://community.deeplearning.ai/t/can-i-build-a-career-as-a-prompt-engineer-without-knowing-how-to-code/829210> | ANSWERED | Ch63 note on the faded 'prompt engineer' title; Ch62 Watch out | None |
| C10 | Have you ever hired someone because of certificates? Is a cloud ML certificate worth it? | <https://community.deeplearning.ai/t/have-you-ever-hired-one-because-of-certificates/880460>; <https://community.deeplearning.ai/t/is-gcp-ml-engineer-certificate-worth-it/268761> | ANSWERED | Ch63 Credentials versus portfolios; Ch65 Certifications: when they matter | None |
| C11 | Data science / AI portfolio project ideas? | <https://news.ycombinator.com/item?id=20075068>; <https://datascience.stackexchange.com/questions/842> | ANSWERED | Ch65 Portfolio projects that prove what you can do | None |
| C12 | With nothing but a portfolio (no degree), how do I start job-hunting? | <https://news.ycombinator.com/item?id=13566927> | PARTLY | Ch63 Credentials versus portfolios (portfolio beats credentials) but no job-search mechanics | Added 'Finding openings and getting through interviews' (Ch63) |
| C13 | Which platforms do you use to look for data science/AI jobs? | <https://community.deeplearning.ai/t/which-platforms-do-you-use-to-look-for-data-science-ai-jobs/32152> | NOT ANSWERED | Not covered (only lab job boards discussed) | Same new Ch63 subsection: careers pages, job sites, LinkedIn, HN 'Who is hiring?' thread (verified Oct 2026), public work |
| C14 | Can I switch from sales to data science/analysis with no degree in a year? | <https://datascience.stackexchange.com/questions/131582> | ANSWERED | Ch63 Table 63.12 (data analyst to data scientist 6–24 months; salesperson to AI account executive) | None |
| C15 | How to incorporate machine learning into my day job? | <https://news.ycombinator.com/item?id=18650646> | ANSWERED | Ch63 task audit and Figure 63.7; Ch65 Track A | None |
| C16 | What is the skillset for programmers at AI startups? | <https://news.ycombinator.com/item?id=12146841> | ANSWERED | Ch62 Levels 3–4; Ch63 Family 2 | None |
| C17 | Should I study machine learning or software engineering? | <https://news.ycombinator.com/item?id=40852322> | ANSWERED | Ch65 Figure 65.2 track chooser | None |
| C18 | Is vibe coding a new mandatory job requirement? | <https://news.ycombinator.com/item?id=47420767> | ANSWERED | Ch63 frontier box (engineers specify, test and review agent work); Ch62 Watch out on learning to code | None |
| C19 | What are your thoughts on the impact of AI on programming careers? Is AI replacing engineers? | <https://news.ycombinator.com/item?id=44647261>; <https://news.ycombinator.com/item?id=43831122> | ANSWERED | Ch63 Tasks, not jobs; jagged frontier; What the evidence shows so far; Ch29 METR study | None |
| C20 | Work on robotics or agents? (Which specialty to bet a career on) | <https://news.ycombinator.com/item?id=42651226> | PARTLY | Ch65 track chooser by interest; Ch49 robotics and Ch28 agents describe both fields | None: a personal choice; the book gives both landscapes and a way to choose |
| C21 | Do I need a master's or PhD to get hired to build AI models? | <https://reddit.sentinel-team.org/posts/1toljz2/snapshots/2026-05-28T07%3A25%3A31.25853Z> | ANSWERED | Ch65 'Do you need a PhD?' (Bachelor's or equivalent experience for research engineering) | None |

### D. Building apps on APIs

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| D1 | How does ChatGPT retain the context of previous questions? | <https://ai.stackexchange.com/questions/38150> | ANSWERED | Ch25 Statelessness: why the model 'remembers' your chat; Ch26 user and assistant messages | None |
| D2 | Meaning of roles in the API (system/user/assistant)? | <https://ai.stackexchange.com/questions/39837> | ANSWERED | Ch26 JSON read line by line; Definition of User and assistant messages; system prompt | None |
| D3 | What is the 'temperature' in the GPT models? | <https://ai.stackexchange.com/questions/32477> | ANSWERED | Ch26 Sampling settings; Ch18 temperature worked example | None |
| D4 | A better explanation of 'top P'? | <https://community.openai.com/t/a-better-explanation-of-top-p/2426> | ANSWERED | Ch26 Definition of Top-p; Ch18 Cutting off the long tail: top-k, top-p and min-p | None |
| D5 | Are there strictly deterministic LLMs? (Why do I get different answers to the same prompt?) | <https://ai.stackexchange.com/questions/43021>; <https://ai.stackexchange.com/questions/50762> | ANSWERED | Ch18 Watch out ('temperature 0 is not deterministic'); Ch31 Definition of Nondeterministic | None |
| D6 | Why does LLM inference cost scale in both input tokens and output tokens? | <https://ai.stackexchange.com/questions/41352> | ANSWERED | Ch26 Definition of input and output tokens; Ch23 prefill versus decode | None |
| D7 | How do I calculate image tokens? | <https://community.openai.com/t/how-do-i-calculate-image-tokens-in-gpt4-vision/492318> | ANSWERED | Ch22 visual tokens with worked cost arithmetic; Ch26 Multimodal input and output | None |
| D8 | How do the 'built on ChatGPT' apps work at a high level? | <https://ai.stackexchange.com/questions/39736> | ANSWERED | Ch26 Why talk to a model with code at all?; Ch61 Layer 5 applications | None |
| D9 | Creating a support chatbot for my business: how? | <https://ai.stackexchange.com/questions/39451> | ANSWERED | Ch27 RAG from end to end; Ch31 Juni support-assistant worked example | None |
| D10 | How do I stop the model answering questions outside the scope of the context I gave it? | <https://community.openai.com/t/how-to-prevent-chatgpt-from-answering-questions-that-are-outside-the-scope-of-the-provided-context-in-the-system-role-message/112027> | ANSWERED | Ch27 'What the model actually sees' (answer only from sources); Ch31 Guardrails (topic filter) and out-of-scope test cases | None |
| D11 | Is anyone using function calling with LLMs in production? How does it work? | <https://news.ycombinator.com/item?id=42775708> | ANSWERED | Ch28 How function calling works, step by step | None |
| D12 | Any models for text to JSON? (How do I get reliable structured output?) | <https://ai.stackexchange.com/questions/37365> | ANSWERED | Ch26 Structured outputs: getting forms, not prose | None |
| D13 | Which LLM provider gives real-time access to the internet through the API? | <https://datascience.stackexchange.com/questions/131595> | ANSWERED | Ch28 Client-side and server-side tools (web search, web fetch, prices) | None |
| D14 | How are companies building LLM-to-SQL database features in production? | <https://news.ycombinator.com/item?id=43015167>; <https://community.openai.com/t/creating-a-chatbot-using-the-data-stored-in-my-huge-database/245942> | ANSWERED | Ch27 Beyond text: tables and images (Definition of Text-to-SQL, and its pitfalls) | None |
| D15 | Building LLM apps? How are you handling user context and memory? | <https://news.ycombinator.com/item?id=44097699> | ANSWERED | Ch28 Memory; Ch25 Memory and Structured notes | None |
| D16 | What is the ideal format to structure AI prompts? | <https://news.ycombinator.com/item?id=39733697> | ANSWERED | Ch25 Your reusable prompt template; Technique 5 (XML tags) | None |
| D17 | Why does prompt engineering work at all? | <https://datascience.stackexchange.com/questions/128274> | ANSWERED | Ch18 Definition of In-context learning; Ch20 Instruction tuning | None |
| D18 | What LLM models are you using and why? (How do I choose a model?) | <https://news.ycombinator.com/item?id=48166147> | ANSWERED | Ch26 Choosing a model; Benchmarks versus your own evals; Ch24 | None |
| D19 | What's the difference between LangChain, LlamaIndex and others? Which framework do you use in production? | <https://news.ycombinator.com/item?id=38126764>; <https://news.ycombinator.com/item?id=38518890> | ANSWERED | Ch28 Agent SDKs and frameworks (table incl. LangGraph, LlamaIndex, and how to choose) | None |
| D20 | Why can't language models continuously learn once trained? Will it learn from my chats? | <https://ai.stackexchange.com/questions/37335>; <https://datascience.stackexchange.com/questions/122225> | ANSWERED | Ch18 (weights do not change while you chat); Ch66 Continual learning | None |
| D21 | What do API errors like 529 (overloaded) mean and what should my app do? | <https://news.ycombinator.com/item?id=47541097> | ANSWERED | Ch26 status-code table (429 and 500–599: wait and retry) and Rate limits and backoff | None |
| D22 | Why do models have a fixed context length? Isn't it an artificial restriction? | <https://ai.stackexchange.com/questions/37624>; <https://ai.stackexchange.com/questions/42313> | ANSWERED | Ch15 (attention cost grows with the square of length) and Ch30 KV cache, but not where readers meet the context window (Ch25) | Added a 'Why is there a limit at all?' paragraph with a KV cache definition to Ch25 The context window |
| D23 | How do I get a model to read a PDF through the API? | <https://datascience.stackexchange.com/questions/128634> | ANSWERED | Ch26 Multimodal input and output (PDFs as content blocks; Files API) | None |
| D24 | Why does ChatGPT type slowly? Is it computing? (streaming) | <https://ai.stackexchange.com/questions/39240> | ANSWERED | Ch26 Streaming and time to first token; Ch23 decode one token at a time | None |
| D25 | Why do LLMs make up facts (hallucinate) even when trained on large datasets? | <https://ai.stackexchange.com/questions/50438> | ANSWERED | Ch25 Why models make things up; Ch27 closed-book problem | None |

### E. Retrieval and RAG

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| E1 | How do I train a custom LLM/ChatGPT on my own documents? | <https://news.ycombinator.com/item?id=38759877>; <https://news.ycombinator.com/item?id=36832572> | ANSWERED | Ch27 Three ways to give a model knowledge; Ch30 What fine-tuning changes | None |
| E2 | How can I teach a book to an LLM? How do I add knowledge to an LLM? | <https://ai.stackexchange.com/questions/42157>; <https://stats.stackexchange.com/questions/616582>; <https://community.openai.com/t/how-do-i-upload-a-book-to-gpt3/1499> | ANSWERED | Ch27 Three ways to give a model knowledge; Ch30 'Fine-tuning is poor at adding facts' | None |
| E3 | Fine-tuning vs. embeddings (RAG): when do you choose which? | <https://community.openai.com/t/fine-tuning-vs-embedding/35813>; <https://news.ycombinator.com/item?id=49181196> | ANSWERED | Ch30 The decision ladder and Key idea; Ch27 | None |
| E4 | Why does fine-tuning not work as well as RAG for adding facts? | <https://ai.stackexchange.com/questions/45701> | ANSWERED | Ch30 What fine-tuning changes, and what it does not | None |
| E5 | How do vector databases work (for the lay-coder)? | <https://datascience.stackexchange.com/questions/123181> | ANSWERED | Ch27 Vector databases: finding neighbors fast (HNSW analogy) | None |
| E6 | Alternatives to a vector DB? Do I even need one? | <https://news.ycombinator.com/item?id=43401138> | ANSWERED | Ch27 'Brute force works, until it does not'; pgvector row in vector-database table | None |
| E7 | Best embedding models? | <https://news.ycombinator.com/item?id=48017668> | PARTLY | Ch27 names two OpenAI models and one open model, with prices, but no way to choose | Added 'Choosing an embedding model' (MTEB leaderboard plus a 20–50 question recall test) with an MTEB definition, Ch27 |
| E8 | How can RAG work when the embedding model is different from the LLM? | <https://ai.stackexchange.com/questions/45919> | PARTLY | Ch27 says the embedding model is separate; does not say the chat model never sees vectors | Added a two-sentence explanation after the Embedding model definition, Ch27 |
| E9 | How does RAG work around limited context length? | <https://datascience.stackexchange.com/questions/126252> | ANSWERED | Ch27 RAG from end to end; Long context or RAG? | None |
| E10 | How should I chunk PDFs for RAG? | <https://ai.stackexchange.com/questions/46493> | ANSWERED | Ch27 Chunking: cutting the book into index cards | None |
| E11 | What are you using to parse PDFs for RAG? | <https://news.ycombinator.com/item?id=41072632> | ANSWERED | Ch27 indexing pipeline step 2 (Definitions of Parsing and OCR) | None |
| E12 | How are you doing RAG locally, with a private knowledge base? | <https://news.ycombinator.com/item?id=46616529>; <https://news.ycombinator.com/item?id=41968366> | PARTLY | Pieces in Ch27 (local embedding model, Chroma) and Ch30 (local server) but never joined up | Added a 'fully private RAG' paragraph after the OpenAI-compatible API definition, Ch30 |
| E13 | How would you architect a RAG system for 10M+ documents today? | <https://news.ycombinator.com/item?id=46000077> | ANSWERED | Ch27 ANN search and HNSW; storage arithmetic for a million passages; metadata filters | None |
| E14 | What's the most effective way to reduce hallucinations in a RAG system? | <https://ai.stackexchange.com/questions/50575> | ANSWERED | Ch27 reranking, contextual retrieval, citations, Evaluating a RAG system | None |
| E15 | Is RAG the future, or will long context windows replace it? | <https://news.ycombinator.com/item?id=40034972> | ANSWERED | Ch27 Long context or RAG? | None |
| E16 | Why does RAG still feel clunky? Why does my RAG chatbot give bad answers? | <https://discuss.huggingface.co/t/why-does-rag-still-feel-clunky-in-2025/164650>; <https://news.ycombinator.com/item?id=44701172> | ANSWERED | Ch27 Evaluating a RAG system (retrieval versus faithfulness failures) | None |
| E17 | Embedding text length vs accuracy: how big should chunks be? | <https://community.openai.com/t/embedding-text-length-vs-accuracy/96564> | ANSWERED | Ch27 chunk size trade-off and overlap | None |
| E18 | Why can't plain keyword search (Lucene) be used to power LLM applications? | <https://ai.stackexchange.com/questions/41277> | ANSWERED | Ch27 Keyword search and BM25; Hybrid search | None |
| E19 | MCP/API search vs vector search: what's winning for you? (agentic search) | <https://news.ycombinator.com/item?id=44957735> | PARTLY | Ch27 Agentic RAG and Ch25 just-in-time retrieval, but not 'do agents need a vector index?' | Added a paragraph on agentic search without a vector database, Ch27 Agentic RAG |
| E20 | How do I evaluate whether my RAG pipeline is any good? | <https://news.ycombinator.com/item?id=41727287> | ANSWERED | Ch27 Evaluating a RAG system; Ch31 evals | None |

### F. Fine-tuning

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| F1 | What is the most efficient way to fine-tune an LLM? | <https://news.ycombinator.com/item?id=39934480> | ANSWERED | Ch30 LoRA and QLoRA; Where to fine-tune (Unsloth on Colab) | None |
| F2 | Is it feasible to train my own LLM (from scratch)? | <https://news.ycombinator.com/item?id=38844324>; <https://datascience.stackexchange.com/questions/122103> | PARTLY | Costs in Ch19 (From FLOPs to dollars) and nanochat in Ch65, but Ch30 never answers it | Added 'What about training your own model from scratch?' to Ch30, reusing Ch19 and Ch65 figures |
| F3 | How does deploying a fine-tuned model work? | <https://news.ycombinator.com/item?id=40129225> | ANSWERED | Ch30 Definitions of Adapter and Merging an adapter; Where to fine-tune (hosted fine-tunes are served by the provider); Exercise 8 (merge and convert to GGUF) | None |
| F4 | When is fine-tuning a small LLM worth it? | <https://news.ycombinator.com/item?id=49807413> | ANSWERED | Ch30 The decision ladder; When fine-tuning genuinely wins; cost worked example | None |
| F5 | Can fine-tuning change the stylistic output while keeping the model's knowledge? | <https://community.openai.com/t/fine-tuning-to-change-the-stylistic-output-while-keeping-the-llm-brain-knowledge/303340> | ANSWERED | Ch30 What fine-tuning changes; catastrophic forgetting | None |
| F6 | What to do when fine-tuning is not working? | <https://community.openai.com/t/what-to-do-when-fine-tuning-is-not-working/21133> | ANSWERED | Ch30 validation loss and overfitting; Data: the part that decides the result; risks | None |
| F7 | How to try out fine-tuning on a laptop? | <https://news.ycombinator.com/item?id=42772164> | ANSWERED | Ch30 QLoRA on a free Colab T4; MLX for Macs; Exercise 8 | None |
| F8 | Custom GPTs vs fine-tuning: what's the difference? | <https://community.openai.com/t/custom-gpts-vs-fine-tuning-whats-the-difference/477738> | PARTLY | Ch25 says a custom assistant is a prompt plus retrieval, but not explicitly that no training happens | Added one sentence contrasting custom assistants with fine-tuning, Ch25 Custom assistants |
| F9 | Fine-tuning or prompt engineering (prompt stuffing): which is more accurate? | <https://datascience.stackexchange.com/questions/122285>; <https://community.openai.com/t/whats-the-most-accurate-fine-tunning-vs-prompt-stuffing/392941> | ANSWERED | Ch30 The decision ladder table (prompt or few-shot first) | None |
| F10 | What do LoRA rank and alpha mean? | <https://datascience.stackexchange.com/questions/123229> | ANSWERED | Ch30 Definition of Rank (r) and the alpha paragraph | None |
| F11 | How much data do I need to fine-tune, and how long should it take? | <https://discuss.huggingface.co/t/my-dataset-is-250-docs-is-multiple-hours-tuning-normal/137239> | ANSWERED | Ch30 Data section ('hundreds to a few thousand'; 300-example split) | None |
| F12 | How do I fine-tune a model and then run it in Ollama? | <https://discuss.huggingface.co/t/how-to-use-hugging-face-to-fine-tune-ollamas-local-model/86134> | ANSWERED | Ch30 Exercise 8 (merge the adapter, convert to GGUF for Ollama or LM Studio) | None |
| F13 | What size language model can you train on a GPU with x GB of memory? | <https://datascience.stackexchange.com/questions/117444> | ANSWERED | Ch30 Under the hood: 16 bytes per parameter for full fine-tuning; QLoRA memory arithmetic | None |
| F14 | Have you successfully fine-tuned an LLM for anything useful? | <https://news.ycombinator.com/item?id=40409098> | ANSWERED | Ch30 When fine-tuning genuinely wins | None |
| F15 | Can I fine-tune on outputs from OpenAI models? (terms of service) | <https://news.ycombinator.com/item?id=37233250> | ANSWERED | Ch30 Watch out (terms of service forbid training a competitor on outputs); Ch24 distillation | None |

### G. Agents, tool use and MCP

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| G1 | What are some actual use cases of AI agents right now? Is anybody getting value from them? | <https://news.ycombinator.com/item?id=39373662>; <https://news.ycombinator.com/item?id=39886178>; <https://news.ycombinator.com/item?id=42629498> | PARTLY | Spread over Ch28, Ch29 and Ch61 (Sierra, MIT NANDA 5%) with no direct answer | Added 'Where agents pay off today, and where they do not', Ch28 |
| G2 | Do you think AI agents are overhyped? | <https://news.ycombinator.com/item?id=40646631> | ANSWERED | Ch28 METR time horizon and 'reliability compounds'; new Ch28 subsection | None |
| G3 | Best multi-agent frameworks? How do swarms of AI agents work? | <https://news.ycombinator.com/item?id=39742800>; <https://news.ycombinator.com/item?id=50047180> | ANSWERED | Ch28 Multi-agent systems | None |
| G4 | Should I use a framework to build an agent? Code vs LangGraph vs workflows | <https://news.ycombinator.com/item?id=41722243>; <https://news.ycombinator.com/item?id=44353964> | ANSWERED | Ch28 Agent SDKs and frameworks (how to choose); Five workflow patterns | None |
| G5 | What makes an AI agent framework production-ready vs a toy? | <https://news.ycombinator.com/item?id=46998170> | ANSWERED | Ch28 frameworks table (durable state); Ch31 LLMOps tracing and budgets | None |
| G6 | What is so good about MCP servers? Why do we need MCP? | <https://news.ycombinator.com/item?id=44678426>; <https://news.ycombinator.com/item?id=49488654>; <https://news.ycombinator.com/item?id=44105131> | ANSWERED | Ch28 The integration problem (10 × 50 versus 10 + 50) | None |
| G7 | What is the benefit of using MCP over a dictionary of functions (plain function calling)? | <https://news.ycombinator.com/item?id=43553482> | ANSWERED | Ch28 The integration problem; Hosts, clients and servers | None |
| G8 | Is MCP mature enough to use safely? | <https://news.ycombinator.com/item?id=43611739> | ANSWERED | Ch28 A plug, not a guarantee (CVEs, NSA warning); Ch31 supply chain | None |
| G9 | Are you team MCP or team CLI? | <https://news.ycombinator.com/item?id=47578918> | NOT ANSWERED | Not covered (tool definitions' context cost; MCP versus command line) | Added 'Every connected tool costs context: MCP or the command line?' with Anthropic's Nov 2025 figures, Ch28 |
| G10 | How do I set up a remote MCP server and connect it to ChatGPT? | <https://community.openai.com/t/how-to-set-up-a-remote-mcp-server-and-connect-it-to-chatgpt-deep-research/1278375>; <https://news.ycombinator.com/item?id=45715628> | ANSWERED | Ch28 transports and OAuth; Exercise 9 'Build and connect your own MCP server' | None |
| G11 | Who is using MCP in production? | <https://news.ycombinator.com/item?id=49548600> | ANSWERED | Ch28 MCP history and adoption (OpenAI, Linux Foundation counts) | None |
| G12 | I still don't understand why AI agents need 'skills' | <https://news.ycombinator.com/item?id=49139845> | ANSWERED | Ch28 Agent Skills; Ch25 Skills and progressive disclosure | None |
| G13 | How are you sandboxing coding agents? | <https://news.ycombinator.com/item?id=46400129>; <https://news.ycombinator.com/item?id=46699324> | ANSWERED | Ch28 and Ch29 Definitions of Sandbox; Ch31 Defense in depth | None |
| G14 | Do you trust AI agents with API keys / private keys? | <https://news.ycombinator.com/item?id=47736831> | ANSWERED | Ch31 least-privilege tools and scoped credentials; Ch28 OAuth scopes | None |
| G15 | When do we expose 'humans as tools' so agents can call us on demand? (human in the loop) | <https://news.ycombinator.com/item?id=46456400> | ANSWERED | Ch28 Stop conditions, budgets and humans in the loop | None |
| G16 | How do you know if AI agents will choose your tool? | <https://news.ycombinator.com/item?id=47127532> | ANSWERED | Ch28 Designing good tools; Exercise 4 'Fix three bad tools' | None |
| G17 | Any local agents to help with repetitive browser tasks? | <https://news.ycombinator.com/item?id=45416971> | ANSWERED | Ch28 Computer-use and browser agents and their security | None |
| G18 | How are you keeping AI coding agents from burning money? | <https://news.ycombinator.com/item?id=47559293>; <https://news.ycombinator.com/item?id=49673825> | ANSWERED | Ch28 budgets and stop conditions; Ch29 What it costs: a worked example | None |
| G19 | Is 'prompt injection' going to be a new common vulnerability? | <https://news.ycombinator.com/item?id=34719586> | ANSWERED | Ch31 Jailbreaks versus prompt injection; lethal trifecta | None |
| G20 | Will MCP replace GUIs talking to back ends via REST APIs? | <https://news.ycombinator.com/item?id=44412773> | PARTLY | Ch28 MCP Apps and computer use touch on it | None: speculative; the book describes the pieces |

### H. Evals, production and security

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| H1 | How are people doing AI evals these days? | <https://news.ycombinator.com/item?id=47319587>; <https://news.ycombinator.com/item?id=40920731> | ANSWERED | Ch31 Evals: how you know it works (golden set, graders, worked example) | None |
| H2 | What tools are you using for AI evals? Everything feels half-baked | <https://news.ycombinator.com/item?id=44194187> | ANSWERED | Ch31 Tracing (LangSmith, Langfuse, Braintrust, Arize Phoenix and others) | None |
| H3 | How are generative AI companies monitoring their systems in production? | <https://news.ycombinator.com/item?id=37579771> | ANSWERED | Ch31 LLMOps: tracing, versioning, gateways, dashboards and drift | None |
| H4 | How are you improving your use of LLMs in production? | <https://news.ycombinator.com/item?id=36787924> | ANSWERED | Ch31 Eval-driven development; LLMOps | None |
| H5 | How are you dealing with PII in production LLM apps? | <https://news.ycombinator.com/item?id=38237861> | ANSWERED | Ch31 Guardrails (personal-data masking); Ch25 PII | None |
| H6 | Using hosted models with private company data: is it safe? Will they train on my data? | <https://discuss.huggingface.co/t/using-hugging-face-models-with-private-company-data/56403> | ANSWERED | Ch25 Privacy and data controls; Ch26 Watch out on API data terms; Ch30 local models | None |
| H7 | How to stop people stealing your agent's instructions, data and files? | <https://community.openai.com/t/how-to-stop-people-stealing-your-agent-data-and-files/1000559> | ANSWERED | Ch31 OWASP LLM07 System Prompt Leakage; Exercise 9 | None |
| H8 | What are you using to mitigate prompt injection? | <https://news.ycombinator.com/item?id=47342718> | ANSWERED | Ch31 Defense in depth; Red-teaming your own system | None |
| H9 | How does one detect hallucinations? | <https://news.ycombinator.com/item?id=39454961> | ANSWERED | Ch62 Verification; Ch27 faithfulness checks; Ch31 graders | None |

### I. Running models locally

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| I1 | Cheapest way to run local LLMs? | <https://news.ycombinator.com/item?id=38425761> | ANSWERED | Ch30 The local toolkit (free apps on the computer you have); memory table | None |
| I2 | Which LLMs can run locally on most consumer computers? | <https://news.ycombinator.com/item?id=40424519> | ANSWERED | Ch30 Will it fit? memory table ('comfortable home' column) | None |
| I3 | MacBook vs dedicated GPU for LLMs? Anyone using a Mac Studio for local AI? | <https://news.ycombinator.com/item?id=48694802>; <https://news.ycombinator.com/item?id=46907001> | ANSWERED | Ch30 Definition of Unified memory; How fast will it be? (bandwidth rule) | None |
| I4 | How can I estimate an LLM's memory requirements from its file size? What computer do I need? | <https://ai.stackexchange.com/questions/40839>; <https://ai.stackexchange.com/questions/40360> | ANSWERED | Ch30 memory rule of thumb; Try it (file size divided by parameters) | None |
| I5 | How much VRAM and how many GPUs to fine-tune a 70B model locally? | <https://discuss.huggingface.co/t/how-much-vram-and-how-many-gpus-to-fine-tune-a-70b-parameter-model-like-llama-3-1-locally/150882> | ANSWERED | Ch30 QLoRA (65B on one 48 GB GPU); full fine-tuning at 16 bytes per parameter | None |
| I6 | Which open models actually fit a 12 GB card? | <https://discuss.huggingface.co/t/which-open-models-actually-fit-a-12-gb-card-we-measured-instead-of-guessing/180521> | ANSWERED | Ch30 memory table plus KV cache arithmetic | None |
| I7 | Can I run a local LLM without a GPU (CPU only, low memory)? | <https://news.ycombinator.com/item?id=48487147>; <https://datascience.stackexchange.com/questions/126058> | PARTLY | Ch30 says llama.cpp runs on CPUs and that spilling out of VRAM is slow, but never answers 'no GPU?' | Added 'No GPU, a small GPU, or a non-NVIDIA one?' to Ch30 Where the memory lives |
| I8 | Should I just get more RAM? (System RAM vs VRAM) | <https://discuss.huggingface.co/t/should-i-just-get-more-ram/132589> | PARTLY | Ch30 'spilling into ordinary memory slows it down a lot' only | Same paragraph plus a Layer offloading definition, Ch30 |
| I9 | How does quantization of models work? | <https://ai.stackexchange.com/questions/43513> | ANSWERED | Ch30 Quantization and GGUF (ruler figure, quant table); Ch23 | None |
| I10 | When to use pruning, quantization, distillation to optimize speed? | <https://ai.stackexchange.com/questions/43054> | PARTLY | Quantization and distillation covered; pruning not covered | Added a paragraph and a Pruning definition (Minitron example, arXiv 2408.11796), Ch30 |
| I11 | Does running a model on vLLM or Transformers use less VRAM than llama.cpp? | <https://ai.stackexchange.com/questions/50561> | PARTLY | Ch30 says vLLM is for serving many users; memory behavior not covered | None: niche server setting, outside a beginner's scope |
| I12 | How do I download a model from Hugging Face and run it locally (with Ollama)? | <https://discuss.huggingface.co/t/how-to-download-a-model-and-run-it-with-ollama-locally/77317>; <https://discuss.huggingface.co/t/how-do-i-run-hugging-face-models-locally-on-my-laptop/173391> | ANSWERED | Ch30 A tour of Hugging Face; The local toolkit; exercise running a model in LM Studio or Ollama | None |
| I13 | Can I use an AMD GPU instead of NVIDIA for local AI? | <https://discuss.huggingface.co/t/list-of-ai-projects-with-amd-gpu-support/53349>; <https://news.ycombinator.com/item?id=38757844> | PARTLY | Only 'many kinds of GPUs' in the llama.cpp definition | Same new Ch30 paragraph: AMD via ROCm, Apple via Metal, others via Vulkan (Ollama GPU docs) |
| I14 | How can I specify the context window size (and what does it do to memory)? | <https://docs.ollama.com/faq> | ANSWERED | Ch30 KV cache worked example ('local apps let you set the context length') | Added the trap of short default windows (Ollama FAQ: 4,096 tokens), Ch30 |
| I15 | How can I tell if my model was loaded onto the GPU? (Why is it so slow?) | <https://docs.ollama.com/faq> | PARTLY | Speed rule given but no way to check where the model is loaded | Same new Ch30 paragraph: `ollama ps` (Ollama FAQ) |
| I16 | Does Ollama send my prompts and answers back? Is local really private? | <https://docs.ollama.com/faq> | PARTLY | Ch30 'nothing leaves the machine' plus LM Studio cloud note; Ollama cloud models not mentioned | Extended the Ch30 frontier box with Ollama's cloud models and local-only mode (Ollama FAQ) |
| I17 | What do you use local LLMs for? Why run locally at all? | <https://news.ycombinator.com/item?id=40287323>; <https://news.ycombinator.com/item?id=44837130> | ANSWERED | Ch30 Why go local, and why not (table and quadrant chart) | None |
| I18 | Who uses open LLMs and coding assistants locally? Are they good enough? | <https://news.ycombinator.com/item?id=45771870> | ANSWERED | Ch30 quality trails the frontier; OpenAI-compatible API lets coding agents use a local model | None |
| I19 | Is it worth spending money on hardware (e.g. a MacBook Pro) to run LLMs locally instead of paying for APIs? | <https://news.ycombinator.com/item?id=47566687> | ANSWERED | Ch30 Worked example: does local save money? | None |
| I20 | Top models I can run with my hardware without 'lobotomization' (too-aggressive quantization)? | <https://discuss.huggingface.co/t/top-5-models-i-can-run-with-my-hardware-no-ai-lobotomization/177283> | ANSWERED | Ch30 quant table and Watch out ('test the specific quant') | None |

### J. Open versus closed models

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| J1 | Open-source LLM for commercial use? (licenses) | <https://news.ycombinator.com/item?id=35512338> | ANSWERED | Ch30 Licenses in plain words (permissive versus custom, Llama 700M MAU clause) | None |
| J2 | How do open-source LLMs compare to GPT-4 (frontier models)? | <https://ai.stackexchange.com/questions/41214> | ANSWERED | Ch30 'How far behind are they?' (Artificial Analysis index); Ch24 open versus closed | None |
| J3 | How can we measure when open models are 'good enough' to replace proprietary frontier models? | <https://ai.stackexchange.com/questions/50806> | ANSWERED | Ch26 Benchmarks versus your own evals; Ch24 Exercise 10 'Open versus closed on your own test' | None |
| J4 | Is Llama 3 fully open source? (open weights vs open source) | <https://ai.stackexchange.com/questions/46854> | ANSWERED | Ch30 and Ch24 Definitions of Open-weight and Open-source; Ch24 Watch out | None |
| J5 | Who is using small open-source LLMs in production? Self-hosted LLMs in your company? | <https://news.ycombinator.com/item?id=36969897>; <https://news.ycombinator.com/item?id=41902860> | ANSWERED | Ch24 the case for open weights; Ch30 worked example (self-hosting with vLLM at volume) | None |

### K. Costs

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| K1 | Will LLM API costs be negligible in a year? | <https://news.ycombinator.com/item?id=44851142> | ANSWERED | Ch23 Why prices fall ten times or more per year; Ch43 | None |
| K2 | Could free/low-cost LLMs be a momentary thing (are prices subsidized)? | <https://news.ycombinator.com/item?id=48176542> | ANSWERED | Ch61 Follow one subscription dollar; AI unit economics, but not reachable from Ch26 pricing | Added a cross-reference sentence in Ch26 How API pricing works |
| K3 | What's your biggest LLM cost multiplier? How do you keep costs low? | <https://news.ycombinator.com/item?id=46838390>; <https://news.ycombinator.com/item?id=40995465> | ANSWERED | Ch31 The levers; Ch26 caching and batch; Ch29 cost worked example | None |
| K4 | How much do you spend monthly on AI subscriptions? (subscription vs API) | <https://news.ycombinator.com/item?id=49290713> | ANSWERED | Ch26 subscription versus API comparison; Ch61 consumer subscription row | None |
| K5 | Why is token usage in coding agents increasing so quickly? (269,738 tokens to edit a 1,200-token file) | <https://community.openai.com/t/why-is-token-usage-in-codex-increasing-so-quickly-now/1386204>; <https://news.ycombinator.com/item?id=44603443> | ANSWERED | Ch29 What it costs: a worked example ('10 to 100 times the tokens'); Ch28 What a tool call costs | None |
| K6 | Would self-hosting a ChatGPT-class model be feasible in compute costs? | <https://ai.stackexchange.com/questions/39044> | ANSWERED | Ch30 Watch out ('Open does not mean runs on my laptop'); Ch23 serving | None |

### L. Deploying

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| L1 | How to deploy LLMs to serve a million users? | <https://news.ycombinator.com/item?id=35530478> | ANSWERED | Ch23 serving and batching; Ch26 rate limits and service tiers; Ch31 gateways and fallbacks | None |
| L2 | Best way to deploy an LLM for hundreds of users? What are you using for inference in production? | <https://news.ycombinator.com/item?id=40881966>; <https://news.ycombinator.com/item?id=49121047> | ANSWERED | Ch30 Definition of vLLM; Ch23 PagedAttention and batching | None |
| L3 | How do I share my demo app (e.g. Gradio) beyond my local machine? | <https://discuss.huggingface.co/t/how-to-share-gradio-app-in-my-local-machine/37979> | PARTLY | Ch29 explains deploying in principle; Ch30 mentions Spaces; no 'where do I host it' or key-placement advice | Added a hosting paragraph to Ch29 (Spaces terms per HF docs) and rule 6 'keep the key on a server' to Ch26 |

### M. Vibe coding and coding agents

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| M1 | Cursor or Windsurf? Which AI coding subscription is best? | <https://news.ycombinator.com/item?id=43959710>; <https://news.ycombinator.com/item?id=39633626> | ANSWERED | Ch29 The coding-agent landscape in late 2026; Choosing the right tool | None |
| M2 | Why is it called 'vibe coding'? | <https://news.ycombinator.com/item?id=44793378> | ANSWERED | Ch29 Vibe coding versus agentic engineering (Karpathy, Feb 2025) | None |
| M3 | Do you have any evidence that agentic coding works? Is anybody producing good code with coding agents? | <https://news.ycombinator.com/item?id=46691243>; <https://news.ycombinator.com/item?id=49934037> | ANSWERED | Ch29 Does AI actually make programmers faster? (METR RCT and the counter-evidence) | None |
| M4 | Become a 10x developer with LLMs: myth or reality? | <https://news.ycombinator.com/item?id=35574308> | ANSWERED | Ch29 same section | None |
| M5 | How are you LLM-coding in an established code base? | <https://news.ycombinator.com/item?id=46292682> | ANSWERED | Ch29 tool table ('change to an existing codebase at work'); instruction files; plan mode | None |
| M6 | What are your best practices for Claude Code? | <https://news.ycombinator.com/item?id=44776941>; <https://news.ycombinator.com/item?id=44362244> | ANSWERED | Ch29 Inside a coding agent (plan mode, permissions, sandbox, AGENTS.md/CLAUDE.md) | None |
| M7 | How to deal with AI-generated sloppy code? | <https://news.ycombinator.com/item?id=41677207> | ANSWERED | Ch29 agentic engineering (tests, review); quality studies | None |
| M8 | Have any successful startups been made by vibe coding? | <https://news.ycombinator.com/item?id=44952225> | PARTLY | Ch29 vibe coding limits; Ch61 app-builder companies | None: no reliable data on startups built purely by vibe coding |
| M9 | Client took over development by vibe coding. What to do? (When to call a professional) | <https://news.ycombinator.com/item?id=47599303> | ANSWERED | Ch29 What can a non-programmer safely build? (decision flowchart) | None |
| M10 | Are you hesitant to install vibe-coded apps? (Are they secure?) | <https://news.ycombinator.com/item?id=50090796> | ANSWERED | Ch29 Lovable review (170 of 1,645 apps exposed data); access rules | Also added Ch26 rule 6 (no keys in frontends) |
| M11 | How do you handle skill atrophy from using coding agents? | <https://news.ycombinator.com/item?id=48554309> | NOT ANSWERED | Not covered (Ch65 warns learners against letting the chatbot think for them) | Added 'Will leaning on agents weaken your own skills?' with Anthropic's Jan 2026 RCT, Ch29 |
| M12 | Are you using an agent orchestrator (several agents in parallel) to write code? | <https://news.ycombinator.com/item?id=46993479> | ANSWERED | Ch29 Generation 5: fleets of agents | None |
| M13 | What are some impressive vibe-coding projects? What can a non-programmer build? | <https://news.ycombinator.com/item?id=45642527> | ANSWERED | Ch29 What can a non-programmer safely build?; AI app builders | None |
| M14 | Why does ChatGPT create fake code (functions and packages that don't exist)? | <https://ai.stackexchange.com/questions/38538> | NOT ANSWERED | Ch31 covers typosquatting but not invented packages | Added paragraph and Package hallucination (slopsquatting) definition with USENIX Security 2025 figures, Ch31 |
| M15 | Any indications Copilot scans your local files? What does a coding assistant see and send? | <https://news.ycombinator.com/item?id=29150011> | PARTLY | Ch25 privacy controls cover chat apps only | Added a Watch out on what coding agents send to the provider, Ch29 Inside a coding agent |
| M16 | Is AI the final nail in the coffin for solo developers? | <https://news.ycombinator.com/item?id=47059223> | ANSWERED | Ch64 The aspiring builder; Ch63 playbook | None |

### N. Startups and business ideas

| # | Question | Source URL | Status before | Where answered | Action |
|---|---|---|---|---|---|
| N1 | How do you plan on making money with the OpenAI API? | <https://news.ycombinator.com/item?id=34622355> | ANSWERED | Ch64 Twenty-six business ideas; How AI businesses charge | None |
| N2 | What's the verdict on GPT wrapper companies? Isn't all SaaS just wrappers? | <https://news.ycombinator.com/item?id=44494189>; <https://news.ycombinator.com/item?id=41382330>; <https://news.ycombinator.com/item?id=42910057> | ANSWERED | Ch64 Thin wrappers and the model eating your feature; Ch61 Moats | None |
| N3 | How many of you are profiting with LLM wrapper apps? Are you making money from LLMs? How? | <https://news.ycombinator.com/item?id=47490278>; <https://news.ycombinator.com/item?id=41555908> | ANSWERED | Ch61 Case studies from 2025–2026; Ch64 Lessons from the winners | None |
| N4 | How to succeed with an AI SaaS when I have no audience and limited budget? | <https://news.ycombinator.com/item?id=39842321> | PARTLY | Ch64 eight-step validation method, but nothing on reaching customers without an audience | Added 'After the pilot: first customers and funding', Ch64 |
| N5 | What is one AI startup idea that's solving a real problem? | <https://news.ycombinator.com/item?id=43626728> | ANSWERED | Ch64 idea tables with who pays and why | None |
| N6 | Is there money in RAG? | <https://news.ycombinator.com/item?id=42749275> | ANSWERED | Ch64 idea 20 (private AI for regulated firms) and RAG-related ideas; Ch27 Areas of opportunity | None |
| N7 | We sold our first AI agent to a legacy industry, now we're stuck. Advice? | <https://news.ycombinator.com/item?id=44062543> | ANSWERED | Ch64 When a service business hits its ceiling; Customer concentration | None |
| N8 | How to reach angel investors for an agentic AI startup? | <https://news.ycombinator.com/item?id=42189648> | NOT ANSWERED | Only definitions of funding rounds and VC (Ch61) and a YC Startup School link | New Ch64 subsection with bootstrapping, angels, accelerators (YC deal verified) and three definitions |
| N9 | No interest in my idea (private LLM and RAG for teams): how to proceed? | <https://news.ycombinator.com/item?id=40960288> | ANSWERED | Ch64 Steps 1–3 (mine your pain, test AI fit, interview buyers); kill rule | None |
| N10 | How do SaaS founders get their first 100 customers? | <https://news.ycombinator.com/item?id=49674396> | PARTLY | Ch64 Step 3 and Step 8 only | Same new Ch64 subsection (first customers) |
| N11 | Why do we see no companies offering to deploy local LLMs (private AI for businesses)? | <https://news.ycombinator.com/item?id=42194889> | ANSWERED | Ch64 idea 20 'Private AI on open-weight models for regulated small firms' | None |
| N12 | Why do LLM providers sell access instead of consulting services? | <https://news.ycombinator.com/item?id=46911911> | ANSWERED | Ch61 Business models; Ch63 forward-deployed engineering departments at the labs | None |
| N13 | How do solo devs protect their work (build a moat) in the age of vibe coding? | <https://news.ycombinator.com/item?id=47884457> | ANSWERED | Ch61 Moats and 'the model eats your feature'; Ch64 Step 7 | None |

