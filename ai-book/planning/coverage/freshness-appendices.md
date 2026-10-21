# Freshness check: appendices and external links (web round, October 21, 2026)

Scope: Appendix A (real-world figures), C (every dated event, with focus on 2023 to October 2026), D (organizations and people, roles as of October 21, 2026), E (every resource and its address), and every external link in chapters/*.md and appendices/*.md. Appendix B was scanned: it holds only worked math examples (GPT-3 6ND, H100 ridge point) that match the checked figures, so it was not edited.

Method notes. Links were fetched with curl through the session proxy (GET, redirects followed), then rechecked with WebFetch where curl was blocked. Claims were checked against primary pages where reachable (company news pages and docs, Epoch AI's downloadable CSV datasets, NVIDIA's earnings releases, ARC Prize, METR's results file, TOP500, EIA, the EU AI Act explorer, court-tracker pages), and against Wikipedia or press only where no primary page was reachable; those rows say "reported" in the book. The shared web-search budget ran out early in this task, so verification relied on direct fetches of known source pages (many taken from planning/research). openai.com, help.openai.com, iea.org, nhtsa.gov and scmp.com block automated fetching (HTTP 403). "Reviewer knowledge" means the fact predates mid-2026, matches the long-standing public record, and was not re-fetched in this round.

## Claims

| Claim or URL | Location | Verdict | Source URL | Change made |
|---|---|---|---|---|
| Milestones 1843 to December 2022 (about 160 rows) | C | CONFIRMED | Settled history (reviewer knowledge; not re-fetched) | None |
| Rows from 2023 to 2025 not listed separately below | C | CONFIRMED | Reviewer knowledge, consistent with the public record; not re-fetched | None |
| GPT-4 about 2.1 × 10^25 FLOP; Llama 3.1 405B 3.8 × 10^25; GPT-4 about $37M, Llama 3.1 about $53M | C, A | CONFIRMED | https://epoch.ai/data/all_ai_models.csv | None |
| GPT-3 training compute "about 3.2 × 10^23" | A (Table A.8) | CORRECTED | https://epoch.ai/data/all_ai_models.csv (3.14 × 10^23) | Now "about 3.1 × 10^23", with the 6ND arithmetic and Epoch's figure |
| GPT-4.5 about 3.8 × 10^26 FLOP and about $366M (Epoch) | C, A | CONFIRMED | https://epoch.ai/data/all_ai_models.csv | None (Epoch's older 2025 page listed 2.1 × 10^26; the current database says 3.8 × 10^26) |
| Grok 3 about 3.5–4.6 × 10^26 FLOP; about $218M | A | CONFIRMED | https://epoch.ai/data/all_ai_models.csv ; https://epoch.ai/data-insights/models-over-1e25-flop | None (database 3.5 × 10^26, older page 4.6 × 10^26; the range already covers both) |
| GPT-6 Astra about 9.4 × 10^26 FLOP (Epoch); DeepSeek-V4-Pro about 9.7 × 10^24 | C, A | CONFIRMED | https://epoch.ai/data/all_ai_models.csv | None |
| GPT-6 Astra range "about 5 × 10^26 to 2 × 10^27" | A | UNVERIFIABLE | Epoch CSV has no bounds for this row | None |
| o3 METR time horizon about 2 hours | C | CONFIRMED | https://metr.org/assets/benchmark_results_1_1.yaml (119.7 minutes) | None |
| Claude Opus 4.6 METR time horizon about 12 hours | C | CONFIRMED | https://metr.org/assets/benchmark_results_1_1.yaml (718.8 minutes) | None |
| Executive Order 14365, December 11, 2025 | C | CONFIRMED | https://en.wikipedia.org/wiki/Executive_Order_14365 | None |
| New York RAISE Act signed December 19, 2025 | C | CONFIRMED | https://en.wikipedia.org/wiki/Responsible_AI_Safety_and_Education_Act | None |
| DeepSeek-V3 (December 26, 2024), R1 (January 20, 2025) | C | CONFIRMED | https://api-docs.deepseek.com/news/news260813 (news index) | None |
| OpenAI restructured October 28, 2025 (Foundation plus Group PBC) | C, D | CONFIRMED | https://en.wikipedia.org/wiki/OpenAI | None |
| Yann LeCun left Meta in November 2025; Advanced Machine Intelligence Labs | C, D | CONFIRMED | https://en.wikipedia.org/wiki/Meta_Superintelligence_Labs | None |
| California SB 53 and SB 243 take effect January 1, 2026 | C | CONFIRMED | Reviewer knowledge (statutes' operative dates); not re-fetched | None |
| Anthropic constitution (January 2026); Claude Cowork research preview (January 2026) | C | CONFIRMED | https://www.anthropic.com/constitution (file names dated Jan/Feb 2026) ; https://en.wikipedia.org/wiki/Claude_(language_model) | None |
| NVIDIA launches Vera Rubin at CES, January 2026 | C | CONFIRMED | https://www.storagereview.com/news/nvidia-launches-vera-rubin-architecture-at-ces-2026-the-vr-nvl72-rack | None |
| Microsoft Maia 200 (January 2026): 216 GB HBM3E, about 7 TB/s, 272 MB SRAM, TSMC 3 nm | C, A, D | CONFIRMED | https://www.trendforce.com/news/?p=52402 (announced January 26, 2026) | None; its "about 10 PFLOPS FP4" stays marked "reported" (not in this source) |
| Colossus 2 first GB200 cluster, reportedly about 110,000 GPUs (January 2026) | C | UNVERIFIABLE | Not reachable this round; already hedged | None |
| Boston Dynamics production electric Atlas, January 5, 2026 | C | CONFIRMED | https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/ | None |
| Meta nuclear deals up to 6.6 GW by 2035, January 9, 2026 | C | CONFIRMED | https://about.fb.com/news/2026/01/meta-nuclear-energy-projects-power-american-ai-leadership/ | None |
| US rule allows case-by-case H200 licenses, January 13–15, 2026 | C | UNVERIFIABLE | No primary page reached (BIS not fetched) | None |
| Character.AI and Google settle (January 7); Grok image scandal and bans (January) | C | CONFIRMED | https://en.wikipedia.org/wiki/2026_in_artificial_intelligence | None |
| Project Genie opens to US Google AI Ultra subscribers, January 29, 2026 | C | CONFIRMED | https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/ | None |
| SpaceX acquires xAI, February 2, 2026 ("reported all-stock deal") | C | CORRECTED | https://en.wikipedia.org/wiki/XAI_(company) | Hedge removed; "all-stock deal valuing xAI at $250 billion" |
| International AI Safety Report 2026, February 3, led by Yoshua Bengio | C, D | CONFIRMED | http://internationalaisafetyreport.org/ | None |
| Claude Opus 4.6 (February 5); Sonnet 4.6 (February 17); Gemini 3.1 Pro (February 19); GPT-5.3-Codex (February 5) | C | CONFIRMED | https://en.wikipedia.org/wiki/Claude_(language_model) ; https://ai.google.dev/gemini-api/docs/changelog ; https://epoch.ai/data/all_ai_models.csv | None |
| Gemini 3 Deep Think upgrade, February 12, 2026 | C | UNVERIFIABLE | No source reached | None |
| GPT-4o retired from ChatGPT, February 13, 2026 | C | CONFIRMED | https://en.wikipedia.org/wiki/2026_in_artificial_intelligence | None |
| New Delhi Declaration "endorsed by about 86–89 countries" | C | CORRECTED | https://www.deccanchronicle.com/nation/current-affairs/india-ai-impact-summit88-countries-endorse-new-delhi-declaration-on-ai-1938895 | Now "(Feb 21) endorsed by 86 countries and two international organizations"; US endorsement confirmed |
| ChatGPT about 900 million weekly active users, February 2026 | C | CONFIRMED | https://en.wikipedia.org/wiki/ChatGPT | None |
| Anthropic distillation-attack report (February 23); RSP v3.0 (February 24) | C | CONFIRMED | https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks ; https://www.anthropic.com/news/responsible-scaling-policy-v3 | None |
| GPT-5.4 (March 5); top US and Chinese models 2.7% apart on Arena (AI Index 2026) | C | CONFIRMED | https://epoch.ai/data/all_ai_models.csv ; https://hai.stanford.edu/ai-index/2026-ai-index-report | None |
| Mississippi reportedly approves ~1.2 GW gas plant for xAI's Southaven site | C | UNVERIFIABLE | https://www.selc.org/news/xai-built-an-illegal-power-plant-to-power-its-data-center/ (27 turbines, about 495 MW, no approval mentioned) | None; already "reportedly" |
| GTC 2026 (March 16): Groq 3 LPX racks of 256 LPUs, Feynman preview; Groq 3 LPU about 500 MB SRAM, 150 TB/s, 1.2 PFLOPS FP8 | C, A | CONFIRMED | https://www.eetimes.com/gtc-2026-keynote-long-live-the-inference-king/ | None |
| White House framework urging preemption, March 20, 2026 | C | CONFIRMED | https://rollcall.com/2026/03/20/white-house-ai-framework-calls-for-preemption-of-state-laws/ | None |
| Sora app shutdown announced March 24, 2026 | C | CONFIRMED | https://en.wikipedia.org/wiki/2026_in_artificial_intelligence | Added closure dates (app April 26; API September 24), matching Chapters 16 and 47 |
| ARC-AGI-3 launch March 25: frontier AI 0.51%, humans 100% | C | CONFIRMED | https://arcprize.org/blog/arc-agi-3-launch | None |
| Gemma 4 (April 2); Mythos Preview and Glasswing (April 7, "thousands of high-severity vulnerabilities"); Opus 4.7 (April 16); π0.7 (April 16) | C | CONFIRMED | https://epoch.ai/data/all_ai_models.csv ; https://www.anthropic.com/glasswing ; https://www.pi.website/ | None |
| Anthropic–Google–Broadcom, multiple GW of TPUs from 2027 (April 6); Anthropic–Amazon up to 5 GW (April 20) | C | CONFIRMED | https://www.anthropic.com/news/google-broadcom-partnership-compute ; https://www.anthropic.com/news/anthropic-amazon-compute | None |
| DeepMind Frontier Safety Framework v3.1 adds tracked capability levels, April 17 | C | CONFIRMED | https://deepmind.google/blog/strengthening-our-frontier-safety-framework/ | None |
| TPU 8t and 8i (April 22) and their specs; Ironwood 192 GB, 7.37 TB/s, 4,614 TFLOPS FP8, 9,216-chip pods; Trillium 32 GB, 918 TFLOPS | C, A, D | CONFIRMED | https://en.wikipedia.org/wiki/Tensor_Processing_Unit | None (TPU 8t's "128 MB on-chip SRAM" not in that source: unverified, left) |
| GPT-5.5 (April 23); GPT-5.5 Instant default from May 5 | C | CONFIRMED | https://en.wikipedia.org/wiki/GPT-5.5 | None |
| DeepSeek-V4 preview April 24: 1.6T total, 49B active, 1M context | C, A | CONFIRMED | https://api-docs.deepseek.com/news/news260424 ; https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro (MIT license, FP4 experts plus FP8, more than 32T tokens) | None |
| Colorado repeals and replaces its AI Act, May 14, 2026 | C | CONFIRMED | https://www.skadden.com/insights/publications/2026/06/colorado-repeals-and-replaces-its-ai-act | None |
| Gemini 3.5 family at Google I/O, May 19 | C | CONFIRMED | https://ai.google.dev/gemini-api/docs/changelog (3.5 Flash GA May 19) | None |
| "May 2026: NVIDIA Rubin enters full production" | C | CORRECTED | https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027 (May 20: no production claim) ; https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027 (Aug 26: "in full production") | May row removed; "says Vera Rubin is in full production" added to the August 26 row |
| Opus 4.8 (May 28); Fable 5 and Mythos 5 (June 9); Sonnet 5 (June 30) | C | CONFIRMED | https://en.wikipedia.org/wiki/Claude_(language_model) ; https://epoch.ai/data/all_ai_models.csv | None |
| Mythos-class access "briefly suspended ... then restored" (June 12) | C | CORRECTED | https://en.wikipedia.org/wiki/Claude_(language_model) (quotes Anthropic) ; https://en.wikipedia.org/wiki/2026_in_artificial_intelligence | Added dates: restored for over 100 US organizations June 26, fully June 30, Fable 5 back July 1; marked "as reported" |
| GPT-5.6 (Luna, Terra, Sol) dated "June 2026" | C | CORRECTED | https://en.wikipedia.org/wiki/GPT-5.6 ; https://epoch.ai/data/all_ai_models.csv | June row now says "limited preview (June 26)"; new row July 9 for the release |
| TOP500 June 2026: LineShine 2,198.4 PFlop/s; El Capitan 1,809 | C, A | CONFIRMED | https://top500.org/lists/top500/2026/06/ | None |
| Gemini Omni Flash preview, June 30 | C | CONFIRMED | https://ai.google.dev/gemini-api/docs/changelog | None |
| Anthropic (June 1, reported) and OpenAI (confirmed June 8) file for IPOs; Alphabet $80 billion equity program (priced at about $85 billion) | C | ADDED | https://en.wikipedia.org/wiki/Anthropic ; https://en.wikipedia.org/wiki/OpenAI ; https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow | New June row (Chapters 43, 44, 61, 64 mention these) |
| SpaceX IPO June 12, 2026, about $75 billion raised | C | ADDED | https://en.wikipedia.org/wiki/XAI_(company) (citing CNBC) | New row, marked "reported" (Chapters 43, 61, 64) |
| SpaceX agrees to buy Cursor (June 16, about $60 billion, closed August 14) | C, D | ADDED | https://en.wikipedia.org/wiki/XAI_(company) | New C row; D's Cursor row now says the deal closed in August 2026 |
| ChatGPT Work (July 2026); apps renamed plugins (July 2026) | C | CONFIRMED | https://en.wikipedia.org/wiki/ChatGPT | Rename added to the July row (Chapters 25 and 28) |
| xAI rebranded SpaceXAI (July 2026) | C, D | ADDED | https://en.wikipedia.org/wiki/XAI_(company) | Added to the July row; D row updated |
| Microsoft "added another gigawatt of capacity this quarter" | C | CONFIRMED | https://www.fool.com/earnings/call-transcripts/2026/08/07/microsoft-msft-q4-2026-earnings-call-transcript/ (call on July 29) | Call date added |
| Waymo fully driverless in Las Vegas, July 8 | C | CONFIRMED | https://electrek.co/2026/07/08/waymo-driverless-las-vegas-four-new-cities/ | None |
| S&P cuts Oracle to BBB-, July 9; FactSet close to $800 billion 2026 capex, July 23 | C | CONFIRMED | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow | None |
| GPT-5.6 released July 9 | C | ADDED | https://en.wikipedia.org/wiki/GPT-5.6 | New row |
| Meta Hyperion to scale to 5 GW, July 13 | C | CONFIRMED | https://www.datacenterknowledge.com/data-center-construction/meta-s-5-gw-hyperion-campus-signals-ai-s-shift-into-utility-territory | None |
| Kimi K3, July 16: 2.8T total, 104B active, MXFP4 quantization-aware training | C, A, D | CONFIRMED | https://epoch.ai/data/all_ai_models.csv ; https://huggingface.co/moonshotai/Kimi-K3 | None |
| Bartz v. Anthropic final approval, July 20, 2026 | C | CONFIRMED | https://authorsguild.org/news/court-grants-final-approval-anthropic-copyright-settlement/ | None |
| "Gemini 3.5 Pro reportedly never gets a general release" | C | CORRECTED | https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/ ; https://ai.google.dev/gemini-api/docs/changelog | Now "reported delayed, and still not generally released by October" (Google called it delayed, not cancelled) |
| Claude Opus 5, July 24 | C | CONFIRMED | https://en.wikipedia.org/wiki/Claude_(language_model) | None |
| EU Digital Omnibus on AI (Regulation 2026/1744) in force July 27; Annex III high-risk rules moved to December 2, 2027; intimate-deepfake ban from December 2, 2026 | C | CONFIRMED | https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/ | None (row already updated by another editor) |
| IMO 2026 perfect-score claims, none certified | C | UNVERIFIABLE | scmp.com source blocked (403) | None; already hedged |
| MCP specification 2026-07-28 with twelve-month deprecation window | C | ADDED | https://modelcontextprotocol.io/specification/2026-07-28/changelog | New row (Chapters 28 and 31) |
| Gemini Robotics 2, ER 2, On-Device 2 (July 30) | C | CONFIRMED | https://ai.google.dev/gemini-api/docs/changelog ; https://deepmind.google/models/gemini-robotics/ | None |
| Zoox receives first US exemption for a purpose-built robotaxi (July 30) | C | HEDGED | nhtsa.gov blocked (403); no primary page reached | "reportedly" and "commercial" added |
| FRONTIER Act introduced in late July | C | CONFIRMED | https://www.theregreview.org/2026/10/07/knapp-the-hidden-costs-of-ai-preemption/ | None |
| EU enforcement powers over general-purpose AI from August 2, 2026 | C | CONFIRMED | https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/ | None |
| OpenAI cannot rule out "Critical" cyber capability (August 2026) | C | UNVERIFIABLE | openai.com blocked (403) | None; already "press reports" |
| Zoox paid rides in Las Vegas, August 10 | C | HEDGED | https://lasvegassun.com/news/2026/aug/06/free-rides-no-more-zoox-robotaxi-service-to-begin/ (headline only, paywalled) | "(reported)" added |
| Meta Muse Glimmer, 30B open weights, August 10 | C | ADDED | https://en.wikipedia.org/wiki/Meta_Superintelligence_Labs ; https://epoch.ai/data/all_ai_models.csv | Added to the August 10 row (Chapters 24 and 30) |
| DeepSeek-V4-Pro GA (August 13); Gemini 3.7 Flash (August 13) | C | CONFIRMED | https://api-docs.deepseek.com/news/news260813 ; https://ai.google.dev/gemini-api/docs/changelog | None |
| Qwen3.8 family dated "Aug 2026" | C | CORRECTED | https://epoch.ai/data/all_ai_models.csv | Now "Jul–Aug 2026": Qwen3.8-Max July 19, 2.4T open model August 8 |
| Stanford "Canaries" update: about 19% below trend, descriptive | C | CONFIRMED | https://digitaleconomy.stanford.edu/news/canariesaug26/ (August 12) | None |
| NVIDIA quarterly revenue $96.2 billion, August 26 | C | CONFIRMED | https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027 | Added "says Vera Rubin is in full production" |
| DOJ "supports fair use for AI training", September 1 | C | HEDGED | https://www.aivortex.io/legal/ai-case-law/nyt-v-openai/ (September 1) ; https://ailawsuittracker.com/cases/new-york-times-v-openai/ (September 2) | Now "Sep 1–2 ... files a statement of interest arguing that copying works to train AI can be fair use ... (sources differ on the day)" |
| Gemini 3.8 Flash, September 2 | C | CONFIRMED | https://ai.google.dev/gemini-api/docs/changelog | None |
| GPT-6 Astra, September 3, first pretraining run on more than 100,000 GPUs | C | CONFIRMED | https://en.wikipedia.org/wiki/GPT-6 ; https://community.openai.com/t/introducing-gpt-6-astra-the-most-intelligent-and-aligned-model-in-the-world/1394703 | None |
| GPT-6 Astra "access first for cyber defenders" | C | CORRECTED | https://en.wikipedia.org/wiki/GPT-6 (limited preview Sep 3, paid users Sep 4) | Now "released first as a limited preview, then to paid users" |
| GPT-6 Astra 62.7% (standard harness) and 99.9% "with a custom harness" on ARC-AGI-3 | C | CORRECTED | https://arcprize.org/blog/astra (September 3) | Dated September 3; harness described as ARC Prize's "Provider Adapter" harness |
| METR stopped updating its time-horizon page (September 8) | C | ADDED | https://metr.org/time-horizons/ | New row (Chapters 28, 60, 66) |
| Claude Fable 5.1 and Mythos 5.1 ("sources give Sep 1 or Sep 15") | C | CORRECTED | https://www.anthropic.com/news (post dated September 15) ; https://en.wikipedia.org/wiki/Claude_(language_model) and Epoch CSV (September 1) | Dated September 15 per Anthropic, noting trackers that list September 1 |
| Grok 4.7 (September 21); Opus 5.5 and GPT-6 Sol and Luna (September 22); Sonnet 5.5 (September 28); GPT-6.1 Sol (September 29); Gemini 4 Argon (around September 30, Epoch) | C, D | CONFIRMED | https://epoch.ai/data/all_ai_models.csv ; https://www.anthropic.com/news ; https://community.openai.com/t/announcing-gpt-6-sol-and-gpt-6-luna-in-the-api-codex-and-chatgpt/1399925 | None |
| Opus 5.5 "tops several capability indices" | C | CONFIRMED | https://artificialanalysis.ai/leaderboards/models (Opus 5.5 first at 58) | None |
| First US construction permit for a BWRX-300 (TVA Clinch River), September 28 | C | CONFIRMED | https://www.gevernova.com/news/press-releases (listing dated September 28; dateline September 29) | None |
| Thomson Reuters v. Ross: Third Circuit, not fair use, September 29 | C | CONFIRMED | https://www.musicbusinessworldwide.com/us-appeals-court-rejects-fair-use-defense-over-ai-training-as-thomson-reuters-wins-copyright-case-backed-by-riaa-and-nmpa/ (filed under seal September 29) ; https://www.plagiarismtoday.com/2026/10/01/understanding-the-reuters-ross-ai-ruling/ | None |
| Claude Frontier Academy: $100 million, 10,000 engineers, October 2 | C | CONFIRMED | https://www.anthropic.com/news/claude-frontier-academy | None |
| US Defense Department stopped using Anthropic products, October 5 | C | ADDED | https://en.wikipedia.org/wiki/Anthropic (citing BBC News) ; https://en.wikipedia.org/wiki/2026_in_artificial_intelligence | New row, "reported" (Chapter 60) |
| "Project Glasswing adds a tiered Cyber Verification Program" (October 6) | C | CORRECTED | https://www.anthropic.com/news/cyber-verification-program | Now: Anthropic expands the existing Cyber Verification Program into three access tiers and folds Project Glasswing into it |
| Claude Haiku 5.5, October 7 | C | CONFIRMED | https://www.anthropic.com/news | None |
| GPT-6 reaches all ChatGPT users October 7–8 | C | CONFIRMED | https://en.wikipedia.org/wiki/GPT-6 (paid October 7, free October 8) | None |
| Gemini 4 Argon GA in API October 13; Pi API beta October 13 | C | CONFIRMED | https://ai.google.dev/gemini-api/docs/changelog ; https://www.pi.website/ | None |
| Meta Muse Wonder and Wonder Full, October 13 (per press reports) | C, D | CONFIRMED | https://artificialanalysis.ai/leaderboards/models (Muse Wonder Full listed at 56); October 13 date rests on press reports only | None; date already hedged "per press reports" |
| China proposes export controls on 40 technologies, October 16 | C | UNVERIFIABLE | No source reached | None; another editor had already added "reportedly" |
| DeepSeek V4.1 Flash update, October 17 | C | CONFIRMED | https://api-docs.deepseek.com/news/news261017 (V4.1-Flash first released September 10) | None |
| Epoch: 95 large AI data centers, about 14.2 GW of IT, about 14.8 million H100e; New Carlisle 1,037 MW (largest); Colossus 2 946 MW, about 1.1 million H100e | C, A | CONFIRMED | https://epoch.ai/data/data_centers/data_centers.csv (95 sites, 14,203 MW, 14.75 million H100e) | None |
| Mistral Large 4 preview (October 2026) | C, D | CONFIRMED | https://en.wikipedia.org/wiki/Mistral_AI (preview October 6; open weights promised for end of October) | Date October 6 added |
| xAI's unit "rebranded SpaceXSI" (October 2026) | C, D | HEDGED | https://en.wikipedia.org/wiki/XAI_(company) (Musk said October 4 it would rename; X account renamed "SpaceX Super Intelligence" October 10) | C and D now say it was reported to be renaming itself SpaceX Super Intelligence (SpaceXSI); D adds the July SpaceXAI rebrand |
| Anthropic reportedly targeting a mid-November listing | C | ADDED | https://www.fool.com/investing/2026/10/20/anthropic-is-targeting-an-ipo-as-soon-as-mid-novem/ | Added to the October row, "reported" (Chapters 43 and 64) |
| H100, H200, B200, B300, A100, V100, MI300X, MI355X, MI455X/Helios, Trainium3/Trn3 UltraServer, Cerebras WSE-3 specs | A | CONFIRMED | Vendor announcements (reviewer knowledge; not re-fetched) | None |
| GB300 NVL72: 1,080 PFLOPS dense FP4, about 20 TB HBM | A | CONFIRMED | https://www.nvidia.com/en-us/data-center/gb300-nvl72/ | None |
| Vera Rubin NVL72: 2,520 PFLOPS NVFP4 training, 20.7 TB HBM4; Rubin 35/50 PFLOPS NVFP4, 17.5 FP8, 288 GB, 19.2 TB/s; NVLink 6 3 TB/s (3.6 at launch) | A | CONFIRMED | https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/ ; https://www.storagereview.com/news/nvidia-launches-vera-rubin-architecture-at-ces-2026-the-vr-nvl72-rack | None |
| Rubin "336 billion transistors" and "4 PFLOPS BF16" | A | UNVERIFIABLE | Not on the NVIDIA pages fetched | None |
| Energy per query (Google 0.24 Wh; OpenAI 0.34 Wh; Epoch 0.3, 2.5 and 40 Wh); LBNL 176 TWh, 4.4%; IEA 415 TWh, 1.5%, 945 TWh by 2030; Ireland 22% | A | CONFIRMED | Published 2024–2025 sources (reviewer knowledge; iea.org blocks fetching) | None |
| US residential electricity 17.3¢ (2025), 18.2¢ (2026), 18.7¢ (2027) | A | CONFIRMED | https://www.eia.gov/outlooks/steo/report/elec_coal_renew.php (October 2026 STEO) | None |
| GPU rental ranges (H100 $2.69–4.29; H200 $3.59–5.29; B200 $5.98–7.99; B300 $6.94–8.99; A100 $1.19–2.79) | A | CONFIRMED | https://www.runpod.io/pricing ; https://lambda.ai/pricing | None |
| API prices: Haiku 5.5 from $0.10/$0.50; Sonnet 5.5 $2/$10; Opus 5.5 $4/$20, fast mode $8/$40; Fable 5.1 $10/$50 | A | CONFIRMED | https://platform.claude.com/docs/en/about-claude/pricing | None |
| Gemini 4 Argon $2/$10 through November 30, 2026, then $4/$20; GPT-6 Astra $10/$50 | A | CONFIRMED | https://ai.google.dev/gemini-api/docs/pricing ; https://community.openai.com/t/introducing-gpt-6-astra-the-most-intelligent-and-aligned-model-in-the-world/1394703 | None |
| JLL and Cushman & Wakefield building costs per MW; JLL 103 GW global capacity | A | UNVERIFIABLE | Not checked (search budget exhausted) | None |
| Flagship model lists for OpenAI, Anthropic, Google DeepMind, Meta, DeepSeek, Qwen, Moonshot, Z.ai (GLM-5.3), Grok 4.7 | D | CONFIRMED | https://epoch.ai/data/all_ai_models.csv ; https://www.anthropic.com/news ; https://ai.google.dev/gemini-api/docs/changelog | None |
| Xiaomi MiMo-V2.6-Pro, top open-weight model on Artificial Analysis | D | CONFIRMED | https://artificialanalysis.ai/models/open-source (index 46, first) | None |
| StepFun "Step 5" | D | CORRECTED | https://artificialanalysis.ai/models/open-source ; Epoch CSV ("Step 5 Preview", September 18) | Now "Step 5 (preview, September 2026)" |
| Mistral founders, 2023, Large 3 Apache-2.0, Medium 3.5 | D | CONFIRMED | https://en.wikipedia.org/wiki/Mistral_AI | None |
| LMArena "began as Chatbot Arena at UC Berkeley" | D | CORRECTED | https://arena.ai/blog/lmarena-is-now-arena/ ; https://en.wikipedia.org/wiki/Arena_(AI_platform) | Row renamed "Arena (formerly LMArena)", renamed January 2026, arena.ai |
| Alexandr Wang "leads TBD Lab" | D | CORRECTED | https://en.wikipedia.org/wiki/Meta_Superintelligence_Labs | Now Meta's chief AI officer leading MSL and its TBD Lab |
| Helen Toner "policy researcher at CSET" | D | CORRECTED | https://en.wikipedia.org/wiki/Helen_Toner | Now interim executive director of CSET |
| David Sacks "White House AI and crypto adviser from 2025" | D | CORRECTED | https://en.wikipedia.org/wiki/David_Sacks | Now: stepped down March 2026, remains PCAST co-chair |
| Sam Altman CEO; Greg Brockman president; Jakub Pachocki chief scientist | D | CONFIRMED | https://en.wikipedia.org/wiki/OpenAI | None |
| Dario Amodei CEO; Daniela Amodei president; Jared Kaplan chief science officer; Jan Leike, Chris Olah, Amanda Askell roles | D | CONFIRMED | https://en.wikipedia.org/wiki/Anthropic | None |
| Mustafa Suleyman leads Microsoft AI | D | CONFIRMED | https://en.wikipedia.org/wiki/Mustafa_Suleyman | None |
| Meta Superintelligence Labs formed mid-2025 with FAIR and TBD Lab | D | CONFIRMED | https://en.wikipedia.org/wiki/Meta_Superintelligence_Labs | None |
| Percy Liang and Tatsunori Hashimoto teach CS336 (Spring 2026, five assignments) | D, E | CONFIRMED | https://cs336.stanford.edu/ | None |
| Other organization and people rows in D (long-standing facts) | D | CONFIRMED | Reviewer knowledge; not individually re-fetched | None |
| Anthropic Academy course titles | E | CONFIRMED | https://anthropic.skilljar.com/ | None |
| OpenAI Academy tracks (Apply AI at Work, Build with AI, Lead AI Adoption) | E | CONFIRMED | https://academy.openai.com/ | None |
| MATS: 12 weeks, $1,250 a week, 631 alumni, 75% in alignment, transparency or security | E | CONFIRMED | https://www.matsprogram.org/ | None |
| Anthropic Fellows: four months, $3,850 a week | E | UNVERIFIABLE | https://alignment.anthropic.com/2025/anthropic-fellows-program-2026/ (four months and about $15,000 a month of compute confirmed; weekly stipend not stated) | None |
| nanochat: GPT-2-class model in about 2 hours on 8 H100s for about $48 | E | CONFIRMED | https://github.com/karpathy/nanochat | None |
| Gandalf (Lakera) password game | E, ch31, ch58 | CORRECTED | https://play.lakera.ai/agent-breaker (every gandalf.lakera.ai path 308-redirects there; the page's code still contains the old password levels but routes to Agent Breaker) | Now Lakera's Gandalf: Agent Breaker at play.lakera.ai; text notes that the old gandalf.lakera.ai address forwards there |

## Links

Every http(s) URL in chapters/*.md and appendices/*.md (excluding localhost and example.com placeholders in code samples) plus every address in Appendix E's Link column, fetched on October 21, 2026. Location is the file(s) where the address appears. "UNVERIFIABLE" here means the host answered but refused automated clients (HTTP 403/429) or the session policy blocked the request; none of these is a dead link, and all are left unchanged.

| Claim or URL | Location | Verdict | Source URL | Change made |
|---|---|---|---|---|
| https://claude.ai/new | 04-internet-and-cloud.md | UNVERIFIABLE | https://claude.ai/new | login page; 403 to automated clients; unchanged |
| https://api.anthropic.com/v1/messages | 04-internet-and-cloud.md, 26-apis.md | CONFIRMED | https://api.anthropic.com/v1/messages | code example; POST-only endpoint answers GET with 404 as expected; none |
| https://api.github.com/repos/pytorch/pytorch | 04-internet-and-cloud.md | UNVERIFIABLE | https://api.github.com/repos/pytorch/pytorch | code example; GitHub API blocked by this session's policy, not by GitHub; unchanged |
| https://playground.tensorflow.org | 12-neural-networks-from-scratch.md, 13-training-deep-networks.md, E-resources.md | CONFIRMED | https://playground.tensorflow.org | resolves (HTTP 200); none |
| https://teachablemachine.withgoogle.com | 12-neural-networks-from-scratch.md, 14-cnns-rnns-embeddings.md, E-resources.md | CONFIRMED | https://teachablemachine.withgoogle.com | resolves (HTTP 200); none |
| https://colab.research.google.com | 12-neural-networks-from-scratch.md, 13-training-deep-networks.md, 14-cnns-rnns-embeddings.md, 15-the-transformer.md, 20-post-training.md, 21-reasoning-models.md, 48-rl-games-planning.md, E-resources.md | CONFIRMED | https://colab.research.google.com | resolves (HTTP 200); none |
| https://huggingface.co | 13-training-deep-networks.md, 15-the-transformer.md | CONFIRMED | https://huggingface.co | resolves (HTTP 200); none |
| https://projector.tensorflow.org | 14-cnns-rnns-embeddings.md | CONFIRMED | https://projector.tensorflow.org | resolves (HTTP 200); none |
| https://poloclub.github.io/cnn-explainer/ | 14-cnns-rnns-embeddings.md | CONFIRMED | https://poloclub.github.io/cnn-explainer/ | resolves (HTTP 200); none |
| https://tiktokenizer.vercel.app | 15-the-transformer.md | CONFIRMED | https://tiktokenizer.vercel.app | resolves (HTTP 200); none |
| https://aistudio.google.com | 15-the-transformer.md, E-resources.md | CONFIRMED | https://aistudio.google.com | resolves (HTTP 200), redirects to https://aistudio.google.com/welcome; none |
| https://huggingface.co/spaces/Xenova/the-tokenizer-playground | 15-the-transformer.md | CONFIRMED | https://huggingface.co/spaces/Xenova/the-tokenizer-playground | resolves (HTTP 200); none |
| https://poloclub.github.io/transformer-explainer/ | 15-the-transformer.md | CONFIRMED | https://poloclub.github.io/transformer-explainer/ | resolves (HTTP 200); none |
| https://bbycroft.net/llm | 15-the-transformer.md, E-resources.md | CONFIRMED | https://bbycroft.net/llm | resolves (HTTP 200); none |
| https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt | 19-pretraining-and-scaling.md | CONFIRMED | https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt | resolves (HTTP 200); none |
| https://www.anthropic.com/constitution | 20-post-training.md | CONFIRMED | https://www.anthropic.com/constitution | resolves (HTTP 200); none |
| https://model-spec.openai.com/ | 20-post-training.md | CONFIRMED | https://model-spec.openai.com/ | resolves (HTTP 200); none |
| https://lmarena.ai | 20-post-training.md, E-resources.md | DEAD LINK FIXED | https://arena.ai/blog/lmarena-is-now-arena/ | 301 redirect to arena.ai (LMArena renamed Arena, Jan 28, 2026). Replaced with arena.ai in E, D (row renamed), ch20 and ch24 (definition, exercise, Going deeper). |
| https://arcprize.org | 21-reasoning-models.md | CONFIRMED | https://arcprize.org | resolves (HTTP 200); none |
| https://www.gutenberg.org/cache/epub/1342/pg1342.txt | 26-apis.md | CONFIRMED | https://www.gutenberg.org/cache/epub/1342/pg1342.txt | resolves (HTTP 200); none |
| https://geocoding-api.open-meteo.com/v1/search | 28-tools-and-agents.md | CONFIRMED | https://geocoding-api.open-meteo.com/v1/search | code example; 200 with ?name= parameter; none |
| https://api.open-meteo.com/v1/forecast | 28-tools-and-agents.md | CONFIRMED | https://api.open-meteo.com/v1/forecast | code example; 429 without parameters, works with them; none |
| https://ultralytics.com/images/bus.jpg | 45-computer-vision.md | CONFIRMED | https://ultralytics.com/images/bus.jpg | resolves (HTTP 200), redirects to a GitHub release asset (image downloads); none |
| https://contentcredentials.org/verify | 47-generative-media.md | CONFIRMED | https://contentcredentials.org/verify | resolves (HTTP 200), redirects to https://verify.contentauthenticity.org/; none |
| https://poloclub.github.io/diffusion-explainer/ | 47-generative-media.md | CONFIRMED | https://poloclub.github.io/diffusion-explainer/ | resolves (HTTP 200); none |
| https://deepmind.google/models/veo/ | 47-generative-media.md | CONFIRMED | https://deepmind.google/models/veo/ | resolves (HTTP 200); none |
| https://deepmind.google/models/genie/ | 47-generative-media.md | CONFIRMED | https://deepmind.google/models/genie/ | resolves (HTTP 200); none |
| https://c2pa.org | 47-generative-media.md | CONFIRMED | https://c2pa.org | resolves (HTTP 200); none |
| https://contentauthenticity.org | 47-generative-media.md | CONFIRMED | https://contentauthenticity.org | resolves (HTTP 200); none |
| https://www.copyright.gov/ai/ | 47-generative-media.md | CONFIRMED | https://www.copyright.gov/ai/ | resolves (HTTP 200); none |
| https://huggingface.co/docs/diffusers | 47-generative-media.md | CONFIRMED | https://huggingface.co/docs/diffusers | resolves (HTTP 200), redirects to https://huggingface.co/docs/diffusers/index; none |
| https://jalammar.github.io/illustrated-stable-diffusion/ | 47-generative-media.md | CONFIRMED | https://jalammar.github.io/illustrated-stable-diffusion/ | resolves (HTTP 200); none |
| https://www.nvidia.com/en-us/ai/cosmos/ | 47-generative-media.md | CONFIRMED | https://www.nvidia.com/en-us/ai/cosmos/ | resolves (HTTP 200); none |
| https://lichess.org | 48-rl-games-planning.md | UNVERIFIABLE | https://lichess.org | 403 to automated clients; unchanged |
| http://incompleteideas.net/book/the-book-2nd.html | 48-rl-games-planning.md | CONFIRMED | http://incompleteideas.net/book/the-book-2nd.html | 200 over http (https has a self-signed certificate; E lists the bare address, which browsers fall back to http for); none |
| https://www.redblobgames.com/pathfinding/a-star/introduction.html | 48-rl-games-planning.md | CONFIRMED | https://www.redblobgames.com/pathfinding/a-star/introduction.html | resolves (HTTP 200); none |
| https://huggingface.co/learn/deep-rl-course | 48-rl-games-planning.md | CONFIRMED | https://huggingface.co/learn/deep-rl-course | resolves (HTTP 200), redirects to https://huggingface.co/learn/deep-rl-course/unit0/introduction; none |
| https://spinningup.openai.com | 48-rl-games-planning.md, E-resources.md | CONFIRMED | https://spinningup.openai.com | resolves (HTTP 200), redirects to https://spinningup.openai.com/en/latest/; none |
| http://www.incompleteideas.net/IncIdeas/BitterLesson.html | 48-rl-games-planning.md | CONFIRMED | http://www.incompleteideas.net/IncIdeas/BitterLesson.html | resolves (HTTP 200); none |
| https://anthropic.skilljar.com | E-resources.md | CONFIRMED | https://anthropic.skilljar.com | resolves (HTTP 200); none |
| https://academy.openai.com | E-resources.md | CONFIRMED | https://academy.openai.com | resolves (HTTP 200); none |
| https://deeplearning.ai/courses | E-resources.md | CONFIRMED | https://deeplearning.ai/courses | resolves (HTTP 200), redirects to https://www.deeplearning.ai/courses; none |
| https://elementsofai.com | E-resources.md | CONFIRMED | https://elementsofai.com | resolves (HTTP 200), redirects to https://www.elementsofai.com/; none |
| https://grow.google | E-resources.md | CONFIRMED | https://grow.google | resolves (HTTP 200); none |
| https://khanacademy.org | E-resources.md | CONFIRMED | https://khanacademy.org | resolves (HTTP 200), redirects to https://www.khanacademy.org/; none |
| https://youtube.com/@AndrejKarpathy | E-resources.md | CONFIRMED | https://youtube.com/@AndrejKarpathy | resolves (HTTP 200), redirects to https://www.youtube.com/@AndrejKarpathy; none |
| https://3blue1brown.com | E-resources.md | CONFIRMED | https://3blue1brown.com | resolves (HTTP 200), redirects to https://www.3blue1brown.com/; none |
| https://platform.openai.com/tokenizer | E-resources.md | UNVERIFIABLE | https://platform.openai.com/tokenizer | 403 to automated clients; tool documented in OpenAI help center; unchanged |
| https://poloclub.github.io/transformer-explainer | E-resources.md | CONFIRMED | https://poloclub.github.io/transformer-explainer | resolves (HTTP 200); none |
| https://gandalf.lakera.ai | E-resources.md | DEAD LINK FIXED | https://play.lakera.ai/agent-breaker | 308 redirect: every gandalf.lakera.ai path now forwards to Lakera's Gandalf: Agent Breaker. E row, ch31 Try it and ch58 exercise updated to play.lakera.ai and describe the new game; old address noted. |
| https://quickdraw.withgoogle.com | E-resources.md | CONFIRMED | https://quickdraw.withgoogle.com | resolves (HTTP 200); none |
| https://oneusefulthing.org | E-resources.md | DEAD LINK FIXED | https://www.oneusefulthing.org/ | Apex domain has no DNS record (proxy 502); www works. E link changed to www.oneusefulthing.org. |
| https://deeplearning.ai/the-batch | E-resources.md | CONFIRMED | https://deeplearning.ai/the-batch | resolves (HTTP 200), redirects to https://www.deeplearning.ai/the-batch; none |
| https://hai.stanford.edu/ai-index | E-resources.md | CONFIRMED | https://hai.stanford.edu/ai-index | resolves (HTTP 200); none |
| https://promptingguide.ai | E-resources.md | CONFIRMED | https://promptingguide.ai | resolves (HTTP 200), redirects to https://www.promptingguide.ai/; none |
| https://platform.claude.com/docs | E-resources.md | CONFIRMED | https://platform.claude.com/docs | resolves (HTTP 200), redirects to https://platform.claude.com/docs/en/home; none |
| https://developers.openai.com | E-resources.md | CONFIRMED | https://developers.openai.com | resolves (HTTP 200); none |
| https://pair.withgoogle.com/guidebook | E-resources.md | CONFIRMED | https://pair.withgoogle.com/guidebook | resolves (HTTP 200); none |
| https://kaggle.com/learn | E-resources.md | CONFIRMED | https://kaggle.com/learn | resolves (HTTP 200); none |
| https://zapier.com | E-resources.md | CONFIRMED | https://zapier.com | resolves (HTTP 200); none |
| https://make.com | E-resources.md | CONFIRMED | https://make.com | resolves (HTTP 200), redirects to https://www.make.com/; none |
| https://n8n.io | E-resources.md | CONFIRMED | https://n8n.io | resolves (HTTP 200); none |
| https://lovable.dev | E-resources.md | UNVERIFIABLE | https://lovable.dev | 403 to automated clients; unchanged |
| https://replit.com | E-resources.md | CONFIRMED | https://replit.com | resolves (HTTP 200); none |
| https://bolt.new | E-resources.md | CONFIRMED | https://bolt.new | resolves (HTTP 200); none |
| https://lmstudio.ai | E-resources.md | CONFIRMED | https://lmstudio.ai | resolves (HTTP 200); none |
| https://ollama.com | E-resources.md | CONFIRMED | https://ollama.com | resolves (HTTP 200); none |
| https://modelcontextprotocol.io | E-resources.md | CONFIRMED | https://modelcontextprotocol.io | resolves (HTTP 200), redirects to https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro; none |
| https://simonwillison.net | E-resources.md | CONFIRMED | https://simonwillison.net | resolves (HTTP 200); none |
| https://hamel.dev | E-resources.md | CONFIRMED | https://hamel.dev | resolves (HTTP 200); none |
| https://reddit.com/r/LocalLLaMA | E-resources.md | CONFIRMED | https://reddit.com/r/LocalLLaMA | resolves (HTTP 200), redirects to https://www.reddit.com/r/LocalLLaMA/; none |
| https://meetup.com | E-resources.md | CONFIRMED | https://meetup.com | resolves (HTTP 200), redirects to https://www.meetup.com/; none |
| https://cs50.harvard.edu/python | E-resources.md | CONFIRMED | https://cs50.harvard.edu/python | resolves (HTTP 200); none |
| https://missing.csail.mit.edu | E-resources.md | CONFIRMED | https://missing.csail.mit.edu | resolves (HTTP 200); none |
| https://skills.github.com | E-resources.md | CONFIRMED | https://skills.github.com | resolves (HTTP 200); none |
| https://sqlbolt.com | E-resources.md | CONFIRMED | https://sqlbolt.com | resolves (HTTP 200); none |
| https://huggingface.co/learn | E-resources.md | CONFIRMED | https://huggingface.co/learn | resolves (HTTP 200); none |
| https://maven.com | E-resources.md | CONFIRMED | https://maven.com | resolves (HTTP 200); none |
| https://anthropic.com/engineering | E-resources.md | CONFIRMED | https://anthropic.com/engineering | resolves (HTTP 200), redirects to https://www.anthropic.com/engineering; none |
| https://github.com/openai/openai-cookbook | E-resources.md | CONFIRMED | https://github.com/openai/openai-cookbook | confirmed by WebFetch; active, not archived; none |
| https://ai.google.dev | E-resources.md | CONFIRMED | https://ai.google.dev | redirects through a Google sign-in check, then loads docs; none |
| https://owasp.org | E-resources.md | CONFIRMED | https://owasp.org | resolves (HTTP 200); none |
| https://latent.space | E-resources.md | CONFIRMED | https://latent.space | resolves (HTTP 200), redirects to https://www.latent.space/; none |
| https://huyenchip.com | E-resources.md | CONFIRMED | https://huyenchip.com | resolves (HTTP 200); none |
| https://eugeneyan.com | E-resources.md | CONFIRMED | https://eugeneyan.com | resolves (HTTP 200); none |
| https://mlops.community | E-resources.md | CONFIRMED | https://mlops.community | resolves (HTTP 200); none |
| https://ai.engineer | E-resources.md | CONFIRMED | https://ai.engineer | resolves (HTTP 200); none |
| https://discuss.huggingface.co | E-resources.md | CONFIRMED | https://discuss.huggingface.co | resolves (HTTP 200); none |
| https://course.fast.ai | E-resources.md | CONFIRMED | https://course.fast.ai | resolves (HTTP 200); none |
| https://karpathy.ai/zero-to-hero.html | E-resources.md | CONFIRMED | https://karpathy.ai/zero-to-hero.html | resolves (HTTP 200); none |
| https://github.com/karpathy/nanochat | E-resources.md | CONFIRMED | https://github.com/karpathy/nanochat | confirmed by WebFetch (curl blocked by session GitHub policy); README: GPT-2-class model ~2 h on 8xH100 for ~$48; none |
| https://cs336.stanford.edu | E-resources.md | CONFIRMED | https://cs336.stanford.edu | resolves (HTTP 200); none |
| https://web.stanford.edu/class/cs224n | E-resources.md | CONFIRMED | https://web.stanford.edu/class/cs224n | resolves (HTTP 200); none |
| https://cs231n.stanford.edu | E-resources.md | CONFIRMED | https://cs231n.stanford.edu | resolves (HTTP 200); none |
| https://introtodeeplearning.com | E-resources.md | CONFIRMED | https://introtodeeplearning.com | resolves (HTTP 200); none |
| https://udlbook.github.io/udlbook | E-resources.md | CONFIRMED | https://udlbook.github.io/udlbook | resolves (HTTP 200); none |
| https://d2l.ai | E-resources.md | CONFIRMED | https://d2l.ai | resolves (HTTP 200); none |
| https://deeplearningbook.org | E-resources.md | DEAD LINK FIXED | https://www.deeplearningbook.org/ | Apex domain fails TLS (certificate does not cover it); www works. Changed in E, ch12 and ch14. |
| https://mml-book.github.io | E-resources.md | CONFIRMED | https://mml-book.github.io | resolves (HTTP 200); none |
| https://probml.github.io/pml-book | E-resources.md | CONFIRMED | https://probml.github.io/pml-book | resolves (HTTP 200); none |
| https://incompleteideas.net/book/the-book-2nd.html | E-resources.md | CONFIRMED | https://incompleteideas.net/book/the-book-2nd.html | bare address in E; https certificate is self-signed, http works; left unchanged; none |
| https://rlhfbook.com | E-resources.md | CONFIRMED | https://rlhfbook.com | resolves (HTTP 200); none |
| https://arxiv.org | E-resources.md | CONFIRMED | https://arxiv.org | resolves (HTTP 200); none |
| https://huggingface.co/papers | E-resources.md | CONFIRMED | https://huggingface.co/papers | resolves (HTTP 200); none |
| https://lilianweng.github.io | E-resources.md | CONFIRMED | https://lilianweng.github.io | resolves (HTTP 200); none |
| https://distill.pub | E-resources.md | CONFIRMED | https://distill.pub | resolves (HTTP 200); none |
| https://sebastianraschka.com | E-resources.md | CONFIRMED | https://sebastianraschka.com | resolves (HTTP 200); none |
| https://interconnects.ai | E-resources.md | CONFIRMED | https://interconnects.ai | resolves (HTTP 200), redirects to https://www.interconnects.ai/; none |
| https://jack-clark.net | E-resources.md | CONFIRMED | https://jack-clark.net | 403 to curl; confirmed by WebFetch (Import AI 477, Oct 19, 2026); none |
| https://dwarkesh.com | E-resources.md | CONFIRMED | https://dwarkesh.com | resolves (HTTP 200), redirects to https://www.dwarkesh.com/; none |
| https://kaggle.com | E-resources.md | CONFIRMED | https://kaggle.com | resolves (HTTP 200); none |
| https://eleuther.ai | E-resources.md | CONFIRMED | https://eleuther.ai | resolves (HTTP 200); none |
| https://forums.fast.ai | E-resources.md | CONFIRMED | https://forums.fast.ai | resolves (HTTP 200); none |
| https://reddit.com/r/MachineLearning | E-resources.md | CONFIRMED | https://reddit.com/r/MachineLearning | resolves (HTTP 200), redirects to https://www.reddit.com/r/MachineLearning/; none |
| https://github.com/gpu-mode/lectures | E-resources.md | CONFIRMED | https://github.com/gpu-mode/lectures | confirmed by WebFetch; none |
| https://triton-lang.org | E-resources.md | CONFIRMED | https://triton-lang.org | resolves (HTTP 200); none |
| https://docs.nvidia.com/cuda | E-resources.md | CONFIRMED | https://docs.nvidia.com/cuda | resolves (HTTP 200); none |
| https://nvidia.com | E-resources.md | CONFIRMED | https://nvidia.com | resolves (HTTP 200), redirects to https://www.nvidia.com/en-us/; none |
| https://huggingface.co/spaces/nanotron/ultrascale-playbook | E-resources.md | CONFIRMED | https://huggingface.co/spaces/nanotron/ultrascale-playbook | resolves (HTTP 200); none |
| https://jax-ml.github.io/scaling-book | E-resources.md | CONFIRMED | https://jax-ml.github.io/scaling-book | resolves (HTTP 200); none |
| https://electricaltrainingalliance.org | E-resources.md | CONFIRMED | https://electricaltrainingalliance.org | resolves (HTTP 200); none |
| https://apprenticeship.gov | E-resources.md | CONFIRMED | https://apprenticeship.gov | resolves (HTTP 200), redirects to https://www.apprenticeship.gov/; none |
| https://uptimeinstitute.com | E-resources.md | CONFIRMED | https://uptimeinstitute.com | resolves (HTTP 200); none |
| https://epoch.ai | E-resources.md | CONFIRMED | https://epoch.ai | resolves (HTTP 200); none |
| https://iea.org | E-resources.md | UNVERIFIABLE | https://iea.org | 403 to automated clients; unchanged |
| https://lbl.gov | E-resources.md | UNVERIFIABLE | https://lbl.gov | www.lbl.gov answers 403 to automated clients; unchanged |
| https://epri.com | E-resources.md | DEAD LINK FIXED | https://www.epri.com/ | Apex domain resets the connection; www works. E link changed. |
| https://sec.gov/edgar | E-resources.md | CONFIRMED | https://sec.gov/edgar | 403 to curl; www.sec.gov/edgar confirmed by WebFetch; none |
| https://datacenterdynamics.com | E-resources.md | UNVERIFIABLE | https://datacenterdynamics.com | 403 to automated clients; unchanged |
| https://datacentermap.com | E-resources.md | UNVERIFIABLE | https://datacentermap.com | 429 rate limit to automated clients; unchanged |
| https://hotchips.org | E-resources.md | CONFIRMED | https://hotchips.org | resolves (HTTP 200); none |
| https://semianalysis.com | E-resources.md | CONFIRMED | https://semianalysis.com | 403 to curl; confirmed by WebFetch; none |
| https://acquired.fm | E-resources.md | CONFIRMED | https://acquired.fm | resolves (HTTP 200), redirects to https://www.acquired.fm/; none |
| https://bluedot.org | E-resources.md | CONFIRMED | https://bluedot.org | resolves (HTTP 200); none |
| https://arena.education | E-resources.md | CONFIRMED | https://arena.education | resolves (HTTP 200), redirects to https://www.arena.education/; none |
| https://matsprogram.org | E-resources.md | CONFIRMED | https://matsprogram.org | resolves (HTTP 200), redirects to https://www.matsprogram.org/; none |
| https://anthropic.com/careers | E-resources.md | CONFIRMED | https://anthropic.com/careers | resolves (HTTP 200), redirects to https://www.anthropic.com/careers; none |
| https://80000hours.org | E-resources.md | CONFIRMED | https://80000hours.org | resolves (HTTP 200); none |
| https://iapp.org | E-resources.md | CONFIRMED | https://iapp.org | resolves (HTTP 200); none |
| https://neelnanda.io | E-resources.md | CONFIRMED | https://neelnanda.io | resolves (HTTP 200), redirects to https://www.neelnanda.io/; none |
| https://nist.gov | E-resources.md | CONFIRMED | https://nist.gov | resolves (HTTP 200), redirects to https://www.nist.gov/; none |
| https://artificialintelligenceact.eu | E-resources.md | CONFIRMED | https://artificialintelligenceact.eu | resolves (HTTP 200); none |
| https://oecd.ai | E-resources.md | CONFIRMED | https://oecd.ai | resolves (HTTP 200), redirects to https://oecd.ai/en/; none |
| https://internationalaisafetyreport.org | E-resources.md | CONFIRMED | https://internationalaisafetyreport.org | resolves (HTTP 200); none |
| https://anthropic.com | E-resources.md | CONFIRMED | https://anthropic.com | resolves (HTTP 200), redirects to https://www.anthropic.com/; none |
| https://openai.com | E-resources.md | UNVERIFIABLE | https://openai.com | host answers 403 to automated clients (Cloudflare); well-known site, unchanged |
| https://deepmind.google | E-resources.md | CONFIRMED | https://deepmind.google | resolves (HTTP 200); none |
| https://model-spec.openai.com | E-resources.md | CONFIRMED | https://model-spec.openai.com | resolves (HTTP 200); none |
| https://anthropic.com/constitution | E-resources.md | CONFIRMED | https://anthropic.com/constitution | resolves (HTTP 200), redirects to https://www.anthropic.com/constitution; none |
| https://incidentdatabase.ai | E-resources.md | CONFIRMED | https://incidentdatabase.ai | resolves (HTTP 200); none |
| https://transformer-circuits.pub | E-resources.md | CONFIRMED | https://transformer-circuits.pub | resolves (HTTP 200); none |
| https://neuronpedia.org | E-resources.md | CONFIRMED | https://neuronpedia.org | resolves (HTTP 200), redirects to https://www.neuronpedia.org/; none |
| https://metr.org | E-resources.md | CONFIRMED | https://metr.org | resolves (HTTP 200); none |
| https://aisi.gov.uk | E-resources.md | CONFIRMED | https://aisi.gov.uk | resolves (HTTP 200), redirects to https://www.aisi.gov.uk/; none |
| https://alignmentforum.org | E-resources.md | CONFIRMED | https://alignmentforum.org | resolves (HTTP 200), redirects to https://www.alignmentforum.org/; none |
| https://lesswrong.com | E-resources.md | CONFIRMED | https://lesswrong.com | resolves (HTTP 200), redirects to https://www.lesswrong.com/; none |
| https://governance.ai | E-resources.md | CONFIRMED | https://governance.ai | resolves (HTTP 200), redirects to https://www.governance.ai/; none |
| https://cset.georgetown.edu | E-resources.md | CONFIRMED | https://cset.georgetown.edu | resolves (HTTP 200); none |
| https://rand.org | E-resources.md | CONFIRMED | https://rand.org | resolves (HTTP 200), redirects to https://www.rand.org:443/; none |
| https://iaps.ai | E-resources.md | CONFIRMED | https://iaps.ai | resolves (HTTP 200), redirects to https://www.iaps.ai/; none |
| https://adalovelaceinstitute.org | E-resources.md | CONFIRMED | https://adalovelaceinstitute.org | resolves (HTTP 200), redirects to https://www.adalovelaceinstitute.org/; none |
| https://ainowinstitute.org | E-resources.md | CONFIRMED | https://ainowinstitute.org | resolves (HTTP 200); none |
| https://80000hours.org/podcast | E-resources.md | CONFIRMED | https://80000hours.org/podcast | resolves (HTTP 200); none |
| https://stratechery.com | E-resources.md | CONFIRMED | https://stratechery.com | 403 to curl; confirmed by WebFetch; none |
| https://lennysnewsletter.com | E-resources.md | CONFIRMED | https://lennysnewsletter.com | resolves (HTTP 200), redirects to https://www.lennysnewsletter.com/; none |
| https://anthropic.com/research/the-anthropic-economic-index | E-resources.md | CONFIRMED | https://anthropic.com/research/the-anthropic-economic-index | resolves (HTTP 200), redirects to https://www.anthropic.com/research/the-anthropic-economic-index; none |
| https://artificialanalysis.ai | E-resources.md | CONFIRMED | https://artificialanalysis.ai | resolves (HTTP 200); none |
| https://menlovc.com | E-resources.md | CONFIRMED | https://menlovc.com | resolves (HTTP 200); none |
| https://sacra.com | E-resources.md | CONFIRMED | https://sacra.com | resolves (HTTP 200); none |
| https://bls.gov/ooh | E-resources.md | CONFIRMED | https://bls.gov/ooh | 403 to curl; www.bls.gov/ooh/ confirmed by WebFetch; none |
| https://levels.fyi | E-resources.md | CONFIRMED | https://levels.fyi | resolves (HTTP 200), redirects to https://www.levels.fyi/; none |
| https://job-boards.greenhouse.io/anthropic | E-resources.md | CONFIRMED | https://job-boards.greenhouse.io/anthropic | resolves (HTTP 200); none |
| https://jobs.ashbyhq.com/openai | E-resources.md | CONFIRMED | https://jobs.ashbyhq.com/openai | resolves (HTTP 200); none |
| https://startupschool.org | E-resources.md | CONFIRMED | https://startupschool.org | resolves (HTTP 200), redirects to https://www.startupschool.org/; none |
| https://ycombinator.com/library | E-resources.md | CONFIRMED | https://ycombinator.com/library | resolves (HTTP 200), redirects to https://www.ycombinator.com/library; none |

## Summary

- Claims checked: 135 table rows (many rows bundle several related facts), plus two block rows covering about 270 settled timeline entries from 1843 to 2025 that were checked against the established record without re-fetching. Verdicts: CONFIRMED 92, CORRECTED 18, HEDGED 4, UNVERIFIABLE 11, ADDED 10.
- Links checked: 175 unique addresses (39 http(s) URLs found in chapters and appendices, 136 further addresses from Appendix E's Link column). CONFIRMED 160, UNVERIFIABLE (live but bot-blocked or policy-blocked) 10, DEAD LINK FIXED 5.
- Links fixed: 5 addresses, changed in 12 places: lmarena.ai to arena.ai (Appendix E, Appendix D row, Chapter 20, Chapter 24 three places); gandalf.lakera.ai to play.lakera.ai with the game's new name (Appendix E, Chapter 31, Chapter 58); oneusefulthing.org to www.oneusefulthing.org (E); deeplearningbook.org to www.deeplearningbook.org (E, Chapters 12 and 14); epri.com to www.epri.com (E). No resource was removed.
- Main factual fixes: Rubin "full production" date (May row unsupported; moved to NVIDIA's August 26 report); GPT-5.6 release moved from June to July 9 (June 26 limited preview); Fable 5.1 and Mythos 5.1 dated September 15 per Anthropic; Cyber Verification Program row rewritten (three tiers, Glasswing folded in); GPT-6 Astra access wording; ARC-AGI-3 harness name and date; New Delhi Declaration count; Gemini 3.5 Pro "never released" softened to delayed; Qwen3.8 dates; Commerce-directive restoration dates; DOJ filing date hedged; Zoox and SpaceXSI hedged; D roles updated for Alexandr Wang, Helen Toner and David Sacks; LMArena renamed Arena; GPT-3 compute 3.1 × 10^23.
- Timeline entries added (events the chapters mention): June IPO filings and Alphabet's equity program; SpaceX IPO (June 12); SpaceX–Cursor deal (June 16); SpaceXAI rebrand and ChatGPT plugins rename (July); GPT-5.6 (July 9); MCP 2026-07-28 specification; Muse Glimmer (August 10); METR stops updating its time-horizon page (September 8); Defense Department stops using Anthropic products (October 5); Anthropic's reported mid-November IPO target; Sora closure dates.
- Unresolved: OpenAI's August "Critical" cyber notice, IMO 2026 claims, China's October 16 proposal, the January H200 rule, Gemini 3 Deep Think (February 12), Southaven approval, Anthropic Fellows stipend, Rubin transistor count, JLL and Cushman cost figures: no reachable source this round (most already carry "reportedly"). Chapters still call the site "LMArena" in running text (Chapters 9, 16, 20, 24, 65); that is historically accurate but chapter owners may want "Arena (formerly LMArena)". Chapter 7 says NVIDIA called Rubin "in full production" at CES in January 2026; the CES coverage fetched here says only that the chips were back from fabrication, so that sentence deserves a check by Chapter 7's owner.
- Validation: validate.py clean on Appendices A, C, D and E (C: 1/1 diagram valid; A, D, E have no diagrams); check.py OK on edited Chapters 12, 14, 20, 24, 31 and 58.
