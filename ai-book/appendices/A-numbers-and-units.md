# Appendix A: Numbers and Units Cheat Sheet

AI is a field of enormous and tiny numbers: trillions of parameters, quadrillions of operations, picojoules per operation, milliseconds per token, gigawatts per campus. This appendix collects the units, prefixes, rules of thumb and reference figures used throughout the book in one place, so you can check an estimate or decode a headline without hunting through chapters.

How to read it. Rules of thumb are approximate by design: they are meant to get you within a factor of two, not to the decimal point. Hardware figures are vendor peak specifications, which real software rarely reaches. Prices and market figures are dated (mostly October 2026) and change quickly. Figures marked "reportedly" or "estimate" come from news reports or outside analysts (such as Epoch AI) rather than from the companies themselves. Chapter numbers point to where each idea is explained.

## Powers of ten and metric prefixes

The exponent counts zeros: `10^9` is a 1 followed by nine zeros. "Billion" and "trillion" use the US meanings (`10^9` and `10^12`). See Chapter 2.

| Power | Name | Prefix | Symbol | Everyday anchor | AI anchor |
|---|---|---|---|---|---|
| `10^-12` | trillionth | pico | p | | About a picojoule for one on-chip arithmetic operation (Chapter 33) |
| `10^-9` | billionth | nano | n | Light travels about 30 cm in a nanosecond in a vacuum | On-chip wires respond in about a nanosecond; "3 nm" chip names are marketing labels, not sizes |
| `10^-6` | millionth | micro | µ | | Light in fiber takes about 5 µs per km |
| `10^-3` | thousandth | milli | m | | About 20 ms per token at 50 tokens per second |
| `10^3` | thousand | kilo | k | A microwave draws about 1 kW | One AI GPU slot draws about 1–2 kW all-in |
| `10^6` | million | mega | M | A million seconds is about 11.6 days | 1 MW is roughly 800 average US homes |
| `10^9` | billion | giga | G | A billion seconds is about 31.7 years | An 8-billion-parameter model; 1 GW is about one large nuclear reactor |
| `10^12` | trillion | tera | T | A trillion seconds is about 31,700 years | Trillions of training tokens; a 1-trillion-parameter model |
| `10^15` | quadrillion | peta | P | | One H100 does about `10^15` operations per second in BF16 |
| `10^18` | quintillion | exa | E | | One GB300 NVL72 rack: about 1.1 exaFLOPS of dense FP4 |
| `10^21` | sextillion | zetta | Z | | A 100,000-GPU Blackwell Ultra cluster: about 1.5 zettaFLOPS of dense FP4 |
| `10^24` | septillion | yotta | Y | | GPT-3's training run used about `3 × 10^23` operations, about a third of a yotta |
| `10^25` to `10^27` | | | | | GPT-4 about `2 × 10^25`; 2026 frontier runs about `10^26` to `10^27` (estimates) |

*Table A.1: Powers of ten with everyday and AI anchors.*

| Scientific notation | Read it as | Example |
|---|---|---|
| `2 × 10^25` | 20 trillion trillion | GPT-4's estimated training compute |
| `3.8 × 10^25` | 38 trillion trillion | Llama 3.1 405B's training compute |
| `9.4 × 10^26` | 940 trillion trillion | Epoch AI's estimate for GPT-6 Astra |
| `1.5 × 10^15` | 1.5 quadrillion | Operations for one long reasoning request (Chapter 44) |

*Table A.2: Reading scientific notation aloud.*

## Bytes and memory

A bit is one 0 or 1. A byte is 8 bits, which can hold 256 different values. Storage makers use powers of 1,000; some operating systems and memory specs use powers of 1,024 (a "gibibyte," GiB, is 1,073,741,824 bytes, about 7% more than a gigabyte). See Chapters 2, 3 and 33.

