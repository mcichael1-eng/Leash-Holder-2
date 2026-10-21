# 10 — Skills, Careers, the AI Industry, and Opportunity

*Research notes for "Everything About AI: From Zero to the Frontier." Compiled October 21, 2026.*

**Reliability notes for the author**
- Figures marked **[P]** come from a primary source I checked directly: SEC filings, BLS, company job boards, official course pages. Figures marked **[S]** come from reputable secondary reporting or aggregators (Sacra, Reuters/Bloomberg/FT relayed through other outlets, law-firm deal announcements). Treat [S] figures as "reported," and date-stamp every number in the book.
- The shared web-search budget ran out partway through this research. A few items, such as the CNBC/Lightcast FDE posting numbers, could not be checked against the original article, and they are flagged where they appear. Spot-check them before print.
- AI money figures go stale within weeks. The book should present them as a snapshot ("as of October 2026") and teach the reader how to look them up again. The habits in §9 and §10 cover this.
- Posted salary ranges from Anthropic and OpenAI are **base salary** ranges. OpenAI's postings add "Offers Equity," and both companies pay equity on top, so total compensation is usually well above the posted range.

---

## 1. Topic map (in teaching order)

### Part A. Orientation: where you fit in the AI economy
1. **The spectrum of involvement.** Show the ladder from casual user to power user, builder, engineer, researcher and frontier researcher. Make the point that most economic value, and most jobs, sit in the middle rungs. Start from where the reader already is (a daily chatbot user for over a year), which already puts them ahead of most people at rung one.
2. **Why this chapter matters now.** In 2025–2026 AI went from a feature to an industry with roughly $700B+ a year of data-center spending. Set out the stakes: new jobs, changing jobs, and a squeeze on entry-level work in AI-exposed fields. Use the Stanford "Canaries" paper and BLS growth figures for evidence.
3. **The vocabulary of money.** Before the industry tour, teach ARR, run-rate, recognized revenue, valuation, pre-/post-money, funding rounds, gross margin and capex. Readers can't interpret AI news without these. Use the speedometer/odometer analogy (§10).

