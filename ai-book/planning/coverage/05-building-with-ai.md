# Coverage audit: 05-building-with-ai.md

Audit of every topic-map item and named sub-item in section 1 of research file 05 (Using and Building with AI) against the book chapters, October 21, 2026. Owning chapters per OUTLINE.md: Part A to Ch 25, Part B to Ch 26, C1–C4 to Ch 27, C5–C6 to Ch 30, D1–D4 and D6 to Ch 28, D5 and D7 to Ch 29, Part E to Ch 31 (with Ch 22 for A3.6, A3.9 and B5). Status reflects the book before this audit's edits.

| Item | Status before | Where covered (chapter and section) | Action taken |
|---|---|---|---|
| A1.1 Model vs. app vs. company | COVERED | Ch 25, "The model, the app and the company" (engine and car-body analogy, company/app/model table) | None |
| A1.2 Text in, text out; tokens | COVERED | Ch 25, "Tokens: what the model reads and what everyone pays for" (tokenizer definition, token counts differ between models, worked word-to-token example) | None |
| A1.3 The context window | COVERED | Ch 25, "The context window: the model's desk" (Figure 25.1, desk analogy) | None |
| A1.4 Statelessness | COVERED | Ch 25, "Statelessness: why the model 'remembers' your chat" (Figure 25.2, 105,000-token worked example) | None |
| A1.5 Why models make things up | COVERED | Ch 25, "Why models make things up" (hallucination, knowledge cutoff, grounding) | None |
| A2.1 Clear and direct | COVERED | Ch 25, "Prompting: how to brief a brilliant new hire" (Anthropic's framing, golden rule) and "Technique 1: Be specific about the job" | None |
| A2.2 The parts of a good prompt | COVERED | Ch 25, "Technique 2: Use the parts of a good prompt" (table, Figure 25.3) and "Your reusable prompt template" | None |
| A2.3 Explaining the "why" | COVERED | Ch 25, "Technique 3: Explain why, not just what" (read-aloud example) | None |
| A2.4 Examples (zero-, one-, few-shot) | COVERED | Ch 25, "Technique 4: Show, don't just tell: examples" (3–5 examples, copying surface features warning) | None |
| A2.5 Structure and delimiters | COVERED | Ch 25, "Technique 5: Separate instructions from material" (delimiters, XML tags, link to prompt injection) | None |
| A2.6 Roles and system prompts | COVERED | Ch 25, "Technique 6: Give it a role, and know what a role can't do" (system prompt, custom instructions as mini system prompt) | None |
| A2.7 Thinking: chain-of-thought and reasoning models | COVERED | Ch 25, "Technique 7: Let it think when the problem is hard" (effort, adaptive thinking, when to turn up/down table); Ch 21 in depth | None |
| A2.8 Iteration and prompt chaining | COVERED | Ch 25, "Technique 8: Break big jobs into a chain" (Figure 25.4) and "Technique 12: Iterate like an editor" | None |
| A2.9 Long documents | COVERED | Ch 25, "Technique 9: Long documents: material first, question last" (up to ~30%, quote-first prompt) | None |
| A2.10 Meta-prompting | COVERED | Ch 25, "Technique 11: Meta-prompting: let the model write the prompt" (prompt generator and improver) | None |
| A2.11 Failure modes | COVERED | Ch 25, "When prompts fail: classic failure modes and how to catch them" (sycophancy, leading questions, made-up citations, overconfidence, lost in the middle, silent truncation, verification habits) | None |
| A3.1 Custom instructions and personalization | COVERED | Ch 25, "Custom instructions: your standing brief" | None |
| A3.2 Memory | COVERED | Ch 25, "Memory: notes the app keeps about you" (saved notes vs chat search, view/edit/delete, incognito chats) | None |
| A3.3 Projects | COVERED | Ch 25, "Projects: a briefing binder for ongoing work" | None |
| A3.4 Custom assistants (GPTs, Gems, Projects/Skills) | COVERED | Ch 25, "Custom assistants: GPTs, Gems and friends" (plus Agent Skill definition) | None |
| A3.5 Artifacts and Canvas | COVERED | Ch 25, "Artifacts and Canvas: building in the side panel" | None |
| A3.6 Files, vision and multimodality | COVERED | Ch 25, "Files, images and other media"; Ch 22, "How a picture becomes tokens" and "Worked example: what does one photo cost?" | None |
| A3.7 Web search and citations | COVERED | Ch 25, "Web search and citations" | None |
| A3.8 Deep research | COVERED | Ch 25, "Deep research: a research assistant that runs for minutes" | None |
| A3.9 Voice mode | COVERED | Ch 25, "Voice mode" (latency challenge); Ch 22, "Speaking: the cascade versus native 'omni' voice" | None |
| A3.10 Connectors, apps and plugins | COVERED | Ch 25, "Connectors: plugging in your other services" (MCP, OAuth, permission screens) | None |
| A3.11 Agent modes inside chat apps | COVERED | Ch 25, "Agent modes: letting the AI act" (ChatGPT agent, ChatGPT Work, Cowork, Gemini Agent, approval prompts) | None |
| A3.12 Privacy and data controls | COVERED | Ch 25, "Privacy and data controls" (training opt-out, retention, consumer vs enterprise, what never to paste) | None |
| A4.1 Context engineering: definition | COVERED | Ch 25, "From prompt engineering to context engineering" (Anthropic's Sept 2025 definition quoted) | None |
| A4.2 Context rot | COVERED | Ch 25, "Context rot: why more context is not always better" (Figure 25.6) | None |
| A4.3 Techniques (compaction, notes, just-in-time, sub-agents, skills) | COVERED | Ch 25, "Compaction", "Structured notes", "Just-in-time retrieval", "Sub-agents and fresh chats", "Skills and progressive disclosure" (table and Figure 25.7) | None |
| B1.1 Client and server | COVERED | Ch 26, "Clients and servers" (restaurant analogy); Ch 4 | None |
| B1.2 The internet request | COVERED | Ch 26, "The web request" (URL, method, headers, body, status-code table) | None |
| B1.3 JSON | COVERED | Ch 26, "JSON, read line by line" | None |
| B1.4 Notebooks and Python | COVERED | Ch 26, "Notebooks and Python, in five minutes" and "Your first API call in Google Colab"; Ch 3 | None |
| B2.1 What an API is | COVERED | Ch 26, "What an API is" (Figure 26.1) | None |
| B2.2 API keys | COVERED | Ch 26, "API keys and how not to lose money" (secrets, spending limits, rotation) | None |
| B2.3 Anatomy of a request | COVERED | Ch 26, "Anatomy of a request and a response" (Figure 26.2) | None |
| B2.4 Anatomy of a response | COVERED | Ch 26, "Anatomy of a request and a response" (content blocks, stop reason, usage) and "Step 5: Read the whole response" | None |
| B2.5 SDKs | COVERED | Ch 26, "What an API is" (SDK definition, raw HTTP shown) | None |
| B2.6 Sampling settings | COVERED | Ch 26, "Sampling settings: the creativity dials" (temperature, top-p, reasoning models restricting them) | None |
| B3.1 Pricing per million tokens | COVERED | Ch 26, "How API pricing works" and "A worked cost example: 1,000 customer emails" (thinking tokens billed as output) | None |
| B3.2 Tokenizers differ | COVERED | Ch 26, "Tokenizers differ: compare cost per task, not per token" (~30% worked comparison) | None |
| B3.3 Rate limits | COVERED | Ch 26, "Rate limits and backoff" (RPM/TPM, usage tiers, 429, exponential backoff with jitter) | None |
| B3.4 Streaming | COVERED | Ch 26, "Streaming and time to first token" (TTFT worked example, code) | None |
| B3.5 Batch APIs | COVERED | Ch 26, "Batch APIs: half price if you can wait" | None |
| B3.6 Prompt caching | COVERED | Ch 26, "Prompt caching: pay once for the part that never changes" (worked example, "stable stuff first") | None |
| B3.7 Service tiers | COVERED | Ch 26, "Service tiers: paying for speed, or waiting for savings" (fast, flex, batch, data residency) | None |
| B4.1 Structured outputs: why | COVERED | Ch 26, "Structured outputs: getting forms, not prose" | None |
| B4.2 JSON Schema | COVERED | Ch 26, "Structured outputs" (definition and full schema example) | None |
| B4.3 Guarantees and failure cases | COVERED | Ch 26, "Structured outputs" (constrained decoding, refusal and max_tokens cases, validate content) | None |
| B4.4 Typical uses | COVERED | Ch 26, "Structured outputs" (extraction, classification, routing, forms) | None |
| B5.1 Multimodal input and output | COVERED | Ch 26, "Multimodal input and output"; Ch 22 | None |
| B5.2 Files APIs and image token cost | COVERED | Ch 26, "Multimodal input and output" (Files API definition); Ch 22, "Worked example: what does one photo cost?" | None |
| B6.1 Model tiers | COVERED | Ch 26, "Choosing a model" (tier table) | None |
| B6.2 Closed vs. open-weight | COVERED | Ch 26, "Choosing a model" (definitions); Ch 30 | None |
| B6.3 Selection criteria | COVERED | Ch 26, "Choosing a model" (six criteria) | None |
| B6.4 Routing and cascades | COVERED | Ch 26, "Routing and cascades" (worked $120 vs $27.90 example) | None |
| B6.5 Benchmarks vs. your evals | COVERED | Ch 26, "Benchmarks versus your own evals" | None |
| C1.1 Embeddings as a map of meaning | COVERED | Ch 27, "Embeddings: turning meaning into coordinates" (2D map, then hundreds of dimensions) | None |
| C1.2 Cosine similarity | COVERED | Ch 27, "Measuring closeness: cosine similarity by hand" | None |
| C1.3 Embedding models and cost | COVERED | Ch 27, "What embeddings cost" ($0.02 per million tokens worked example) | None |
| C2.1 Keyword search (BM25) | COVERED | Ch 27, "Keyword search and BM25" | None |
| C2.2 Semantic search | COVERED | Ch 27, "Semantic search" | None |
| C2.3 Hybrid search and RRF | COVERED | Ch 27, "Hybrid search and reciprocal rank fusion" | None |
| C3.1 Vector DBs and ANN (HNSW) | COVERED | Ch 27, "Approximate nearest neighbor search and HNSW" | None |
| C3.2 Vector DB options | COVERED | Ch 27, "What a vector database adds" (Chroma, pgvector, Pinecone, Weaviate, Qdrant, Milvus, Elasticsearch/OpenSearch table) | None |
| C3.3 Metadata filters | COVERED | Ch 27, "Metadata filters and permissions" | None |
| C4.1 The idea of RAG | COVERED | Ch 27, "Why a model needs to look things up" and "RAG from end to end" | None |
| C4.2 Indexing pipeline | COVERED | Ch 27, "The indexing pipeline: preparing the library" | None |
| C4.3 Query pipeline | COVERED | Ch 27, "The query pipeline: answering a question" and "What the model actually sees" | None |
| C4.4 Chunking | COVERED | Ch 27, "Chunking: cutting the book into index cards" | None |
| C4.5 Contextual retrieval | COVERED | Ch 27, "Contextual retrieval: giving each chunk its backstory" (35%/49%/67% table) | None |
| C4.6 Reranking | COVERED | Ch 27, "Reranking: a second, pickier judge" (top 50–150 candidates) | None |
| C4.7 Query transformation | COVERED | Ch 27, "Query transformation: fixing the question before searching" (rewriting, decomposition, HyDE) | None |
| C4.8 Agentic RAG | COVERED | Ch 27, "Agentic RAG: letting the model drive the search" | None |
| C4.9 GraphRAG and knowledge graphs | COVERED | Ch 27, "GraphRAG: questions about the whole collection" | None |
| C4.10 Long context vs. RAG | COVERED | Ch 27, "Long context or RAG?" | None |
| C4.11 Evaluating RAG | COVERED | Ch 27, "Evaluating a RAG system" (recall@k, faithfulness, citation checks) | None |
| C5.1 What fine-tuning is | COVERED | Ch 30, "What fine-tuning changes, and what it does not" | None |
| C5.2 The decision ladder | COVERED | Ch 30, "The decision ladder" (with worked cost example) | None |
| C5.3 Types (SFT, DPO, RFT, distillation) | COVERED | Ch 30, "The fine-tuning menu" | None |
| C5.4 LoRA and QLoRA | COVERED | Ch 30, "LoRA: the clip-on lens" and "QLoRA: fine-tuning on one GPU" | None |
| C5.5 Data | COVERED | Ch 30, "Data: the part that decides the result" (held-out test set) | None |
| C5.6 Where to fine-tune | COVERED | Ch 30, "Where to fine-tune" (hosted, Hugging Face TRL/PEFT, Unsloth, Axolotl) | None |
| C5.7 Risks | COVERED | Ch 30, "The risks of fine-tuning" (overfitting, catastrophic forgetting, weakened safety, maintenance) | None |
| C6.1 Open-weight models | COVERED | Ch 30, "Open-weight models: what you can download" | None |
| C6.2 Memory rule of thumb | COVERED | Ch 30, "Will it fit? The memory rule of thumb" | None |
| C6.3 Quantization and GGUF | COVERED | Ch 30, "Quantization and GGUF" | None |
| C6.4 Local tools | COVERED | Ch 30, "The local toolkit" (Ollama, LM Studio, llama.cpp, MLX, vLLM) | None |
| C6.5 Why and why not local | COVERED | Ch 30, "Why go local, and why not" (with worked cost example) | None |
| D1.1 The model only asks; your code acts | COVERED | Ch 28, "From talking to doing" and "The round trip" | None |
| D1.2 Tool definitions | COVERED | Ch 28, "The tool definition" | None |
| D1.3 Client-side vs. server-side tools | COVERED | Ch 28, "Client-side and server-side tools" (table with costs) | None |
| D1.4 Parallel calls, tool choice, errors as information | COVERED | Ch 28, "Choosing, combining and failing" | None |
| D1.5 Tool design | COVERED | Ch 28, "Designing good tools" (bad vs better definition table) | None |
| D2.1 Agents vs. workflows | COVERED | Ch 28, "Who decides the next step?" (train vs taxi analogy) | None |
| D2.2 The agent loop and ReAct | COVERED | Ch 28, "The agent loop" ("Think, act, observe, repeat", "A worked trace") | None |
| D2.3 Planning | COVERED | Ch 28, "Planning" (to-do list, re-planning example) | None |
| D2.4 Memory for agents | COVERED | Ch 28, "Memory" (short-term, working notes, long-term; episodic, semantic, procedural) | None |
| D2.5 Stop conditions and budgets | COVERED | Ch 28, "Stop conditions, budgets and humans in the loop" (30-step cost example) | None |
| D2.6 Workflow patterns | COVERED | Ch 28, "Five workflow patterns" (Figure 28.3 and table) | None |
| D2.7 Multi-agent systems (orchestrator, handoffs, debate and critique) | THIN | Ch 28, "Multi-agent systems": orchestrator, subagents, handoffs, benefits and costs explained; critique only as the single-call evaluator-optimizer pattern; debate between agents not mentioned (only as an AI-safety method in Ch 56) | Added a ~200-word paragraph to Ch 28 "Multi-agent systems" explaining critique and debate setups, their costs and limits, with a cross-reference to Ch 56; new definitions "Critic agent" and "Multi-agent debate"; Key terms updated |
| D2.8 Harnesses | COVERED | Ch 28, "Harnesses: the software around the model" (ARC-AGI-3 same-model example) | None |
| D2.9 Long-running agents and METR | COVERED | Ch 28, "How long can an agent work on its own?" (background agents, METR table, reliability compounding) | None |
| D3.1 MCP | COVERED | Ch 28, "The Model Context Protocol (MCP)" (hosts/clients/servers, primitives, transports, OAuth, registries, MCP Apps, Tasks, 2026-07-28 spec table) | None |
| D3.2 A2A and AP2 | COVERED | Ch 28, "A2A: agents talking to agents" (Agent Cards, AP2) | None |
| D3.3 Agent Skills | COVERED | Ch 28, "Agent Skills: playbooks loaded on demand" (SKILL.md example, progressive disclosure worked example); Ch 25 | None |
| D3.4 Instruction files (AGENTS.md, CLAUDE.md) | COVERED | Ch 28, "Instruction files: AGENTS.md and CLAUDE.md" | None |
| D3.5 Plugins and marketplaces | COVERED | Ch 28, "Plugins" (hooks, Cowork marketplace) | None |
| D3.6 Governance (Agentic AI Foundation) | COVERED | Ch 28, "Who governs the standards?" (AAIF, goose, A2A under Linux Foundation, why neutrality matters) | None |
| D4.1 Computer use | COVERED | Ch 28, "Computer-use and browser agents" (Figure 28.9 loop) | None |
| D4.2 Browser agents | COVERED | Ch 28, "Computer-use and browser agents" (DOM vs screenshots; Atlas, Claude in Chrome, Gemini in Chrome, Comet, Cowork, Codex) | None |
| D4.3 Where they work and fail | COVERED | Ch 28, "Computer-use and browser agents" (forms, chores, legacy apps; CAPTCHAs, confusing UIs, long chains) | None |
| D4.4 Security | COVERED | Ch 28, "Why browser agents are a security problem"; Ch 31, "AI security" | None |
| D5.1 Evolution of coding assistants | COVERED | Ch 29, "From autocomplete to coding agents" (five-generation timeline) | None |
| D5.2 How a coding agent works | COVERED | Ch 29, "Inside a coding agent" (harness, loop, worked cost example) | None |
| D5.3 The products | COVERED | Ch 29, "The coding-agent landscape in late 2026" | None |
| D5.4 Vibe coding | COVERED | Ch 29, "Vibe coding versus agentic engineering" (Karpathy, Feb 2025) | None |
| D5.5 Agentic engineering | COVERED | Ch 29, "Vibe coding versus agentic engineering" (specs, plan mode, tests, CI, sandboxes) | None |
| D5.6 What non-programmers can safely build | COVERED | Ch 29, "What can a non-programmer safely build?" | None |
| D6.1 Why frameworks | COVERED | Ch 28, "Agent SDKs and frameworks" | None |
| D6.2 Provider-native SDKs | COVERED | Ch 28, "Agent SDKs and frameworks" (Claude Agent SDK, OpenAI Agents SDK, Google ADK, hosted agents) | None |
| D6.3 Independent frameworks | COVERED | Ch 28, "Agent SDKs and frameworks" (LangGraph, LlamaIndex, CrewAI, Microsoft Agent Framework, Pydantic AI, Mastra) | None |
| D6.4 How to choose | COVERED | Ch 28, "Agent SDKs and frameworks" (five-step guide, start with no framework) | None |
| D7.1 Automation platforms and webhooks | COVERED | Ch 29, "No-code automation: making your apps talk to each other", "The three big platforms", "Worked example: the receipt logger" | None |
| D7.2 AI app builders | COVERED | Ch 29, "AI app builders: describe it, get an app" | None |
| D7.3 Limits | COVERED | Ch 29, "Their limits" (security defaults, lock-in, costs at scale, hand-off) | None |
| E1.1 Why evals | COVERED | Ch 31, "Why 'vibes' do not scale" | None |
| E1.2 Define success | COVERED | Ch 31, "Step 1: Define success in measurable terms" | None |
| E1.3 Golden datasets | COVERED | Ch 31, "Step 2: Build a golden dataset" and "How many test cases is enough?" (20, 200, 2,000 with margin-of-error table) | None |
| E1.4 Graders and judge biases | COVERED | Ch 31, "Step 3: Choose graders" and "The biases of AI judges" (position, verbosity, self-preference; calibration worked example) | None |
| E1.5 Offline vs. online | COVERED | Ch 31, "Offline and online evaluation" (A/B tests, thumbs, edits, eval flywheel) | None |
| E1.6 Agent evals | COVERED | Ch 31, "Evaluating agents" (pass@k and pass^k; SWE-bench, Terminal-Bench, tau-bench, OSWorld) | None |
| E1.7 Eval-driven development | COVERED | Ch 31, "Eval-driven development" | None |
| E2.1 Tracing | COVERED | Ch 31, "Tracing: the flight recorder" (spans, OpenTelemetry, Figure 31.4) | None |
| E2.2 LLMOps tools | COVERED | Ch 31, "Tracing: the flight recorder" (LangSmith, Langfuse, Braintrust, Arize Phoenix, Weave, Helicone) | None |
| E2.3 Versioning | COVERED | Ch 31, "Versioning: pin everything" | None |
| E2.4 Operations (gateways, budgets, deprecations) | COVERED | Ch 31, "Gateways, fallbacks and budgets" and "Versioning: pin everything" | None |
| E3.1 Input checks | COVERED | Ch 31, "Guardrails: checks around the model" (topic filters, PII masking, injection classifiers) | None |
| E3.2 Output checks | COVERED | Ch 31, "Guardrails: checks around the model" (moderation, schema, groundedness, policy rules) | None |
| E3.3 Action checks | COVERED | Ch 31, "Guardrails: checks around the model" (allow-lists, spend limits, approvals; Figure 31.6) | None |
| E3.4 Guardrail tools | COVERED | Ch 31, "Guardrails: checks around the model" (Llama Guard-style, NeMo Guardrails, Guardrails AI, cloud content safety) | None |
| E4.1 Prompt injection | COVERED | Ch 31, "Why language models are easy to fool" and "Jailbreaks versus prompt injection" (direct vs indirect, OWASP #1, no complete fix) | None |
| E4.2 Jailbreaks | COVERED | Ch 31, "Jailbreaks versus prompt injection" (role-play, encodings, many fake dialogues) | None |
| E4.3 Data exfiltration and lethal trifecta | COVERED | Ch 31, "Data exfiltration and the lethal trifecta" (image-link worked example, Figure 31.9) | None |
| E4.4 Tool and supply-chain risks | COVERED | Ch 31, "Poisoned tools and the AI supply chain" (tool poisoning, CVEs, typosquatting, OAuth scopes) | None |
| E4.5 Excessive agency | COVERED | Ch 31, "Excessive agency" (Replit database deletion) | None |
| E4.6 Defenses | COVERED | Ch 31, "Defense in depth" (reader-actor split, treat output as untrusted) and "Red-teaming your own system" | None |
| E4.7 Frameworks (OWASP LLM Top 10, OWASP agentic work, NIST AI RMF, MITRE ATLAS) | THIN | Ch 31, "The frameworks builders use": OWASP Top 10 (2025), NIST AI RMF and MITRE ATLAS explained; OWASP's separate agentic-security work not mentioned | Added a ~130-word paragraph to Ch 31 "The frameworks builders use" on why agents need separate security guidance and OWASP's agentic-application work, hedged (no edition details, since research file 05 gives none) with a mapping exercise |
| E5.1 The quality-cost-speed triangle | COVERED | Ch 31, "The triangle" and "Worked example: three model tiers for Juni" | None |
| E5.2 Levers | COVERED | Ch 31, "The levers" (table and worked caching/batching examples) and "Cascades and routing" | None |
| E5.3 Unit economics | COVERED | Ch 31, "Unit economics: can the product pay for itself?" (agentic 10–100x worked example) | None |
| E6.1 Copilot vs. autopilot | COVERED | Ch 31, "Copilot or autopilot?" (Figure 31.14 autonomy quadrant) | None |
| E6.2 UX patterns | COVERED | Ch 31, "Patterns that work" (Table 31.8) | None |
| E6.3 Trust calibration | COVERED | Ch 31, "Calibrating trust" (automation bias, under-trust) | None |
| E6.4 Conversation vs. GUI | COVERED | Ch 31, "When chat is the wrong interface" (generative UI, artifacts, MCP Apps) | None |
| E6.5 Onboarding and expectation-setting | COVERED | Ch 31, "When chat is the wrong interface" (closing paragraph on setting expectations) | None |
| E7.1 Adoption stages | COVERED | Ch 31, "How organizations adopt AI" (Figure 31.15 ladder, shadow AI) | None |
| E7.2 Buy vs. build | COVERED | Ch 31, "Buy or build?" (MIT NANDA ~67% vs about a third) | None |
| E7.3 Governance | COVERED | Ch 31, "Governance and change management" (policy, data classification, inventory, audit logs, SOC 2, ZDR, laws) | None |
| E7.4 Change management | COVERED | Ch 31, "Governance and change management" (training, champions, measuring value, redesigning workflows) | None |
| E7.5 Typical first wins | COVERED | Ch 31, "How organizations adopt AI" (support deflection, content, coding, document processing, internal search, back office) | None |

**Summary.** All 163 named sub-items in the five parts of the topic map were checked by searching the owning chapters for their key terms and reading the passages. Before this audit, 161 were COVERED, 2 were THIN and none were MISSING. Chapters 25 to 31 are thorough: almost every sub-item has its own section or subsection with a definition, a worked example or a diagram. The two thin spots were narrow: Chapter 28 explained orchestrators, subagents and handoffs but not agents that critique or debate each other (D2.7), and Chapter 31 covered the OWASP Top 10, NIST AI RMF and MITRE ATLAS but not OWASP's separate agentic-security work (E4.7). Both gaps were filled with short passages in the owning chapters, adding two definitions to Chapter 28. Research file 05 gives no detail on OWASP's agentic guidance, so the new Chapter 31 text describes it only in general terms and tells readers to check the current edition. Chapters 28 and 31 pass validate.py (all diagrams valid) and check.py (OK).