| Unit | Bytes | Everyday example | AI example |
|---|---|---|---|
| Byte (B) | 1 | One English letter | One 8-bit model weight |
| Kilobyte (KB) | `10^3` | A short email | A chatbot request is about 10–40 KB |
| Megabyte (MB) | `10^6` | A minute of MP3 audio | KV cache per token: about 0.07 MB (compact attention) to 0.33 MB (Llama 3 70B) |
| Gigabyte (GB) | `10^9` | A two-hour HD movie is a few GB | H100: 80 GB of HBM; H200: 141 GB; B300 and Rubin: 288 GB; MI455X: 432 GB |
| Terabyte (TB) | `10^12` | A large laptop drive | One NVL72 rack: about 20 TB of HBM; 1 trillion 8-bit weights: 1 TB; 15 trillion tokens of text: about 60 TB |
| Petabyte (PB) | `10^15` | | Raw web crawls; a 9,216-chip Ironwood TPU pod has 1.77 PB of HBM |

*Table A.3: Bytes from letters to web crawls.*

| Memory or storage tier | Typical capacity | Typical bandwidth | Typical latency |
|---|---|---|---|
| Registers | kilobytes per core | highest of all | under a nanosecond |
| On-chip SRAM (caches) | megabytes; up to hundreds of MB on inference chips (TPU 8i: 384 MB) | tens of TB/s; Groq 3 LPU about 150 TB/s | about 1–10 ns |
| HBM beside the GPU | 80–432 GB per chip | about 3.35 TB/s (H100) to 19–22 TB/s (Rubin) | hundreds of ns |
| CPU memory (DRAM, LPDDR) | up to terabytes per server | about 100 GB/s to 1 TB/s | about 100 ns |
| Local SSD | terabytes | about 10 GB/s | tens of microseconds |
| Network storage | petabytes | shared | milliseconds |

*Table A.4: The memory hierarchy, fastest and smallest at the top (Chapter 33). Each step down is bigger, slower and cheaper per byte.*

| Link | Bandwidth | Notes |
|---|---|---|
| Home internet | 0.1–1 Gb/s | Divide bits per second by 8 for bytes: 1 Gb/s = 125 MB/s |
| PCIe 5.0 x16 | about 64 GB/s each way | Inside a server |
| NIC for AI back-end networks | 400 Gb/s to 1.6 Tb/s (50–200 GB/s) | Between servers and racks |
| NVLink 5 (Blackwell) | 1.8 TB/s per GPU | Inside one rack-scale domain |
| NVLink 6 (Rubin) | 3–3.6 TB/s per GPU | Vendor figures differ between launch and product page |

*Table A.5: Interconnect speeds. Watch the difference between b (bits) and B (bytes).*

## FLOP and FLOPS: counting and speed of computation

A FLOP is one floating-point operation (one multiply or one add): a count of work. FLOPS (or FLOP/s) is operations per second: a speed. One multiply-accumulate counts as 2 FLOP. See Chapters 5, 19, 32 and 37.

| Rule of thumb | Formula | Example |
|---|---|---|
| Inference cost per token | about 2 × N FLOP (N = active parameters) | 50 billion active: `10^11` FLOP per token |
| Training cost | about 6 × N × D FLOP (D = training tokens) | Llama 3.1 405B: 6 × 405 × `10^9` × 15.6 × `10^12` ≈ `3.8 × 10^25` |
| Training time | FLOP ÷ (GPUs × peak FLOPS × utilization) | `10^27` FLOP on 100,000 GPUs at `1.2 × 10^15` effective each ≈ 97 days |
| Single-user decode speed limit | memory bandwidth ÷ bytes read per token | 70 GB of 8-bit weights on an H200 (4.8 TB/s): about 69 tokens per second |
| Roofline ridge point | peak FLOPS ÷ memory bandwidth | H100: 989 × `10^12` ÷ 3.35 × `10^12` ≈ 295 FLOP per byte |

*Table A.6: The compute formulas used throughout the book.*

