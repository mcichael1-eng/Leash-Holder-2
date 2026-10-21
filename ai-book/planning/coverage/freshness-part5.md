# Freshness check, Part V (Chapters 25 to 31), web-verified October 21, 2026

Scope: every At the frontier box, every API price and worked cost example, context windows, product and plan names, coding and agent tools, agent protocols (MCP, A2A, Agent Skills, AGENTS.md), frameworks, open-weight model table, security frameworks. Primary sources were used wherever they could be fetched. The shared web-search quota ran out partway through; after that only direct fetches of official pages were possible, so a handful of older (2023 to 2025) historical facts were not re-checked and are marked UNVERIFIABLE (not re-checked) rather than CONFIRMED.

Main source keys used below:
- [A] Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- [B] Anthropic models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- [C] OpenAI API pricing: https://developers.openai.com/api/docs/pricing
- [D] OpenAI models: https://developers.openai.com/api/docs/models
- [E] Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- [F] Gemini models: https://ai.google.dev/gemini-api/docs/models
- [G] Claude Opus 5.5 migration guide: https://platform.claude.com/docs/en/models/opus-5-5/migration-guide
- [H] What's new in Claude Haiku 5.5: https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5
- [I] Claude prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- [M] METR time horizons page and data: https://metr.org/time-horizons and https://metr.org/assets/benchmark_results_1_1.yaml
- [V] Anthropic API version 2026-10-21 migration guide: https://platform.claude.com/docs/en/api/migration-2026-10-21

