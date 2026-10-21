# Freshness check, Part VI (Chapters 32–37): compute, chips, memory, networking, distributed training

Web fact-check run on October 21, 2026, against vendor pages, keynote and press releases, SEC filings, US government releases and Epoch AI data. Every At the frontier box in Chapters 32–37 and every row of the chip spec tables (Tables 32.1, 32.2, 32.4, 32.7, 33.5, 33.6, 34.1, 34.3, 34.4, 35.1–35.7, 35.10, 36.1 and the Huawei roadmap table) was checked. Each chip-name correction was then searched for across the whole book, including Chapters 1, 2 and 38–44 and the appendices, and the other mentions were fixed to match.

Limits of this pass: the shared WebSearch budget ran out partway through. After that, checks used direct fetches of known primary URLs only. Items that could not be reached that way are marked UNVERIFIABLE and were left unchanged. Long-settled historical specs (V100, A100, TPU v1–v5, MI300X and MI325X, the Copilot+ 40 TOPS rule, DeepSeek-V3's GPU-hours, the Horowitz energy table) were not re-fetched and are not listed below.

## Results

| Claim | Chapter and section | Verdict | Source URL | Change made |
|---|---|---|---|---|
| NVIDIA Q2 FY2027 (quarter ended Jul 26, 2026): revenue $96.2B (+106%), data center $89.0B (+117%), gross margin 75.0%, Q3 outlook $108B ±2% with no China data-center compute revenue assumed | Ch 35 "The size of the business"; Ch 32 Watch out; Ch 35 "Who holds what" | CONFIRMED | https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm | None |
| Vera Rubin "ramping into full production" with racks at CoreWeave, Google Cloud, Azure, OCI and Nebius | Ch 32 At the frontier (Rubin platform) | CONFIRMED | same as above | None |
| Vera Rubin production shipments began in the quarter starting Jul 27, 2026 | Ch 32 At the frontier (Rubin platform) | ADDED | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm | Added one sourced clause |
| Rubin platform is six chips: Vera CPU, Rubin GPU, NVLink 6 switch, ConnectX-9, BlueField-4, Spectrum-6 | Ch 32 and Ch 34 At the frontier boxes | CONFIRMED | https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer | None |
| Rubin per GPU: 50 PF NVFP4 sparse (inference), 35 PF NVFP4 dense, 17.5 PF FP8, 4 PF BF16, 288 GB HBM4, 19.2 TB/s on the product page vs 22 TB/s at launch, 336B transistors, two dies | Tables 32.2, 32.4, 32.7, 33.5, 33.7, 35.1, 35.2, 35.7; Ch 33 At the frontier (HBM4) | CONFIRMED | https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/ ; https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/ | None |
| Rubin made on TSMC N3 | Table 32.7; Ch 32 "CUDA changes the game"; Table 35.1 and Figure 35 timeline; Ch 36 "Transistor shapes" and Table 36.1; Ch 2 At the frontier; Appendix A | HEDGED | NVIDIA pages above do not name the node; widely reported only | Marked "reported" or "reportedly" in all seven places |
| Vera Rubin NVL72: 3,600 PF sparse / 2,520 PF dense NVFP4, 1,260 PF FP8, 288 PF BF16, 20.7 TB HBM4, 1,400 TB/s, NVLink 216 TB/s (3 TB/s per GPU) now vs 260 TB/s at launch, 36 × 88 Olympus cores, up to 54 TB LPDDR5X | Tables 32.2, 34.3, 35.4; Table 32.7 (Vera row) | CONFIRMED | https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/ ; https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer | None |
| Vera Rubin rack power "not given" | Table 34.3 | CONFIRMED | https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/ (page gives only about 40,000 GPUs per 100 MW AI factory) | None |
| GB300 NVL72: 1,080 PF dense / 1,440 PF sparse FP4; 720 PF FP8 and 360 PF BF16 "as listed" | Table 34.3 and the "Two traps" paragraph | CORRECTED | https://www.nvidia.com/en-us/data-center/gb300-nvl72/ (footnote: all tensor figures with sparsity unless noted); https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/ (5 PF dense FP8 per GPU) | FP8 and BF16 labeled sparse; added dense values (about 360 PF FP8, 180 PF BF16) |
| GB300 NVL72: 20 TB HBM3E, up to 576 TB/s, 130 TB/s NVLink, 2,592 Grace cores | Tables 34.1, 34.3 | CONFIRMED | https://www.nvidia.com/en-us/data-center/gb300-nvl72/ | None |
| B300 (Blackwell Ultra): about 15 PF dense FP4, 288 GB HBM3E (12-high), 8 TB/s, two dies | Tables 32.7, 33.5, 33.7, 34.1, 35.1, 35.7 | CONFIRMED | https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/ | None |
| B200: 192 GB HBM3E, 8 TB/s, 208B transistors, NVLink 5 at 1.8 TB/s | Table 35.1; Ch 34 "Chiplets" | CONFIRMED | same as above; https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/ | None |
| H100 SXM: about 989 TF BF16 and 1,979 TF FP8 dense, 80 GB, 3.35 TB/s, 700 W | Tables 32.1, 32.4, 32.7, 33.4, 33.5, 35.1, 35.2 | CONFIRMED | https://www.nvidia.com/en-us/data-center/h100/ (sparse figures are exactly double) | None |
| H200: 141 GB HBM3E, 4.8 TB/s, same compute as H100 | Tables 32.7, 33.5, 33.7, 35.1 | CONFIRMED | https://www.nvidia.com/en-us/data-center/h200/ | None |
| Rubin Ultra (Kyber, 2H 2027): GTC 2025 plan of 15 EF FP4 inference, 5 EF FP8, about 600 kW per rack | Table 35.1; Table 34.4 | CONFIRMED | https://www.networkworld.com/article/3848394/nvidia-details-its-gpu-cpu-and-system-roadmap-for-the-next-three-years.html | None |
| GTC 2026 update to Rubin Ultra: Kyber "NVL144", 144 packages of four compute dies, about 1 TB HBM4E each | Table 35.1 | ADDED | https://tech.yahoo.com/computing/articles/nvidia-updates-data-center-roadmap-204256462.html | Added as "reported" |
| Feynman (2028): die stacking, custom HBM, Rosa CPU, new LPU; TSMC A16 | Ch 32, 33, 34 At the frontier boxes; Table 35.1; Ch 36 At the frontier (leading edge) | CONFIRMED (A16 stays "reported": NVIDIA has not named the node) | https://tech.yahoo.com/computing/articles/nvidia-updates-data-center-roadmap-204256462.html | None |
| Groq 3 LPU: 500 MB SRAM, 150 TB/s, 256 per LPX rack | Tables 32.7, 35.7, Ch 37 inference-chip table; Ch 32 Table 32.8 | CONFIRMED | https://www.nvidia.com/en-us/data-center/lpx/ | None |
| Groq 3 LPU: about 1.2 PFLOPS FP8 | Tables 32.7, 35.7; Ch 37 inference-chip table | HEDGED | https://www.theregister.com/2026/03/19/nvidia_lpx_deep_dive/ (NVIDIA's LPX page lists no FP8 figure) | Marked "(reported)"; Table 32.7 caption updated |
| LPX + Vera Rubin up to 35× throughput per megawatt | Ch 33 At the frontier (industry product lines); Ch 37 table | CONFIRMED (vendor projection) | https://www.nvidia.com/en-us/data-center/lpx/ | None |
| NVIDIA–Groq (Dec 2025): non-exclusive license; price about $20B | Table 35.10; Ch 32 "Inference specialists"; Table 35.8 | CONFIRMED (license type in 10-Q; price still reported) | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm | None |
| Spectrum-6 co-packaged optics reaching customer sites in mid-2026 | Ch 36 At the frontier (packaging) | CONFIRMED | https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm | None |
| Vera Rubin trains MoE models with one-quarter of Blackwell's GPUs | Ch 37 At the frontier (parallelism) | CONFIRMED (vendor claim) | https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer | None |
| H200 China sales under 1% of data-center revenue | Ch 35 "China and export controls"; Ch 36 "Geopolitics, part 1" | CONFIRMED | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm | None |
| "NVIDIA said in March 2026 it had received licenses, but China reportedly restricted imports" | Ch 36 "Geopolitics, part 1" and Figure 36.10; Ch 35 "China and export controls" | CORRECTED | same 10-Q ("Beginning in February 2026, the USG granted licenses ... such sales were restricted by the PRC government") | February, not March; China's restriction attributed to NVIDIA's filings instead of "reportedly" |
| MI355X: 288 GB HBM3E, 8 TB/s, 10.1 PF MXFP4, 1,400 W | Tables 32.7, 33.5, 35.3, 35.7 | CONFIRMED | https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html | None |
| MI355X "20.1 PF sparse" FP4 | Table 35.3 | CORRECTED | same AMD page (no sparse FP4 figure; 10.1 PF sparse is the FP8 figure); https://www.theregister.com/2025/06/12/amd_mi355x/ | Removed; added AMD's 185B transistor count |
| MI455X: 432 GB HBM4, about 40 PF FP4, about 20 PF FP8, 3.6 TB/s scale-up, TSMC 2 nm and 3 nm chiplets | Tables 32.7, 33.1, 33.5, 35.3, 35.7; Ch 33 At the frontier (HBM4) | CONFIRMED | https://www.amd.com/en/products/accelerators/instinct/mi400.html ; https://www.theregister.com/2026/01/07/mi500x_amd_ai/ | None |
| MI455X bandwidth 19.6 TB/s | Tables 33.5, 35.7; Table 35.4 and Helios paragraph; Ch 33 At the frontier | HEDGED | https://www.amd.com/en/products/rackscale-solutions/helios.html (lists both 23.3 and 19.6 TB/s); https://www.amd.com/en/products/accelerators/instinct/mi400.html (23.3) | Ranges 19.6–23.3 TB/s; ridge point about 1,717–2,041; Helios rack about 1.4–1.7 PB/s |
| Helios: 72 MI455X, 2.9 EF FP4, 1.4 EF FP8, 31 TB HBM4, 260 TB/s scale-up over UALink-over-Ethernet, Venice with up to 256 Zen 6 cores, Vulcano NICs; ramps from 2H 2026 | Ch 35 AMD section; Ch 34 "Other ways to scale up"; Table 34.4; Ch 38 At the frontier | CONFIRMED | https://www.amd.com/en/products/rackscale-solutions/helios.html ; https://ir.amd.com/news-events/press-releases/detail/1295/amd-reports-second-quarter-2026-financial-results | None |
| MI430X ships in 2026 | Table 35.3 | CORRECTED | https://www.amd.com/en/products/accelerators/instinct/mi400.html ("expected to be available in 2027") | Year changed to AMD-expected 2027; added 432 GB HBM4 and 288 TFLOPS FP64 |
| MI440X in an 8-GPU server; MI500 in 2027 (CDNA 6, 2 nm, HBM4E) | Table 35.3 | CONFIRMED (reported) | https://www.theregister.com/2026/01/07/mi500x_amd_ai/ | None |
| OpenAI–AMD 6 GW, first 1 GW of MI450 in 2H 2026 | Ch 35 "How the moat is being crossed"; Table 35.10 | CONFIRMED | https://www.amd.com/en/products/rackscale-solutions/helios.html (partnership listed); AMD Q2 2026 release above | None |
| Meta–AMD up to 6 GW (Feb 2026); first gigawatt a custom MI450-based GPU in Helios, shipping 2H 2026 | Table 35.10 | ADDED | https://ir.amd.com/news-events/press-releases/detail/1279/ | New row |
| Anthropic–AMD up to 2 GW of MI450 in Helios (Jul 22, 2026), first gigawatt 1H 2027, AMD equity investment up to $5B | Table 35.10 | ADDED | https://newsroom.amd.com/news/amd-anthropic-strategic-partnership/ | New row; caption now "September 2025 to July 2026" |
| Ironwood: 4,614 TF FP8, 192 GB HBM3E, 7.37 TB/s, pods of 256 or 9,216 chips, 42.5 EF per pod | Tables 32.7, 33.5, 34.1, 34.4, 35.5, 35.7; Ch 32 "Fixed-function chips" | CONFIRMED | https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/ | None |
| Trillium (v6e): 918 TF BF16, 32 GB HBM, 256-chip pods | Ch 32 "Fixed-function chips"; Table 35.5 | CONFIRMED | https://docs.cloud.google.com/tpu/docs/v6e | None |
| TPU 8t: 12.6 PF FP4, 216 GB HBM, 6.5 TB/s, 128 MB SRAM, 3D torus, 9,600-chip superpods with 2 PB HBM | Tables 32.7, 33.5, 34.4, 35.5, 35.7; Ch 32 and Ch 33 At the frontier | CONFIRMED | https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive ; https://www.storagereview.com/news/google-announces-tpu-8t-sunfish-and-tpu-8i-zebrafish | None |
| TPU 8i: 10.1 PF FP4, 288 GB HBM, 8.6 TB/s, 384 MB SRAM (3× Ironwood), Boardfly, 1,152 chips, up to 80% better performance per dollar | Tables 32.7, 32.8, 33.5, 34.4, 35.5, 35.7, Ch 37 inference table; Ch 32, 33 At the frontier | CONFIRMED | https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive | None |
| Virgo fabric links more than 134,000 TPU 8t chips | Ch 37 At the frontier (parallelism) | CONFIRMED | same Google deep dive | None |
| Google: JAX and Pathways scale to more than a million TPU chips in one training cluster | Ch 32, 34, 37 At the frontier boxes | CONFIRMED | same Google deep dive | None |
| TPU 8 design partners (Broadcom; MediaTek for 8i) | Table 35.6 | UNVERIFIABLE | Google's pages do not say; reported only | None (already labeled "reported") |
| Trainium3: 3 nm, 144 GB HBM3E, 4.9 TB/s, about 2.5 PF MXFP8; 144 per UltraServer, 362 PF, 20.7 TB, 706 TB/s; GA December 2025 | Tables 32.7, 33.5, 34.4, 35.7; Ch 35 Amazon | CONFIRMED | https://press.aboutamazon.com/2025/12/trainium3-ultraservers-now-available-enabling-customers-to-train-and-deploy-ai-models-faster-at-lower-cost ; https://aws.amazon.com/ai/machine-learning/trainium/ | None |
| Trainium "UltraClusters of up to a million chips" | Ch 34 At the frontier (million chips); Ch 35 Amazon | CORRECTED (wording) | https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap (thousands of UltraServers, up to 1 million Trainium3); AWS page says "hundreds of thousands" | Ch 35 reworded to AWS's actual claim; Ch 34 box left as is |
| Trainium4 will support NVLink Fusion | Ch 35 Amazon; Ch 34 NVLink Fusion definition | CONFIRMED | same TechCrunch article | None |
| Project Rainier: about 500,000 Trainium2 chips at launch | Ch 35 Amazon; Table 35.10; Ch 37 At the frontier (scale) | CONFIRMED | https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster | Ch 37 "reportedly" changed to "according to Amazon" |
| Anthropic–Amazon (Apr 20, 2026): up to 5 GW, nearly 1 GW of Trainium2/3 by end-2026, more than $100B over ten years "reported" | Ch 35 Amazon; Table 35.10; Ch 42 | CORRECTED (attribution) | https://www.anthropic.com/news/anthropic-amazon-compute | Now attributed to Anthropic's own statement in Ch 35 (two places) and Ch 42 |
| Maia 200 specs: TSMC 3 nm, 216 GB HBM3E at 7 TB/s, 272 MB SRAM, more than 10 PF FP4 and 5 PF FP8, 750 W, more than 140B transistors, Ethernet scale-up to 6,144 chips; deployed in Iowa with Arizona next | Tables 32.7, 33.6, 33.10, 34.4, 35.7, 36.1, Ch 37 inference table; Ch 34 and Ch 35 text; Appendix A | CORRECTED | https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ | Removed the "(reported)" hedges (primary source exists); "about 10" became "more than 10"; added 750 W and transistor count; "then Arizona" became "with Arizona next" |
| Maia 200 design partner Marvell | Table 35.6 | UNVERIFIABLE | none reachable | None (already "per industry reports") |
| OpenAI–Broadcom: 10 GW, Ethernet, 2H 2026 to 2029 | Ch 35 "Microsoft, Meta, OpenAI and Intel"; Table 35.10 | CONFIRMED | https://www.maginative.com/article/openai-and-broadcom-to-co-design-custom-ai-chips-deploy-10-gw-by-2029/ | None |
| Whether OpenAI–Broadcom chips were deployed by October 2026 | Ch 35 | UNVERIFIABLE | none reachable after the search budget ran out | None (book already says "not confirmed") |
| Intel Crescent Island (160 GB LPDDR5X, sampling 2H 2026); Intel investment in SambaNova cleared May 2026 | Ch 35 "Microsoft, Meta, OpenAI and Intel"; Table 35.8 | UNVERIFIABLE | Intel newsroom URL returned 404 | None |
| Cerebras WSE-3: 46,225 mm², 4 trillion transistors, 900,000 cores, 44 GB SRAM, about 125 PF | Tables 32.7, 35.7, 35.8; Ch 32 definition | CONFIRMED (Cerebras now quotes 250 PF for the newer WSE-3T) | https://www.cerebras.ai/chip ; https://www.cerebras.ai/press-release/cerebras-unveils-cs-4-up-to-30-times-faster-than-gpu-based-solutions-3347356 | None |
| Cerebras CS-4 (Aug 18, 2026): three WSE-3T wafers per rack, 750 PF (vendor) | Table 35.8 | ADDED | https://www.cerebras.ai/press-release/cerebras-unveils-cs-4-up-to-30-times-faster-than-gpu-based-solutions-3347356 | Replaced the vague "vendor lists newer systems" note |
| OpenAI–Cerebras 750 MW plus a 1.25 GW option | Table 35.10; Table 35.8 | UNVERIFIABLE | CNBC returned 403 | None (already "reported") |
| HBM4 (JEDEC, April 2025): 2,048-bit, up to 2 TB/s per stack, 4–16 high, up to 64 GB | Table 33.6 | CONFIRMED | https://en.wikipedia.org/wiki/High_Bandwidth_Memory | None |
| HBM3: 819 GB/s per stack at 6.4 Gb/s | Table 33.6 | CONFIRMED | same | None |
| HBM4E samples in 2026 | Table 33.6 | CONFIRMED (Samsung shipped 12-high HBM4E to customers in May 2026) | same | None |
| HBM3E users list | Table 33.6 | ADDED | https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ | Added Maia 200 |
| TSMC N2 (first nanosheet node) in volume production since 4Q 2025; A16 adds backside power | Ch 36 "Transistor shapes"; Ch 36 At the frontier (leading edge) | CONFIRMED | https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm | None |
| ASML is the only EUV supplier; an EUV tool costs about $180M; Reuters (Dec 2025) reported a Chinese prototype EUV system | Ch 36 At the frontier (EUV); Ch 36 cost table and choke-point table | CONFIRMED | https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography | None |
| Huawei roadmap (Huawei Connect 2025): 950PR Q1 2026 on Huawei's own HBM; 950DT Q4 2026 | Ch 36 Huawei table | CONFIRMED | https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech | None |
| Huawei Connect 2026: 960DT pulled forward to Q1 2027, 960PR to Q3 2027, 970 in 2028, 980 in 2029; Atlas 960E SuperPoD (4,096 NPUs, 8 EF FP8, 1 PB HBM); Atlas 950 in commercial use; 256,000-card SuperCluster; up to 512,000 NPUs (1 million with multi-rail) | Ch 36 Huawei table; Ch 34 At the frontier (million chips); Ch 35 "China and export controls" | CONFIRMED (reported) | https://www.crnasia.com/news/2026/artificial-intelligence/huawei-outlines-ascend-960-roadmap-and-million-processor-ai | None |
| BIS rule of Jan 13, 2026: H200, MI325X and similar chips moved to case-by-case review; conditions include US third-party testing; 50% cap; 25% charge via tariff | Ch 36 "Geopolitics, part 1"; Ch 35 "China and export controls" | CONFIRMED | https://www.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china ; https://www.iaps.ai/research/bis-licensing-policy-for-h200s | None |
| Eligibility "TPP below 21,000 or memory bandwidth below 6,500 GB/s" | Ch 36 "Geopolitics, part 1" | HEDGED | https://www.iaps.ai/research/bis-licensing-policy-for-h200s (says "and"); https://www.cfr.org/articles/new-ai-chip-export-policy-china-strategically-incoherent-and-unenforceable (says "or") | Now says both limits and notes that summaries differ on one-or-both |
| Rule covers "China and Macau" | Ch 36 "Geopolitics, part 1" | CORRECTED | BIS release above names China only | Changed to "China" |
| BIS eased export controls for the UAE on Jul 10, 2026 (license-free advanced computing items for the government and approved companies) | Ch 36 Figure 36.10 and "The 2026 outcome" | ADDED | https://www.bis.gov/press-release/department-commerce-eases-export-controls-uae | New sentence and timeline event |
| No replacement global licensing rule by mid-October 2026 | Ch 36 "The 2026 outcome" | CONFIRMED (BIS news list shows none) | https://www.bis.gov/news-updates | None |
| China proposed export controls on 40 technologies on Oct 16, 2026 | Ch 36 Figure 36.10, "The 2026 outcome", At the frontier (systems); Appendix C | HEDGED | Not found on https://english.mofcom.gov.cn/ ; no other source reachable | Marked "reportedly" in all four places |
| Epoch: frontier training compute up 5× per year since 2020; training cost up 3.5× per year | Ch 37 At the frontier (scale of training) | CONFIRMED | https://epoch.ai/trends | None |
| Colossus 2: about 1.1 million H100-equivalents and 946 MW | Ch 37 At the frontier; Table 34.1 | CONFIRMED | https://epoch.ai/trends ; https://epoch.ai/data/data_centers/data_centers.csv | None |
| Hyperion about 3.7M H100e by Jan 2028; about $38B capex per GW | Ch 37 At the frontier (scale); Ch 36 cost table | CONFIRMED | https://epoch.ai/trends | None |
| GPT-6 Astra: first OpenAI pretraining run on more than 100,000 GPUs, at Stargate in Abilene, Texas; Epoch estimate 9.4e26 FLOP (CI about 5e26–2e27) | Ch 37 At the frontier; Table 37.2 | CONFIRMED | https://epoch.ai/data/all_ai_models.csv ; https://en.wikipedia.org/wiki/GPT-6 (Fortune quote) | None |
| Epoch compute estimates: GPT-4 2.1e25, Grok 3 3.5e26, GPT-4.5 3.8e26, Grok 4 5e26 (speculative), Llama 3.1 405B 3.8e25, DeepSeek-V4-Pro 9.7e24 | Tables 32.1, 37.1, 37.2 | CONFIRMED | https://epoch.ai/data/all_ai_models.csv | None |
| DeepSeek-V4: 1.6T/49B active, FP4 experts plus FP8 elsewhere, about 10% of V3.2's KV cache at 1M tokens | Ch 32 and Ch 33 At the frontier; Ch 37 "Mixed precision"; Table 37.1 | CONFIRMED (the card says more than 32T tokens; Epoch uses 33T) | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro | None |
| "Kimi K3 was trained with MXFP4 quantization-aware training" | Ch 32 At the frontier (precision); Ch 37 "Mixed precision" | CORRECTED | https://huggingface.co/moonshotai/Kimi-K3 (MXFP4 weights and MXFP8 activations, QAT from the SFT stage) | Now says QAT starts at the fine-tuning stage (not pretraining) |
| Kimi K3: 69 of 93 layers linear attention (KDA) | Ch 33 At the frontier (KV cache) | CONFIRMED | same | None |
| Anthropic–Google: up to 1M TPUs, well over 1 GW in 2026 (Oct 23, 2025) | Ch 37 At the frontier (scale); Table 35.10 | CONFIRMED | https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services | None |
| Anthropic–Google–Broadcom (Apr 6, 2026): "multiple gigawatts" of next-generation TPUs from 2027 | Table 35.10 | CONFIRMED (the 3.5 GW figure stays "reported") | https://www.anthropic.com/news/google-broadcom-partnership-compute | None |
| Microsoft Fairwater Wisconsin and Atlanta linked by an "AI WAN" | Table 34.1 | CONFIRMED | https://blogs.microsoft.com/blog/2025/11/12/infinite-scale-the-architecture-behind-the-azure-ai-superfactory/ | None |

## Summary

- Rows checked: 80. Many rows cover several table cells or several chapters.
- CONFIRMED: 54. Every NVIDIA, Google TPU, AWS Trainium and Epoch figure in the tables matched its primary source.
- CORRECTED: 9.
  - GB300 FP8 and BF16 are sparse figures; the dense values are now given.
  - H200 licenses began in February 2026, not March, and China's restriction now rests on NVIDIA's 10-Q, not a "reportedly".
  - The unsupported MI355X "20.1 PF sparse" FP4 figure is removed.
  - MI430X is due in 2027, not 2026.
  - Maia 200 now uses Microsoft's published specs.
  - The Kimi K3 FP4 claim is narrowed.
  - "China and Macau" became "China".
  - Attribution is fixed for the Anthropic–Amazon $100B figure and the Trainium million-chip claim.
- HEDGED: 5.
  - Rubin on TSMC N3, which NVIDIA has not stated.
  - The Groq 3 FP8 rate.
  - The MI455X 19.6 vs 23.3 TB/s bandwidth.
  - The TPP "and/or" test in the BIS rule.
  - China's reported October 16 export-control proposal.
- UNVERIFIABLE: 5, all left unchanged.
  - The TPU 8 design partners.
  - The Maia 200 design partner.
  - The OpenAI–Broadcom deployment status.
  - Intel Crescent Island and the SambaNova investment.
  - The OpenAI–Cerebras terms.
- ADDED: 7.
  - Rubin production shipments.
  - The GTC 2026 Rubin Ultra details.
  - The Meta–AMD and Anthropic–AMD deals.
  - The Cerebras CS-4.
  - The UAE export-control easing.
  - Maia 200 in the HBM3E list.
- Files edited:
  - Chapters 2, 32, 33, 34, 35, 36, 37 and 42.
  - Appendices A and C.
- All edited files pass validate.py, and check.py reports OK for chapters 2, 32–37 and 42.
- Left for the owners of other chapters: Chapters 17, 23, 24 and 30 and Appendix A also say Kimi K3 was "trained with" MXFP4 QAT. Chapter 30 also says "from the start", which overstates it, because the model card says QAT begins at the SFT stage.