| Device or system | Peak speed (approximate) | Notes |
|---|---|---|
| Copilot+ PC NPU | 40+ TOPS | Integer operations; not directly comparable to FLOPS |
| NVIDIA H100 SXM | about 989 TFLOPS dense BF16 | About `10^15` |
| NVIDIA B300 | about 15 PFLOPS dense FP4 | |
| NVIDIA Rubin | 35 PFLOPS dense NVFP4 (training); 4 PFLOPS dense BF16 | 50 PFLOPS NVFP4 is a sparse inference figure |
| Google Ironwood TPU | 4,614 TFLOPS FP8 | |
| GB300 NVL72 rack | 1,080 PFLOPS dense FP4 | 72 GPUs |
| Ironwood pod (9,216 chips) | 42.5 EFLOPS FP8 | |
| Fastest supercomputers, June 2026 | LineShine 2.198 EFLOPS; El Capitan 1.809 EFLOPS | 64-bit scientific benchmark, a different precision from AI figures |

*Table A.7: Computing speeds. Always ask which precision, dense or sparse, and per chip or per rack.*

| Training run | Estimated total compute | Source |
|---|---|---|
| GPT-3 (2020) | about `3.15 × 10^23` | 6ND from published size and tokens (6 × 175 billion × 300 billion); Epoch AI lists `3.14 × 10^23` |
| DeepSeek-V4-Pro (2026) | about `9.7 × 10^24` | 6ND with 49 billion active parameters and about 33 trillion tokens |
| GPT-4 (2023) | about `2.1 × 10^25` | Epoch AI estimate |
| Llama 3.1 405B (2024) | about `3.8 × 10^25` | Meta |
| Grok 3 (2025) | about `3.5–4.6 × 10^26` | Epoch AI estimates |
| GPT-4.5 (2025) | about `3.8 × 10^26` | Epoch AI estimate |
| GPT-6 Astra (2026) | about `9.4 × 10^26` (range about `5 × 10^26` to `2 × 10^27`) | Epoch AI estimate |

*Table A.8: Training compute of well-known models. Frontier training compute has grown about 5× per year since 2020 (Epoch AI).*

## Tokens, words and pages

A token is a chunk of text, often a word or part of a word (Chapter 18). Ratios vary by tokenizer and language: non-English text and code often need more tokens per word. Anthropic says 1 million tokens is about 555,000 English words on the tokenizer introduced with Claude Opus 4.7, against about 750,000 words on its earlier tokenizer.

| Rule of thumb | Value |
|---|---|
| Words per token (English) | about 0.75 |
| Tokens per word (English) | about 1.3 |
| Characters per token (English) | about 4 |
| Bytes per token of stored plain text | about 4 |
| Tokens per single-spaced page (about 500 words) | about 650 |

*Table A.9: Converting between tokens, words and pages.*

| Text | Words (approx.) | Tokens (approx.) |
|---|---|---|
| A typical chat question | 20–50 | 25–70 |
| One single-spaced page | 500 | 650 |
| A 12-page contract | 6,000 | 8,000 |
| A typical novel | 80,000–100,000 | 100,000–130,000 |
| A 1-million-token context window | 555,000–750,000 | 1,000,000, roughly six to eight novels |
| Llama 3's training data | about 11.7 trillion | about 15.6 trillion |
| DeepSeek-V4-Pro's training data | about 25 trillion | about 33 trillion |
| Epoch AI's estimate of all high-quality public human text (2024) | about 225 trillion | about 300 trillion (range 100–1,000 trillion) |

*Table A.10: How much text is how many tokens. Reading 15 trillion tokens at 250 words a minute, 8 hours a day, would take a person about 257,000 years.*

## Model sizes and memory at each precision

Memory for weights = parameters × bytes per parameter. FP32 uses 4 bytes, BF16 and FP16 use 2, FP8 and INT8 use 1, and 4-bit formats (FP4, INT4, MXFP4, NVFP4) use about 0.5 plus a little extra for scale factors. For mixture-of-experts models, all parameters must be stored, but only the active ones are read for each token. See Chapters 5, 23 and 30.