| Claim | Chapter and section | Verdict | Source URL | Change made |
|---|---|---|---|---|
| Model lineup by lab: GPT-6 family (Luna, Sol, Astra), GPT-6.1 Sol, GPT-5.6; Claude Haiku/Sonnet/Opus 5.5, Fable 5.1; Gemini 3.8 Flash, Gemini 4 Argon | 25, three-layer table | CONFIRMED | [C] [D] [B] [F] | None |
| Newer Claude tokenizer (4.7 and later) gives about 30% more tokens; about 555k vs 750k English words per 1M tokens | 25 tokens; 26 tokenizers; 31 model updates | CONFIRMED | [A] [B] | None |
| Current Claude models write up to 128,000 tokens per reply; 1M context | 25 context window; 26 frontier box 1 | CONFIRMED | [B] | None |
| Quote: "a brilliant but new employee who lacks context on your norms" | 25 mental model | CORRECTED | [I] | Quote completed: "...on your norms and workflows" |
| Long documents first, question last; up to about 30% better on complex multi-document inputs | 25 technique and answers; 27 prompt assembly | CONFIRMED | [I] | None |
| Anthropic suggests 3 to 5 examples | 25 examples | CONFIRMED | [I] | None |
| Text-to-speech ellipses example in Anthropic guidance | 25 give reasons | CONFIRMED | [I] | None |
| Prefill no longer accepted on the final turn from Claude 4.6 models | 25 definition; 31 model updates | CONFIRMED | [I] [G] | None |
| At the frontier (25, thinking): adaptive thinking steered by effort; manual extended thinking deprecated or rejected on newest models | 25 reasoning | CONFIRMED | [B] [G] [H] | None |
| OpenAI launched Deep Research in February 2025 | 25 deep research | UNVERIFIABLE (not re-checked) | none fetched | None |
| Feature-name table: Personal Intelligence (Gemini), Apps formerly Extensions, Gems, Canvas, Artifacts, Gemini Live | 25 feature table | CONFIRMED (Personal Intelligence, reported); rest not re-checked | https://www.androidauthority.com/google-gemini-personal-intelligence-rollout-3632287 | None |
| ChatGPT "renamed its apps to plugins in July 2026" | 25 frontier box and feature table; 28 connector definition and Exercise 5 | CORRECTED | https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex (July 9, 2026: app directory replaced by plugin directory, apps packaged into plugins); https://alpic.ai/blog/in-chatgpt-codex-merge-openai-combines-apps-and-plugins-all-based-on-mcp | Reworded in four places: the app directory was replaced by a plugin directory that packages apps, not a simple rename |
| ChatGPT reached 900 million weekly active users in February 2026 | 25 frontier box | CONFIRMED (reported, OpenAI figure) | https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users | None |
| A plugin can bundle skills, MCP connectors and an optional interface | 25 frontier box; 28 plugins | CONFIRMED | https://developers.openai.com/apps-sdk ("skills, MCP servers, and optional UI") | None |
| MCP Apps extension shows interactive UI in chat | 25 frontier box; 28; 31 | CONFIRMED (live January 26, 2026) | https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/ | None |
| Claude memory details (chat search on paid plans; memory default-on for Free, Pro, Max; opt-in Team/Enterprise; per-project memory; sensitive topics excluded; incognito excluded; deleting a chat keeps derived memories) | 25 memory | CONFIRMED | https://support.claude.com/en/articles/11817273 | None |
| ChatGPT agent (July 2025), Atlas browser (October 2025), Operator (January 2025) | 25 agent modes; 28 computer use | UNVERIFIABLE (not re-checked) | none fetched | None |
| ChatGPT Work launched July 2026 | 25 agent modes; 25 and 28 frontier boxes | CONFIRMED (reported, July 9, 2026) | https://www.androidauthority.com/chatgpt-work-launch-3685935/ | None |
| Cowork "is now just Claude", rolling out to Pro and Max; scheduled tasks with laptop closed; approval before significant actions and always before deleting | 25 agent modes; 31 frontier box | CONFIRMED | https://claude.com/product/cowork | None |
| Gemini Agent and Gemini in Chrome | 25 table; 28 frontier box | CONFIRMED (reported) | https://www.eesel.ai/es/blog/gemini-agent-agente-trabajo-google | None |
| MCP introduced November 2024, now under the Linux Foundation | 25 definition | CONFIRMED | https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation | None |
| Anthropic context-engineering post, September 2025 | 25, 28 | CONFIRMED (September 29, 2025) | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | None |
| At the frontier (25, context engineering): long-running agents; 1M windows; METR doubling 4 to 7 months, about 4 since 2023 | 25 | CONFIRMED (METR fits: 187.8 days all-time, 128.7 days since 2023) | [M] [B] [D] | None |
| Agent Skills began at Anthropic, released as open standard | 25, 28 definitions | CONFIRMED | https://agentskills.io/ | None |
| Anthropic API prices: Haiku 5.5 $0.10/$0.50 (above 100k tokens $0.50/$2.50); Sonnet 5.5 $2/$10; Opus 5.5 $4/$20; Fable 5.1 $10/$50 | 26 price table; 27; 28; 29; 30; 31 | CONFIRMED | [A] | None |
| Opus 5.5 is the default "for most workloads"; Fable 5.1 for demanding reasoning and long agentic work | 26 price and tier tables | CONFIRMED | [B] | None |
| OpenAI prices: gpt-6-luna $0.10/$0.50 (cached $0.01); gpt-6.1-sol $2/$10 (cached $0.10); gpt-6-astra $10/$50 (cached $1.00) | 26 price table; 31 tier table | CONFIRMED | [C] | None |
| OpenAI long-context surcharge above 272k input tokens (not mentioned) | 26 price table | ADDED | [C] | Notes column now gives $0.20/$0.75, $4/$15 and $20/$75 above 272k tokens |
| Gemini 3.8 Flash $0.75/$3.75, free tier, rises January 1, 2027; Gemini 4 Argon $2/$10 rising to $4/$20 on December 1, 2026 | 26 price table | CONFIRMED | [E] | None |
| Worked example, 1,000 emails: $3.80 Sonnet, $1.90 batch, $0.19 Haiku, $7.60 Opus, $19.00 Fable; thinking adds $3.00 | 26; recap; 31 batching lever | CONFIRMED (inputs unchanged) | [A] | None |
| Heavy chat user on API about $16.50 a month vs $20 plan | 26 | CONFIRMED (inputs unchanged) | [A] | None |
| Batch about 50% off at Anthropic, OpenAI and Google | 26 batch and tiers; 31 levers | CONFIRMED | [A] [C] [E] | None |
| Cache reads: "0.1 times on most models, including Sonnet 5.5 ($0.20 per MTok)" | 26 prompt caching | CORRECTED | [A] (Sonnet 5.5 and Opus 5.5 reads are 0.05x; Sonnet 5.5 $0.10) | Now: 0.1x on most models (Haiku 5.5 $0.01), 0.05x on Sonnet 5.5 ($0.10) and Opus 5.5 ($0.20), 0.025x on Fable 5.1 ($0.25) |
| Caching worked example, 50,000-token manual, 10 questions: $0.215, about 79% cheaper | 26 prompt caching | CORRECTED | [A] | Recomputed: reads 9 x 50,000 x $0.10 = $0.045; total $0.170; about 83% cheaper |
| Fast mode on Opus 5.5 at $8/$40 (2x) | 26 definition and tiers; 31 levers | CONFIRMED | [A] | None |
| OpenAI renamed priority processing to Fast mode on July 30, 2026 | 26 definition; 31 | CONFIRMED | https://developers.openai.com/api/docs/guides/fast-mode ; [C] | None |
| Flex: half price at OpenAI; matches batch for Gemini Flash | 26 tiers table | CONFIRMED | [C] [E] | Extended: also matches batch for Gemini 4 Argon |
| Gemini Priority about 1.8x | 26 tiers table | CONFIRMED | [E] | None |
| OpenAI Ultrafast tier (about 6x, gpt-6-astra and gpt-6.1-sol only) | 26 tiers table | ADDED | [C] | Added to the Priority or Fast row |
| OpenAI regional processing +10% for models released on or after March 5, 2026 | 26 tiers table | CONFIRMED | [C] | None |
| Current Claude models reject custom temperature and top-p | 26 sampling | CONFIRMED | [G] [H] | Added that API version 2026-10-21 rejects temperature, top_p and top_k outright |
| Raw request shows anthropic-version 2023-06-01 and x-api-key | 26 request walkthrough | CORRECTED / ADDED | [V]; https://platform.claude.com/docs/en/api/sdks/python ; https://pypi.org/project/anthropic/ (2.0.0 released October 21, 2026) | Example now shows 2026-10-21 and authorization: Bearer (what Python SDK 2.0 sends), plus one sentence that 2023-06-01 and x-api-key still work |
| Anthropic Python SDK retries twice by default | 26 rate limits; answers | CONFIRMED | https://platform.claude.com/docs/en/api/sdks/python | None |
| Thinking block carries no visible text by default on current Claude models | 26 response walkthrough | CONFIRMED (display defaults to omitted) | [G] | None |
| Routing example: $120 to $27.90 a day, about 77% and $33,000 a year | 26 routing; answers | CONFIRMED (inputs unchanged) | [A] | None |
| Haiku 5.5 is 40 times cheaper than Opus 5.5 | 26 exercises | CONFIRMED | [A] | None |
| At the frontier (26, cost controls): reads down to 0.025x on top model; 1M context; 128k output | 26 | CONFIRMED | [A] [B] | None |
| At the frontier (26, convergence): batch, caching, fast/flex, effort, 1M windows across providers; Anthropic web search $10 per 1,000 | 26 | CONFIRMED | [A] [C] [D] [E] | None |
| Free Gemini API tier for Flash-class models in AI Studio | 26 first call | CONFIRMED | [E] | None |
| Frontier models offer about 1M-token context | 27 options; 27 long context | CONFIRMED (Claude 1M, OpenAI 1.05M, Gemini 4 Argon 1M) | [B] [D] [F] | None |
| text-embedding-3-small $0.02, text-embedding-3-large $0.13 per MTok | 27 embedding costs | CONFIRMED | [C] | None |
| Contextual retrieval (September 2024): 35%, 49%, 67%; 5.7% to 1.9%; 50 to 100 token notes; top-20 beats 5 or 10 | 27 | CONFIRMED | https://www.anthropic.com/news/contextual-retrieval | None |
| Long context vs RAG at Opus 5.5 prices: $800, $40, $34 a day | 27 and Exercise 7 | CONFIRMED (0.05x reads on Opus 5.5) | [A] | None |
| OWASP 2025 lists Vector and Embedding Weaknesses | 27 risks | CONFIRMED (correctly dated 2025) | https://genai.owasp.org/llm-top-10/ | None |
| At the frontier (27, three boxes): permission-aware connectors via MCP; agentic search is default in leading apps; retrieval everywhere | 27 | CONFIRMED in substance (chat search, connectors and MCP documented); qualitative trend wording not separately checkable | https://support.claude.com/en/articles/11817273 ; https://claude.com/product/cowork | None |
| GraphRAG (Edge et al., 2024) | 27 | UNVERIFIABLE (not re-checked) | none fetched | None |
| Tool-call round-trip cost at Opus 5.5 prices | 28 | CONFIRMED | [A] | None |
| Some newest Claude models reject forced tool choice | 28 tool choice | CONFIRMED (Opus 5.5 rejects any and tool) | [G] | None |
| Anthropic server tools: web search $10 per 1,000; web fetch free; code execution free with search or fetch, else 1,550 free hours then $0.05 per hour | 28 tool table | CONFIRMED | [A] | None |
| 30-step agent run: about $4.26, about $0.70 with caching | 28 stop conditions | CONFIRMED (arithmetic re-checked at Opus 5.5 0.05x reads) | [A] | None |
| ARC Prize, September 2026: GPT-6 Astra 62.7% standard harness, 99.9% with state-preserving harness and compaction | 28 harness | CONFIRMED (September 3, 2026) | https://arcprize.org/blog/astra | None |
| At the frontier (28, harnesses): Claude Agent SDK, OpenAI Agents SDK and hosted agents; ChatGPT agent and Work, Cowork, Gemini Agent | 28 | CONFIRMED | https://code.claude.com/docs/en/overview ; https://openai.github.io/openai-agents-python/ ; [A] (Managed Agents) | None |
| METR table: GPT-4 about 4 min; Claude 3.5 Sonnet about 11 min; o1 about 39 min; o3 about 2 h; GPT-5 about 3.4 h; Opus 4.6 about 12 h (5 to 60 h); Mythos Preview early about 17 h | 28 METR | CONFIRMED (4.0, 11.4, 38.8, 119.7, 203.0, 718.8 and 1,044.8 minutes) | [M] | None |
| METR: original doubling about 7 months; since 2023 about 4 months; above 16 h unreliable; page stopped updating September 2026 | 28 METR | CONFIRMED (no longer updated, noted September 8, 2026) | [M] | None |
| MCP history: November 25, 2024; OpenAI March 2025; ChatGPT MCP support September 2025; donated to AAIF December 2025; close to half a billion SDK downloads a month; more than 10,000 servers (Wikipedia) | 28 MCP | CONFIRMED | https://blog.modelcontextprotocol.io/posts/2026-07-28/ ; https://en.wikipedia.org/wiki/Model_Context_Protocol ; https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/ | None |
| MCP 2026-07-28 spec: released July 28, 2026 after a May release candidate; "largest revision since launch"; stateless core, server/discover, subscriptions/listen, Tasks extension, MRTR, cacheable lists, OAuth/OpenID alignment, Sampling/Roots/Logging deprecated, 12-month deprecation policy | 28 spec table | CONFIRMED (RC May 21, 2026) | https://modelcontextprotocol.io/specification/2026-07-28/changelog ; https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ | None |
| MCP security: Invariant Labs tool poisoning April 2025; CVE-2025-6514 (9.6) July 2025; CVE-2025-49596; NSA May 2026 quote | 28; 31 supply chain | CONFIRMED (secondary source) | https://en.wikipedia.org/wiki/Model_Context_Protocol | None |
| A2A: Linux Foundation project; v1.0 first stable spec; April 2026 more than 150 organizations; Azure AI Foundry, Copilot Studio, Bedrock AgentCore; LangGraph and CrewAI; AP2 more than 60 organizations | 28 A2A | CONFIRMED (LF release dated April 9, 2026) | https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year ; https://a2a-protocol.org/latest/ | None |
| AAIF launched December 2025 with MCP, goose and AGENTS.md | 28 governance | CONFIRMED (December 9, 2025) | https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation | None |
| Missing June to October 2026 governance developments | 28 governance | ADDED | https://www.linuxfoundation.org/press/agentic-ai-foundation-launches-mcpa-certification-to-validate-mcp-expertise ; https://blog.modelcontextprotocol.io/posts/mcp-roadmap/ | One sentence: AAIF MCPA certification (September 2026); MCP roadmap (August 2026) prioritizes agent identity and enterprise security |
| Claude Cowork gained a plugin marketplace in February 2026 | 28 plugins | CONFIRMED (private plugin marketplaces, February 24, 2026) | https://claude.com/product/cowork | None |
| Claude Cowork has a built-in browser "since August 2026" | 28 computer use | UNVERIFIABLE (browser confirmed; August 2026 date not found in release notes) | https://claude.com/product/cowork ; https://support.claude.com/en/articles/12138966-release-notes | None; flagged |
| Anthropic's Chrome pilot reduced but did not eliminate attacks | 28 defenses | CONFIRMED | https://claude.com/blog/claude-for-chrome | None |
| OpenAI Agents SDK is a production-ready upgrade of Swarm | 28 SDK table | CONFIRMED | https://openai.github.io/openai-agents-python/ | None |
| Google ADK in Python, TypeScript, Java and Go | 28 SDK table | CORRECTED | https://adk.dev/ | Now "Python, TypeScript, Go, Java and Kotlin" |
| Microsoft Agent Framework succeeds Semantic Kernel and AutoGen; RC February 2026, 1.0 reported April 2026 | 28 SDK table | CONFIRMED (successor); dates UNVERIFIABLE, already marked "reported" | https://learn.microsoft.com/en-us/agent-framework/overview/ | None |
| At the frontier (28, center of gravity): MCP, skills, plugins, A2A; identity still being worked out in MCP and A2A specs | 28 | CONFIRMED | https://blog.modelcontextprotocol.io/posts/mcp-roadmap/ | None |
| Building effective agents (December 2024) | 28, 29, 31 | UNVERIFIABLE (not re-checked) | none fetched | None |
| Claude Code research preview February 24, 2025; GA May 2025 | 29 generations | CONFIRMED | https://www.anthropic.com/news/claude-3-7-sonnet ; https://www.anthropic.com/news/claude-4 | None |
| OpenAI Codex launched May 2025 | 29 | UNVERIFIABLE (not re-checked) | none fetched | None |
| At the frontier (29, manager of agents): METR horizons from minutes (2023) to many hours (2026) | 29 | CONFIRMED | [M] | None |
| Coding-agent session cost: cache reads 0.1x ($0.20) on Sonnet 5.5, total about $0.92, "about three quarters" saved | 29 cost example; answer 4 | CORRECTED | [A] | Recomputed at 0.05x ($0.10): 1.62M x $0.10 = $0.16; total about $0.76; "about four fifths"; answer key updated |
| Claude Pro $20 a month; Max $100 or $200 | 29; 31 | CONFIRMED (Pro $20 monthly; Max "from $100") | https://claude.com/pricing | None |
| Claude Code surfaces and features (terminal, VS Code, JetBrains, desktop, web, mobile, Slack, GitHub Actions; CLAUDE.md and AGENTS.md, skills, hooks, MCP, sub-agents, background agents, cloud scheduled tasks, Agent SDK) | 29 table | CONFIRMED | https://code.claude.com/docs/en/overview | None |
| Codex "runs on GPT-6.1 Sol" | 29 table | CORRECTED | https://learn.chatgpt.com/docs/models ; https://learn.chatgpt.com/docs | Now: OpenAI recommends GPT-6.1 Sol for most coding, Astra and Luna also offered (feature list confirmed) |
| Cursor: cloud agents, Bugbot, CLI, own Composer models | 29 table | CONFIRMED (Composer models not detailed on pricing page) | https://cursor.com/pricing | None |
| GitHub Copilot: cloud agent with Copilot, Claude or Codex; Free 2,000 completions; Pro $10, Pro+ $39, Max $100, Business $19, Enterprise $39 | 29 table and prices | CONFIRMED (Claude and Codex agents in preview on Pro+ and Max) | https://github.com/features/copilot/plans ; https://docs.github.com/en/copilot/get-started/plans | None |
| Antigravity: Gemini 4 Argon and 3.8 Flash; free for individual developers | 29 table | CORRECTED | https://antigravity.google/ | Now: Gemini 3.8 Flash, and Gemini 4 Argon for Google AI Pro and Ultra subscribers; no charge for individuals |
| Cognition (Devin, Windsurf), SWE-series models; $1B run-rate in September 2026 | 29 table and revenue | CONFIRMED (SWE-2 September 10; $1B post September 25, 2026) | https://cognition.com/blog | None |
| Claude Code run-rate above $2.5 billion (February 2026) | 29 revenue | CONFIRMED (February 12, 2026) | https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation | None |
| Roundups in October 2026 ranked Claude Code first, Codex second | 29 watch out | UNVERIFIABLE | none | None |
| Karpathy coined "vibe coding" February 2, 2025; Collins word of the year | 29 | UNVERIFIABLE (not re-checked) | none fetched | None |
| Lovable 170 of 1,645 apps (May 2025); Veracode October 2025; CodeRabbit December 2025 (1.7x, 2.74x); Replit database deletion July 2025 | 29; 31 | UNVERIFIABLE (not re-checked) | none fetched | None |
| METR RCT July 2025: 19% slower, felt about 20% faster | 29; 31 | UNVERIFIABLE (not re-checked) | none fetched | None |
| Zapier Agents work across 9,000+ apps | 29 platforms table | CONFIRMED | https://zapier.com/agents | None |
| n8n fair-code license, self-hostable, AI agent features | 29 platforms table | CONFIRMED | https://github.com/n8n-io/n8n | None |
| Receipt automation on Haiku 5.5 about 1.5 cents a month | 29 | CONFIRMED | [A] | None |
| Lovable reportedly valued at about $13.3 billion (August 2026) | 29 app builders | CORRECTED (now attributed to company announcement) | https://lovable.dev/blog (Series C post, August 12, 2026) | Now: announced a $400 million round at a $13.3 billion valuation |
| Replit Agent launched September 2024 | 29 | UNVERIFIABLE (not re-checked) | none fetched | None |
| Fine-tuning-vs-caching ladder: Sonnet cache reads 0.1x ($0.20), about $350 a month | 30 cost ladder | CORRECTED | [A] | Recomputed at 0.05x ($0.10): cached input $20; total about $330 |
| Haiku option about $36 a month; 95% saving | 30 cost ladder | CONFIRMED | [A] | None |
| Distillation: about 24,000 fraudulent accounts, over 16 million exchanges (February 2026) | 30 watch out | CONFIRMED (February 23, 2026) | https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks | None |
| At the frontier (30, low precision): Kimi K3 "trained with 4-bit (MXFP4) QAT", labs train low precision "from the start" | 30 | CORRECTED | https://huggingface.co/moonshotai/Kimi-K3 | Now: Kimi K3 used MXFP4 QAT from its fine-tuning (SFT) stage onward |
| Gemma 4 QAT checkpoints | 30 frontier box | CONFIRMED (QAT collections published) | https://huggingface.co/collections/google/gemma-4 | None |
| DeepSeek V4: V4-Pro GA August 2026; 1.6T/49B and 284B/13B; MIT; 1M context | 30 open-weights table | CONFIRMED (V4-Pro GA August 13, 2026) | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro ; https://api-docs.deepseek.com/news/news261017 | ADDED: V4.1-Flash is multimodal, September 2026, updated October 2026 |
| Qwen3.8 (August 2026): 27B dense Apache 2.0; 2.4T/95B needs a license above US$50 million revenue | 30 table | CONFIRMED (threshold applies to model-as-a-service and AI work-assistant businesses) | https://huggingface.co/Qwen/Qwen3.8-27B ; https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/main/LICENSE | None |
| Kimi K3 (July 2026) 2.8T/104B | 30 table | CONFIRMED | https://huggingface.co/moonshotai/Kimi-K3 | None |
| GLM-5.3 and MiMo-V2.6-Pro among top open models | 30 table | CONFIRMED | https://artificialanalysis.ai/leaderboards/models | None |
| gpt-oss (August 2025, 120B and 20B, Apache 2.0) | 30 table | UNVERIFIABLE (not re-checked) | none fetched | None |
| Gemma 4: April 2026; license "see the model card" | 30 table | CORRECTED | https://ai.google.dev/gemma/docs/releases (initial release March 31, 2026; 12B June 3, 2026); https://huggingface.co/google/gemma-4-31B-it (Apache 2.0) | Now "Late March 2026; 12B added June 2026" and "Apache 2.0". Note: Chapters 17 and 24 (outside this Part) say April 2026 / April 2, 2026; flag for their owners |
| Mistral: Medium 3.5 (128B, April 2026); Large 3 (December 2025, 675B/41B, Apache 2.0) | 30 table | CONFIRMED | https://docs.mistral.ai/getting-started/models/ ; https://huggingface.co/mistralai | ADDED Medium 3.5 license (modified MIT) |
| Mistral Large 4 (missing) | 30 table | ADDED | https://mistral.ai/news/mistral-large-4 | Preview October 6, 2026; 1T total, 52B active; weights promised by end of October |
| Meta Muse Glimmer open 30B (August 2026) | 30 table | UNVERIFIABLE (already hedged "according to public reports"; Meta blog shows Muse Spark 1.1, Muse Image and Video, no Glimmer) | https://ai.meta.com/blog/ | None |
| Artificial Analysis Intelligence Index, October 21, 2026: best open MiMo-V2.6-Pro 46; best closed Claude Opus 5.5 58 | 30 | CONFIRMED | https://artificialanalysis.ai/leaderboards/models | None |
| Ollama 9M+ monthly installs and 1B+ model downloads | 30 tools table | CONFIRMED | https://ollama.com/ | None |
| llama.cpp about 132k GitHub stars | 30 tools table | CONFIRMED (131.9k) | https://github.com/ggml-org/llama.cpp | None |
| At the frontier (30, local AI): LM Studio offers access to large open models alongside local ones | 30 | CONFIRMED (Bionic with Kimi K3, DeepSeek V4 Pro) | https://lmstudio.ai/ | None |
| An open model of about 30B beats 2023's GPT-4 on many tasks | 30 frontier box | UNVERIFIABLE (consistent with indexes; no direct source fetched) | none | None |
| $2,000 of cloud usage: about 4 billion Haiku or 200 million Sonnet output tokens | 30 | CONFIRMED | [A] | None |
| Tier table (Fable/astra $10/$50; Sonnet/sol $2/$10; Haiku/luna $0.10/$0.50) and per-reply costs | 31 cost section | CONFIRMED | [A] [C] | None |
| Caching lever: Sonnet 5.5 reads 0.1x ($0.20), reply $0.0040, 53% saving | 31 levers | CORRECTED | [A] | Recomputed at 0.05x ($0.10): $0.00375 (about $0.0038), 56% saving |
| Exercise 7: cached cost $0.0040; cap about 30 agent tasks with caching | 31 Exercise 7 | CORRECTED | [A] | Formula now uses 0.1 per MTok, gives $0.00375; check value 32 tasks (14 without caching unchanged) |
| Cached input billed at 2.5% to 10% of normal | 31 levers table | CONFIRMED | [A] | None |
| At the frontier (31, browser agents): Claude for Chrome 24% to 11%; IASR November 2025 says sophisticated attackers often bypass defenses | 31 | CONFIRMED (23.6% to 11.2%, August 25, 2025; IASR update November 25, 2025) | https://claude.com/blog/claude-for-chrome ; https://internationalaisafetyreport.org/ | "reportedly cut" changed to "reported that its defenses cut" (primary source) |
| OWASP Top 10 for LLM Applications: "current edition is dated 2025" | 31 definition and Table 31.4 | CORRECTED | https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/ ; https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/ | Definition now notes a 2026 edition (August 2026); new sentence after Table 31.4 says rankings were updated and excessive agency moved to third, per the announcement (full 2026 list is behind a download gate, so the 2025 table is kept and labeled) |
| OWASP agentic work "has begun" | 31 agentic risks | CORRECTED / ADDED | same OWASP URLs (Top 10 for Agentic Applications referenced; Agent Control Standard September 1, 2026) | Now says OWASP has published a Top 10 for Agentic Applications and took on an Agent Control Standard in September 2026 |
| EU AI Act Article 50 transparency duties phase in during 2026 | 31 expectations | CONFIRMED (applies August 2, 2026; Article 50(2) for older systems by December 2, 2026) | https://artificialintelligenceact.eu/implementation-timeline/ | None |
| At the frontier (31, enterprise): MCP and A2A under Linux Foundation projects; Agent Skills; identity is the bottleneck | 31 | CONFIRMED | Linux Foundation URLs above; https://blog.modelcontextprotocol.io/posts/mcp-roadmap/ | None |
| At the frontier (31, agent evals): labs grade agents with environments and rubric judges; long open-ended work hard to evaluate | 31 | UNVERIFIABLE (qualitative) | none | None |
| Constitutional classifiers 86% to 4.4% (February 2025); GPT-4o sycophancy rollback (April 2025); MIT NANDA 95% (August 2025); NIST AI RMF (January 2023) and AI 600-1 (July 2024) | 31 | UNVERIFIABLE (not re-checked) | none fetched | None |