### Part B. The AI value chain ("the stack"), from the ground up
4. **Layer 0: energy, land and construction.** Data centers need power (measured in gigawatts), cooling, land, permits and skilled trades. Explain why power has become the bottleneck and why electricians and community-relations managers now appear on AI-lab job boards.
5. **Layer 1: chips and hardware.** GPUs (Nvidia), custom accelerators (Google TPU, Amazon Trainium), chip foundries (TSMC), memory (HBM from SK Hynix, Samsung, Micron) and networking. Use Nvidia's quarterly numbers to show the scale: Data Center was about 92% of a $96B quarter.
6. **Layer 2: cloud and compute providers.** Hyperscalers (Microsoft Azure, AWS, Google Cloud, Oracle) and "neoclouds" (CoreWeave, Nebius, Lambda and others). Explain renting versus owning compute and what a multi-year compute deal is.
7. **Layer 3: foundation-model labs.** OpenAI, Anthropic, Google DeepMind, Meta, xAI (now inside SpaceX), Mistral, and Chinese labs (DeepSeek, Alibaba's Qwen, Moonshot and others). Cover closed versus open-weight models and how labs make money: API, subscriptions, enterprise seats, and increasingly ads and agents.
8. **Layer 4: data and tooling.** Human-data and expert-data firms (Scale AI, Surge, Mercor), evaluation and observability tools, vector databases, orchestration frameworks, and standards such as the Model Context Protocol (MCP). This layer contains "picks and shovels" businesses.
9. **Layer 5: applications.** Horizontal assistants (ChatGPT, Claude, Gemini, Copilot), coding tools (Cursor, Claude Code, Codex), vertical apps (Harvey for law), customer-service agents (Sierra, Decagon), app builders (Lovable, Replit), and answer engines (Perplexity).
10. **Layer 6: services.** Consultancies, systems integrators, AI automation agencies, forward-deployed engineering teams, and trainers and educators. Explain why "services" are growing alongside software: the MIT finding that roughly 5% of pilots reach measurable profit-and-loss (P&L) impact.
11. **Where money flows.** Follow a dollar from a ChatGPT subscription down to a TSMC wafer. Cover circular deals (chipmaker invests in lab, lab buys chipmaker's chips), "up to" commitments, and the gap between capex and revenue.

### Part C. Inside a frontier lab
12. **How a frontier lab is organized.** Research (pretraining, post-training/RL, multimodal, agents, interpretability, alignment, evals); scaling and compute (training infrastructure, inference, kernels, data-center delivery); product (consumer apps, API platform, coding agents, devices); Applied AI and go-to-market (architects, FDEs, sales, customer success); safeguards and policy; security; and general and administrative functions. Use October 2026 job-board counts to show that research is a minority of hiring.
13. **How a model gets made and shipped, as a team sport.** Walk the pipeline (data → pretraining → post-training → evals → safety review → inference → product → customer deployment) and name the role that owns each step.

### Part D. AI businesses
14. **Business models.** API/usage, subscriptions, per-seat enterprise, outcome-based pricing, "wrappers," vertical AI, agents-as-a-service, services-as-software, data businesses, infrastructure, and education.
15. **AI unit economics.** Every AI query costs compute, so AI gross margins tend to be lower than classic software. Show the OpenAI gross-margin estimate and Anthropic's "revenue per dollar of compute" metric.
16. **Defensibility (moats).** Cover why "the model eats your feature," and what does protect a business: proprietary data loops, deep workflow integration, distribution, trust and compliance, switching costs, and speed.
17. **The 2025–2026 startup landscape.** Case studies: Cursor (a "wrapper" that reached a $60B acquisition), Harvey, Lovable, Sierra, Mercor, Scale AI, and the lessons from each.

### Part E. Skills
18. **The skill tree.** Seven levels, from AI literacy to frontier research, plus cross-cutting branches (policy, sales/solutions, writing and teaching, domain expertise). For each skill: what it is, why it matters, how to learn it (§3).
19. **Power-user skills in depth.** Prompting → context engineering, verification, delegation to agents, and building reusable "Projects/Skills/GPTs." These skills give the most value for the least effort.
20. **Builder skills.** No-code automation, AI app builders, and connecting tools via MCP. Teach "describe → build → test → iterate."
21. **Engineering skills.** Python, SQL, APIs, evals, retrieval-augmented generation (RAG), agents, MLOps, and then GPUs, kernels and distributed systems. Explain why each layer exists.
22. **Research and safety skills.** Research taste, experiment design, replication, interpretability, alignment and evaluations.

### Part F. Roles and careers
23. **The roles catalog.** About 35 roles with day-to-day work, skills, backgrounds and pay (§4).
24. **Pay in AI: reality versus headlines.** Lay out four tiers: BLS medians; big-tech Levels.fyi medians; frontier-lab posted ranges; and the handful of reported nine-figure offers. Explain base, bonus, equity, vesting and tender offers.
25. **Career paths.** Typical transitions: domain professional → AI implementation lead; software engineer → AI engineer → ML engineer; PhD → research scientist; salesperson → AI account executive; electrician → data-center critical-facilities technician.

### Part G. How AI is changing existing jobs
26. **Tasks, not jobs.** Exposure is measured at the task level. Cover automation versus augmentation, the "jagged frontier," and why information work is most exposed (Microsoft Copilot study).
27. **Evidence so far.** Entry-level employment declines in exposed occupations (Stanford "Canaries"); 88% organizational adoption alongside few pilots reaching P&L impact; the 50-point gap between experts and the public on whether AI's job impact is positive.
28. **Adapting a career.** Become the person who redesigns the workflow rather than the person whose tasks get automated. Build "judgment + verification + domain context."

### Part H. Opportunities
29. **By audience.** Non-technical professional, aspiring builder, aspiring engineer or researcher, entrepreneur, investor, skilled trades (§8).

### Part I. Learning and staying current
30. **Staged roadmap.** 0–3 months, 3–12 months, 1–3 years, with resources (§9).
31. **Certifications: when they matter.** Mostly in enterprise, cloud and governance hiring. Portfolios matter more for building roles.
32. **Portfolio projects.** Building in public.
33. **Evaluating AI news and hype.** A checklist covering run-rate versus revenue, "up to" deals, benchmarks, demos versus deployments, and the incentives of whoever is reporting (§9.6).

---

## 2. Glossary candidates (business, career, industry, and skills terms)

*Plain-English definitions, 1–3 sentences each. Terms are grouped for teaching, so they are not in alphabetical order.*

### Money and business terms
1. **Revenue.** Money a company earns from customers in a period, before subtracting costs.
2. **Recognized revenue (GAAP revenue).** Revenue counted under formal accounting rules, only when the service has actually been delivered. It is the most conservative and comparable revenue number.
3. **ARR (Annual Recurring Revenue).** The yearly value of a company's ongoing subscriptions or contracts. It is a forward-looking speed reading, not money already collected.
4. **Run-rate (annualized revenue).** Take recent revenue (often the last month) and multiply it to a full year: one $5B month gives a "$60B run-rate." It flatters fast-growing companies and is calculated differently by different firms.
5. **Bookings / backlog / RPO (remaining performance obligations).** Contracts signed but not yet delivered or paid. CoreWeave's $99.4B backlog is future work, not money in hand.
6. **Gross margin.** Revenue minus the direct cost of delivering the product, as a percentage. AI companies pay for compute on every request, so their gross margins are often lower than traditional software.
7. **Operating margin / profit.** What remains after all operating costs (salaries, research, sales), not just delivery costs.
8. **Burn rate / free cash flow.** Burn is how fast a company spends cash beyond what it brings in. Negative free cash flow means it needs outside funding to continue.
9. **Capex (capital expenditure).** Money spent on long-lived physical assets such as data centers, chips and power equipment. Big-tech AI capex is the main driver of the data-center boom.
10. **Opex (operating expenditure).** Ongoing costs such as salaries, rent and cloud bills.
11. **Depreciation.** Spreading the cost of a physical asset (like a GPU) over its useful life in the accounts. It matters because AI chips may become obsolete quickly.
12. **Valuation.** What investors agree a company is worth in a funding round or on the stock market. For private companies it is a negotiated price on a small slice, not a cash value.
13. **Pre-money / post-money valuation.** Value before the new investment versus after adding it. Raising $65B at $965B post-money means the company was valued at $900B before the cash arrived.
14. **Funding round (Seed, Series A, B, C…).** A stage of selling ownership to investors for cash. Later letters usually mean larger, later-stage rounds.
15. **Venture capital (VC).** Investment firms that buy stakes in young, risky companies, hoping a few become huge.
16. **Strategic investor.** A company (not a pure financial fund) that invests for business reasons. Nvidia, Amazon, Google and Microsoft investing in AI labs are examples.
17. **Tender offer / secondary sale.** Existing shareholders, often employees, sell shares to new investors. No new money goes to the company.
18. **IPO (initial public offering).** When a private company first sells shares on a public stock exchange. SpaceX listed in June 2026, and Anthropic was reported to be targeting mid-November 2026.
19. **Confidential filing (S-1).** Submitting IPO paperwork to the SEC privately before making it public.
20. **Market cap (market capitalization).** Share price × number of shares: the public market's valuation.
21. **Revenue multiple.** Valuation divided by revenue or run-rate. It shows how much investors pay per dollar of sales, which reflects their growth expectations.
22. **Unit economics.** Profit or loss on one unit (one customer, one query, one seat). The question is whether serving each additional user makes or loses money.
23. **CAC / LTV.** Customer acquisition cost versus customer lifetime value. A healthy business earns much more from a customer than it spent to win them.
24. **Churn / net revenue retention (NRR).** Churn is customers leaving. NRR over 100% means existing customers spend more each year, even after accounting for those who leave.
25. **Compute deal / compute commitment.** A multi-year contract to buy or reserve computing capacity (chips, cloud time, data-center power), often worth tens or hundreds of billions. Headlines often use the maximum "up to" value.
26. **"Up to" deal / contingent investment.** A headline maximum that depends on conditions. For example, part of Amazon's reported OpenAI investment was contingent on an IPO or a technical milestone.
27. **Circular deal.** A supplier invests in a customer who then spends the money buying from that supplier, such as a chipmaker investing in a lab that buys its chips. It can inflate apparent demand.
28. **Hyperscaler.** The largest cloud companies (Amazon/AWS, Microsoft/Azure, Google Cloud, plus Meta and Oracle for their own buildouts), which build data centers at enormous scale.
29. **Neocloud.** A newer cloud company specializing in renting GPUs for AI, such as CoreWeave.
30. **Gigawatt (GW).** A billion watts of power, now the unit labs and clouds use to describe data-center size. 1 GW is roughly the output of a large power plant.
31. **Moat.** A lasting advantage that stops competitors from copying a business and taking its customers.
32. **Wrapper.** A product built on top of someone else's AI model, adding interface, workflow or data. "Thin wrappers" add little and are easily copied, while "thick wrappers" become deep products.
33. **"The model eats your feature."** The risk that a model provider releases your startup's main feature as a built-in capability.
34. **Vertical AI.** AI products built for one industry (law, healthcare, accounting) with domain-specific workflows and data.
35. **Horizontal AI.** General-purpose tools used across industries, such as chat assistants or coding tools.
36. **Seat-based pricing.** Charging per user per month, the classic software model.
37. **Usage-based pricing.** Charging per amount used, such as per token, per API call or per credit.
38. **Outcome-based pricing.** Charging only when a result is achieved, such as per resolved customer-support ticket.
39. **Services-as-software.** Selling the outcome of a service (bookkeeping done, tickets resolved) delivered largely by AI agents, instead of selling a tool to humans.
40. **Systems integrator (SI) / GSI.** Large consulting firms (such as Accenture or Deloitte) that implement technology for enterprises. They are a major distribution channel for AI.
41. **Go-to-market (GTM).** Everything involved in selling a product: sales, marketing, partnerships, customer success.
42. **Enterprise / mid-market / SMB.** Customer-size segments: large corporations, medium firms, and small-and-medium businesses.
43. **Pilot / proof of concept (POC).** A small trial deployment to test whether AI works for a use case before full rollout.
44. **Product-market fit (PMF).** When a product so clearly meets a market need that customers pull it from you.
45. **Distribution.** Access to customers (channels, partnerships, existing user bases). In AI it is often a stronger moat than technology.
46. **Data flywheel.** A loop in which usage generates data that improves the product, which attracts more usage.
47. **Switching cost.** How painful it is for a customer to move to a competitor.
48. **Total addressable market (TAM).** The total revenue available if a product won every possible customer.
49. **Public benefit corporation (PBC).** A for-profit company legally required to weigh a stated public mission alongside profit. Anthropic and OpenAI Group are PBCs.

### Industry and technical terms a career-changer will hear
50. **Foundation model / frontier model.** A large general-purpose model trained on broad data. "Frontier" means among the most capable in existence.
51. **Frontier lab.** A company training frontier models: OpenAI, Anthropic, Google DeepMind, Meta, xAI and a few others.
52. **Open-weight model.** A model whose trained parameters are published so anyone can run or modify it. Running it still costs compute.
53. **API (application programming interface).** A way for software to talk to other software. Developers send text to a model's API and receive responses, paying per token.
54. **Token.** A chunk of text (roughly ¾ of an English word) that models read and write. It is the unit of AI pricing.
55. **Inference.** Running a trained model to produce answers. This is the ongoing cost of serving users.
56. **Training (pretraining / post-training).** Pretraining teaches a model general knowledge from huge datasets. Post-training (fine-tuning, reinforcement learning) shapes it into a helpful, safe assistant with particular skills.
57. **GPU / accelerator.** Chips specialized for the parallel math AI needs. Nvidia GPUs dominate, while Google TPUs and Amazon Trainium are alternatives.
58. **CUDA / kernel.** CUDA is Nvidia's programming platform for GPUs. A kernel is a small program that runs on the GPU, and writing faster kernels makes AI cheaper.
59. **MLOps / LLMOps.** The practices and tools for deploying, monitoring and updating models in production reliably.
60. **RAG (retrieval-augmented generation).** Looking up relevant documents and handing them to the model with the question, so answers draw on your data.
61. **Agent.** An AI system that takes multi-step actions toward a goal (using tools, browsing, writing code), not just answering once.
62. **MCP (Model Context Protocol).** An open standard for connecting AI assistants to tools and data sources, a kind of "USB-C port for AI."
63. **Evals (evaluations).** Systematic tests of whether an AI system does what you want. They are the "unit tests" and "report cards" of AI products, and among the most important skills of 2025–2026.
64. **Benchmark.** A standardized public test used to compare models. Useful, but models can be tuned to benchmarks, and benchmarks "saturate" when top models all score near 100%.
65. **Prompt engineering.** Writing instructions that get good results from a model.
66. **Context engineering.** The broader 2025-era skill of assembling everything a model sees (instructions, examples, documents, tool results, memory) so it can do a task well.
67. **Human data / RLHF data.** Human-written examples, ratings and expert demonstrations used to train and evaluate models. The work is often done by contractors via firms like Scale, Surge or Mercor.
68. **RL environment.** A simulated task setup (with a way to score success) in which models practice and learn by reinforcement learning. Building them became a business in 2025–2026.
69. **Red teaming.** Deliberately attacking a system to find failures and harms before bad actors do.
70. **Interpretability.** Research into what is happening inside a model's neural network.
71. **Alignment.** Making AI systems reliably pursue intended goals and values.
72. **Safeguards / trust and safety.** Teams and systems that detect and prevent misuse of AI products.
73. **Jagged frontier.** AI capability is uneven: superhuman at some tasks and surprisingly poor at nearby ones. Stanford's 2026 AI Index notes a model that wins IMO gold yet reads analog clocks correctly only about half the time.
74. **AI exposure.** How much a job's tasks could be done or assisted by AI. It is measured at the task level, not the job level.
75. **Automation vs. augmentation.** Automation is AI doing the task instead of a person. Augmentation is AI helping a person do it better or faster.

### Career terms
76. **FDE (forward-deployed engineer).** An engineer embedded with a customer to build and deploy solutions on-site, half engineer and half consultant. The role originated at Palantir and became one of the fastest-growing AI roles in 2025–2026.
77. **Solutions architect / Applied AI architect / solutions engineer.** Technical experts on the sales side who design how a customer will use the product, run demos and proofs of concept, and guide implementation.
78. **AI engineer (LLM application engineer).** A software engineer who builds products on top of foundation models (prompts, RAG, agents, evals), as distinct from training models.
79. **ML engineer (MLE).** An engineer who builds, trains, deploys and maintains machine-learning models in production.
80. **Research engineer vs. research scientist.** Research engineers build the infrastructure and run large experiments. Research scientists set research direction and hypotheses. At frontier labs the line is blurry, and many postings are "RE/RS."
81. **Performance engineer.** Makes training and inference faster and cheaper (kernels, compilers, parallelism).
82. **TPM (technical program manager).** Coordinates complex technical projects across teams, such as a data-center buildout or a model launch.
83. **AE (account executive).** A salesperson who owns closing deals with a set of customers.
84. **OTE (on-target earnings).** Sales compensation: base salary plus expected commission if targets are hit.
85. **CSM (customer success manager).** Ensures customers adopt and get value from a product after purchase, driving renewals and expansion.
86. **Total compensation (TC).** Base salary + bonus + equity (stock) per year. Tech pay comparisons use TC.
87. **Equity / RSUs / options / vesting.** Ownership granted as pay. It "vests" (becomes yours) over time, typically four years. At private labs its value depends on future valuations and liquidity.
88. **Levels (L4, E5, IC3…).** Company-specific seniority ladders that determine pay bands.
89. **Levels.fyi.** A crowdsourced site where tech workers report verified compensation. It is the standard reference for tech pay, but skews toward large, high-paying companies.
90. **Portfolio.** Public evidence of what you can do: projects, write-ups, code repositories, demos. In AI it often matters more than credentials.
91. **T-shaped skills.** Deep expertise in one area (the vertical bar) plus broad working knowledge across many (the horizontal bar).
92. **Fellowship / residency.** Time-boxed, paid programs where newcomers do research with mentorship. Examples are the Anthropic Fellows Program and MATS.
93. **Expert contractor (AI trainer).** A domain expert (doctor, lawyer, coder, mathematician) paid to write, grade or critique model outputs for training and evaluation.
94. **AI governance.** The policies, processes and controls organizations use to manage AI risk and comply with laws.
95. **EU AI Act.** The European Union's risk-based AI law. Its obligations phase in from 2025 onward and apply to many companies selling into the EU (check the current timeline, as delays to some obligations have been proposed).
96. **AISI / CAISI.** Government AI-safety bodies: the UK AI Security Institute and the US Center for AI Standards and Innovation. They test frontier models and employ technical and policy staff.
97. **Hype cycle.** The pattern of inflated expectations, disillusionment, then steady productive use that new technologies often follow.
98. **Picks and shovels.** Selling tools and infrastructure to everyone in a boom (as in the gold rush) instead of betting on one winner. Nvidia is the classic AI example.
99. **Critical facilities / mission-critical technician.** Tradespeople who run and maintain a data center's power and cooling systems 24/7.
100. **Powered land / interconnection queue.** Land with a confirmed connection to enough electricity, and the waiting list to connect new loads to the grid. Both are major bottlenecks for AI data centers.

---

## 3. Skills map (grouped by level)

Format: **Skill**: what it is | why it matters | how to learn it.

### Level 0: AI literacy (everyone; weeks)
- **How LLMs work, conceptually**: next-token prediction, training versus inference, why models hallucinate, context windows, knowledge cutoffs. | People who understand the mechanism predict failures and trust appropriately. | Karpathy's "Intro to Large Language Models" and "Deep Dive into LLMs like ChatGPT" talks (YouTube); 3Blue1Brown's neural-network series; Anthropic's "AI Capabilities and Limitations" and "AI Fluency: Framework & Foundations" (anthropic.skilljar.com); DeepLearning.AI "Generative AI for Everyone."
- **Capabilities and limitations map**: the jagged frontier, which tasks models are strong or weak at, and how fast that changes. | It avoids both over-trust and under-use. | Personal experiments (Exercise 3); METR and Epoch AI research summaries; Stanford AI Index.
- **Responsible use**: privacy (what not to paste), copyright, disclosure, bias, workplace policy. | Mistakes here can cost jobs and create legal exposure. | Your employer's AI policy; Anthropic AI Fluency course; OpenAI Academy "Apply AI at Work."

### Level 1: Power user (everyone; 1–3 months to fluency)
- **Prompting fundamentals**: clear tasks, role/context, examples, output format, step-by-step decomposition, asking the model to ask *you* questions. | It is the biggest single quality lever and costs nothing. | Anthropic and OpenAI prompt-engineering guides (docs.claude.com; platform.openai.com/docs); DeepLearning.AI "AI Prompting for Everyone" (Andrew Ng, about 7 hours); promptingguide.ai.
- **Context engineering**: deliberately supplying the right documents, examples, constraints, background and memory; using Projects, custom instructions, Skills, connectors. | In 2025–2026 the quality bottleneck moved from wording to *what the model knows about your situation*. | Hugging Face "Context Course"; Anthropic Claude 101 and "Introduction to agent skills"; practice by building a reusable project for one recurring task.
- **Verification and critical reading**: checking citations, cross-model checking, spotting confident errors, sampling outputs. | AI output is only as valuable as your ability to catch its mistakes. | Make "verify three claims" a habit; the "AI as Normal Technology"/"AI Snake Oil" writing by Narayanan & Kapoor.
- **Delegating to agents**: giving multi-step tasks to agentic tools (deep research, computer-use and coding agents, desktop agents), setting checkpoints, reviewing work. | Agents turn hours of work into minutes, but only for people who can scope and review. | Use ChatGPT agent/deep research, Claude Cowork/Claude Code, Gemini; Anthropic "Introduction to Claude Cowork."
- **Multimodal use**: images, voice, documents, spreadsheets, screenshots, generating images, slides and video. | Much real work isn't plain text. | Practice converting a messy PDF or photo into structured data.
- **Personal workflow design**: knowing which of your weekly tasks AI should do, assist with, or not touch. | It compounds: 5 hours a week saved is 250 hours a year. | Exercise 1 (automation audit).

### Level 2: Builder (non-programmers can reach this; 2–6 months)
- **Workflow automation**: connecting apps with triggers and actions (Zapier, Make, n8n, Power Automate) plus AI steps. | It moves AI from "chat" to "runs while you sleep," and it underpins most SMB AI consulting. | Each tool's free tier and templates; build three automations for your own job.
- **No-code/vibe-coded app building**: describing an app in plain language to tools like Lovable, Replit, Bolt or Claude Code, then iterating. | Non-engineers can now ship internal tools and prototypes (Lovable reported roughly $400M+ run-rate by March 2026, mostly from such builders [S]). | DeepLearning.AI "Build with Andrew" (about 1 hour, no coding); build a small tool you'll actually use.
- **Spreadsheet + AI analysis**: formulas, pivot tables, using AI to write formulas, clean data and chart it. | It is the most universal business data tool. | Excel/Sheets with Copilot or Gemini; Kaggle Learn "Intro to Programming" when ready.
- **Connecting tools to AI (MCP and connectors)**: plugging the assistant into email, drive, calendar, CRM, databases. | Context access is what makes assistants useful at work. | Anthropic "Introduction to Model Context Protocol"; the Hugging Face MCP material.
- **Custom assistants**: building GPTs, Claude Projects, Gems or Skills for repeatable tasks and sharing them with a team. | One well-built assistant can uplift a whole team. | Build one for a teammate and collect feedback (Exercise 9).
- **Basic evaluation for builders**: keeping a set of 20 test inputs with expected outputs and re-running them after changes. | It is the habit that separates hobby projects from reliable tools. | Hamel Husain's evals writing (hamel.dev); Exercise 14.

### Level 3: Technical foundations (3–12 months part-time)
- **Python basics**: variables, loops, functions, files, packages, notebooks. | It is the language of AI, and AI coding assistants make it far easier to learn now than before. | DeepLearning.AI "AI Python for Beginners" (about 11.5 hours); Harvard CS50P; Kaggle Learn Python.
- **Command line, Git and GitHub**: running programs, version control, publishing code. | These are needed for any engineering work and for a portfolio. | GitHub Skills; "The Missing Semester" (MIT).
- **SQL**: querying databases. | Most business data lives in databases, and SQL is still the top data-job requirement. | SQLBolt, Mode SQL tutorial, Kaggle Learn SQL.
- **Data analysis (pandas, visualization, statistics)**: cleaning, summarizing and charting data; distributions, averages, variance, sampling, A/B tests. | You need it to evaluate AI systems and to work as an analyst or data scientist. | Kaggle Learn (Pandas, Data Visualization); DeepLearning.AI "Data Analytics" certificate (about 147 hours).
- **APIs and JSON**: calling web services, reading documentation, handling API keys safely. | Every LLM application is an API call. | Anthropic "Claude Platform 101" / "Building with the Claude API"; OpenAI Academy "Build with AI."
- **Math for ML (basic)**: linear algebra (vectors, matrices), calculus (derivatives, gradients), probability. | It is required for understanding training, and less so for building apps. | 3Blue1Brown "Essence of Linear Algebra" and "Essence of Calculus"; DeepLearning.AI "Mathematics for Machine Learning and Data Science" (about 94 hours); Khan Academy.

### Level 4: AI application engineering and AI product (6–24 months)
- **LLM application engineering**: prompt pipelines, structured outputs, tool/function calling, streaming, cost and latency tradeoffs, model selection. | This is the job of the "AI engineer," the most-hired technical AI role outside the labs. | Chip Huyen, *AI Engineering* (O'Reilly, 2025); Anthropic and OpenAI cookbooks; Hugging Face LLM Course.
- **RAG and search**: chunking, embeddings, vector databases, hybrid search, reranking, citations. | It is how companies make AI work on their own documents. | Hugging Face Open-Source AI Cookbook; LlamaIndex/LangChain docs; build Exercise 19.
- **Agents and tool use**: agent loops, planning, memory, MCP servers, multi-agent patterns, sandboxing. | Agents were the dominant product pattern of 2025–2026. | Hugging Face Agents Course; DeepLearning.AI "Agentic AI" (Andrew Ng, about 10 hours); Anthropic "Building effective agents" guidance; Claude Agent SDK and OpenAI Agents SDK docs.
- **Evals and observability**: building test sets, error analysis, LLM-as-judge, regression testing, tracing production failures. | Labs and startups repeatedly name it the most underrated skill, and it is what separates a demo from a product. | Hamel Husain & Shreya Shankar's "AI Evals for Engineers & PMs" (Maven); DeepLearning.AI "Evaluating AI Agents"; OpenAI and Anthropic eval docs.
- **AI security**: prompt injection, data exfiltration through tools, permissioning, PII handling. | Agents with tool access create new attack surfaces. | OWASP Top 10 for LLM Applications; Simon Willison's prompt-injection writing.
- **Fine-tuning basics**: when to fine-tune versus prompt versus RAG; LoRA; preference tuning. | It is occasionally the right tool, and knowing when not to fine-tune is equally important. | Hugging Face "a smol course" (post-training); Unsloth/TRL docs.
- **AI product management**: picking problems AI can actually solve, defining quality, designing evals with domain experts, pricing for compute costs, managing non-determinism. | Many AI products fail at the problem-selection and quality-definition stage. | Lenny's Newsletter/Podcast AI episodes; evals course above; ship a small product (Exercise 22).
- **AI design and UX**: designing for uncertainty (showing sources, confidence, undo), conversational and agent UX, human-in-the-loop review screens. | Good UX turns a 90%-accurate model into a trusted tool. | Study the interfaces of Claude, ChatGPT, Cursor and Perplexity; Google PAIR "People + AI Guidebook."

### Level 5: ML engineering and infrastructure (1–3+ years)
- **Classical ML**: regression, trees and gradient boosting, train/validation/test splits, overfitting, metrics. | It still powers most production ML (fraud, ranking, forecasting) and builds intuition. | Andrew Ng's Machine Learning Specialization (about 95 hours); Géron's *Hands-On Machine Learning*.
- **Deep learning and PyTorch**: neural networks, backpropagation, optimizers, CNNs, transformers, training loops. | It is the core of modern AI. | fast.ai "Practical Deep Learning for Coders" (free, about a year of coding assumed); Karpathy "Neural Networks: Zero to Hero"; *Understanding Deep Learning* (Prince, free PDF); *Dive into Deep Learning* (d2l.ai).
- **MLOps**: experiment tracking, model registries, CI/CD for models, monitoring drift, feature stores. | Models that are not in production create no value. | Chip Huyen, *Designing Machine Learning Systems*; MLOps Community; cloud ML certifications.
- **Data engineering**: pipelines, warehouses (Snowflake, BigQuery, Databricks), orchestration (Airflow, Dagster), data quality. | It supplies the data that makes AI work, and it is a large, steady job market. | DeepLearning.AI/AWS "Data Engineering" (about 107 hours); *Fundamentals of Data Engineering* (Reis & Housley).
- **Distributed systems**: how work is split across many machines; networking, fault tolerance, consistency. | Frontier training runs span tens of thousands of chips. | Hugging Face "The Ultra-Scale Playbook"; Google DeepMind's "How to Scale Your Model" (jax-ml.github.io/scaling-book); Kleppmann's *Designing Data-Intensive Applications*.
- **GPU and infrastructure engineering**: cluster management (Kubernetes, Slurm), GPU health, storage, networking (InfiniBand), scheduling. | Compute is the scarcest resource in AI, and this work keeps it busy. | Lab job descriptions (Anthropic "Compute," OpenAI "Scaling" teams); cloud provider docs; GPU MODE community.
- **CUDA/kernel programming and inference optimization**: writing GPU kernels (CUDA, Triton), quantization, batching, KV-cache management, speculative decoding; serving engines (vLLM, SGLang, TensorRT-LLM). | Faster kernels translate directly into millions of dollars of savings, which is why posted performance-engineer ranges at Anthropic reach $850K base [P]. | *Programming Massively Parallel Processors* (Hwu, Kirk, El Hajj); GPU MODE lectures (github.com/gpu-mode); Triton tutorials; Stanford CS336's systems assignment (writing FlashAttention-2 in Triton).

### Level 6: Frontier research (2–5+ years; often but not always a PhD)
- **Pretraining and scaling science**: data curation at web scale, architectures, scaling laws, training stability. | It sets the base capability of every model. | Stanford CS336 "Language Modeling from Scratch" (Spring 2026; lectures on YouTube); Karpathy's nanochat (trains a GPT-2-class model for about $48 of rented GPU time [P]); Raschka, *Build a Large Language Model (From Scratch)*.
- **Post-training and RL**: supervised fine-tuning, RLHF, RL from verifiable rewards, reasoning models, RL environments, agent training. | Most of the 2024–2026 capability gains (reasoning, coding, agents) came from here, and it is the most-posted research specialty at Anthropic in Oct 2026 [P]. | Nathan Lambert's RLHF book and Interconnects newsletter; CS336 assignment 5; Hugging Face TRL.
- **Evaluation research**: designing benchmarks, measuring dangerous capabilities, long-horizon task evals. | Labs can't improve what they can't measure, and governments rely on evals for oversight. | METR and Epoch AI papers; UK AISI's Inspect framework; lab system cards.
- **Interpretability**: mechanistic interpretability, features, circuits, probing. | Understanding internals is central to safety and debugging. | ARENA curriculum; Anthropic's Transformer Circuits thread; Neel Nanda's guides; MATS.
- **Alignment and safety research**: scalable oversight, AI control, adversarial robustness, model welfare, misuse safeguards. | It is a small but growing field: 80,000 Hours estimated only about 300 people (76–536 FTE) working on technical existential-risk safety as of 2022 [P]. | BlueDot Impact courses; ARENA bootcamps; MATS; Anthropic Fellows Program; 80,000 Hours career guide.
- **Research skills**: reading papers fast, replicating results, experiment design, ablations, writing, research taste (choosing the right problems). | Taste is the scarcest research asset, and it is the main thing headline compensation is buying. | Replicate a paper end-to-end (Exercise 27); publish at workshops; join a fellowship.

### Cross-cutting branches (any level)
- **AI policy and governance**: law (EU AI Act, US state laws, export controls), risk frameworks (NIST AI RMF, ISO/IEC 42001), compute governance, lab safety frameworks. | Every large organization now needs AI governance, and governments need technical literacy. | IAPP AIGP certification; BlueDot governance courses; GovAI, CSET, RAND publications; Anthropic's and OpenAI's policy job descriptions for realistic skill lists.
- **AI sales, solutions and forward-deployed work**: discovery (finding the problem), demos, scoping, proofs of concept, change management, ROI cases. | Labs' biggest hiring categories in Oct 2026 are Sales/GTM and Applied AI [P]. | Read lab "Applied AI Architect" and FDE postings; do a free implementation for a local business (Exercise 17).
- **Technical writing, education and developer relations**: docs, tutorials, courses, workshops. | Adoption is bottlenecked by understanding. Anthropic was hiring a Lead Technical Instructor ($270K–$365K) and Developer Education Lead ($290K–$365K) [P]. | Write public explainers; contribute docs to open-source projects.
- **Domain expertise + AI**: deep knowledge of a field (medicine, law, accounting, logistics, teaching, trades) combined with AI skill. | Domain experts design the evals, spot errors and know which problems matter. Expert contractors also earn $85+/hour on average via Mercor [S]. | Apply Levels 1–2 to your field; write about it.
- **Data-center trades and engineering**: electrical, mechanical/HVAC, controls, networking, construction management, commissioning. | Physical buildout is the binding constraint on AI. | Apprenticeships (IBEW/NECA electrical training), community college HVAC/controls programs, data-center operator training programs.

---

## 4. Roles catalog

**How to read pay figures.** "Anthropic posted" = US base-salary range on Anthropic's Greenhouse job board, retrieved Oct 21, 2026 (https://job-boards.greenhouse.io/anthropic). "OpenAI posted" = US base range on OpenAI's Ashby job board, retrieved Oct 21, 2026 (https://jobs.ashbyhq.com/openai), with equity offered on top. Frontier labs are the top of the market, and typical employers pay far less. BLS = U.S. Bureau of Labor Statistics May 2025 medians.

**Pay context in four tiers** (use this to calibrate readers):
1. **National medians (BLS, May 2025)** [P]: software developers $135,980 (10% projected growth 2025–35); computer & information research scientists $140,300 (22% growth; typical entry: master's); data scientists $120,230 (35% growth); electricians $63,190 (9% growth, with data centers cited as a driver).
   - https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm
   - https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm
   - https://www.bls.gov/ooh/math/data-scientists.htm
   - https://www.bls.gov/ooh/construction-and-extraction/electricians.htm
2. **Big tech (Levels.fyi, self-reported, Oct 2026)** [S]: median total compensation for US ML engineers is about $465K at Meta, $420K at Apple, $333K at Google and $261K at Nvidia.
   - https://www.levels.fyi/companies/meta/salaries/software-engineer/title/machine-learning-engineer (and the equivalent Apple, Google and Nvidia pages)
3. **Frontier-lab posted base ranges (Oct 2026)** [P]: commonly $200K–$500K base, with research and performance roles reaching $850K base, plus equity.
4. **Outliers**: in mid-2025 Meta reportedly offered a small number of top researchers packages of up to $300M over four years (Wired, as summarized by Entrepreneur), and one reported offer was up to $1.5B over six or more years [S]. Meta's CTO said such sums went to only a few senior leaders and were multi-year stock, not "signing bonuses" [S].
   - https://www.entrepreneur.com/business-news/meta-makes-billion-dollar-job-offer-competing-for-ai-talent/495672
   - https://www.axios.com/2025/07/03/ai-salaries-meta-openai-zuckerberg-altman

These are not typical AI salaries and should be taught as such.

### A. Roles open to non-technical and early-technical people

**1. AI-enabled professional (any field)**
- *Day to day:* Your existing job, with AI drafting, researching, analyzing and automating parts of it. You become the person who redesigns your team's workflow.
- *Skills:* Levels 0–2, domain expertise, verification.
- *Backgrounds:* Anyone.
- *Pay:* Your field's pay. PwC's AI Jobs Barometer has reported wage premiums for jobs requiring AI skills; verify the current year's figure before citing it.

**2. Expert contractor / AI trainer (human data)**
- *Day to day:* Writing ideal answers, grading model outputs, building hard test questions, critiquing reasoning in your specialty (medicine, law, finance, coding, math, languages).
- *Skills:* Deep domain knowledge, precise writing, consistency.
- *Backgrounds:* Professionals, graduate students, PhDs.
- *Pay:* Mercor reports experts average $85+/hour and pays out over $2M per day to its network [S] (https://sacra.com/c/mercor/). Generalist annotation pays far less. Work is project-based and can disappear abruptly; Scale AI ended work with about 500 contractors in July 2025 after its Meta deal [S] (https://sacra.com/c/scale-ai/).

**3. AI automation specialist / AI implementation consultant (SMB-focused)**
- *Day to day:* Auditing a small business's workflows; setting up automations (intake, scheduling, follow-ups, document processing); configuring assistants; training staff; maintaining systems.
- *Skills:* Levels 1–2, process mapping, sales, trust-building.
- *Backgrounds:* Operations, consulting, office management, marketing, IT support.
- *Pay:* Freelance and agency pricing varies widely. No reliable survey was found, so treat any specific number as anecdotal.

**4. AI transformation / adoption lead (inside a company)**
- *Day to day:* Running an internal AI program: picking use cases, governance, vendor selection, training, measuring ROI.
- *Skills:* Change management, Level 1–2 AI fluency, governance basics, metrics.
- *Backgrounds:* Operations, strategy, IT, L&D, consulting.
- *Pay:* Varies by company size. No authoritative source was found.

**5. AI account executive (sales)**
- *Day to day:* Prospecting, discovery calls, demos with solutions engineers, negotiating enterprise contracts, forecasting.
- *Skills:* Enterprise sales, credible AI literacy, industry knowledge.
- *Backgrounds:* SaaS or industry sales.
- *Pay:* Anthropic posted on-target earnings (OTE) of $222,800–$290,000 (startup/AI-native AEs), $290,000–$380,000 (mid-market), and $380,000–$450,000 (federal enterprise) [P]. OpenAI posted ranges for Account Directors of $176K–$350K plus commission and equity [P]. Sales is Anthropic's largest department by open roles (124 of 675) [P].

**6. Customer success manager (AI products)**
- *Day to day:* Onboarding customers, driving usage, running business reviews, flagging churn risk, coordinating with engineering.
- *Skills:* Relationship management, product expertise, change management.
- *Backgrounds:* Account management, consulting, support.
- *Pay:* Anthropic posted $200,000–$265,000 base (most CSM postings), $265K–$350K (national security) [P]. OpenAI posted $176K–$234K plus commission [P].

**7. AI policy / governance / compliance professional**
- *Day to day:* Tracking legislation, drafting internal policies, risk assessments, regulator engagement, writing usage policies, assessing models against frameworks.
- *Skills:* Law and policy, technical literacy, writing, stakeholder management.
- *Backgrounds:* Law, public policy, government, compliance, privacy (IAPP).
- *Pay:* Anthropic posted Policy Design Manager at $245K–$285K, Technical AI Governance at $265K–$295K, and Head of Policy Design at $330K–$395K [P]. OpenAI posted Model Policy Manager at $207K–$335K [P]. Government and think-tank pay is much lower.

**8. Trust & safety / safeguards analyst**
- *Day to day:* Investigating misuse (fraud, cyber abuse, child safety, weapons-related requests), enforcing policies, writing threat intelligence.
- *Skills:* Investigation, domain expertise in a harm area, data analysis, resilience to disturbing content.
- *Backgrounds:* T&S at social platforms, intelligence, law enforcement, cybersecurity.
- *Pay:* Anthropic posted Safeguards Enforcement Analyst at $245K–$330K [P].

**9. Community engagement manager (data centers)**
- *Day to day:* Working with local governments, residents, utilities and workforce programs where data centers are built.
- *Skills:* Local politics, communications, economic development.
- *Backgrounds:* Government affairs, economic development, utilities, campaigns.
- *Pay:* Anthropic posted six regional roles at $265K–$295K [P]. This shows how physical buildout is creating non-technical roles.

**10. Data-center trades and technicians**
- *Day to day:* Installing and maintaining electrical distribution, cooling, cabling and network gear; commissioning; 24/7 critical-facility operations.
- *Skills:* Licensed trade skills, safety, controls systems, fiber and network work.
- *Backgrounds:* Electricians, HVAC techs, military technicians, lineworkers.
- *Pay:* BLS median for electricians is $63,190 [P]. At the high end, OpenAI posted "Datacenter Networking Technician, AI Compute Deployment – Stargate" at $157K–$302K and "Site Operations Technician" at $157K–$221K, both with equity [P].

**11. Technical writer / developer educator / AI instructor**
- *Day to day:* Writing docs, tutorials, courses; running workshops; building demo apps.
- *Skills:* Clear writing, Level 3–4 technical skills, teaching.
- *Backgrounds:* Writing, teaching, developer relations, engineering.
- *Pay:* Anthropic posted Lead Technical Instructor at $270K–$365K, Developer Education Lead at $290K–$365K, and Head of Technical Training at $365K–$435K [P].

**12. AI product manager**
- *Day to day:* Deciding what to build, defining quality with evals, working with research and engineering on model behavior, prioritizing, launching, and watching metrics and costs.
- *Skills:* Product sense, Level 4 understanding (evals, cost, latency), user research, writing.
- *Backgrounds:* PM, engineering, design, consulting, domain experts.
- *Pay:* Anthropic posted $305K–$460K [P]. OpenAI posted $293K–$530K plus equity [P].

**13. AI product designer / UX / conversation designer**
- *Day to day:* Designing chat and agent interfaces, review/approval flows, trust signals, prototyping with AI.
- *Skills:* Interaction design, prototyping (increasingly by coding with AI), understanding model behavior.
- *Backgrounds:* Product and UX design.
- *Pay:* Anthropic posted $305K–$460K [P]. OpenAI posted $245K–$334K plus equity [P].

### B. Technical builder roles

**14. Data analyst**
- *Day to day:* Pulling data with SQL, dashboards, answering business questions, increasingly with AI copilots.
- *Skills:* SQL, spreadsheets, BI tools, statistics.
- *Backgrounds:* Business, economics, sciences.
- *Pay:* BLS doesn't separate this title cleanly. Data scientists (the next step up) have a $120,230 median [P].

**15. Data scientist**
- *Day to day:* Experiments (A/B tests), modeling, metrics design, and at AI companies, analyzing product usage, safety data and go-to-market.
- *Skills:* Statistics, Python/SQL, causal inference, communication.
- *Backgrounds:* Quantitative degrees.
- *Pay:* BLS median $120,230, 35% projected growth [P]. Anthropic posted $285K–$380K; OpenAI posted $230K–$385K plus equity [P].

**16. Data engineer**
- *Day to day:* Building pipelines, warehouses, data quality checks; at labs, pretraining-data infrastructure.
- *Skills:* SQL, Python, Spark, orchestration, cloud.
- *Backgrounds:* Software engineering, analytics.
- *Pay:* Anthropic posted Pre-training Data Infrastructure Engineer at $500K–$850K [P], the top end for this specialty.

**17. Software engineer (AI-assisted)**
- *Day to day:* Building products, now heavily paired with coding agents. More time goes to specifying, reviewing and testing than to typing code.
- *Skills:* Programming, system design, code review, using agents well.
- *Backgrounds:* CS degree, bootcamp, self-taught.
- *Pay:* BLS median $135,980 [P]. Frontier labs post $300K–$485K for senior roles (Anthropic) and $230K–$490K (OpenAI) [P].

**18. AI engineer / LLM application engineer**
- *Day to day:* Building features on model APIs: prompts and context pipelines, RAG, tool use, agents, evals, monitoring cost and latency.
- *Skills:* Level 4 plus solid software engineering.
- *Backgrounds:* Software engineers, data scientists, ambitious builders.
- *Pay:* Levels.fyi and job-board aggregates vary widely by title definition (third-party blogs cite US medians from about $150K to $280K) [S]. Treat these as soft.

**19. Forward-deployed engineer (FDE)**
- *Day to day:* Embedding with a customer for weeks or months: scoping their problem, building custom integrations and agents on their systems, handling messy data and security reviews, and feeding product gaps back to the lab.
- *Skills:* Full-stack engineering, LLM app engineering, customer communication, ambiguity tolerance, travel.
- *Backgrounds:* Software engineers with consulting or startup experience; ex-Palantir.
- *Pay:* OpenAI posted Forward Deployed Software Engineer (SF) at $185K–$325K plus equity, and FDE managers at $302K–$385K [P]. OpenAI now has a dedicated "Forward Deployed Engineering" department (31 open roles) [P]. Anthropic posted FDE manager roles at $320K–$405K [P].
- *Demand:* US FDE postings were reportedly up more than 1,000% year-over-year in Jan–Aug 2026 per Lightcast data cited by CNBC; I could not open the CNBC original, so verify [S]. Indeed reported a roughly 19× year-over-year increase in India [S] (https://www.peoplematters.in/news/workforce-planning/demand-for-forward-deployed-engineers-jumps-19-fold-in-india-report-52770).

**20. Solutions architect / Applied AI architect / Applied AI engineer**
- *Day to day:* Pre- and post-sale technical work: architecture design, demos, proofs of concept, prompt and eval workshops, partner enablement.
- *Skills:* Level 4 skills, communication, industry knowledge (finance, healthcare, public sector).
- *Backgrounds:* Sales engineering, consulting, software engineering.
- *Pay:* Anthropic posted Applied AI Architect at $240K–$380K and Applied AI Engineer at $200K–$320K [P]. OpenAI posted Applied AI Engineer at $197K–$335K plus equity [P]. Anthropic's Applied AI department had 61 open roles [P].

**21. ML engineer (MLE)**
- *Day to day:* Training and fine-tuning models, building features, deploying and monitoring models (recommendation, fraud, ranking, increasingly LLM fine-tunes).
- *Skills:* Level 5 skills (ML, PyTorch, MLOps), software engineering.
- *Backgrounds:* CS or quantitative degrees, often a master's.
- *Pay:* Levels.fyi big-tech medians $261K–$465K [S].

**22. MLOps / ML platform engineer**
- *Day to day:* Building the internal platforms on which other teams train and serve models: pipelines, registries, GPU scheduling, monitoring.
- *Skills:* Infrastructure, Kubernetes, cloud, ML lifecycle.
- *Backgrounds:* DevOps/SRE, backend engineering.
- *Pay:* Varies widely by employer. No strong single source was found.

**23. Infrastructure / GPU cluster / reliability engineer**
- *Day to day:* Keeping tens of thousands of accelerators healthy: fleet management, hardware health, storage, networking, incident response.
- *Skills:* Linux, distributed systems, networking, automation.
- *Backgrounds:* SRE, HPC, systems engineering.
- *Pay:* OpenAI posted Fleet/GPU Infrastructure SWE at $230K–$490K and Collective Communication at $380K–$500K [P]. OpenAI's "Scaling" department had 106 open roles [P].

**24. Performance / kernel / inference engineer**
- *Day to day:* Profiling training and inference; writing CUDA/Triton kernels; optimizing parallelism, memory and serving systems; porting to new chips (TPU, Trainium).
- *Skills:* Level 5 at depth: GPU architecture, C++/CUDA, compilers, numerical methods.
- *Backgrounds:* HPC, systems, game engines, compilers, quant finance.
- *Pay:* Anthropic posted Performance Engineer at $280K–$850K and Inference Engine/Systems at $350K–$850K [P]. OpenAI posted Training Performance Engineer at $295K–$500K and Kernel Performance at $266K–$445K plus equity [P].

**25. Data-center engineers (electrical, mechanical, controls, capacity delivery)**
- *Day to day:* Designing power and cooling, sourcing equipment, managing construction-to-operations, planning capacity.
- *Skills:* Licensed or degreed engineering, critical-facility experience.
- *Backgrounds:* Utilities, construction, hyperscaler facilities.
- *Pay:* Anthropic posted Data Center Electrical/Mechanical/Controls Engineer at $320K–$405K [P]. OpenAI posted Data Center Design Engineer (Electrical) at $257K–$327K plus equity [P].

**26. Technical program manager (TPM)**
- *Day to day:* Coordinating launches, compute buildouts, safety programs, and research operations across many teams.
- *Skills:* Program management, technical fluency, risk tracking.
- *Backgrounds:* Engineering, program management, the military.
- *Pay:* OpenAI posted $207K–$445K plus equity [P].

**27. Security engineer (AI/infrastructure security)**
- *Day to day:* Protecting model weights, infrastructure and user data; red-teaming; detection and response.
- *Skills:* Security engineering, cloud, threat modeling, knowledge of AI-specific attacks.
- *Backgrounds:* Security engineering, government.
- *Pay:* Anthropic posted Security SWE at $320K–$405K and Red Team Engineer at $320K–$405K [P]. Anthropic's Security department had 53 open roles [P].

### C. Research roles

**28. Research engineer**
- *Day to day:* Implementing and running large experiments (pretraining runs, RL pipelines, evals), building research tooling, debugging training at scale.
- *Skills:* Strong engineering plus ML depth, experiment hygiene.
- *Backgrounds:* SWE→ML transitions, MS/PhD, self-taught people with strong public work.
- *Pay:* Anthropic posted $315K–$560K (Interpretability), $350K–$500K (Alignment, Production Post-Training), and $500K–$850K (RL, Code RL, Computer Use, Post-Training Evals) [P]. OpenAI posted Research Engineer at $250K–$445K plus equity [P].

**29. Research scientist**
- *Day to day:* Setting research agendas, designing experiments, interpreting results, writing papers or internal reports, mentoring.
- *Skills:* Research taste, deep ML knowledge, math, a track record.
- *Backgrounds:* PhD typical (ML, physics, math, neuroscience), plus a publication or open-source record.
- *Pay:* Anthropic posted Research Scientist, Interpretability at $350K–$850K [P]. OpenAI posted $250K–$445K (general), $380K–$850K (Foundations, Search), and Researcher, Training $300K–$600K, all plus equity [P].

**30. Alignment / safety / interpretability researcher**
- *Day to day:* Research on oversight, control, robustness, interpretability, dangerous-capability evals, model behavior.
- *Skills:* Research skills plus safety-specific knowledge.
- *Backgrounds:* Often via MATS, ARENA, Anthropic Fellows, or PhD programs.
- *Pay:* OpenAI posted Researcher, Alignment at $295K–$500K and Safety Systems researchers at $380K–$500K plus equity [P]. Anthropic posted RE/RS Alignment at $350K–$500K [P].
- *On-ramps:* Anthropic Fellows pays a $3,850/week stipend plus about $15K/month in compute for 4 months [P]. MATS pays $1,250/week plus $2,000/week in compute for 12 weeks [P] (https://www.matsprogram.org/).

**31. Evals researcher / engineer**
- *Day to day:* Building capability and safety benchmarks, running model evaluations before launch, measuring long-horizon agent performance.
- *Skills:* Experimental design, statistics, domain knowledge, engineering.
- *Backgrounds:* Research engineering, domain experts with coding skill.
- *Pay:* Anthropic posted Research Engineer, Post-Training Model Evaluations at $500K–$850K [P]. Government AI institutes and nonprofits (METR, Epoch) pay less.

**32. Research economist / social scientist at labs**
- *Day to day:* Measuring AI's economic effects with usage data (for example, Anthropic's Economic Index).
- *Skills:* Econometrics, data science, policy writing.
- *Backgrounds:* Economics PhD.
- *Pay:* Anthropic posted $320K–$405K [P].

### D. Adjacent and ecosystem roles

**33. AI investor / analyst (VC, equity research)**
- *Day to day:* Evaluating companies, modeling compute economics, tracking revenue.
- *Skills:* Finance, technical literacy, network.
- *Backgrounds:* Banking, consulting, operators.
- *Pay:* Not reliably surveyed here.

**34. AI founder**
- *Day to day:* Everything: customer discovery, building, selling, hiring, fundraising.
- *Skills:* Speed, domain insight, distribution.
- *Backgrounds:* Any. Domain experts are increasingly common founders of vertical AI companies.
- *Pay:* High variance.

**35. Government / public-sector AI roles**
- *Day to day:* Model testing at AI institutes, procurement, agency AI deployment, standards work.
- *Skills:* Technical evaluation, policy, security clearance (sometimes).
- *Backgrounds:* Technical or policy.
- *Pay:* Public pay scales, well below lab levels.

**Note on "prompt engineer."** The standalone role that went viral in 2023 has largely been absorbed into other roles (AI engineer, PM, applied AI architect). Prompting and context engineering are now expected skills rather than a job title. Labs still hire around prompts, for example Anthropic's "Software Engineer, Tokens and Prompt Structures" at $320K–$405K [P], but as engineering roles.

---
## 5. Current state and key facts (2025–2026)

*All figures are as of the date given. [P] = primary source checked; [S] = secondary report.*

### 5.1 Frontier labs: revenue, valuation, funding

**OpenAI**
- **Annualized revenue (run-rate):** About $20B at the end of 2025. $25B by the end of February 2026. $40B in July 2026. About $50B in September 2026, per the Financial Times. A Bloomberg report on October 9, 2026 said OpenAI expects to reach or exceed $70B annualized by the end of 2026 [S]. The FT noted that a previously circulated $70B figure came from comparing OpenAI with Anthropic using a different method. This is a useful teaching example for the hype checklist.
  - https://sacra.com/c/openai/
  - https://www.bloomberg.com/news/articles/2026-10-09/openai-expects-70-billion-in-annualized-revenue-by-end-of-2026
- **Recognized revenue:** OpenAI booked $13.1B in 2025. It expected about $36B for full-year 2026 according to a company presentation seen by the FT [S]. Sacra lists quarterly revenue of $5.7B for Q1 2026 and $6.7B for Q2 2026 [S].
- **Funding:** On March 31, 2026, OpenAI closed $122B at an $852B post-money valuation. SoftBank co-led with a16z, D.E. Shaw, MGX, TPG and T. Rowe Price–advised accounts. Bloomberg Law reported Amazon agreeing to invest $50B, of which $35B was contingent on an IPO or a technical milestone, with Nvidia and SoftBank at $30B each. More than $3B came from individual investors through bank channels [S].
  - https://siliconangle.com/2026/03/31/openai-just-closed-record-breaking-122b-funding-round-brings-value-852b/
  - https://news.bloomberglaw.com/tech-and-telecom-law/openai-valued-at-852-billion-after-closing-122-billion-round
- **Structure:** In October 2025 OpenAI converted its for-profit into OpenAI Group PBC, controlled by the nonprofit OpenAI Foundation [S].
- **Users:** ChatGPT has more than 1B weekly active users. It had more than 50M consumer subscribers and more than 9M paying business users as of February 2026. Ads reached $1B annualized in August 2026 [S] (Sacra).
- **Economics:** Sacra estimates a 33% gross margin and inference costs projected at $14.1B for 2026. The FT reported projected cumulative negative free cash flow of $278B over 2026–2030 [S].
- **IPO:** OpenAI filed confidentially on June 8, 2026. Its CFO targets a listing "by 2027," and Sam Altman reportedly ruled out a 2026 listing [S].
- **Compute commitments (largest disclosed, all [S]):**
  - Stargate: a $500B, 10 GW plan.
  - Microsoft: a $250B Azure commitment (October 2025).
  - AWS: an initial $38B, plus a $100B eight-year expansion announced February 2026.
  - Oracle: about $300B over roughly five years.
  - Nvidia: at least 10 GW, with up to $100B of Nvidia investment.
  - Cerebras: more than $10B.

**Anthropic**
- **Run-rate revenue:** Over $5B in August 2025. About $9B at the end of 2025. $14B on February 12, 2026. Over $30B on April 6, 2026. Over $47B in early May 2026. Over $65B at the end of July 2026 (Bloomberg; Anthropic did not comment) [S].
  - https://sacra.com/c/anthropic/
  - https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth
- **Recognized quarterly revenue:** $4.8B in Q1 2026, $11.5B in Q2 and $16.8B in Q3. Q3 had an 11% adjusted operating margin excluding stock-based compensation, its second straight adjusted-profitable quarter [S].
- **Accounting caveats:** Cloud-reseller sales are booked gross, which inflates the top line relative to net-reporting peers. Sacra cites $1.70 of revenue per $1 of compute in Q3 2026, which is not a gross margin [S]. A WSJ-reported draft prospectus showed a first-half 2026 net loss above $80B, "mostly from accounting provisions" [S].
- **Funding history:**
  - Series F, September 2025: $13B at $183B post-money (led by ICONIQ).
  - Series G, February 12, 2026: $30B at $380B (led by GIC and Coatue).
  - Series H, late May 2026: $65B at $965B post-money, led by Altimeter, Dragoneer, Greenoaks and Sequoia [S]. Orrick, a law firm on the deal, announced the round (https://www.orrick.com/en/News/2026/05/Anthropic-Raises-65B-Series-H-at-965B-Post-Money-Valuation).
  - Strategic investors include Amazon, Google, Nvidia (up to $10B) and Microsoft (up to $5B) [S].
- **IPO:** Anthropic filed confidentially on June 1, 2026. As of October 20, 2026, reports said it was targeting a mid-November IPO, with a public filing around October 26 and a roadshow from about November 9. The debut valuation talk had moved from about $2T to about $1.5T [S].
  - https://www.fool.com/investing/2026/10/20/anthropic-is-targeting-an-ipo-as-soon-as-mid-novem/
  - https://www.ifre.com/equities/2499407/anthropic-pushes-ahead-with-mid-november-ipo
- **Customers:**
  - 300,000+ business customers (October 2025).
  - 1,000+ customers spending more than $1M a year (April 2026).
  - Eight of the Fortune 10.
  - Claude Code reached $1B annualized in November 2025 and $2.5B in February 2026 [S].
- **Enterprise share:** Menlo Ventures estimated Anthropic held 40% of enterprise LLM API spend in 2025, versus 27% for OpenAI [S] (https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/).

**xAI / SpaceX**
- SpaceX absorbed xAI in an all-stock deal that closed in early February 2026. CNBC reported it valued the combination at $1.25T [S].
- SpaceX listed on Nasdaq on June 12, 2026. It priced at $135, raised about $75B, and closed day one at roughly a $2.1T value [S].
  - https://www.fortune.com/2026/06/12/spacex-ipo-trading-first-day-live-updates-elon-musk/
- On June 16, 2026, SpaceX agreed to acquire Anysphere, the maker of Cursor, for about $60B in stock [S].
  - https://itwire.com/it-industry-news/deals/spacex-to-buy-cursor-for-us-60-billion

### 5.2 Chips, cloud and capex
- **Nvidia** (Q2 FY2027, quarter ended July 26, 2026) [P]:
  - Revenue $96.2B, up 106% year over year.
  - Data Center revenue $89.0B, up 117%.
  - Gross margin 75.0%.
  - Q3 outlook $108.0B ±2%, assuming no China data-center compute revenue.
  - "Vera Rubin, now in full production."
  - https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm
- **Hyperscaler 2026 capex guidance** (Microsoft, Alphabet, Amazon, Meta combined): about $720–745B, with company definitions differing [S]. By company:
  - Microsoft: about $175B.
  - Alphabet: $195–205B.
  - Amazon: about $220B.
  - Meta: $130–145B.
  - https://www.yieldtheory.app/research/hyperscaler-ai-capex-tracker-2026
- **CoreWeave** (neocloud) [S]:
  - FY2025 revenue about $5.1B; FY2026 guidance $12–13B.
  - Backlog $99.4B as of March 31, 2026.
  - Microsoft was about 67% of FY2025 revenue, a classic customer-concentration risk.
  - IPO March 28, 2025.
  - https://sacra.com/c/coreweave/

### 5.3 Startups and the application layer (selected)

| Company | Category | Latest reported revenue | Valuation / event | Source |
|---|---|---|---|---|
| Cursor (Anysphere) | Coding | $2.6B annualized B2B (Reuters) to $4B+ (Dealroom), mid-2026 | $60B SpaceX acquisition, June 2026 | [S] itwire; dealroom.co |
| Harvey | Vertical (legal) | ARR above $400M (Aug 2026) | $15.5B (Sep 2026) | [S] https://sacra.com/c/harvey/ |
| Lovable | App builder | About $600M annualized (Sep 2026) | $13.3B Series C (Aug 2026) | [S] https://sacra.com/c/lovable/ |
| Sierra | Customer-service agents | About $200M ARR (May 2026) | $15.8B (May 2026) | [S] https://sacra.com/c/sierra/ |
| Perplexity | Answer engine | About $750M annualized (Aug 2026 est.) | $20B (Sep 2025) | [S] https://sacra.com/c/perplexity/ |
| Mercor | Expert data marketplace | About $2B gross run-rate (Jun 2026) | $10B (Oct 2025) | [S] https://sacra.com/c/mercor/ |
| Scale AI | Data labeling | About $2B (2025 est.) | Meta bought 49% for $14.3B (Jun 2025); Google, OpenAI and others left | [S] https://sacra.com/c/scale-ai/ |

Business-model notes from these cases:
- **Harvey** pricing starts around $1,200 per lawyer per month, with roughly 20-seat minimums. About 10% of its staff are ex-lawyers in customer roles.
- **Sierra** charges per conversation or per successful resolution (outcome-based).
- **Mercor's** headline revenue is gross; contractors receive 60–70% of it.
- **Lovable** combines subscriptions ($25–$50 per month) with usage credits.

### 5.4 Enterprise adoption and economics
- **Enterprise generative-AI spend:** $37B in 2025, up from $11.5B in 2024 (3.2×). About $19B of that went to the application layer (Menlo Ventures, a VC with portfolio interests) [S].
- **Pilot outcomes:** The MIT NANDA "GenAI Divide" report (July 2025) found only about 5% of enterprise genAI pilots delivered rapid revenue acceleration or measurable P&L impact. Media turned this into "95% fail." It attributed the gap to brittle workflows and poor fit to daily operations, not model quality [S].
  - https://virtualizationreview.com/articles/2025/08/19/mit-report-finds-most-ai-business-investments-fail-reveals-genai-divide
- **Stanford AI Index 2026** [P/S]:
  - 88% of organizations report adopting AI.
  - US private AI investment was $285.9B in 2025, more than 23× China's private figure.
  - AI researchers and developers moving to the US are down 89% since 2017, with an 80% drop in the last year.
  - New AI PhDs in the US and Canada rose 22% from 2022 to 2024, mostly going into academia.
  - 73% of experts versus 23% of the public expect AI's job impact to be positive.
  - More than 80% of US high-school and college students use AI for schoolwork.
  - https://hai.stanford.edu/ai-index/2026-ai-index-report

### 5.5 Jobs and labor-market evidence
- **Entry-level squeeze:** In "Canaries in the Coal Mine?" (Brynjolfsson, Chandar, Chen; Stanford Digital Economy Lab), workers aged 22–25 in the most AI-exposed occupations saw a relative employment decline of 13% in the August 2025 version and 16% in the later version. This was after controlling for firm-level shocks. Older workers in the same occupations held steady. Declines concentrate where AI automates rather than augments, and adjustment shows up in headcount more than pay [P/S].
  - https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine
- **Task-level exposure:** Microsoft researchers analyzed about 200,000 Bing Copilot conversations. Information work (creating, processing and communicating information) was the most common and most successful AI-assisted activity, so most occupations have some exposure [P].
  - https://arxiv.org/abs/2507.07935
- **BLS projections 2025–2035** [P]:
  - Data scientists: +35%.
  - Computer and information research scientists: +22%.
  - Software developers: +10%, with AI development cited as a demand driver.
  - Electricians: +9%, with data-center electricity demand cited.
- **What labs are hiring for (October 21, 2026 job boards)** [P]:
  - *Anthropic, 675 open roles:* Sales 124; AI Research & Engineering 68; Applied AI 61; Security 53; Finance 52; Software Engineering–Infrastructure 52; Engineering & Design–Product 51; Safeguards 42; TPM 27; Compute 25; Product Management, Support & Operations 24; People 19; Legal 19; Marketing 18; Public Policy 15; Data Science 9; Communications 5; Public Benefit 5; Technical Education 4; Hardware 2.
  - *OpenAI, 809 open roles:* Go To Market 149; Applied AI 120; Scaling 106; Research 51; User Operations 51; Marketing 46; Forward Deployed Engineering 31; Finance 31; Security 29; Consumer Devices 27; People 19; Safety Systems 18; Data Science 18; OpenAI for Gov 15; and smaller groups.
  - *Lesson:* research is roughly 5–10% of open roles at both labs. Most hiring is in selling, deploying, scaling, securing and governing AI.
- **FDE boom:**
  - Lightcast data cited by CNBC reportedly shows US FDE postings rising from fewer than 200 in 2023 to more than 7,300 in the first nine months of 2026. I could not verify this against the CNBC original [S].
  - Secondary reports say OpenAI committed more than $4B to a deployment business, AWS launched a $1B FDE initiative, and Anthropic launched a $100M program to train 10,000 such engineers by the end of 2027. These need verification against primary announcements [S].
- **Talent war:** In June–July 2025 Meta formed Meta Superintelligence Labs, took a 49% stake in Scale AI (Alexandr Wang joined Meta), and made widely reported eight- and nine-figure multi-year offers. OpenAI reportedly said it was "recalibrating" compensation [S].

### 5.6 Learning-ecosystem facts (verified October 2026)
- **Karpathy, "Neural Networks: Zero to Hero":** 8 lectures, from micrograd to building GPT and its tokenizer. Prerequisites are solid Python and intro math [P] (https://karpathy.ai/zero-to-hero.html).
- **Karpathy's nanochat:** a minimal full-stack LLM training harness covering tokenizer, pretraining, SFT, RL, eval and inference. It trains a GPT-2-capability model for about $48, roughly 2 hours on an 8×H100 node [P] (https://github.com/karpathy/nanochat).
- **fast.ai "Practical Deep Learning for Coders":** free, 9 lessons of about 90 minutes, assumes about a year of coding. Part 2 is 30+ hours. The page still shows the 2022 edition [P] (https://course.fast.ai/).
- **Hugging Face Learn:** 12 free courses, including LLM, Agents, Context (context engineering for code agents), smol (post-training), Deep RL, Robotics (LeRobot), Diffusion, Audio and Computer Vision [P] (https://huggingface.co/learn).
- **Anthropic Academy:** 23 entries, including Claude 101, Claude Code 101, Claude Platform 101, Building with the Claude API, Introduction to MCP, MCP Advanced Topics, Introduction to agent skills, Introduction to subagents, AI Capabilities and Limitations, and an AI Fluency series (framework, educators, students, nonprofits, small businesses, builders, creative work) [P] (https://anthropic.skilljar.com/).
- **OpenAI Academy:** tracks for Apply AI at Work, Build with AI (Codex, API), Lead AI Adoption, and Teach and Learn with AI, plus events and communities [P] (https://academy.openai.com/).
- **DeepLearning.AI:** Machine Learning Specialization (about 95 hours); Deep Learning Specialization (about 127 hours); Math for ML & Data Science (about 94 hours); AI Python for Beginners (about 11.5 hours); AI Prompting for Everyone (about 7 hours); Generative AI for Everyone (about 5 hours); Agentic AI (about 10 hours); Build with Andrew (about 1 hour); Data Engineering with AWS (about 107 hours) [P] (https://www.deeplearning.ai/courses/).
- **Stanford CS336 "Language Modeling from Scratch":** Spring 2026, Hashimoto and Liang. Five assignments: basics, systems/Triton, scaling laws, data, and alignment/reasoning RL. Lectures are on YouTube [P] (https://cs336.stanford.edu/).
- **Safety on-ramps:**
  - MATS: 12 weeks; $1,250/week stipend plus $2,000/week compute; 631 alumni since 2021; 75% now work in alignment, transparency or security [P].
  - ARENA: 4–5 week in-person London bootcamps with costs covered; curriculum online [P].
  - BlueDot Impact: free courses, including a 2-hour "The Future of AI" [P].
  - Anthropic Fellows: 4 months, $3,850/week stipend [P].
- **Certifications:** AWS Certified AI Practitioner costs $100, with 65 questions in 90 minutes and no prerequisites [P]. IAPP AIGP is the AI Governance Professional credential [P].

---

## 6. Diagram ideas

1. **The AI value chain ("the stack").** Seven horizontal layers, bottom to top: Energy & Land → Chips → Cloud/Data Centers → Foundation Models → Data & Tooling → Applications → Services → Customers. Label each layer with 3–5 example companies and one headline 2026 number (Nvidia $89B quarterly data-center revenue; $720–745B hyperscaler capex; OpenAI and Anthropic run-rates; Menlo's $37B enterprise spend). Draw arrows showing money flowing *down* and capability flowing *up*.
2. **Circular money map.** Nodes for Nvidia, Microsoft, Amazon, Google, Oracle, CoreWeave, OpenAI, Anthropic and SoftBank. Draw one style of edge for equity investments and another for compute purchases. Highlight loops where a supplier invests in a customer that buys from it. Caption: "Why 'up to' and contingent numbers need care."
3. **Run-rate race chart, 2024–2026.** Two lines: OpenAI ($6B → $20B → $40B → ~$50B) and Anthropic (~$1B → $9B → $30B → $65B). Annotate "methods differ: gross vs. net, monthly vs. weekly annualization." Pair it with a small bar chart of recognized quarterly revenue to show the gap between run-rate and booked revenue.
4. **The AI skill tree.** A video-game tech tree with seven levels (Literacy → Power User → Builder → Technical Foundations → AI App Engineering → ML/Infra Engineering → Frontier Research). Side branches for Policy, Sales/Solutions/FDE, Writing/Education, Domain Expertise and Data-Center Trades. Mark "you are here" at Level 1 for the reader.
5. **Career transition map.** Starting points on the left (non-technical professional, student, software engineer, scientist/PhD, salesperson, tradesperson). Destination roles on the right. Arrows labeled with the 1–3 skills that bridge each transition, such as "SWE → AI engineer: evals + RAG + agents."
6. **Frontier lab org chart with hiring bars.** A boxes-and-lines chart (Research | Scaling/Compute | Product | Applied AI/GTM | Safeguards & Policy | Security | G&A). Next to each box, a bar for the Oct 2026 open-role count at Anthropic and OpenAI. Caption: "Research is under 10% of hiring."
7. **Model pipeline as a relay race.** Data → Pretraining → Post-training/RL → Evals → Safety review → Inference/serving → Product → Customer deployment (FDE). Above each baton handoff, name the roles that own it.
8. **Four tiers of AI pay (log scale).** BLS medians (~$120–140K) → big-tech Levels.fyi ML medians (~$260–465K) → frontier-lab posted base ranges ($200K–$850K plus equity) → reported outlier offers ($100M+ multi-year). Caption: "Headlines describe the far right; most careers live on the left."
9. **A day in the life, side by side.** Three vertical timelines (FDE at a customer site; research engineer babysitting a training run; AI PM reviewing eval results and a launch). Show proportions of time spent coding, meeting, reviewing, writing and traveling.
10. **Business model matrix.** A 2×2 grid: horizontal versus vertical, and software (tool) versus outcome (service). Place examples: ChatGPT/Claude (horizontal tool), Harvey (vertical tool), Sierra (horizontal-ish outcome), AI bookkeeping agency (vertical outcome). Overlay pricing type: seat, usage, outcome.
11. **The moat ladder.** Rungs from weakest to strongest: thin wrapper → workflow product → integrated system of record → proprietary data flywheel + distribution + trust/compliance. Beside the bottom rung: "the model eats your feature" risk.
12. **AI unit-economics waterfall.** Classic SaaS: $1 of revenue → about $0.20 delivery cost → about $0.80 gross profit. AI app: $1 → large inference cost → smaller gross profit. Reference OpenAI's estimated ~33% gross margin [S] and say clearly that this varies by company.
13. **Pilot-to-production funnel.** Many organizations explore → fewer pilot → few deploy → about 5% achieve measurable P&L impact (MIT NANDA). Label the "learning gap" at the narrowest point.
14. **Task exposure 2×2.** X-axis: AI exposure of tasks. Y-axis: automation versus augmentation. Plot example tasks. Show where entry-level employment declines cluster (high exposure plus automation, per "Canaries").
15. **The data-center job ecosystem.** A cutaway of a data center (substation, electrical room, cooling plant, white space with racks, network room, security, control room), each zone labeled with trades and roles and example posted pay (technicians $157K–$302K at OpenAI/Stargate; data-center engineers $320K–$405K at Anthropic). Add the community-engagement manager outside the fence.
16. **Learning roadmap timeline.** Three bands (0–3 months, 3–12 months, 1–3 years) across four swim lanes (Power User/Professional, Builder, Engineer, Researcher). Each lane carries specific course logos and portfolio milestones.
17. **Hype-evaluation flowchart.** "Is the number revenue, run-rate, bookings, or 'up to'? → Who is the source and what do they gain? → Is there a primary document? → What's the denominator? → Is the benchmark independent? → Has it shipped to real users?"
18. **T-shaped professional.** A tall bar for domain expertise (e.g., nursing) and a wide crossbar for AI skills (prompting, automation, evals, governance). A second figure shows the "π-shaped" professional with two deep areas, such as law plus software.

---
## 7. Practical exercises and projects (easy to hard)

### Tier 1: Power user (no coding)
1. **Audit your week for AI automation.** For one week, log every task in 30-minute blocks. Tag each task: *AI does it* / *AI assists* / *human only*, and *frequency × time*. Rank the top five candidates by hours saved. *Deliverable:* a one-page "automation map" of your job.
2. **The same task three ways.** Give one real work task (such as summarizing a report for your boss) to ChatGPT, Claude and Gemini with an identical prompt. Score the outputs on accuracy, usefulness and tone. Then improve your prompt with context and examples and re-score. *Lesson:* context matters more than which model you use.
3. **Map the jagged frontier.** Design 15 mini-tests in your own field: easy, hard, tricky, and "requires local knowledge." Record where the model is excellent and where it fails confidently. Repeat the test in three months.
4. **Verification drill.** Ask for a researched answer with citations on a topic you know well. Check every citation. Count the claims that were correct, misattributed or invented. Write your personal "trust rules."
5. **Build a reusable assistant.** Create a Claude Project, custom GPT or Gem for one recurring task (meeting notes into action items, client email triage). Include instructions, two worked examples and reference docs. Use it for two weeks and refine it.
6. **Delegate to an agent.** Give a deep-research or agent tool a real multi-step task, such as comparing five vendors against your requirements and producing a table. Note where you had to intervene. Write a better brief and run it again.
7. **Read the money.** Take one AI funding headline this week and classify every number in it: revenue, run-rate, bookings, valuation, or an "up to" commitment. Find the primary source (company blog, SEC filing). Write three sentences explaining what the headline did and did not say.

### Tier 2: Builder (no-code / low-code)
8. **First automation.** Using Zapier, Make or n8n, build: new form submission → AI summarizes and classifies → row added to a spreadsheet → email notification. Then add an error case and handle it.
9. **Team assistant with feedback.** Build an assistant for a colleague's task, collect their feedback on 10 real uses, and iterate. *Lesson:* user research for AI.
10. **Vibe-code an internal tool.** With Lovable, Replit or Claude Code, build a small working app you'll use (a tracker, calculator or intake form). Publish it, then write down what broke and how you fixed it.
11. **Connect your assistant to your data.** Set up connectors or MCP servers (drive, calendar, email) and complete a task that needs all three, such as preparing a briefing for tomorrow's meetings. Write a one-paragraph privacy assessment.
12. **Spreadsheet analyst.** Take a messy public dataset (city budget, sports stats) and, with AI help, clean it, pivot it, chart it, and write a five-bullet insight memo. Then check every number the AI computed.
13. **Price an AI feature.** Estimate the cost of a feature (for example, summarizing 1,000 support tickets a day) using a model's per-token pricing. Compare a small model with a frontier model. *Lesson:* unit economics.
14. **Your first eval set.** For your assistant from #5, write 20 test inputs with "what good looks like" notes. Score outputs before and after changing the instructions. Track results in a spreadsheet.

### Tier 3: Technical foundations to AI engineering
15. **Python + API "hello world."** Write a 30-line Python script that sends a document to a model API and saves a structured JSON summary. Handle API keys safely with environment variables.
16. **SQL + AI analyst.** Load a public dataset into SQLite, write 10 SQL queries yourself, then have an AI write 10 and compare correctness.
17. **Free implementation for a small business.** Find a local business (a dentist, contractor or nonprofit). Interview the owner, map one painful workflow (intake, quotes, scheduling, reviews), implement an AI-assisted fix, measure the time saved after two weeks, and write a case study. *This is the best portfolio item for aspiring consultants and FDEs.*
18. **Build a RAG app with citations.** Index 50–200 documents (a policy manual, your field's public guidelines). Answer questions with citations. Build a 30-question eval and measure accuracy. Try two chunking strategies and compare.
19. **Agent with tools.** Build an agent that uses two or three tools (search, calculator, a database) and an MCP server you write yourself. Log every tool call, then analyze the failures.
20. **Error analysis write-up.** Collect 100 real outputs from a system you built. Hand-label failure types, count them, fix the top category, and re-measure. Publish the write-up. *This is exactly what hiring managers for AI-engineer roles want to see.*
21. **Prompt-injection red team.** Against your own agent from #19, attempt 15 injection attacks (malicious text in documents, tool outputs, web pages). Document successes and implement mitigations.
22. **Ship a micro-product.** Ship a small vertical AI tool for a niche you know (an inspection-report generator for HVAC techs, a lesson-plan differentiator for teachers). Get 10 real users and a feedback loop. Track cost per user.

### Tier 4: ML engineering, infrastructure and research
23. **Micrograd to GPT.** Work through Karpathy's "Zero to Hero" lectures, typing every line. Write a blog post explaining backpropagation to your past self.
24. **Fine-tune a small open model.** Fine-tune a small open-weight model on a narrow task with LoRA (Hugging Face TRL/Unsloth). Compare it against prompting a frontier model on your eval set from #18, including cost.
25. **Train a tiny LLM end-to-end.** Run Karpathy's nanochat (about $48 of rented GPU time), or a smaller CPU or single-GPU variant. Document each stage: tokenizer, pretraining, SFT, RL, eval.
26. **Write a GPU kernel.** Implement and benchmark a matrix-multiply or softmax kernel in Triton or CUDA, comparing it to PyTorch's built-in. Use the GPU MODE lectures as a guide.
27. **Replicate a paper.** Pick a recent, small-scale interpretability or post-training paper. Reproduce its key figure, then note discrepancies and one extension. Post the code and write-up publicly, and use it as an application to MATS, ARENA or the Anthropic Fellows Program.
28. **Design a novel eval.** Create a benchmark of 50–200 hard tasks in a domain you know (tax law edge cases, clinical triage vignettes, plumbing code questions). Use expert-written gold answers and a scoring rubric. Run several frontier models and publish the results with honest limitations. *This turns domain expertise directly into AI-research credibility.*

---

## 8. Areas of opportunity, by audience

### 8.1 Non-technical professional (the reader's most likely starting point)
- **Become your team's AI workflow designer.** The scarce skill is redesigning a workflow, not prompting. Organizations report 88% adoption, but few pilots reach P&L impact. The gap is people who connect AI to real work.
- **Domain expert + AI ("the AI-native accountant, nurse, paralegal, teacher, recruiter").** You know which errors matter, so you can write the evals, guidelines and quality checks that engineers can't.
- **Expert contractor work.** Labs pay for expert judgment to train and evaluate models (Mercor experts average $85+/hour [S]). It works as a side income and an education, but it is project-based and volatile.
- **Internal AI trainer / champion.** Run lunch-and-learns, build shared assistants, write your company's prompt library. This often becomes a formal "AI adoption lead" role.
- **AI governance and compliance.** Every regulated industry needs AI risk policies, vendor reviews and (for EU business) AI Act compliance. Credentials like IAPP AIGP help here. Backgrounds in privacy, legal, audit and risk transfer directly.
- **Sales and customer success for AI products.** The largest hiring category at frontier labs (Anthropic Sales: 124 open roles [P]). Industry knowledge plus AI fluency is the qualification.
- **Protect your on-ramp.** If you are early-career in a highly exposed occupation (the "Canaries" pattern), invest in skills AI complements: judgment, client relationships, cross-functional coordination, and verification of AI output.

### 8.2 Aspiring builder (no-code to low-code)
- **AI implementation for small businesses.** Local service businesses (clinics, law offices, trades, real estate, restaurants) need intake automation, scheduling, follow-ups, review responses, quoting and document processing. Offer a fixed-price audit, then implementation, then a monthly retainer.
- **Internal tools inside your company.** Vibe-coded dashboards, trackers and assistants. Being "the person who builds things" is a fast route into product or ops-engineering roles.
- **Templates and productized setups.** Sell or share proven automation templates and assistants for a niche (an n8n intake flow for physiotherapy clinics).
- **Content and education.** Explain AI for a specific audience (AI for nurses, AI for contractors). Niche newsletters, YouTube channels and workshops do well because general AI content is saturated.
- **Evaluation-as-a-service for a domain.** Help companies in your industry test whether AI tools actually work on their cases.

### 8.3 Aspiring engineer or researcher
- **AI engineer / LLM application engineer.** The broadest technical demand outside the labs. The differentiators are evals, RAG quality and agent reliability, shown through public error-analysis write-ups.
- **Forward-deployed engineering.** The fastest-growing AI role of 2025–2026 (OpenAI has a dedicated FDE department; FDE postings grew several-fold [S]). It suits engineers who like customers, ambiguity and travel.
- **Inference and performance engineering.** Every efficiency gain is money. Posted ranges reach $850K base at Anthropic [P]. Systems, HPC, game-engine and compiler backgrounds transfer well.
- **Data-center and compute engineering.** Electrical, mechanical and controls engineers with critical-facility experience are being hired directly by labs ($320K–$405K posted at Anthropic [P]).
- **Safety, evals and interpretability.** The field is small, funded on-ramps exist (MATS, ARENA, Anthropic Fellows), and public replications count heavily.
- **Research engineering via open-source.** Contributions to vLLM, SGLang, Hugging Face libraries, nanochat-style projects, or eval frameworks are visible proof of skill.

### 8.4 Entrepreneur
- **Vertical AI with deep workflow integration.** Harvey (legal) shows the pattern: domain-specific workflows, ex-practitioners on staff, premium per-seat pricing, and growth to $400M+ ARR [S]. Opportunities remain in less-glamorous verticals (insurance claims, freight, construction estimating, compliance, dental billing, government services).
- **Outcome-priced agents.** Charging per resolution or per completed task (Sierra's model) aligns price with value and sidesteps seat-count shrinkage as AI reduces headcount.
- **Services-as-software and AI-enabled services firms.** Buy or build a service business (bookkeeping, IT support, back-office) and run it with AI for better margins. Distribution and trust come with the business.
- **Human data and RL environments.** Labs buy expert data and training environments. Mercor went from about $760M to about $2B gross run-rate in six months [S]. Concentrated customer bases and abrupt shifts (Scale AI after the Meta deal) are the risk.
- **Picks and shovels for AI builders.** Evals, observability, security (prompt-injection defense), agent infrastructure, data pipelines, compliance tooling.
- **Physical buildout supply chain.** Power equipment, cooling, construction services, workforce training, and site development ("powered land" developers appear on OpenAI's job board [P]).
- **Defensibility checklist:** Would your product get *better* or *obsolete* when the next model ships? Do you own proprietary data, workflow position, distribution or trust that a lab can't easily replicate? Can you survive inference costs at scale (unit economics)?

### 8.5 Investor (including ordinary retail investors)
- **Understand the layers.** Public exposure exists to chips (Nvidia and others), hyperscalers, neoclouds (CoreWeave), memory, power and utilities, and newly listed AI-heavy companies (SpaceX/xAI; a possible Anthropic IPO). Different layers carry different risks: concentration, capex overbuild, competition, regulation.
- **Watch the bridge between capex and revenue.** Hyperscalers are spending about $720–745B in 2026 [S], while frontier lab revenue is growing fast but includes heavy losses (OpenAI's projected −$278B cumulative free cash flow 2026–2030 per FT [S]). The question is whether application revenue grows into the infrastructure.
- **Read primary documents.** 10-Qs, S-1s, earnings releases (Nvidia's 8-K is a model of clarity). Note customer concentration (CoreWeave and Microsoft) and contingent deal terms.
- **Hype-cycle discipline.** Hot IPOs can swing wildly. SpaceX priced at $135, hit about $225, and later traded back below its $150 open, per the Motley Fool [S]. This is educational context, not investment advice.

### 8.6 Skilled trades and the physical AI economy
- **Electricians** (BLS: about 821,000 jobs, +9% growth 2025–2035, data centers cited [P]); **HVAC/mechanical techs and pipefitters** (liquid cooling); **lineworkers and substation techs** (grid connection); **low-voltage and fiber techs** (network cabling); **controls technicians** (building automation); **construction managers and commissioning agents**; **critical-facility operators** (24/7 operations).
- **Pay upside:** Lab and Stargate-adjacent roles post $157K–$302K for technicians [P], well above trade medians. Contractor and union pay near large builds is also high (verify locally).
- **Pathways:** Registered apprenticeships (electrical JATCs), community-college HVAC/controls programs, military technical experience, data-center operator training programs. Pairing trade credentials with basic AI literacy (documentation, diagnostics, scheduling) is a further differentiator.
- **Adjacent non-trade roles:** Community engagement managers, permitting and land specialists, workforce-development managers (OpenAI posted "Workforce Development & Education Manager, Infrastructure Sites" at $176K–$385K [P]).

---

## 9. Learning roadmap and resources

### 9.1 Stage 1: 0–3 months, "fluent power user" (everyone)
**Goal:** Use AI expertly and safely in your own work, understand how it works conceptually, and read AI news critically.
- **Understand the machine (about 10 hours):**
  - Karpathy's "Intro to Large Language Models" and "Deep Dive into LLMs like ChatGPT" (YouTube).
  - 3Blue1Brown's neural-network and transformer videos (https://www.3blue1brown.com/).
  - Anthropic "AI Capabilities and Limitations."
- **Structured fluency (about 15–25 hours):**
  - Anthropic "AI Fluency: Framework & Foundations" and Claude 101 (https://anthropic.skilljar.com/).
  - DeepLearning.AI "Generative AI for Everyone" and "AI Prompting for Everyone" (https://www.deeplearning.ai/courses/).
  - OpenAI Academy "Apply AI at Work" (https://academy.openai.com/).
  - Google "AI Essentials" (Coursera / grow.google) as an alternative.
- **Practice:** Exercises 1–7. Build three reusable assistants.
- **Read (pick two):**
  - Ethan Mollick, *Co-Intelligence* (practical use).
  - Arvind Narayanan & Sayash Kapoor, *AI Snake Oil* (skepticism).
  - Chris Miller, *Chip War* (industry).
  - Karen Hao, *Empire of AI*, or Parmy Olson, *Supremacy* (lab history).
- **Optional start of the technical track:** DeepLearning.AI "AI Python for Beginners" (about 11.5 hours).
- **Milestone:** You save 3+ hours a week, have a written "trust rules" doc, and can explain run-rate versus revenue.

### 9.2 Stage 2: 3–12 months, choose a track

**Track A: Professional / implementer (non-coding or light coding)**
- Workflow automation (Zapier/Make/n8n academies), no-code building (Lovable/Replit; DeepLearning.AI "Build with Andrew"), connectors and MCP (Anthropic "Introduction to MCP"), Claude Cowork / ChatGPT agents.
- Governance: IAPP AIGP study materials. NIST AI Risk Management Framework (free).
- Business: Anthropic "AI Fluency for Small Businesses" and "Deploying Claude Enterprise with Confidence"; OpenAI Academy "Lead AI Adoption."
- Portfolio: Exercises 8–14, plus #17 (free small-business implementation) written up as a case study.
- Certification (optional): AWS Certified AI Practitioner ($100, 90 minutes [P]) if you work in an AWS-heavy enterprise; AIGP for governance roles.

**Track B: Builder → AI engineer**
- Python: AI Python for Beginners → Harvard CS50P → Kaggle Learn (Python, Pandas, SQL).
- APIs: Anthropic "Claude Platform 101" and "Building with the Claude API"; OpenAI Academy "Build with AI"; provider cookbooks.
- LLM apps: Hugging Face LLM Course, Agents Course and Context Course (https://huggingface.co/learn); DeepLearning.AI "Agentic AI."
- Evals: Hamel Husain's blog (hamel.dev) and the "AI Evals for Engineers & PMs" course (Hamel Husain & Shreya Shankar); DeepLearning.AI "Evaluating AI Agents."
- Book: Chip Huyen, *AI Engineering* (O'Reilly, 2025).
- Portfolio: Exercises 15–22. Publish error analyses and evals, not just demos.

**Track C: Pre-ML foundations (for future ML engineers and researchers)**
- Math: 3Blue1Brown "Essence of Linear Algebra" and "Essence of Calculus"; DeepLearning.AI "Mathematics for ML and Data Science" (about 94 hours); Khan Academy probability.
- ML: Andrew Ng's Machine Learning Specialization (about 95 hours); Géron, *Hands-On Machine Learning*.
- Deep learning: fast.ai Part 1 (free; https://course.fast.ai/).

### 9.3 Stage 3: 1–3 years, depth and specialization
- **Deep learning from scratch:**
  - Karpathy "Neural Networks: Zero to Hero" (https://karpathy.ai/zero-to-hero.html), then nanochat (https://github.com/karpathy/nanochat).
  - Simon Prince, *Understanding Deep Learning* (free, https://udlbook.github.io/udlbook/).
  - *Dive into Deep Learning* (https://d2l.ai).
  - Sebastian Raschka, *Build a Large Language Model (From Scratch)*.
- **University courses (free online):** Stanford CS336 Language Modeling from Scratch (https://cs336.stanford.edu/); Stanford CS224N (NLP) and CS231n (vision); MIT 6.S191 (intro deep learning); fast.ai Part 2.
- **Systems and scale:**
  - Hugging Face "The Ultra-Scale Playbook" (https://huggingface.co/spaces/nanotron/ultrascale-playbook).
  - Google DeepMind "How to Scale Your Model" (https://jax-ml.github.io/scaling-book/).
  - GPU MODE lectures and Discord (https://github.com/gpu-mode/lectures).
  - *Programming Massively Parallel Processors*.
  - Kleppmann, *Designing Data-Intensive Applications*.
- **MLOps:** Chip Huyen, *Designing Machine Learning Systems*; MLOps Community; cloud ML certifications (AWS ML Engineer Associate, Google Cloud Professional ML Engineer) for enterprise-facing roles.
- **Safety and alignment:**
  - BlueDot Impact courses (https://bluedot.org/).
  - ARENA curriculum and bootcamps (https://www.arena.education/).
  - MATS (https://www.matsprogram.org/).
  - Anthropic Fellows Program (Anthropic careers page).
  - 80,000 Hours AI safety career review (https://80000hours.org/career-reviews/ai-safety-researcher/).
- **Post-training and RL:** Nathan Lambert's RLHF book and Interconnects; Hugging Face "a smol course" and TRL docs; CS336 assignment 5.
- **Policy track:** GovAI, CSET (Georgetown), RAND and IAPS publications; BlueDot governance courses; lab policy job descriptions as syllabi.
- **Portfolio:** Exercises 23–28. Contribute to open-source, publish replications, apply to fellowships.

### 9.4 Certifications: do they matter?
- **They matter most** where buyers or HR filter on them: cloud-centric enterprises (AWS, Google Cloud and Microsoft AI certs), consulting and systems integrators, government contracting, and governance and compliance (IAPP AIGP).
- **They matter little** for frontier-lab research, research engineering and startup engineering, where public work (code, papers, evals, write-ups) dominates. Lab postings typically require a "Bachelor's degree or an equivalent combination of education, training, and/or experience" [P] (Anthropic postings).
- **Completion certificates** from free courses (Anthropic Academy, DeepLearning.AI, Hugging Face) are useful as structured learning and as signals of initiative, not as job qualifications.
- **Rule of thumb:** one relevant certification plus three strong portfolio pieces beats five certifications and no portfolio.

### 9.5 Staying current

**Newsletters**
- Import AI (Jack Clark, jack-clark.net): research and policy.
- The Batch (DeepLearning.AI).
- One Useful Thing (Ethan Mollick): practical use.
- Simon Willison's blog (simonwillison.net): hands-on LLM tools and security.
- Latent Space (swyx & Alessio): AI engineering.
- Interconnects (Nathan Lambert): post-training and open models.
- Ahead of AI (Sebastian Raschka): research digests.
- SemiAnalysis (Dylan Patel): chips, data centers, compute economics.
- Stratechery (Ben Thompson): business strategy.
- AI as Normal Technology (Narayanan & Kapoor): skeptical, evidence-based.
- Don't Worry About the Vase (Zvi Mowshowitz): exhaustive weekly roundups.
- Epoch AI (epoch.ai): data on compute, training costs and trends.

**Podcasts**
- Dwarkesh Podcast (deep interviews with lab leaders and researchers).
- Latent Space.
- No Priors.
- Hard Fork (general audience).
- Lenny's Podcast (AI product).
- Training Data (Sequoia).
- Cognitive Revolution.
- Acquired (company histories, including Nvidia).
- 80,000 Hours Podcast (safety and policy careers).
- Machine Learning Street Talk.

**Data and leaderboards (use critically)**
- Epoch AI (trends and benchmarks hub).
- METR (long-horizon task evaluations).
- Artificial Analysis (price, speed and quality comparisons).
- LMArena (human preference votes; style-sensitive).
- Stanford AI Index (annual).
- Lab system and model cards (primary source for capabilities and safety testing).

**Communities**
- Hugging Face (forums, Discord).
- Kaggle.
- r/LocalLLaMA (open models).
- GPU MODE Discord (kernels).
- MLOps Community.
- fast.ai forums.
- AI Engineer conference community.
- LessWrong / Alignment Forum (safety).
- Local AI meetups and company "AI guilds."

**People to follow (by area)**
- *Teaching and fundamentals:* Andrej Karpathy, Andrew Ng, Jeremy Howard.
- *Applied AI engineering:* Simon Willison, Chip Huyen, Hamel Husain, swyx.
- *Research digests:* Sebastian Raschka, Nathan Lambert, Lilian Weng (blog).
- *Labs and leaders:* Dario Amodei (essays such as "Machines of Loving Grace"), Sam Altman (blog), Demis Hassabis, Jack Clark.
- *Interpretability:* Chris Olah.
- *Economics and work:* Ethan Mollick, Erik Brynjolfsson.
- *Industry and compute:* Dylan Patel, Ben Thompson.
- *Interviews:* Dwarkesh Patel.
- *Skeptics and critics* (essential for balance): Arvind Narayanan & Sayash Kapoor, Gary Marcus, François Chollet (ARC Prize).

**A sustainable routine**
- 20 minutes a day with one newsletter and one hands-on try of something new.
- A weekly hour with one long-form podcast or paper.
- A monthly re-run of your personal jagged-frontier test (Exercise 3).
- A quarterly update of your skills map and portfolio.

### 9.6 Habits for evaluating AI news and hype (the checklist)
1. **What kind of number is it?** Recognized revenue ≠ run-rate ≠ ARR ≠ bookings ≠ "up to" commitments ≠ valuation. In 2026, OpenAI's run-rate was reported as both about $50B and about $70B depending on method [S], and Anthropic books cloud-reseller sales gross [S]. Compare like with like.
2. **Who says so, and what do they gain?** VC surveys (portfolio interests), company blogs (marketing), short-sellers, rival labs. A source with an incentive can still be right, so look for corroboration.
3. **Find the primary source.** Read the SEC filing, the paper, the system card or the official blog, not the tweet about the article about the paper.
4. **Look for the denominator and the comparison.** "1,000% growth" in FDE postings started from fewer than 200. "95% of pilots fail" was a reframing of a "5% achieved measurable P&L impact" finding.
5. **Benchmarks: independent, uncontaminated, unsaturated?** Prefer third-party evaluations (METR, Epoch, government institutes) over a lab's own chart. Remember the jagged frontier: an IMO gold medal says little about reading a clock.
6. **Demo versus deployment.** Has it shipped to real users at scale, and what do those users report? Adoption (88%) is not impact (about 5% of pilots).
7. **"Up to," contingent and circular.** Check conditions, timelines, and whether money flows back to the investor as purchases.
8. **Wait 48 hours.** First reports of leaks, valuations and "breakthroughs" are frequently revised.
9. **Track predictions.** Keep a note of what experts predicted and check back. It is the best way to learn whose judgment to trust.
10. **Separate "can" from "will" from "should."** Technical feasibility, economic adoption and social desirability are different questions with different evidence.

---

## 10. Common misconceptions and analogies

### 10.1 Misconceptions
1. **"You need a PhD to work in AI."** Research is under 10% of open roles at Anthropic (68 of 675) and OpenAI (51 Research of 809) as of October 2026 [P]. Sales, applied AI, infrastructure, security, policy and operations dominate. Even lab research postings accept "an equivalent combination of education, training, and/or experience."
2. **"Prompt engineering is the hot new career."** It became a baseline skill. The 2025–2026 version is *context engineering* plus *evals*, embedded in AI-engineer, PM and solutions roles.
3. **"AI researchers all earn $100 million."** A handful of 2025 Meta offers were reportedly in that range (multi-year, mostly stock). Posted frontier-lab research base ranges run about $250K–$850K, and the BLS median for research scientists is $140,300 [P].
4. **"Learning to code is pointless now."** AI writes much of the code, but reading, specifying, testing and debugging it is what lets you direct and trust agents. BLS still projects 10% growth for software developers 2025–2035, citing AI development as a driver [P].
5. **"AI will take all jobs next year" / "AI is all hype with no job effects."** The evidence sits between these. Entry-level employment in highly exposed occupations fell 13–16% relative to peers in the "Canaries" data, while older workers and less-exposed roles held steady or grew [P/S], and new roles (FDE, AI engineer, data-center trades) are expanding.
6. **"Wrappers are worthless."** Thin wrappers are fragile. But Cursor, built on others' models, reached a multi-billion-dollar run-rate and a $60B acquisition [S], and Harvey and Lovable built big businesses on top of foundation models. Workflow depth, distribution and data make the difference.
7. **"A $965B valuation means the company has $965B."** A valuation is the price of a small slice extrapolated to the whole company. Anthropic raised $65B at that valuation; the rest is an agreed estimate of future value.
8. **"ARR is how much money they made last year."** ARR and run-rate are speedometer readings of the current pace. Recognized revenue is the odometer. Anthropic's Q1–Q3 2026 recognized revenue ($4.8B + $11.5B + $16.8B) is far below its $65B run-rate headline because of rapid growth and method [S].
9. **"Certifications are the way in."** They help in enterprise, cloud and governance contexts. For building roles, a portfolio with evals and write-ups matters more.
10. **"Non-technical people have no place in AI."** Sales, customer success, policy, trust & safety, community engagement, education and the trades are all hiring, many at high pay [P].
11. **"AI jobs are only in San Francisco."** Lab postings span London, Dublin, Paris, Munich, Tokyo, Seoul, Sydney, Bangalore, Mumbai, Singapore, Washington DC and remote US [P]. Implementation work exists wherever businesses are.
12. **"Open-weight models are free."** The weights are free, but running them requires compute, engineering and maintenance.
13. **"Bigger funding means a better business."** Mega-rounds fund compute. Profitability depends on unit economics (OpenAI's estimated 33% gross margin; projected large negative cash flow [S]).
14. **"Adoption equals value."** 88% of organizations use AI, but only about 5% of pilots show measurable P&L impact in MIT's study [S]. Value comes from redesigning workflows.
15. **"You must master all the math before touching AI."** Top-down learning (build first, then understand) is a proven approach (fast.ai, Karpathy). Math becomes necessary at Level 5 and above, not Level 1–4.
16. **"Data-center jobs are all high-tech."** Most of the workforce building them is electricians, mechanical trades, construction and operations staff.

### 10.2 Analogies
- **The AI value chain as the electricity industry.** Chips are turbines, data centers are power plants, foundation models are the grid's electricity, apps are appliances, and services are electricians wiring homes. Most fortunes in electrification were made by those who *used* electricity in new ways, not only by generators.
- **Picks and shovels in a gold rush.** Nvidia sells the shovels. Selling to every miner can beat betting on one mine, until the rush ends.
- **Run-rate vs. revenue as speedometer vs. odometer.** Run-rate tells you how fast the car is going this minute. Recognized revenue tells you how far it actually went.
- **Valuation as the price of one house setting the street's value.** If one share sells at a price, the whole company is "worth" that times the number of shares, even though nobody could buy the whole thing at that price.
- **"Up to" deals as a gym membership "up to 365 visits."** The headline is the maximum, not what will happen.
- **Circular deals as a store lending you money to buy its products.** It's real business, but it makes "sales" look bigger than independent demand.
- **Wrapper businesses as restaurants using the same food supplier.** Everyone buys from the same wholesaler (the model). Winners differ on recipe (workflow), location (distribution), service (trust) and loyalty (switching costs). If the supplier opens its own restaurant next door, that is "the model eats your feature."
- **A moat around a castle.** Proprietary data and deep integration are water-filled moats. A clever prompt is a moat you can step over.
- **Context engineering as briefing a brilliant new hire with amnesia.** Every morning they remember nothing. What you put in the briefing folder determines how good their work is.
- **Evals as a driving test.** You don't trust a driver because they said they can drive. You test them on a fixed route with known hazards, and re-test after changes.
- **The FDE as a tailor who comes to your house.** An off-the-rack suit (the product) needs fitting to your body (your systems and data). The tailor also tells the factory which sizes to add.
- **Solutions architect as an architect versus a builder.** They design how the system will fit the customer's site. The FDE or customer team builds it.
- **A frontier lab as a film studio.** Research is the creative team, infrastructure is the soundstages and cameras, product is distribution, Applied AI is the marketing and theater partnerships, and safety is standards and practices. Most studio employees aren't directors.
- **Research engineer vs. research scientist as a chef vs. a recipe inventor in a test kitchen.** At frontier labs most people do both.
- **Kernel/performance engineer as a Formula 1 mechanic.** Small tuning gains on an enormous fleet translate into huge savings.
- **The skill tree as a video game.** You don't need to unlock every branch. Pick a path, level up, and use what you unlock. Respec is allowed.
- **T-shaped skills as a T.** The vertical bar is depth in your domain. The crossbar is AI fluency that lets you connect it to everything.
- **The jagged frontier as a coastline.** AI capability isn't a straight line. Some bays reach far inland (superhuman math), while nearby headlands remain unreached (reading an analog clock).
- **Entry-level squeeze as a ladder with missing bottom rungs.** Experienced people can still climb, but newcomers need new ways onto the ladder, such as portfolios, apprenticeships and AI-complementary skills.
- **The learning roadmap as learning a language.** First you get by as a tourist with phrases (power user), then you hold conversations (builder), then you get fluent (engineer), then you write poetry (researcher). Immersion (daily use) beats grammar books alone.

---

## Appendix: key source URLs (consolidated)

**Primary**
- Nvidia Q2 FY2027 results: https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm
- BLS Occupational Outlook pages (software developers, research scientists, data scientists, electricians), cited in §4.
- Anthropic jobs (Greenhouse): https://job-boards.greenhouse.io/anthropic (API: https://boards-api.greenhouse.io/v1/boards/anthropic/jobs?content=true)
- OpenAI jobs (Ashby): https://jobs.ashbyhq.com/openai (API: https://api.ashbyhq.com/posting-api/job-board/openai?includeCompensation=true)
- Stanford AI Index 2026: https://hai.stanford.edu/ai-index/2026-ai-index-report
- Canaries in the Coal Mine: https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine
- Microsoft "Working with AI": https://arxiv.org/abs/2507.07935
- Course pages: karpathy.ai/zero-to-hero.html; github.com/karpathy/nanochat; course.fast.ai; huggingface.co/learn; anthropic.skilljar.com; academy.openai.com; deeplearning.ai/courses; cs336.stanford.edu; matsprogram.org; arena.education; bluedot.org; 80000hours.org/career-reviews/ai-safety-researcher/; aws.amazon.com/certification/certified-ai-practitioner/; iapp.org/certify/aigp/

**Secondary (verify before print)**
- Sacra company pages: openai, anthropic, coreweave, scale-ai, mercor, harvey, lovable, sierra, perplexity (https://sacra.com/c/<name>/)
- Bloomberg on OpenAI's $70B target (Oct 9, 2026): https://www.bloomberg.com/news/articles/2026-10-09/openai-expects-70-billion-in-annualized-revenue-by-end-of-2026
- OpenAI $122B round: https://siliconangle.com/2026/03/31/openai-just-closed-record-breaking-122b-funding-round-brings-value-852b/ ; https://news.bloomberglaw.com/tech-and-telecom-law/openai-valued-at-852-billion-after-closing-122-billion-round
- Anthropic Series H (Orrick): https://www.orrick.com/en/News/2026/05/Anthropic-Raises-65B-Series-H-at-965B-Post-Money-Valuation
- Anthropic IPO timing: https://www.fool.com/investing/2026/10/20/anthropic-is-targeting-an-ipo-as-soon-as-mid-novem/ ; https://www.ifre.com/equities/2499407/anthropic-pushes-ahead-with-mid-november-ipo
- Anthropic $30B run-rate: https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth
- SpaceX IPO: https://www.fortune.com/2026/06/12/spacex-ipo-trading-first-day-live-updates-elon-musk/ ; SpaceX–Cursor: https://itwire.com/it-industry-news/deals/spacex-to-buy-cursor-for-us-60-billion ; SpaceX–xAI merger: https://www.fool.com/investing/2026/03/31/spacex-absorbed-xai-at-a-combined-125-trillion-val/
- Cursor revenue: https://dealroom.co/news/134107-cursor-tops-4b-annualized-revenue/
- Hyperscaler capex tracker: https://www.yieldtheory.app/research/hyperscaler-ai-capex-tracker-2026
- Menlo Ventures 2025 report: https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/
- MIT NANDA coverage: https://virtualizationreview.com/articles/2025/08/19/mit-report-finds-most-ai-business-investments-fail-reveals-genai-divide
- Meta talent war: https://www.entrepreneur.com/business-news/meta-makes-billion-dollar-job-offer-competing-for-ai-talent/495672 ; https://www.axios.com/2025/07/03/ai-salaries-meta-openai-zuckerberg-altman ; https://www.theregister.com/2025/06/13/meta_offers_10m_ai_researcher/
- FDE demand (India/Indeed): https://www.peoplematters.in/news/workforce-planning/demand-for-forward-deployed-engineers-jumps-19-fold-in-india-report-52770
- Levels.fyi ML engineer pages: https://www.levels.fyi/companies/meta/salaries/software-engineer/title/machine-learning-engineer (and the Apple, Google and Nvidia equivalents)

**Not verified this session (search budget exhausted).** PwC AI Jobs Barometer wage-premium figure; WEF Future of Jobs 2025 numbers; the CNBC/Lightcast FDE posting count; the OpenAI/AWS/Anthropic FDE investment figures; current EU AI Act timeline after proposed delays. Check these before the book cites them.