| Parameters | FP32 | BF16 | FP8 / INT8 | 4-bit | Example models |
|---|---|---|---|---|---|
| 1 billion | 4 GB | 2 GB | 1 GB | 0.5 GB | Small on-device models |
| 8 billion | 32 GB | 16 GB | 8 GB | 4 GB (about 4.7 GB as a real file) | Runs on a laptop at 4-bit |
| 27–31 billion | 108–124 GB | 54–62 GB | 27–31 GB | 14–16 GB | Qwen3.8-27B; Gemma 4 31B |
| 70 billion | 280 GB | 140 GB | 70 GB | 35 GB | Llama 3 70B |
| 117 billion | 468 GB | 234 GB | 117 GB | about 60 GB | gpt-oss-120b fits on one 80 GB GPU with 4-bit experts |
| 405 billion | 1.6 TB | 810 GB | 405 GB | about 200 GB | Llama 3.1 405B |
| 1 trillion | 4 TB | 2 TB | 1 TB | 500 GB | |
| 1.6 trillion total (49 billion active) | 6.4 TB | 3.2 TB | 1.6 TB | 800 GB | DeepSeek-V4-Pro (FP4 experts, FP8 elsewhere) |
| 2.8 trillion total (104 billion active) | 11.2 TB | 5.6 TB | 2.8 TB | 1.4 TB | Kimi K3 (MXFP4 weights; quantization-aware training from the fine-tuning stage onward, not in pretraining) |

*Table A.11: Weight memory by model size and precision. Compare with GPU memory: H100 80 GB, H200 141 GB, B300 288 GB, NVL72 rack about 20 TB.*

| Other memory rules of thumb | Value | Example |
|---|---|---|
| Training state with Adam in mixed precision | about 16 bytes per parameter | 70 billion parameters: about 1.12 TB before activations |
| KV cache per token | 2 × layers × KV heads × head size × bytes | Llama 3 70B (80, 8, 128, 2 bytes): about 0.33 MB per token |
| KV cache for a long conversation | tokens × bytes per token | 100,000 tokens × 0.33 MB ≈ 33 GB |
| Compact attention (MLA, DeepSeek-V3 style) | about 0.07 MB per token | 15,400 tokens ≈ 1.1 GB |

*Table A.12: Memory beyond the weights (Chapters 23 and 33).*

## GPU and TPU key specs (approximate)

Vendor peak figures as of October 2026, from the research behind Chapters 32 to 35. They are approximate: vendors revise numbers between announcement and shipment, and headline compute figures differ by precision, by dense versus sparse counting (sparse is usually double) and by per-chip versus per-rack reporting.