## Summary

- Claims checked: 130 rows (several rows bundle related facts).
- CONFIRMED: 93 (a few with small extra details added in the same row, such as DeepSeek V4.1-Flash and the Mistral Medium 3.5 license)
- CORRECTED: 17 (two of them, the API-version example and the OWASP agentic sentence, also add new material)
- HEDGED: 0 as a separate verdict (corrections that soften a claim are counted as CORRECTED)
- ADDED: 4 standalone rows (OpenAI long-context prices, OpenAI Ultrafast tier, AAIF and MCP roadmap sentence, Mistral Large 4)
- UNVERIFIABLE: 16 (mostly 2023 to 2025 history not re-fetched after the web-search quota ran out, plus the Cowork browser date, Muse Glimmer, the October 2026 roundup ranking and two qualitative claims)

Most important fixes:
1. Claude Sonnet 5.5 cache reads cost 0.05x ($0.10 per MTok), not 0.1x ($0.20). Every worked example that used the old figure was recomputed and its answer keys updated: Chapter 26 manual example ($0.170, 83%), Chapter 29 agent session ($0.76, four fifths), Chapter 30 cost ladder ($330), Chapter 31 caching lever ($0.00375, 56%) and Exercise 7 (32 tasks).
2. Anthropic released API version 2026-10-21 and Python SDK 2.0 today (October 21, 2026): the Chapter 26 raw-request example now shows the new version and Bearer header, and the sampling paragraph notes that the new version rejects temperature, top_p and top_k.
3. OWASP published a 2026 edition of its LLM Top 10 (August 2026) and a Top 10 for Agentic Applications; Chapter 31 no longer calls the 2025 edition current.
4. Product details: ChatGPT apps were folded into a plugin directory (not simply renamed); Codex recommends rather than "runs on" GPT-6.1 Sol; Antigravity's Gemini 4 Argon needs a paid Google AI plan; Google ADK adds Kotlin; Kimi K3's QAT starts at fine-tuning; Gemma 4 date and Apache 2.0 license.

Unresolved for other owners: Chapters 17 and 24 date Gemma 4 to April 2026 / April 2, 2026, while Google's release notes give March 31, 2026 (Chapter 24 also lists its license as "See model card"; it is Apache 2.0).

All edited files pass validate.py (25, 26, 28, 29, 30, 31) and check.py for chapters 25, 26, 28, 29, 30 and 31. Chapter 27 needed no edits.