| Chip (year) | Memory | Memory bandwidth | Headline compute (approx.) | Power and notes |
|---|---|---|---|---|
| NVIDIA V100 (2017) | 16/32 GB HBM2 | | | First tensor cores |
| NVIDIA A100 (2020) | 40/80 GB HBM2e | about 2 TB/s | | Introduced TF32 and BF16 support |
| NVIDIA H100 SXM (2022) | 80 GB HBM3 | 3.35 TB/s | about 989 TFLOPS dense BF16 | 700 W; 80 billion transistors |
| NVIDIA H200 (2024) | 141 GB HBM3E | 4.8 TB/s | same as H100 | More and faster memory |
| NVIDIA B200 (2024–25) | 192 GB HBM3E | 8 TB/s | | Two dies, 208 billion transistors; about 1 kW or more |
| NVIDIA B300 (late 2025) | 288 GB HBM3E | 8 TB/s | about 15 PFLOPS dense FP4 | Blackwell Ultra |
| NVIDIA Rubin (2026) | 288 GB HBM4 | about 19–22 TB/s | 35 PFLOPS dense NVFP4; 17.5 PFLOPS FP8; 4 PFLOPS BF16 | 336 billion transistors (NVIDIA); TSMC N3 (reported) |
| AMD MI300X (2023) | 192 GB HBM3 | 5.3 TB/s | | Chiplet design |
| AMD MI355X (2025) | 288 GB HBM3E | 8 TB/s | 10.1 PFLOPS dense MXFP4 | 1,400 W, liquid-cooled |
| AMD MI455X (2026) | 432 GB HBM4 | about 19.6 TB/s (up to 23.3 cited) | about 40 PFLOPS dense FP4; about 20 PFLOPS FP8 | In the Helios rack |
| Google TPU Trillium (v6e, 2024) | 32 GB HBM | | 918 TFLOPS BF16 | |
| Google TPU Ironwood (v7, 2025) | 192 GB HBM3E | 7.37 TB/s | 4,614 TFLOPS FP8 | Pods of up to 9,216 chips |
| Google TPU 8t (2026) | 216 GB HBM | 6.5 TB/s | 12.6 PFLOPS FP4 | Training chip; 128 MB on-chip SRAM |
| Google TPU 8i (2026) | 288 GB HBM | 8.6 TB/s | 10.1 PFLOPS FP4 | Inference chip; 384 MB on-chip SRAM |
| AWS Trainium3 (2025) | 144 GB HBM3E | 4.9 TB/s | about 2.5 PFLOPS FP8 | 3 nm |
| Microsoft Maia 200 (2026) | 216 GB HBM3E | about 7 TB/s | more than 10 PFLOPS FP4 | 272 MB on-die SRAM |
| Groq 3 LPU (2026) | about 500 MB SRAM, no HBM | about 150 TB/s (SRAM) | about 1.2 PFLOPS FP8 | 256 per LPX rack |
| Cerebras WSE-3 | 44 GB on-chip SRAM | | | One wafer: 46,225 mm², 4 trillion transistors |

*Table A.13: Accelerator specs, approximate.*

| Rack or pod | Chips | Fast memory | Headline compute (approx.) | Power |
|---|---|---|---|---|
| NVIDIA GB300 NVL72 | 72 GPUs + 36 CPUs | about 20 TB HBM | 1,080 PFLOPS dense FP4 | about 120–140 kW |
| NVIDIA Vera Rubin NVL72 | 72 GPUs + 36 CPUs | 20.7 TB HBM4 | 2,520 PFLOPS dense NVFP4 (training) | |
| AMD Helios | 72 MI455X | 31 TB HBM4 | 2.9 EFLOPS dense FP4 | |
| AWS Trn3 UltraServer | 144 Trainium3 | 20.7 TB HBM3E | 362 PFLOPS MXFP8 | |
| Google Ironwood pod | 9,216 TPUs | 1.77 PB HBM | 42.5 EFLOPS FP8 | |
| NVIDIA Rubin Ultra Kyber rack (planned 2027) | 144 GPU packages (reported) | HBM4E | 15 EFLOPS FP4 (inference, 2025 plan) | about 600 kW |

*Table A.14: Rack-scale and pod-scale systems, approximate (Chapters 34 and 35).*

## Power and energy units

Power (watts) is a rate, like speed. Energy (watt-hours) is an amount, like distance: power × time = energy. See Chapters 39 to 41.

| Unit | Equals | Real-world comparison |
|---|---|---|
| 1 watt (W) | 1 joule per second | A phone charger draws about 20 W; a 10 W LED bulb |
| 1 kilowatt (kW) | 1,000 W | A microwave; a hair dryer is about 1.5 kW; an average US home averages about 1.2 kW over a year |
| 1 megawatt (MW) | 1,000 kW | Roughly 800 average US homes; a small enterprise data center is 1–5 MW |
| 1 gigawatt (GW) | 1,000 MW | About one large nuclear reactor; roughly 800,000 average US homes |
| 1 joule (J) | 1 watt for 1 second | About the energy to lift an apple one meter |
| 1 watt-hour (Wh) | 3,600 J | A 10 W LED bulb for 6 minutes |
| 1 kilowatt-hour (kWh) | 1,000 Wh | The unit on your electricity bill |
| 1 megawatt-hour (MWh) | 1,000 kWh | Wholesale electricity is priced per MWh |
| 1 gigawatt-hour (GWh) | 1 million kWh | A 100,000-GPU training run for 90 days uses roughly 470 GWh (Chapter 44) |
| 1 terawatt-hour (TWh) | 1 billion kWh | 1 GW running for a full year is 8.76 TWh |

*Table A.15: Power and energy units.*

| Thing | Power or energy | Source or note |
|---|---|---|
| One median Gemini Apps text prompt (May 2025) | 0.24 Wh | Google; includes idle machines and overhead; not independently verified |
| One average ChatGPT query | about 0.34 Wh | OpenAI's chief executive, June 2025 |
| One typical GPT-4o query | about 0.3 Wh | Epoch AI, February 2025 |
| A query with 10,000 / 100,000 input tokens | about 2.5 Wh / about 40 Wh | Epoch AI, February 2025, on that era's hardware |
| A long reasoning request with a document and a search | about 1.2 Wh | Chapter 44's estimate |
| Boiling a kettle | about 100 Wh | |
| A 10-mile electric-car drive | about 3 kWh | |
| An average US home for a year | about 10,500 kWh | |
| One H100 chip | 700 W | Chip rating |
| One AI GPU with its share of server, network and cooling | about 1.2–2.2 kW | H100 about 1.2–1.5 kW (Epoch AI uses 1.5 kW); GB300-class about 1.8 kW of IT power as a share of its rack, about 2.2 kW once cooling is added |
| A 2015 enterprise rack | about 5–10 kW | |
| A GB200 or GB300 NVL72 rack | about 120–140 kW | About 100 homes in one cabinet |
| US data centers, 2023 | 176 TWh, about 4.4% of US electricity | Lawrence Berkeley National Laboratory |
| All data centers worldwide, 2024 | about 415 TWh, about 1.5% of world electricity | International Energy Agency; projected about 945 TWh by 2030 |
| Ireland's data centres, 2025 | 23% of metered electricity (22% in 2024) | Central Statistics Office |

*Table A.16: Energy and power with real-world comparisons.*

| Electrical and thermal reference values | Value |
|---|---|
| US household voltage | 120/240 V |
| Transmission lines | 69,000–765,000 V |
| Campus medium voltage | about 1–35 kV (e.g. 34.5 kV) |
| Inside the building | 480 or 415 V |
| Rack power shelf output | about 48–54 V DC; 800 V DC planned for 2027-era racks |
| Chip core voltage | about 1 V or less |
| One "ton" of cooling | 12,000 BTU per hour, about 3.5 kW of heat |
| Heat carried by water versus air, per unit volume | about 3,500 times more |
| PUE: ideal / leading AI sites / industry average | 1.0 / about 1.1–1.2 (Google's fleet: 1.09 in 2025) / about 1.5–1.6 (1.54 in the Uptime Institute's 2025 survey, as cited by Google) |
| US average residential electricity price | 17.3¢/kWh (2025), 18.2¢ (2026), 18.7¢ (2027 forecast), per the EIA |

*Table A.17: Electrical and cooling reference values (Chapters 39 and 40).*

## Data center scale ladder

| Level | Typical power | Accelerators | Example |
|---|---|---|---|
| One GPU slot, all-in | about 1–2 kW | 1 | Chip plus its share of CPUs, network and cooling |
| 8-GPU server | about 10–12 kW | 8 | HGX-style H100 server (8 × about 1.2–1.5 kW) |
| AI rack | about 120–140 kW | 72 | GB200 or GB300 NVL72 |
| Next-generation rack | about 600 kW, heading toward 1 MW | 144 packages (reported) | NVIDIA Kyber, planned for 2027 |
| Data hall | about 5–50 MW | thousands to tens of thousands | One large room of a campus |
| Cluster | about 180 MW of IT for 100,000 GPUs | 100,000 | About 217 MW from the grid at PUE 1.2 |
| xAI Colossus 1 (2024) | about 150 MW (after upgrades), reportedly | about 100,000 H100s | Built in 122 days, reportedly |
| Large campus | about 1 GW | 500,000 to over 1 million | xAI Colossus 2: about 946 MW of IT, about 1.1 million H100-equivalents (Epoch AI) |
| Largest tracked site by power, October 2026 | about 1,037 MW of IT | | Anthropic and Amazon's New Carlisle, Indiana site (Epoch AI) |
| Announced megaprojects | 1.2–5 GW | | Stargate Abilene about 1.2 GW; Meta Hyperion planned 5 GW |
| All large AI data centers tracked by Epoch AI | about 14.2 GW of IT (about 18.5 GW with overhead) | about 14.8 million H100-equivalents | 95 sites, October 2026 |
| Global data center capacity | about 103 GW (2025), about 200 GW expected by 2030 | | JLL forecast |

*Table A.18: From one chip to the whole industry (Chapters 34, 38 and 42). Real sites use on average about 60–80% of their capacity.*

## Cost rules of thumb

All prices in US dollars, dated and approximate. List prices are what anyone can pay; large customers negotiate lower contract prices that are not public. See Chapters 19, 23, 26 and 43.

| Item | Rule of thumb (October 2026 unless noted) | Source or note |
|---|---|---|
| Renting an H100 | about $2.69–4.29 per GPU-hour on demand | RunPod and Lambda list prices |
| Renting an H200 | about $3.59–5.29 per GPU-hour | RunPod |
| Renting a B200 | about $5.98–7.99 per GPU-hour | RunPod and Lambda |
| Renting a B300 | about $6.94–8.99 per GPU-hour | RunPod |
| Renting an A100 | about $1.19–2.79 per GPU-hour | RunPod and Lambda |
| Buying an H100 | about $25,000–40,000 | Reported |
| Buying a GB200 or GB300 NVL72 rack | about $3–4 million | Reported |
| One EUV lithography machine | about $180 million | |
| One leading-edge chip factory | $20 billion or more | |

*Table A.19: Hardware and rental prices.*

| Building cost per MW of IT capacity | Value | Source |
|---|---|---|
| Shell and core, global average | $10.7 million (2025); $11.3 million (2026 forecast) | JLL |
| Most modern greenfield facilities | about $17.6 million | Cushman & Wakefield, 2026 |
| AI tenant fit-out | up to about $25 million | JLL |
| All-in, including chips, per GW of IT | about $38 billion; NVIDIA's chief executive has cited about $50–60 billion | Epoch AI; reported |
| Share of all-in cost that is IT equipment | the large majority; building and power gear roughly 20–30% | |

*Table A.20: Building costs per megawatt (Chapters 42 and 43).*

| API price per million tokens, input / output | Model |
|---|---|
| from $0.10 / $0.50 | Claude Haiku 5.5 |
| $2 / $10 | Claude Sonnet 5.5; Gemini 4 Argon introductory price through November 30, 2026 |
| $4 / $20 | Claude Opus 5.5; Gemini 4 Argon after November 30, 2026 |
| $10 / $50 | Claude Fable 5.1; GPT-6 Astra |
| about 50% off | Batch APIs (results within hours) |
| about 2× | Anthropic's "fast mode" for Opus 5.5 ($8 / $40) |

*Table A.21: Sample API list prices, October 2026 (Chapter 26). Prices for a fixed level of capability have fallen roughly 10× or more per year; GPT-4-level performance on MMLU went from $37.50 per million tokens in March 2023 to $0.18 in February 2025 (Epoch AI).*

| Cost formula | Worked example |
|---|---|
| $ per million tokens = $ per GPU-hour ÷ (tokens per second × 3,600) × 1,000,000 | $3 per hour at 1,000 tokens per second: about $0.83; at 5,000 tokens per second: about $0.17 |
| Rack version | 72 GPUs × $4 per hour at 865,000 tokens per second (Microsoft's Fairwater figure): about $0.09 per million |
| Training GPU-hours = FLOP ÷ (peak FLOPS × utilization × 3,600) | Llama 3.1 405B at 40% of H100 peak: about 26.7 million GPU-hours, about $67 million at $2.50 per hour |
| Electricity per GPU-hour | 1.5 kW × 1 hour × $0.08 per kWh = $0.12, small next to a $2–8 rental price |
| Electricity per MW-year | 8,760 MWh × $70–80 per MWh ≈ $0.6–0.7 million |
| A site drawing 100 MW for a year at full load | about 876 GWh, about $61–70 million at 7–8 cents per kWh; a site with 100 MW of IT at PUE 1.2 draws 120 MW: about 1,051 GWh and $74–84 million (Chapter 39) |

*Table A.22: Cost formulas with worked examples.*

| Published or estimated training compute costs (final run only) | Value |
|---|---|
| GPT-4 (2023) | about $37 million (Epoch AI, 2023 dollars) |
| Llama 3.1 405B (2024) | about $53 million (Epoch AI) |
| DeepSeek-V3 final run (2024) | about $5.6 million: 2.788 million H800 GPU-hours at an assumed $2 per hour; excludes research and staff |
| Grok 3 (2025) | about $218 million (Epoch AI) |
| GPT-4.5 (2025) | about $366 million (Epoch AI) |
| A 2026 flagship (100,000 GPUs for 90 days) | about $0.4–1.1 billion at $2–5 per GPU-hour (back-of-envelope estimate) |

*Table A.23: Training-run costs. Total program costs (experiments, failed runs, data, people) are several times the final run.*

## Handy conversions

| Conversion | Value |
|---|---|
| Watt-hours to joules | 1 Wh = 3,600 J; 1 kWh = 3.6 million J |
| kWh to BTU | 1 kWh ≈ 3,412 BTU |
| Average power from annual energy | watts = watt-hours per year ÷ 8,760 |
| 1 MW running for a year | 8,760 MWh = 8.76 GWh |
| 1 GW running for a year | 8.76 TWh |
| Capacity price | $ per MW-day × 365 ÷ 1,000 = $ per kW-year |
| Bits to bytes | divide by 8 (800 Gb/s = 100 GB/s) |
| Seconds in a day / 90 days / a year | 86,400 / about 7.8 million / about 31.5 million |
| Light in fiber | about 200,000 km per second: about 5 µs per km, 5 ms per 1,000 km |
| Tokens per second to milliseconds per token | ms per token = 1,000 ÷ tokens per second (50 tokens per second = 20 ms) |
| Tokens and words (English) | tokens ≈ words × 1.3; words ≈ tokens × 0.75 |
| Weight memory | bytes = parameters × bits per parameter ÷ 8 |
| Inference compute | FLOP per token ≈ 2 × active parameters |
| Training compute | FLOP ≈ 6 × active parameters × training tokens |
| Energy per token | joules = power in watts ÷ tokens per second |
| Rack unit | 1U = 1.75 inches = 4.445 cm |
| Rack width | 19 inches inside |
| Volume | 1 US gallon = 3.785 liters; an Olympic pool holds about 2.5 million liters |
| Distance | 1 mile = 1.609 km |
| Temperature | °F = °C × 9 ÷ 5 + 32 (30 °C = 86 °F; 80 °C = 176 °F) |
| Uptime "nines" | 99.9% ≈ 8.8 hours down per year; 99.99% ≈ 53 minutes; 99.999% ≈ 5 minutes |
| Growth rates | 5× per year = 3,125× in 5 years; doubling every 4 months ≈ 8× per year |

*Table A.24: Conversions and formulas worth memorizing.*
