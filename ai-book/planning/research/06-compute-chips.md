# 06 — Compute: From Transistor to AI Supercomputer, and the Chip Industry

Research notes for the book *Everything About AI: From Zero to the Frontier*. Status as of **October 21, 2026**.

**How these notes were verified:** Specs, dates and deals in Section 4 were checked against vendor pages, press releases, earnings releases and reputable analysis (URLs are given inline and in the source list at the end). The web-search budget ran out partway through the research. Because of that, a few industry facts are marked **[verify]**: they are widely reported, but I could not re-check them against a primary source in this pass. Vendor performance numbers are *peak, on-paper* figures. When a number is "sparse" (it assumes half the multiplications can be skipped), that is said explicitly.

---

## 1. Topic map (teaching order, simplest → most advanced)

### Part A — What a computer physically does
1. **Bits and numbers.** Every piece of information is stored as a pattern of 0s and 1s. Explain binary with light switches, and show how 8 switches give 256 patterns. Build up to "a number in a computer has a fixed number of bits, and that choice matters later" (this sets up precision).
2. **The transistor as a switch.** A transistor is a tiny electrically controlled switch with no moving parts. Use the image of a garden hose with a pinch valve, where a small voltage on the "gate" opens or closes the flow. State the scale: a modern AI chip has more than 200 billion of them.
3. **Logic gates → adders → arithmetic.** A few transistors make a gate (AND, OR, NOT). A few gates make an adder, and adders plus shifting make a multiplier. The point is that all arithmetic is built from switches.
4. **The clock.** The chip moves in lockstep with a metronome, measured in GHz (billions of ticks per second). Explain that clocks stopped getting much faster around 2005 because of heat, which is why the industry turned to *more workers* instead of *faster workers*.
5. **Memory vs. compute (von Neumann architecture).** The processor does math, memory holds data, and a "bus" connects them. Introduce the idea that *moving data costs more time and energy than doing math on it*. This is the seed of the "memory wall."
6. **The CPU.** Cover cores, threads, caches and instruction sets (x86, Arm, RISC-V). A CPU is a handful of very smart, flexible workers that are excellent at branching, step-by-step logic.
7. **Moore's Law and Dennard scaling.** Transistor counts doubled roughly every two years. Until about 2005, smaller transistors also used proportionally less power (Dennard scaling). When that power benefit ended, the industry moved to multicore and then to massively parallel accelerators.

### Part B — Why AI needs special hardware
8. **What a neural network actually computes.** Almost all of it is multiply-and-add (MAC) operations arranged as *matrix multiplications*. Show a 2×2 matrix multiply by hand. Point out that a chatbot reply is trillions of these.
9. **FLOP vs. FLOPS.** A FLOP is one floating-point operation (a count). FLOPS is how many per second (a speed). Use scientific notation (10^15 = peta, 10^18 = exa). Distinguish *peak* from *achieved*, and *dense* from *sparse* numbers.
10. **Parallelism.** Explain SIMD/SIMT: one instruction, thousands of data items. Tell the GPU story: built for video-game pixels, made programmable with CUDA (2006–07), then AlexNet (2012) showed GPUs could train neural nets.
11. **Tensor cores and systolic arrays.** These are special circuits that do a whole small matrix multiply per clock tick. A systolic array is a grid of multipliers that pass numbers to their neighbors like a bucket brigade, which is the core of a TPU.
12. **Numeric precision.** Walk down the ladder: FP32 → TF32 → BF16/FP16 → FP8 → FP6/FP4 (MXFP4, NVFP4) → INT8/INT4. Fewer bits means more math per second, less memory, less energy and less data movement, at the cost of accuracy, which software has to manage. Use a "ruler with fewer tick marks" picture.
13. **The memory hierarchy.** Registers → SRAM caches → HBM → CPU DRAM → SSD → network storage. Each step down is larger, slower and cheaper per byte. Show latency and bandwidth on a log scale.
14. **Memory bandwidth and the memory wall.** Compute has grown faster than memory bandwidth for decades, so many AI tasks wait on memory rather than math. Introduce *arithmetic intensity* (math per byte moved) and the *roofline model*.
15. **HBM (High Bandwidth Memory).** HBM is stacked DRAM sitting right next to the GPU on a silicon interposer, with a very wide bus. Cover the generations (HBM3 → HBM3E → HBM4 → HBM4E), the three suppliers, and why HBM supply is a bottleneck.

### Part C — The accelerator zoo
16. **NVIDIA GPUs.** Volta (first tensor cores) → Ampere A100 → Hopper H100/H200 → Blackwell B200/GB200 → Blackwell Ultra B300/GB300 → Vera Rubin (2026) → Rubin Ultra (2027) → Feynman (2028). Explain "superchip" (CPU+GPU), and why NVIDIA now sells racks, not just chips.
17. **AMD Instinct.** MI300X → MI325X → MI350/MI355X → MI400 family (MI455X, MI430X) in the Helios rack → MI500 (2027). AMD's pitch is more memory per GPU and open standards. Its main gap has been software (ROCm).
18. **Google TPUs.** v1 (2015, inference) → v4 → v5e/v5p → Trillium (v6e) → Ironwood (v7) → TPU 8t/8i (2026). These are systolic-array ASICs linked by an inter-chip interconnect (ICI) and optical circuit switches, built mostly for Google's own use and for Google Cloud customers such as Anthropic.
19. **Hyperscaler custom silicon.** AWS Trainium/Inferentia, Microsoft Maia, Meta MTIA, and OpenAI–Broadcom. Explain *why* a cloud company builds its own chip: cost, supply security and bargaining power. Explain the role of design partners (Broadcom, Marvell, MediaTek, Alchip).
20. **Alternative architectures.** Cerebras (wafer-scale), Groq LPU (SRAM-only, deterministic, now licensed to NVIDIA), SambaNova (reconfigurable dataflow), Etched (transformer-only ASIC), Tenstorrent (RISC-V and open software), d-Matrix (in-memory compute), plus photonic interconnect startups. Discuss trade-offs (SRAM capacity vs. bandwidth) rather than hype.
21. **Edge/NPUs.** Phone and laptop neural processing units (Apple Neural Engine and M5 GPU neural accelerators, Qualcomm Hexagon, Intel/AMD NPUs, Google Tensor), TOPS ratings, and why on-device inference is constrained by memory and battery.
22. **Software stack and the CUDA moat.** Drivers → CUDA → libraries (cuBLAS, cuDNN, NCCL, TensorRT) → frameworks (PyTorch, JAX) → compilers (XLA, Triton, torch.compile) → serving engines (vLLM, SGLang, TensorRT-LLM, Dynamo). Explain why 20 years of software makes NVIDIA hard to displace, and how ROCm, XLA/JAX, Triton and Neuron are chipping at it.

### Part D — From chip to supercomputer (the physical hierarchy)
23. **The package.** Silicon die(s) + HBM stacks + interposer + substrate. Cover chiplets, the reticle limit (~858 mm²), multi-die GPUs (Blackwell = two dies), and TSMC CoWoS.
24. **The board and server.** An 8-GPU baseboard (HGX) or superchip trays, host CPUs, PCIe, NICs and DPUs, power delivery, and liquid cold plates.
25. **Scale-up networking.** NVLink/NVSwitch (memory-semantic, very high bandwidth, short reach), the NVL72 rack as "one giant GPU," Google ICI, AWS NeuronLink/NeuronSwitch, and UALink as the open alternative.
26. **Scale-out networking.** InfiniBand, Ethernet/RoCE, Spectrum-X, Ultra Ethernet; NICs (ConnectX), DPUs (BlueField); topologies (fat-tree/Clos, rail-optimized, 3D torus, dragonfly); "front-end" vs. "back-end" networks.
27. **Optics.** Copper vs. fiber, pluggable transceivers (800G/1.6T), co-packaged optics (CPO) and optical circuit switches (OCS). Explain why power and reliability push optics closer to the chip.
28. **Rack power and cooling (a bridge to the data-center chapter).** Racks went from ~10 kW to 120–140 kW (GB200/GB300) to a planned ~600 kW (Rubin Ultra Kyber). Cover direct-to-chip liquid cooling and 800 V DC power.
29. **Pods, superpods, clusters, "AI factories."** Count upward: GPU → node → rack → pod → building → campus. Today's frontier is 100k–1M+ accelerators, and some training runs span multiple data centers.

### Part E — Training at scale
30. **Training compute math.** Training FLOPs ≈ 6 × N (parameters) × D (tokens). Inference ≈ 2 × N per token. Work examples: GPT-3 ≈ 3×10^23; Llama 3.1 405B ≈ 3.8×10^25; frontier runs in 2025–26 at 10^26 and beyond.
31. **Memory needs of training.** Weights + gradients + optimizer state (~16 bytes per parameter with Adam in mixed precision) + activations. This is why one model needs many GPUs even before speed is considered.
32. **Parallelism strategies.** Data parallel; ZeRO/FSDP (sharding the optimizer state, gradients and weights); tensor parallel (split each matrix); pipeline parallel (split the layers; "bubbles"); sequence/context parallel (split the long input); expert parallel (MoE). Combine them as "3D/4D/5D parallelism," and map each to the network tier it uses.
33. **Collective communication.** All-reduce, all-gather, reduce-scatter, all-to-all, broadcast; ring vs. tree algorithms; NCCL/RCCL. Explain why the slowest link sets the pace.
34. **Utilization.** MFU (model FLOPs utilization) vs. HFU. Typical frontier MFU is about 35–50%. Cover where time goes: communication, memory stalls, pipeline bubbles, stragglers, failures.
35. **Failures, checkpointing and goodput.** At 100k GPUs, something breaks every few minutes to hours. Use Llama 3's 419 unexpected interruptions in 54 days. Cover checkpoints, hot spares and asynchronous checkpointing, and present "goodput" as the real metric.
36. **Low-precision training.** BF16 mixed precision became standard. FP8 training arrived with Hopper (DeepSeek-V3 is a public example), and FP4 training is emerging with Blackwell and Rubin (NVFP4).

### Part F — Inference hardware and economics
37. **Prefill vs. decode.** Reading the prompt is compute-bound and parallel. Generating each new token is memory-bandwidth-bound and sequential. Explain the KV cache and why long contexts eat memory.
38. **Throughput vs. latency.** Batching, tokens/second per user vs. per GPU, time-to-first-token (TTFT), and the "Pareto frontier" of interactivity vs. cost.
39. **Inference tricks that change hardware economics.** Quantization, speculative decoding, continuous batching, paged attention, disaggregated prefill/decode (e.g., NVIDIA Dynamo), MoE with expert parallelism across NVL72, and prompt caching.
40. **Cost per token.** $/GPU-hour ÷ tokens/hour. Also cover tokens per watt, total cost of ownership (TCO), depreciation, and why prices for a fixed capability fall 10×–100×+ per year.
41. **Specialized inference silicon.** Groq 3 LPX, Rubin CPX (prefill), TPU 8i, Maia 200, Inferentia, and the 2026 trend of *splitting* chips into training and inference variants.

### Part G — How chips are made
42. **From sand to wafer.** Polysilicon → ingot → 300 mm wafers. Introduce cleanrooms.
43. **Front-end fabrication.** Hundreds to over 1,000 steps: deposit, pattern (lithography), etch, implant, polish, repeated in layers. Explain the "printing press with light" analogy.
44. **Process nodes and transistor shapes.** Planar → FinFET (2011+) → gate-all-around nanosheets (TSMC N2, Intel 18A, Samsung SF3/SF2) → backside power (Intel PowerVia, TSMC A16). Stress that node names are marketing, not physical sizes.
45. **Lithography.** DUV (193 nm), EUV (13.5 nm), High-NA EUV (0.55 NA). ASML is the sole EUV supplier. Cover tool cost and complexity (tin-droplet plasma, mirrors in vacuum).
46. **Yield and the reticle limit.** Defects per cm², why big dies yield worse, binning, and why chiplets help.
47. **Advanced packaging.** CoWoS-S/-L/-R, SoIC (3D hybrid bonding), Intel EMIB/Foveros, UCIe for chiplet interconnect. Explain why packaging, not just wafers, became an AI bottleneck.
48. **Memory manufacturing.** DRAM dies, TSVs (through-silicon vias), stacking 8/12/16 high, base (logic) die, and custom HBM4 base dies made at logic foundries.
49. **The supply chain map.** EDA (Synopsys, Cadence, Siemens) → IP (Arm) → chip designers (NVIDIA, AMD, Broadcom, hyperscalers) → foundries (TSMC, Samsung, Intel, SMIC) → equipment (ASML, Applied Materials, Lam, Tokyo Electron, KLA) → materials (wafers, photoresists, gases) → memory (SK hynix, Samsung, Micron) → OSAT/packaging (TSMC, ASE, Amkor) → server ODMs (Foxconn, Quanta, Wistron, Wiwynn, Supermicro, Dell) → clouds and neoclouds.
50. **Costs.** Design cost (hundreds of millions of dollars), wafer prices, fab costs (tens of billions of dollars), GPU and rack prices, and cloud rental prices.

### Part H — Industry, money and geopolitics
51. **Market structure.** NVIDIA's dominance (data-center revenue of $89B in one quarter), AMD as the main merchant alternative, custom ASICs via Broadcom and others, and neoclouds (CoreWeave, Nebius, Lambda, Crusoe).
52. **The mega-deals of 2025–26.** OpenAI–NVIDIA, OpenAI–AMD, OpenAI–Broadcom, Anthropic–Google TPU, Anthropic–AWS Trainium, Anthropic–Microsoft/NVIDIA, NVIDIA–Groq, NVIDIA–Intel.
53. **Export controls.** The Oct 2022, Oct 2023 and Dec 2024 rules; the AI Diffusion Rule and its rescission (2025); H20 back-and-forth; the Jan 2026 case-by-case H200/MI325X policy (TPP < 21,000) with a 25% mechanism; China's counter-moves.
54. **China's domestic stack.** Huawei Ascend roadmap and SuperPoDs, SMIC 7 nm/5 nm-class with DUV multi-patterning, CXMT memory, Cambricon and others.
55. **Taiwan concentration risk, CHIPS Act and reshoring.** TSMC Arizona, Intel's government stake, Samsung Texas, Japan's Rapidus, and tariffs.

### Part I — Edge and on-device AI
56. **Why run AI locally.** Privacy, latency, cost and offline use. Limits are memory capacity and bandwidth, power and heat. Cover NPUs, unified memory (Apple), small models (1–8B parameters), 4-bit quantization, and AI PCs (Copilot+ 40+ TOPS requirement), plus desktop "AI supercomputers" (DGX Spark).

### Part J — The frontier and what comes next
57. **Roadmaps 2026–2028.** Rubin → Rubin Ultra/Kyber (2027) → Feynman (2028, A16, 3D stacking); MI500 (2027); TPU 8 successors; Trainium4 (NVLink Fusion); Huawei Ascend 960/970.
58. **Physics limits and bets.** Power density, interconnect energy, co-packaged and in-package optics, 3D stacking of logic and memory, in-memory/analog compute, photonic compute, and why quantum computers are not AI accelerators today.
59. **The energy question.** FLOPs per watt improve ~30–40% per year at the chip level, yet total AI power demand keeps rising (Jevons paradox). Hand off to the data-center and energy chapter.

---
## 2. Glossary candidates (plain-English definitions)

*Grouped by theme. Each entry is a candidate for the book's glossary.*

### 2.1 Basics of computing
1. **Bit** — The smallest unit of information: a single 0 or 1, like one light switch being off or on.
2. **Byte** — Eight bits grouped together. One byte can represent 256 different values, such as one letter of English text.
3. **Binary** — Counting with only two digits (0 and 1). Computers use it because a switch is either off or on.
4. **Transistor** — A microscopic switch made of silicon that turns electrical current on or off when a small voltage is applied to its "gate." Modern AI chips contain hundreds of billions of them.
5. **Logic gate** — A tiny circuit of a few transistors that makes a simple yes/no decision (AND, OR, NOT). All computer arithmetic is built from gates.
6. **Integrated circuit (IC) / chip** — Many transistors and wires manufactured together on one piece of silicon. "Chip" and "IC" mean the same thing.
7. **Die** — A single rectangular piece of silicon cut from a wafer, containing one chip's circuitry. A product may contain several dies in one package.
8. **Clock speed (GHz)** — How many times per second a chip's internal metronome ticks. 2 GHz means 2 billion ticks per second, and work happens in step with these ticks.
9. **Core** — An independent processing unit within a chip. A CPU might have 8–256 large cores; a GPU has thousands of small ones.
10. **Thread** — A single sequence of instructions being executed. One core can juggle one or more threads.
11. **CPU (Central Processing Unit)** — The general-purpose "brain" of a computer, optimized to run varied, step-by-step tasks quickly. It handles AI's control logic and data preparation but does little of the heavy math in modern AI.
12. **Instruction set architecture (ISA)** — The "vocabulary" of commands a processor understands. Examples are x86 (Intel/AMD), Arm (phones, Apple Macs, NVIDIA Grace/Vera, Google Axion) and RISC-V (an open standard).
13. **Arm** — A company (and the ISA it licenses) whose energy-efficient CPU designs are used in nearly all phones and increasingly in data-center CPUs.
14. **RISC-V** — A free, open instruction set anyone can use without license fees. It is popular with startups and in some AI chips (e.g., Meta's MTIA, Tenstorrent).
15. **Moore's Law** — Gordon Moore's observation (1965; revised 1975) that the number of transistors on a chip doubles about every two years. It is an industry trend, not a law of physics.
16. **Dennard scaling** — The historical rule that smaller transistors used proportionally less power. It broke down in the mid-2000s, which ended rapid clock-speed increases and pushed chips toward parallelism.
17. **Von Neumann bottleneck** — The slowdown caused by having to shuttle data back and forth between separate processor and memory. It is the root of today's "memory wall."
18. **Parallelism** — Doing many operations at the same time instead of one after another. It is the central idea behind GPUs and AI accelerators.
19. **SIMD / SIMT** — "Single Instruction, Multiple Data / Threads": one command applied to many numbers at once, like a drill sergeant ordering a whole platoon to step forward.
20. **Latency** — How long one thing takes from start to finish (e.g., the time to fetch one piece of data or to get the first word of a chatbot answer).
21. **Throughput** — How much total work gets done per unit of time (e.g., tokens per second across all users).

### 2.2 The math of AI hardware
22. **Matrix** — A rectangular grid of numbers. Neural-network weights are stored as matrices.
23. **Matrix multiplication (matmul / GEMM)** — The core operation of neural networks: combining two grids of numbers by many multiply-and-add steps. GEMM ("general matrix multiply") is the technical name.
24. **Multiply-accumulate (MAC)** — One multiplication followed by adding the result to a running total. One MAC counts as 2 FLOPs.
25. **Tensor** — A generalization of a matrix to any number of dimensions (a list, a grid, a cube of numbers, and so on). It is the basic data object in AI software.
26. **FLOP (floating-point operation)** — One arithmetic operation (like a multiply or add) on decimal-style numbers. Used as a *count* of total work, e.g., "trained with 10^26 FLOP."
27. **FLOPS / FLOP/s** — Floating-point operations *per second*. A *speed*, e.g., an H100 delivers ~10^15 FLOP/s (1 petaFLOPS) in BF16.
28. **Tera / Peta / Exa / Zetta** — Prefixes for 10^12, 10^15, 10^18 and 10^21. An exaFLOP is a billion billion operations.
29. **TOPS** — Trillions of operations per second. It is usually quoted for integer math on phone/laptop NPUs and is not directly comparable to FLOPS.
30. **Peak vs. achieved performance** — Peak is the theoretical maximum on a spec sheet. Achieved is what real software gets (often 30–60% of peak for training).
31. **Dense vs. sparse FLOPS** — "Sparse" figures assume a special 2:4 pattern where half the numbers are zero and can be skipped, which doubles the headline number. Dense figures are the realistic baseline.
32. **Arithmetic intensity** — How many math operations are performed for each byte of data moved from memory. High intensity keeps compute busy; low intensity leaves it waiting on memory.
33. **Roofline model** — A chart showing whether a workload is limited by compute (flat "roof") or by memory bandwidth (sloped "roof"), based on its arithmetic intensity.
34. **Compute-bound / memory-bound** — Whether a task is slowed mainly by the speed of math or by the speed of fetching data.
35. **Scaling laws** — Empirical relationships showing that model quality improves predictably as compute, data and parameters increase. They are why companies buy ever-larger clusters.
36. **6ND rule** — Rule of thumb: training a dense transformer takes about 6 × (number of parameters) × (number of training tokens) FLOPs.
37. **Parameter** — One adjustable number (weight) inside a neural network. Frontier models have hundreds of billions to trillions.
38. **Token** — A chunk of text (roughly ¾ of an English word) that a language model reads or writes. It is the unit of both training data and inference billing.

### 2.3 Numbers and precision
39. **Floating point** — A way of storing numbers as sign + exponent (scale) + mantissa (significant digits), like scientific notation. It lets one format hold both tiny and huge values.
40. **Precision** — How many bits are used per number. More bits mean finer detail; fewer bits mean faster, cheaper math with more rounding error.
41. **Exponent / mantissa** — The exponent sets how big or small the number is (range). The mantissa sets how many significant digits it keeps (detail).
42. **FP64** — 64-bit "double precision," used in scientific simulation. It is mostly irrelevant for AI and increasingly de-emphasized on AI chips.
43. **FP32** — 32-bit "single precision." It was the original standard for neural-net training and is now mainly used for sensitive parts like optimizer state.
44. **TF32** — NVIDIA's 19-bit "TensorFloat-32" format (FP32 range, FP16-like detail), introduced with the A100 to speed up FP32-style math on tensor cores.
45. **FP16 (half precision)** — 16-bit floating point with 5 exponent bits. It is fast but has a small range, so it needs tricks ("loss scaling") during training.
46. **BF16 (bfloat16)** — Google's 16-bit "brain float" with the same range as FP32 (8 exponent bits) but less detail. It became the default for training large models.
47. **FP8 (E4M3 / E5M2)** — 8-bit floating-point formats introduced in hardware with NVIDIA Hopper. E4M3 favors detail; E5M2 favors range.
48. **FP6 / FP4** — 6- and 4-bit floating-point formats. FP4 (E2M1) can only represent 16 distinct values (such as 0, 0.5, 1, 1.5, 2, 3, 4, 6 and their negatives), so it relies on scaling tricks.
49. **Microscaling (MX) formats (MXFP8/MXFP6/MXFP4)** — An open industry standard (Open Compute Project) where each block of 32 small numbers shares one scale factor. This lets very low-bit numbers cover a wide range.
50. **NVFP4** — NVIDIA's 4-bit format (Blackwell and later) that uses smaller blocks of 16 values, each with an FP8 scale plus a tensor-wide scale, for better accuracy than plain FP4.
51. **INT8 / INT4** — 8- or 4-bit whole-number formats used mainly for inference after quantization.
52. **Quantization** — Converting a model's numbers to fewer bits (e.g., 16-bit → 4-bit) to save memory and speed up inference, ideally with little loss in quality.
53. **Mixed precision** — Doing most math in a low-precision format while keeping a few sensitive values (like a master copy of weights) in higher precision.

### 2.4 Accelerators and chip types
54. **Accelerator** — Any chip specialized to do a certain kind of work (here, AI math) much faster and more efficiently than a CPU.
55. **GPU (Graphics Processing Unit)** — A chip with thousands of simple cores, originally for rendering graphics. Its massive parallelism makes it the workhorse of AI.
56. **Streaming Multiprocessor (SM) / Compute Unit (CU)** — The repeated building block inside an NVIDIA (SM) or AMD (CU) GPU. Each contains many small cores, tensor cores and local memory.
57. **CUDA core** — NVIDIA's name for a GPU's basic arithmetic unit that handles general (non-matrix) math.
58. **Tensor core** — A specialized circuit inside NVIDIA GPUs (since Volta, 2017) that multiplies small matrices in one step. AMD's equivalent is the "Matrix Core"; Google's is the MXU.
59. **Systolic array** — A grid of multiply-add units where data pulses through neighbor-to-neighbor, like a bucket brigade, reusing each number many times. It is the heart of Google's TPU.
60. **ASIC (Application-Specific Integrated Circuit)** — A chip designed for one job. AI ASICs (TPU, Trainium, Maia, MTIA) trade flexibility for efficiency.
61. **TPU (Tensor Processing Unit)** — Google's family of AI ASICs, first deployed in 2015, now in its 8th generation (TPU 8t/8i).
62. **NPU (Neural Processing Unit)** — A small AI accelerator inside phones and laptops (e.g., Apple Neural Engine, Qualcomm Hexagon). It is rated in TOPS.
63. **LPU (Language Processing Unit)** — Groq's inference chip, which stores model weights in very fast on-chip SRAM and runs on a fixed, compiler-planned schedule.
64. **Wafer-scale engine** — Cerebras's approach of using an entire silicon wafer as one giant chip instead of cutting it into many small chips.
65. **FPGA (Field-Programmable Gate Array)** — A chip whose circuitry can be rewired after manufacturing. It is useful for prototyping and niche AI tasks.
66. **DPU (Data Processing Unit) / SuperNIC** — A network card with its own processors that offloads networking, storage and security work from the CPU (e.g., NVIDIA BlueField, AMD Pensando).
67. **Superchip** — NVIDIA's term for a CPU and GPU(s) tightly linked on one board (e.g., Grace + 2 Blackwell = GB200; Vera + 2 Rubin).
68. **Chiplet** — A smaller die designed to be combined with others in one package, rather than building one huge die. It improves yield and lets companies mix process technologies.
69. **Reticle limit** — The maximum area (~26 mm × 33 mm ≈ 858 mm²) that a lithography machine can print in one exposure. It caps the size of a single die.
70. **TDP / TBP (thermal design power / total board power)** — The power a chip or card is designed to draw and dissipate, e.g., 700 W for an H100 SXM and ~1,400 W for an MI355X.
71. **Form factor (SXM, OAM, PCIe card)** — The physical shape and connector of an accelerator module. SXM (NVIDIA) and OAM (open standard) are high-power mezzanine modules; PCIe cards plug into standard slots.

### 2.5 Memory
72. **Memory hierarchy** — The layered set of storage from tiny-and-instant (registers) to huge-and-slow (disks). Each layer is bigger, slower and cheaper per byte.
73. **Register** — The handful of storage slots inside a core where numbers sit while being computed on. It is the fastest memory there is.
74. **SRAM (static RAM)** — Very fast, expensive, power-hungry memory built from transistors on the chip itself. It is used for caches and, in some AI chips (Groq, Cerebras), as main memory.
75. **Cache (L1/L2/L3)** — Small SRAM stores near the cores that keep recently used data close at hand to avoid slow trips to main memory.
76. **DRAM** — Dynamic RAM: dense, cheaper memory using tiny capacitors that must be constantly refreshed. It is the main memory of computers.
77. **HBM (High Bandwidth Memory)** — DRAM chips stacked vertically (8–16 high) and placed right beside the processor with a very wide connection, delivering terabytes per second. It is the critical memory of AI accelerators.
78. **HBM3E / HBM4 / HBM4E** — Successive HBM generations. HBM4 (JEDEC standard April 2025) doubles the interface width to 2,048 bits and is used in NVIDIA Rubin and AMD MI400.
79. **TSV (through-silicon via)** — A vertical wire drilled through a silicon die that connects stacked dies. It is how HBM stacks are wired together.
80. **Base die (logic die)** — The bottom die of an HBM stack that manages communication with the processor. With HBM4 it can be customized and made at a logic foundry.
81. **GDDR / LPDDR** — Other DRAM types. GDDR is fast graphics memory on gaming cards (also used in NVIDIA Rubin CPX); LPDDR is low-power memory in phones, laptops and server CPUs like Grace/Vera.
82. **Unified memory** — A design (e.g., Apple silicon, NVIDIA GB10/DGX Spark) where CPU and GPU share one pool of memory, letting large models fit without copying.
83. **Memory bandwidth** — How many bytes per second can move between memory and the processor (e.g., 8 TB/s for a B200). It is often the true limit on AI speed.
84. **Memory capacity** — How many bytes the memory can hold (e.g., 288 GB per Rubin GPU). It determines what model sizes and context lengths fit.
85. **Memory wall** — The long-running gap where processors' math speed grows faster than memory's ability to feed them, so chips increasingly wait on data.
86. **KV cache** — Memory that stores intermediate results (keys and values) for every previous token in a conversation so the model doesn't recompute them. It grows with context length and number of users.
87. **NAND flash / SSD** — Non-volatile storage that keeps data with power off. It holds datasets and checkpoints and is much slower than DRAM.

### 2.6 Interconnects and networking
88. **Interconnect** — Any link that moves data between chips, boards, racks or buildings.
89. **Bus** — A shared data highway inside or between components.
90. **PCIe (PCI Express)** — The standard connector inside servers linking CPUs to GPUs, NICs and SSDs. Each new version roughly doubles speed (PCIe 5.0 ≈ 64 GB/s per direction for 16 lanes; PCIe 6.0 doubles that).
91. **SerDes** — Serializer/deserializer circuits that turn parallel data into very fast single-lane signals and back. They are the building blocks of every high-speed link.
92. **NVLink** — NVIDIA's high-speed GPU-to-GPU link, far faster than PCIe (e.g., 900 GB/s per GPU on Hopper, 1.8 TB/s on Blackwell).
93. **NVSwitch** — A switch chip that lets every GPU in an NVLink domain talk to every other GPU at full NVLink speed.
94. **NVLink domain / scale-up domain** — The group of accelerators connected by the ultra-fast, memory-like fabric (72 GPUs in an NVL72 rack). Inside it, GPUs can directly read each other's memory.
95. **NVL72** — NVIDIA's rack-scale system with 72 GPUs (and 36 CPUs) linked by NVLink into one domain. It is liquid-cooled and roughly 120–140 kW.
96. **NVLink-C2C** — NVIDIA's chip-to-chip link joining CPU and GPU in a superchip (e.g., Grace–Blackwell, Vera–Rubin).
97. **NVLink Fusion** — NVIDIA's program letting other companies' CPUs or accelerators connect to NVLink fabrics (AWS says Trainium4 will support it).
98. **Scale-up vs. scale-out** — Scale-up means making one tightly coupled unit bigger (more GPUs in one NVLink domain). Scale-out means connecting many such units over a network.
99. **InfiniBand** — A low-latency, high-bandwidth networking technology long dominant in supercomputers and AI clusters (NVIDIA Quantum switches).
100. **Ethernet** — The world's standard networking technology, now adapted for AI back-ends (e.g., NVIDIA Spectrum-X, Broadcom Tomahawk).
101. **RDMA / RoCE** — Remote Direct Memory Access lets one machine read or write another's memory without involving its CPU. RoCE is RDMA over Converged Ethernet.
102. **Ultra Ethernet (UEC)** — An industry consortium and specification (1.0 released June 2025) that tunes Ethernet for AI and HPC traffic.
103. **UALink** — "Ultra Accelerator Link," an open scale-up standard (1.0 in April 2025) backed by AMD, Intel, Google, Meta, Microsoft and others as an alternative to NVLink.
104. **NIC (Network Interface Card)** — The card that connects a server to the network (e.g., NVIDIA ConnectX-8/9 at 800 Gb/s).
105. **Switch** — A box that routes data between many connected machines. AI clusters use thousands of them in layered tiers.
106. **Topology** — The wiring pattern of a network. Examples: fat-tree/Clos (layers of switches), torus (each chip linked to neighbors in a grid that wraps around, used by TPUs), and dragonfly (groups fully linked to each other).
107. **Rail-optimized network** — A cluster design where GPU #1 of every server connects to the same switch "rail," GPU #2 to another, and so on, minimizing hops for collective operations.
108. **Bisection bandwidth** — The total bandwidth across a cut that splits the network into two halves. It measures how well the whole cluster can talk at once.
109. **Optical transceiver** — A pluggable module that converts electrical signals to laser light for fiber (e.g., 800G and 1.6T modules). Clusters use millions of them.
110. **Co-packaged optics (CPO)** — Putting the optical converters right next to the switch or GPU chip instead of in pluggable modules, saving power and improving reliability.
111. **Optical circuit switch (OCS)** — A switch that redirects light beams with tiny mirrors, without converting to electricity. Google uses OCS to reconfigure TPU pods.
112. **Copper vs. fiber** — Copper cables are cheap and low-power but only reach a few meters at top speeds. Fiber reaches kilometers but needs power-hungry transceivers.
113. **Front-end vs. back-end network** — The front-end connects servers to users and storage. The back-end (compute fabric) carries accelerator-to-accelerator training traffic.

### 2.7 Systems and clusters
114. **Node / server** — One computer, typically 4–8 GPUs plus CPUs, memory, NICs and storage.
115. **HGX / DGX** — NVIDIA's 8-GPU baseboard design sold to server makers (HGX), and NVIDIA's own branded complete systems (DGX).
116. **Rack** — A standardized cabinet (~2 m tall) holding servers, switches, power shelves and cooling. AI racks now draw 100+ kW.
117. **Pod / SuperPOD** — A pre-designed group of racks wired together as one training unit (e.g., a TPU pod of 9,216 Ironwood chips).
118. **Cluster** — A large collection of nodes networked together to work on shared jobs. Frontier AI clusters have 100,000 to over 1,000,000 accelerators.
119. **AI factory** — NVIDIA's marketing term for a data center whose product is tokens (AI outputs), emphasizing throughput and cost per token.
120. **Liquid cooling (direct-to-chip)** — Cooling by pumping liquid through metal cold plates mounted on chips. It is required for the densest AI racks (e.g., GB200/GB300 NVL72).
121. **H100-equivalent (H100e)** — A unit used by analysts (e.g., Epoch AI) to compare clusters of different chips by converting their compute to the number of H100s that would match it.

### 2.8 Distributed training
122. **Distributed training** — Splitting one model's training across many accelerators that must coordinate constantly.
123. **Data parallelism (DP)** — Every GPU holds a full copy of the model and processes different data. GPUs then average their gradients.
124. **ZeRO / FSDP** — Techniques (Microsoft DeepSpeed's ZeRO; PyTorch's Fully Sharded Data Parallel) that split ("shard") optimizer states, gradients and weights across GPUs so each holds only a slice, saving memory.
125. **Tensor parallelism (TP)** — Splitting individual matrix multiplications across several GPUs. It needs very fast links, so it is usually kept inside an NVLink domain.
126. **Pipeline parallelism (PP)** — Splitting the model's layers into stages on different GPUs, like an assembly line. Idle "bubbles" occur while the pipeline fills and drains.
127. **Sequence / context parallelism** — Splitting a very long input sequence across GPUs so long-context training fits in memory.
128. **Expert parallelism (EP)** — In mixture-of-experts models, placing different "experts" on different GPUs and routing each token to the right one.
129. **Mixture of Experts (MoE)** — A model design where only a few of many sub-networks ("experts") activate for each token, so total parameters can be huge while compute per token stays modest.
130. **Collective communication** — Coordinated data exchanges among many GPUs, such as all-reduce, all-gather, reduce-scatter and all-to-all.
131. **All-reduce** — A collective in which every GPU contributes numbers (e.g., gradients), they are summed, and everyone receives the total. It is the backbone of data-parallel training.
132. **All-to-all** — Every GPU sends a different chunk to every other GPU. It is used heavily by MoE expert routing.
133. **NCCL / RCCL** — NVIDIA's (and AMD's) libraries that perform collective communication efficiently over NVLink and networks.
134. **Gradient** — The direction and size of the adjustment for each parameter computed during training.
135. **Optimizer state** — Extra numbers per parameter (e.g., Adam's running averages) kept during training. Often larger than the model itself.
136. **Checkpoint** — A saved snapshot of the model and optimizer state so training can resume after a failure.
137. **Straggler** — A slow GPU or node that holds back thousands of others waiting for it at a synchronization point.
138. **MFU (Model FLOPs Utilization)** — The fraction of the hardware's peak FLOPS that goes into the model's necessary math. 35–50% is typical for large training runs.
139. **Goodput** — The share of total cluster time that produces useful training progress after subtracting failures, restarts and waiting.
140. **Job interruption / failure rate** — How often a training run halts. At large scale, hardware faults happen every few hours or more often.

### 2.9 Inference
141. **Inference** — Running a trained model to produce outputs (answers, images). It is what happens every time you chat with an AI.
142. **Prefill** — The phase where the model reads your whole prompt at once. It is compute-heavy and highly parallel.
143. **Decode** — The phase where the model generates one token at a time. Each step re-reads the model weights, so it is usually memory-bandwidth-bound.
144. **Batching / continuous batching** — Serving many users' requests together so each read of the weights is shared, raising throughput.
145. **Time to first token (TTFT)** — How long until the first word of a response appears. It is mainly set by prefill.
146. **Tokens per second (per user / per GPU)** — Speed of generation as seen by one user (interactivity) vs. total output across all users on a chip (throughput).
147. **Speculative decoding** — Using a small fast "draft" model to guess several tokens that the big model then verifies in one step, speeding up generation.
148. **Disaggregated serving** — Running prefill and decode on different (sometimes different kinds of) chips, each optimized for its phase (e.g., NVIDIA Dynamo; Rubin CPX for prefill; Groq LPX for decode).
149. **Cost per million tokens** — The price (or internal cost) to generate a million tokens. It is the core unit of AI inference economics.
150. **TCO (total cost of ownership)** — All costs of running hardware over its life: purchase, power, cooling, space, networking, staff and depreciation.

### 2.10 Manufacturing and industry
151. **Wafer** — A thin, round slice of ultra-pure silicon (today 300 mm across) on which hundreds of chips are made at once.
152. **Fab (fabrication plant)** — A factory that manufactures chips on wafers in ultra-clean rooms. A leading-edge fab costs on the order of $20 billion or more.
153. **Foundry** — A company that manufactures chips designed by others (TSMC, Samsung Foundry, Intel Foundry, SMIC).
154. **Fabless** — A chip company that designs chips but outsources manufacturing (NVIDIA, AMD, Broadcom, Qualcomm, Apple).
155. **IDM (integrated device manufacturer)** — A company that both designs and manufactures its own chips (Intel, Samsung, and memory makers).
156. **Process node (e.g., N3, N2, A16, 18A)** — A generation of manufacturing technology. The names ("3 nm," "2 nm") are marketing labels, not the physical size of any feature.
157. **FinFET** — A 3D transistor shape (2011 onward) where the channel is a vertical fin wrapped by the gate on three sides for better control.
158. **Gate-all-around (GAA) / nanosheet** — The next transistor shape (TSMC N2, Intel 18A "RibbonFET," Samsung 3 nm) where the gate fully surrounds stacked horizontal sheets of silicon.
159. **Backside power delivery** — Moving the power wires to the back of the wafer so the front can be used for signal wiring (Intel "PowerVia," TSMC A16 "Super Power Rail").
160. **Photolithography** — Printing circuit patterns by shining light through a patterned mask onto a light-sensitive coating on the wafer.
161. **DUV (deep ultraviolet) lithography** — Lithography using 193 nm light. It is widely used and can make 7 nm-class chips with multiple exposures.
162. **EUV (extreme ultraviolet) lithography** — Lithography using 13.5 nm light generated by blasting tin droplets with a laser. ASML is the only supplier, and each tool costs ~$180M+.
163. **High-NA EUV** — The next generation of EUV tools (numerical aperture 0.55 vs. 0.33) that can print features ~1.7× smaller in one exposure. It costs roughly twice as much as standard EUV [price: verify].
164. **Multi-patterning** — Exposing the same layer multiple times to print features finer than the light could manage in one pass. It costs more and lowers yield; China relies on it without EUV.
165. **Yield** — The percentage of chips on a wafer that work. Large dies have lower yields because each defect ruins a bigger area.
166. **Binning** — Sorting finished chips by how well they perform and selling partially defective or slower ones as lower-tier products.
167. **Advanced packaging** — Techniques to combine multiple dies (logic, HBM) in one package with dense connections, such as TSMC CoWoS, SoIC, Intel EMIB/Foveros.
168. **CoWoS (Chip-on-Wafer-on-Substrate)** — TSMC's 2.5D packaging that places GPU dies and HBM stacks side by side on a silicon interposer. Its capacity has been a key AI supply bottleneck.
169. **Interposer** — A thin slab of silicon (or organic material with silicon bridges) with dense wiring that connects dies sitting on top of it.
170. **Hybrid bonding** — Directly fusing copper pads of two stacked dies without solder bumps, enabling ultra-dense 3D connections.
171. **UCIe** — "Universal Chiplet Interconnect Express," an open standard for connecting chiplets from different vendors inside one package.
172. **OSAT** — Outsourced semiconductor assembly and test companies (e.g., ASE, Amkor) that package and test chips.
173. **EDA (electronic design automation)** — The software used to design chips (Synopsys, Cadence, Siemens). No modern chip can be designed without it.
174. **Tape-out** — The moment a chip design is finalized and sent to the foundry for manufacturing.
175. **ODM (original design manufacturer)** — Companies (Foxconn, Quanta, Wistron, Wiwynn) that build servers and racks for cloud providers.
176. **Hyperscaler** — The giant cloud companies (Amazon, Microsoft, Google, Meta, Oracle) that buy most AI hardware.
177. **Neocloud** — Newer GPU-focused cloud providers (e.g., CoreWeave, Nebius, Lambda, Crusoe) that rent AI compute.
178. **CUDA** — NVIDIA's programming platform (since 2006–07) for running general computations on its GPUs. Its large ecosystem is NVIDIA's biggest competitive "moat."
179. **ROCm** — AMD's open-source software platform, its answer to CUDA.
180. **Kernel (GPU kernel)** — A small program that runs on the GPU to perform one operation (e.g., a matrix multiply or attention). Writing fast kernels is a prized skill.
181. **Compiler (XLA, Triton, torch.compile)** — Software that translates high-level model code into efficient instructions for a specific chip.
182. **Export controls** — Government rules limiting which chips, tools or technology can be sold to which countries. The US uses them to restrict China's access to advanced AI chips and chipmaking equipment.
183. **TPP (Total Processing Performance)** — The US export-control metric for a chip's power (roughly peak operations × bit length). The January 2026 H200 policy covers chips with TPP below 21,000.
184. **Entity List** — A US government list of foreign companies that need special licenses to receive US technology (e.g., Huawei, SMIC).
185. **CHIPS and Science Act** — 2022 US law providing ~$52.7B (including ~$39B in manufacturing incentives) plus tax credits to bring chipmaking back to the US.

---
## 3. Prerequisites and dependencies

**Core chains (each arrow means "must be taught before"):**

- Bits → binary numbers → *floating point (exponent + mantissa)* → precision formats (FP32 → BF16 → FP8 → FP4) → quantization → low-precision training and inference economics.
- Transistor → logic gates → arithmetic circuits → clock and cores → CPU → *why clocks stopped scaling (Dennard)* → parallelism → GPU → tensor cores/systolic arrays → accelerator zoo.
- Neural network = weights + matrix multiplication (from the ML chapters) → MAC/FLOP → FLOPS → peak vs. achieved → MFU.
- Memory vs. compute (von Neumann) → memory hierarchy → bandwidth vs. capacity → arithmetic intensity/roofline → memory wall → HBM → why decode is memory-bound → KV cache → inference economics.
- Parameters and tokens (from the LLM chapter) → 6ND training FLOPs → training-time and cluster-size estimates → cost of frontier runs.
- Memory needs of training (weights + gradients + optimizer + activations) → *why one GPU is not enough* → parallelism strategies → collective communication → interconnect tiers (NVLink vs. InfiniBand/Ethernet) → network topology → cluster design.
- Chip → package (die, HBM, interposer) → board/server → rack (NVL72) → pod → cluster → data center (handoff to data-center/energy chapter).
- Wafer → lithography → process node → yield/reticle limit → chiplets → advanced packaging (CoWoS) → supply chain bottlenecks → geopolitics/export controls.

**Dependency table:**

| Concept | Needs first |
|---|---|
| FLOPS and training compute | Matrix multiply, MAC, scientific notation |
| Tensor cores / systolic arrays | Matrix multiply, parallelism, data reuse |
| Precision formats | Bits, floating point, range vs. detail |
| Roofline / memory wall | FLOPS, bandwidth, arithmetic intensity |
| HBM | DRAM, bandwidth, packaging basics |
| Inference speed (tokens/s) | Decode, KV cache, memory bandwidth, batching |
| Cost per token | Tokens/s, GPU-hour pricing, utilization |
| NVLink vs. InfiniBand | Bandwidth, latency, scale-up vs. scale-out |
| Parallelism strategies | Training memory budget, gradients, interconnect tiers |
| All-reduce / all-to-all | Data parallelism, MoE |
| MFU, goodput | Peak FLOPS, failures, checkpointing |
| Process nodes | Transistor, lithography; node names are labels |
| EUV / High-NA | Light wavelength and resolution (simple optics) |
| Yield and chiplets | Defects, die area, reticle limit |
| CoWoS bottleneck | Interposer, HBM, chiplets |
| Export-control thresholds (TPP) | FLOPS, precision (bit length), bandwidth |
| China's chip strategy | Lithography (DUV vs. EUV), multi-patterning, HBM supply |
| Edge AI limits | Memory capacity, bandwidth, quantization, power |
| Roadmap literacy (Rubin, MI450, TPU 8) | All of the above; dense vs. sparse; rack vs. chip numbers |

**Cross-chapter hooks:** This chapter needs *neural networks, parameters, tokens, transformers, attention, MoE* from the ML/LLM chapters. It feeds *data centers, power and cooling, energy, AI economics and policy*.

---

## 4. Current state and key facts (2025–2026)

> Read every spec with three questions: *Which precision? Dense or sparse? Per chip, per package, or per rack?* Vendors also revise numbers between announcement and shipment, and Vera Rubin below is a live example.

### 4.1 NVIDIA

**Business scale.**
- In Q2 of fiscal 2027 (the quarter ended July 26, 2026; reported Aug 26, 2026), NVIDIA reported total revenue of **$96.2B** (+106% year over year) and **Data Center revenue of $89.0B** (+117% YoY).
  - GAAP gross margin was 75.0% and GAAP net income $59.7B.
  - The Q3 FY27 outlook is **$108B ±2%**. It assumes **no** data-center compute revenue from China.
  - Vera Rubin is "ramping into full production," with racks running at CoreWeave, Google Cloud, Microsoft Azure, Oracle Cloud Infrastructure and Nebius.
  - The Groq 3 LPX inference accelerator is in full production, and Spectrum-6 switches with co-packaged-optics support are arriving at sites.
  - Source: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027 ; summary at https://theenergymag.com/news/market-news/nvidia-q2-revenue-hits-96-2-b-as-data-center-surges-117-and-vera-rubin-ramps
- At GTC 2026 (March 16, 2026), NVIDIA said combined Blackwell + Vera Rubin purchase orders target **~$1 trillion through 2027** (https://www.jonpeddie.com/news/nvidia-gtc-2026-keynote/).

**Product generations (teaching table; vendor peak specs):**

| Generation (year) | Key part | Memory | Notable |
|---|---|---|---|
| Volta (2017) | V100 | 16/32 GB HBM2 | First tensor cores |
| Ampere (2020) | A100 | 40/80 GB HBM2e, ~2 TB/s | TF32, BF16, 2:4 sparsity |
| Hopper (2022) | H100 SXM | 80 GB HBM3, 3.35 TB/s | FP8 + Transformer Engine; ~989 TFLOPS dense BF16; 700 W; 80B transistors (TSMC 4N) |
| Hopper refresh (2024) | H200 | 141 GB HBM3E, 4.8 TB/s | Same compute, more and faster memory |
| Blackwell (2024–25) | B200 / GB200 | 192 GB HBM3E (180 GB usable in some systems), 8 TB/s | Two reticle-size dies acting as one GPU; 208B transistors; FP4; NVLink 5 at 1.8 TB/s per GPU; GB200 NVL72 rack |
| Blackwell Ultra (2H 2025) | B300 / GB300 | 288 GB HBM3E (12-high), 8 TB/s | ~15 PFLOPS dense FP4 per GPU; GB300 NVL72 rack = 1.1 EF dense FP4 (1.44 EF sparse), 20 TB HBM, 130 TB/s NVLink, 2,592 Grace Arm cores |
| Vera Rubin (2026) | Rubin GPU + Vera CPU, VR NVL72 | 288 GB HBM4 per GPU | 336B transistors, TSMC N3; 50 PFLOPS NVFP4 inference (sparse), 35 PFLOPS NVFP4 training (dense), 17.5 PF FP8 dense, 4 PF BF16 dense per GPU |
| Rubin Ultra (2H 2027) | Kyber rack | HBM4E | GTC 2025 plan: "NVL576" (counting dies), 15 EF FP4 inference, 5 EF FP8, ~600 kW rack |
| Feynman (2028) | — | "Custom HBM" | Previewed GTC 2026: reported 3D die stacking, TSMC A16, new "Rosa" CPU, new LPU; Kyber rack scaled further (reported) |

- **GB300 NVL72 rack-level specs** (NVIDIA page): 72 Blackwell Ultra GPUs + 36 Grace CPUs.
  - FP4 1,440 PF (sparse) / 1,080 PF (dense); FP8 720 PF; BF16 360 PF.
  - 20 TB HBM at up to 576 TB/s; 130 TB/s NVLink; 37 TB "fast memory."
  - Source: https://www.nvidia.com/en-us/data-center/gb300-nvl72/
- **Vera Rubin NVL72** (NVIDIA product page, fetched Oct 2026): 3,600 PF NVFP4 inference (sparse); 2,520 PF NVFP4 training (dense); 1,260 PF FP8; 288 PF BF16.
  - 20.7 TB HBM4; Vera CPU = 88 custom Arm "Olympus" cores; up to 54 TB LPDDR5X per rack.
  - The page says "Available Now." Source: https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/
  - **Spec drift:**
    - CES 2026 launch coverage cited **22 TB/s HBM4 per GPU** and **3.6 TB/s NVLink 6 per GPU (260 TB/s per rack)** (https://www.storagereview.com/news/nvidia-launches-vera-rubin-architecture-at-ces-2026-the-vr-nvl72-rack).
    - The current product page lists **19.2 TB/s** per GPU (1,400 TB/s per rack) and **3 TB/s NVLink per GPU (216 TB/s per rack)**.
    - This makes a good teaching example of why to check the vendor's current spec sheet.
  - NVIDIA's own projected claims vs. GB200: up to 10× lower cost per million tokens for agentic inference, and MoE training with ¼ the GPUs.
- **Naming note:** At GTC 2025 NVIDIA said Rubin racks would be called "NVL144" (counting GPU *dies*). The shipping product is branded **NVL72** (counting packages). Rubin Ultra was announced as "NVL576" (https://www.networkworld.com/article/3848394/nvidia-details-its-gpu-cpu-and-system-roadmap-for-the-next-three-years.html), and GTC 2026 coverage describes Kyber as 144 GPU packages per NVLink domain.
- **Rubin platform = six new chips:** Vera CPU, Rubin GPU, NVLink 6 switch, ConnectX-9 SuperNIC, BlueField-4 DPU and Spectrum-6 Ethernet switch (https://www.techbriefs.com/component/content/article/54442-ces-2026-nvidia-unveils-new-six-chip-rubin-ai-platform).
- **Groq deal and LPX:**
  - In late Dec 2025 NVIDIA paid a reported ~$20B for a *non-exclusive license* to Groq's inference technology and hired its leadership (CEO Jonathan Ross). Groq stayed independent and GroqCloud kept running (https://www.fierce-network.com/cloud/heres-why-nvidia-dropping-20b-groqs-ai-tech).
  - At GTC 2026, NVIDIA introduced the **Groq 3 LPU / LPX rack**: 256 LPUs per rack. Per chip: ~500 MB SRAM, ~150 TB/s SRAM bandwidth, ~1.2 PF FP8.
  - It is positioned for low-latency token generation alongside Vera Rubin (which holds the KV cache), and NVIDIA claims up to 35× throughput per megawatt at high interactivity (https://www.eetimes.com/gtc-2026-keynote-long-live-the-inference-king/).
- **Rubin CPX** (announced Sept 2025): a GDDR7-based GPU for long-context *prefill*. Its 2026 status was not confirmed in this research pass [verify].
- **Edge/desktop parts:** DGX Spark (GB10, 128 GB unified memory; shipped Oct 2025) [verify price/specs]. "RTX Spark," a 1-petaflop Windows PC superchip with Microsoft, launched per the Q2 FY27 release.
- **CUDA moat:** CUDA has been available since 2006–07. NVIDIA's libraries (cuBLAS, cuDNN, NCCL, TensorRT-LLM, Dynamo) and nearly two decades of developer habit are why rival hardware with competitive specs still struggles. MLPerf Training 6.0 (2026): NVIDIA says Blackwell led every category (Q2 FY27 release).

### 4.2 AMD

- **MI300X (Dec 2023):** 192 GB HBM3, 5.3 TB/s; 153B transistors; chiplet design. **MI325X (late 2024):** 256 GB HBM3E, 6 TB/s.
- **MI350X / MI355X (shipping 2H 2025, CDNA 4):**
  - 288 GB HBM3E, 8 TB/s; **10.1 PFLOPS dense MXFP4** (20.1 sparse); MXFP6/MXFP4 support; **1,400 W** (MI355X, liquid-cooled).
  - Sources: https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html ; https://www.theregister.com/2025/06/12/amd_mi355x/
- **MI400 family (2026, CDNA 5):**
  - **MI455X**: ~40 PF dense FP4, ~20 PF FP8, **432 GB HBM4**, 19.6 TB/s (a later AMD briefing cited up to 23.3 TB/s), 3.6 TB/s scale-up bandwidth; TSMC 2 nm/3 nm chiplets.
  - **MI430X** targets mixed HPC (FP64) and AI. MI440X comes in an 8-GPU box.
  - Sources: https://www.theregister.com/2026/01/07/mi500x_amd_ai/ ; https://www.digitalcitizen.life/amd-instinct-mi455x-brings-432gb-of-hbm4-and-40-pflops-of-ai-compute-to-helios/
- **Helios rack:**
  - 72 MI455X + EPYC "Venice" (2 nm, up to 256 Zen 6 cores) + Pensando "Vulcano" NICs; Meta's Open Rack Wide form factor; UALink tunneled over Ethernet.
  - Rack totals: 2.9 EF dense FP4, 1.4 EF FP8, 31 TB HBM4, ~1.4 PB/s.
  - Shipments begin 2H 2026 and ramp through 2027. AMD claims up to 30% more tokens per dollar than a Rubin NVL72 (a vendor claim). Source: https://www.datacenterfrontier.com/machine-learning/news/55399746/amd-helios-takes-ai-infrastructure-fight-to-rack-scale
- **MI500 (2027):** CDNA 6, TSMC 2 nm, HBM4E.
- **OpenAI–AMD (Oct 6, 2025):** a multi-generation **6 GW** agreement, starting with **1 GW of MI450 in 2H 2026**. It includes a warrant giving OpenAI the right to buy up to 160M AMD shares [verify warrant detail] (https://www.igorslab.de/en/amd-helios-in-production-mi455x-epyc-venice-openai-challenge-nvidia-ai-racks/).

### 4.3 Google TPUs

- **History:**
  - v1 (2015, 28 nm, INT8 inference, 256×256 systolic array) → v2 (2017, added BF16, HBM) → v3 (2018) → v4 (2021, 4,096-chip pods with optical circuit switches).
  - Then v5e/v5p (2023) → Trillium/v6e (2024; 918 TFLOPS BF16, 32 GB HBM, 256-chip pods).
  - Source: https://en.wikipedia.org/wiki/Tensor_Processing_Unit
- **Ironwood (TPU v7):**
  - Announced April 2025; GA announced Nov 2025; "now generally available" per Cloud Next 2026.
  - **4,614 TFLOPS FP8**, **192 GB HBM3E at 7.37 TB/s**, pods of 256 or **9,216 chips** (42.5 EF FP8 per pod, 1.77 PB of HBM).
  - Sources: https://www.theregister.com/2025/04/10/googles_7thgen_ironwood_tpus_debut/ ; https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next26
- **TPU 8 (announced Cloud Next, April 22, 2026), split into training and inference chips:**
  - **TPU 8t (training):** 12.6 PF FP4, 216 GB HBM, 6.5 TB/s, 128 MB on-chip SRAM, 3D torus.
    - Up to **9,600 chips / 2 PB HBM per superpod**; ~3× Ironwood processing power; up to 2.7× training price-performance.
    - The **Virgo** fabric links 134,000+ TPU 8t chips (47 Pb/s bisection), and Google says JAX/Pathways can scale past **1 million TPU chips** in one training cluster.
  - **TPU 8i (inference):** 10.1 PF FP4, 288 GB HBM, 8.6 TB/s, **384 MB SRAM** (3× prior), "Boardfly" topology connecting 1,152 chips, and a Collectives Acceleration Engine. It claims up to 80% better inference price-performance.
  - Arm Axion host CPUs. Process node and power were not disclosed.
  - Source: https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive
- **Anthropic–Google (Oct 2025):** access to **up to 1 million TPUs**, worth tens of billions of dollars, bringing well over 1 GW online in 2026 (https://www.maginative.com/article/anthropic-secures-1m-google-tpus-while-keeping-amazon-as-primary-training-partner/).
- Google also offers NVIDIA systems and said it will be among the first to offer Vera Rubin NVL72.

### 4.4 Amazon (AWS)

- **Trainium2:** Trn2 UltraServers of 64 chips. **Project Rainier** (Indiana) for Anthropic was activated Oct 2025 with ~500,000 Trainium2 chips [verify count].
- **Trainium3 (GA Dec 2025):** AWS's first **3 nm** AI chip.
  - **144 GB HBM3E, 4.9 TB/s** per chip; Trn3 UltraServer = **144 chips, 362 PF MXFP8** (≈2.5 PF FP8 per chip), 20.7 TB HBM3E, 706 TB/s aggregate.
  - Up to 4.4× compute and 4× energy efficiency vs. Trn2 UltraServers; NeuronSwitch-v1 fabric.
  - UltraClusters 3.0 can scale to very large counts (AWS has cited up to 1M chips).
  - Sources: https://aws.amazon.com/ai/machine-learning/trainium/ ; https://press.aboutamazon.com/2025/12/trainium3-ultraservers-now-available-enabling-customers-to-train-and-deploy-ai-models-faster-at-lower-cost
- **Trainium4** will support **NVIDIA NVLink Fusion** (https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap).

### 4.5 Microsoft, Meta, OpenAI and other custom silicon

- **Microsoft Maia 200 (Jan 2026):** TSMC 3 nm; reported 216 GB HBM3E at 7 TB/s, 272 MB on-die SRAM, ~10 PF FP4 / ~5 PF FP8; Ethernet-based scale-up to 6,144 accelerators.
  - It is deployed in Iowa (then Arizona) for Microsoft 365 Copilot and OpenAI models. Microsoft claims 30% better perf/$ than its existing fleet.
  - A Maia 300 successor was reported for late 2026 [verify].
  - Source: https://www.trendforce.com/news/?p=52402 ; https://tbreak.com/microsoft-maia-200-a-custom-ai-accelerator/
- **Meta MTIA:** RISC-V-based inference accelerators (MTIA v1, v2/"2i"). A 2025 ISCA paper reported 44% lower TCO than GPUs on specific inference tasks.
  - Meta acquired RISC-V startup **Rivos** (~$2B valuation; announced fall 2025) to accelerate MTIA, including toward training (https://www.barchart.com/story/news/35149291/meta-meta-expands-ai-chip-ambitions-with-2-billion-rivos-acquisition).
- **OpenAI–Broadcom (Oct 13, 2025):** OpenAI designs and Broadcom develops custom accelerators plus Ethernet networking, for **10 GW** deployed from **2H 2026 through 2029** (https://www.maginative.com/article/openai-and-broadcom-to-co-design-custom-ai-chips-deploy-10-gw-by-2029/). First-deployment status as of Oct 2026 was not confirmed here.
- **OpenAI–NVIDIA (Sept 2025 letter of intent):** at least 10 GW of NVIDIA systems, with NVIDIA intending to invest up to $100B progressively; the first GW is on Vera Rubin in 2H 2026. Later reports suggested the terms were restructured [verify].
- **Anthropic–Microsoft–NVIDIA (Nov 2025):** Anthropic committed ~$30B of Azure compute (up to 1 GW on NVIDIA Grace Blackwell/Vera Rubin), with NVIDIA and Microsoft investing up to $10B and $5B respectively [verify exact figures].
- **Intel:**
  - Gaudi 3 (2024; 128 GB HBM2e) had limited traction. Intel announced "Crescent Island," an inference GPU with 160 GB LPDDR5X, for 2H 2026 sampling [verify].
  - Intel 18A (RibbonFET GAA + PowerVia backside power) entered products with Panther Lake (launched around CES 2026) [verify].
  - The **US government took a 9.9% stake** (433.3M shares at $20.47, Aug 2025) and **NVIDIA invested $5B** (Sept 2025) to co-develop x86 CPUs with NVLink and PC chips. Intel also invested in SambaNova (cleared May 2026).
  - Source: https://en.wikipedia.org/wiki/Intel
- **Design partners:** Broadcom (Google TPU, Meta, OpenAI), Marvell (AWS, Microsoft), MediaTek (reported for TPU 8i [verify]), Alchip/GUC (Taiwan).

### 4.6 Alternative architectures

- **Cerebras:** WSE-3 is a single wafer-scale chip, **46,225 mm², 4 trillion transistors, 900,000 cores**. The original WSE-3 had 44 GB on-chip SRAM and ~125 PF peak (sparse FP16).
  - The current page lists a WSE-3T at 250 PF and a CS-4 system of three WSE-3T [vendor claims] (https://www.cerebras.ai/chip).
  - It is strong at fast inference (thousands of tokens/s per user) because weights stream from SRAM.
- **Groq:** The LPU stores weights in on-chip SRAM (~230 MB per first-generation chip) and uses a compiler-scheduled, deterministic design. It needs hundreds of chips for a large model. Its technology is now licensed to NVIDIA (above).
- **SambaNova (SN40L RDU):** reconfigurable dataflow with three memory tiers (SRAM, HBM, DDR) to hold many models at once. Intel invested in 2026.
- **Etched (Sohu):** an ASIC hard-wired for transformer inference. It is a bet that architectures won't change.
- **Tenstorrent (Blackhole; CEO Jim Keller):** RISC-V cores with an open-source software stack; licenses IP.
- **d-Matrix (Corsair):** digital in-memory compute for inference.
- **Photonic interconnect:** Lightmatter, Ayar Labs, Celestial AI and others work on optical I/O.
- Chinese entrants: Cambricon, Hygon, Moore Threads, MetaX, Biren, Alibaba T-Head, Baidu Kunlunxin.

### 4.7 Memory (HBM)

- **Generations** (JEDEC / Wikipedia):
  - HBM3: 1,024-bit bus, 6.4 Gb/s per pin, 819 GB/s per stack (H100).
  - HBM3E: ~1–1.2 TB/s per stack; 8/12/16-high; 24–48 GB per stack.
  - **HBM4** (JEDEC standard April 2025): **2,048-bit** interface, up to 2 TB/s per stack at 8 Gb/s, 4–16-high, up to 64 GB per stack.
  - Shipping HBM4 runs faster than the base spec: Rubin's 8 stacks deliver ~19–22 TB/s, i.e., ~2.4–2.75 TB/s per stack.
  - HBM4E samples were reported in 2026. Source: https://en.wikipedia.org/wiki/High_Bandwidth_Memory
- **Suppliers:** SK hynix (market leader and NVIDIA's primary HBM supplier since HBM3), Samsung and Micron. Industry trackers in 2025 put SK hynix at roughly half or more of HBM shipments [verify exact share].
  - NVIDIA announced a multiyear memory alliance with SK hynix (Q2 FY27 release).
  - HBM4 base dies can be custom logic made at TSMC, which is a big shift in the memory business.
- **Why HBM is a bottleneck:**
  - HBM uses ~3× the wafer area per bit of standard DRAM [verify ratio] and needs TSV stacking and advanced packaging.
  - Memory makers shifting capacity to HBM tightened supply of ordinary DRAM in 2025–26 (a "memory supercycle") [verify specifics].
- **Trend:** GPU memory bandwidth has grown ~28%/year since 2008, vs. much faster growth in compute (https://epoch.ai/trends). "AI and Memory Wall" (Gholami et al., 2024) estimated that over ~20 years peak compute grew ~3.0× every two years vs. ~1.6× for DRAM bandwidth and ~1.4× for interconnect (https://arxiv.org/abs/2403.14123).

### 4.8 Interconnect and networking

- **NVLink generations:** Hopper NVLink 4 = 900 GB/s per GPU; Blackwell NVLink 5 = 1.8 TB/s per GPU (130 TB/s per NVL72); Rubin NVLink 6 = 3.6 TB/s at launch (current product page: 3 TB/s per GPU, 216 TB/s per rack).
- **PCIe:** 5.0 = 32 GT/s per lane (~64 GB/s per direction on x16). 6.0 doubles that. The 7.0 spec (128 GT/s) was released in 2025 [verify date].
- **Open alternatives:** **UALink 1.0** (April 2025; up to 1,024 accelerators in one scale-up pod; 200 Gb/s lanes) and **Ultra Ethernet 1.0** (June 2025). AMD's Helios tunnels UALink over Ethernet.
- **Scale-out:**
  - NVIDIA Quantum InfiniBand (X800 at 800 Gb/s), Spectrum-X Ethernet, and Spectrum-6 with co-packaged optics (arriving at sites mid-2026).
  - Broadcom Tomahawk 6 (102.4 Tb/s switch chip, 2025).
  - ConnectX-9 (1.6 Tb/s class) in Rubin systems.
- **Google:** ICI plus optical circuit switches. The TPU 8t Virgo fabric reaches 134k chips at 47 Pb/s bisection.
- **Huawei:** "Hi-ONE" optical interconnect for the Atlas 960E SuperPoD. Huawei says it replaces ~48,000 800G optical modules with ~5,500 units and saves 550+ kW (https://www.crnasia.com/news/2026/artificial-intelligence/huawei-outlines-ascend-960-roadmap-and-million-processor-ai).

### 4.9 Manufacturing and supply chain

- **TSMC:** N2 (first-generation nanosheet GAA) began **volume production in Q4 2025**. A16 adds a backside power rail (https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm).
  - Rubin is on N3, while AMD MI455X uses N2/N3 chiplets. Feynman is reported to target A16 (2028).
  - TSMC held roughly 70% of global foundry revenue in 2025 per TrendForce rankings [verify].
  - TSMC announced a total **US$165B** Arizona investment (March 2025) [verify].
- **Lithography:**
  - EUV uses **13.5 nm** light from tin-droplet plasma (~50,000 droplets per second), with mirrors in vacuum. A typical EUV tool costs **~$180M** and weighs nearly 200 tons.
  - DUV immersion (193 nm) reaches ~38 nm single-exposure resolution vs. ~13 nm for NXE:3400-class EUV.
  - **High-NA EUV** (0.55 NA; EXE:5000/5200B) reaches **8 nm resolution**, prints features ~1.7× smaller and gives ~2.9× density vs. standard EUV. It is aimed at sub-2 nm logic and leading DRAM.
  - **ASML is the only EUV supplier.** Reuters reported (Dec 2025) a Chinese prototype EUV system.
  - Sources: https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography ; https://www.asml.com/en/products/euv-lithography-systems/twinscan-exe-5200b
- **Packaging:** TSMC CoWoS (-S silicon interposer; -L local silicon bridges, used for Blackwell/Rubin) has been the gating capacity for AI accelerators since 2023. Intel offers EMIB/Foveros as an alternative (Feynman reportedly uses Intel EMIB for an I/O die [verify]).
- **Costs (order of magnitude):**
  - A leading-edge chip design costs several hundred million dollars.
  - Leading-edge wafers are reported at ~$20k (N3) to ~$30k (N2) each [verify].
  - A leading-edge fab costs $20B+.
  - An H100 sold for ~$25–40k, and a GB200/GB300 NVL72 rack for ~$3–4M [verify]. Third-party estimates put a VR NVL72 at ~$5–7M (low-confidence source).

### 4.10 Training compute, cluster scale and utilization

- **Growth:** Frontier training compute grows **~5× per year** (since 2020), doubling every ~5.2 months. Training cost grows ~3.5×/year. Total installed AI compute grows ~3.4×/year. AI chip performance per dollar grows ~1.49×/year (since 2023), and GPU energy efficiency ~1.34×/year (https://epoch.ai/trends, updated Feb 2026).
- **Big runs (Epoch estimates):**
  - GPT-4 ~2.1×10^25 FLOP; Llama 3.1 405B 3.8×10^25; Grok-3 ~4.6×10^26.
  - As of June 2025, Epoch counted 30+ public models above 10^25 FLOP from 12 developers (https://epoch.ai/data-insights/models-over-1e25-flop).
  - 2026 frontier runs are believed to be in the 10^26–10^27 range, but labs rarely disclose them.
- **Largest sites:**
  - Epoch lists xAI's **Colossus 2** (Memphis) at **~1.1 million H100-equivalents**, and Meta Hyperion is projected at ~3.7M H100e by Jan 2028.
  - A gigawatt-scale site takes ~2 years to build and costs ~$38B in up-front capex per GW of IT power (https://epoch.ai/trends).
  - Google says TPU 8t training can span **>1M chips**.
- **Reliability and utilization (Llama 3 405B, a public reference point):**
  - It used 16,384 H100s with BF16 **MFU of 38–43%** and 4D parallelism (TP, CP, PP, FSDP-style DP).
  - In a **54-day** window there were **466 job interruptions (419 unexpected)**; ~78% were attributed to hardware, GPU issues were the largest category, and HBM3 caused 17.2%.
  - Effective training time was >90%. Synchronized GPU activity caused power swings of tens of megawatts.
  - Source: https://arxiv.org/html/2407.21783v3
- **DeepSeek-V3 (Dec 2024)** is a public example of large-scale **FP8 training**: 2,048 H800 GPUs and ~2.8M GPU-hours.

### 4.11 Inference economics

- **Prices fall fast:**
  - The price to reach a fixed capability level fell **9× to 900× per year** depending on the benchmark (Epoch, March 2025). GPT-4-level MMLU went from $37.50 per million tokens (Mar 2023) to $0.18 (Gemini 2.0 Flash, Feb 2025).
  - The GPT-4 level on GPQA fell ~40× per year (https://epoch.ai/data-insights/llm-inference-price-trends).
- **Cloud GPU rental (on-demand list prices, Oct 2026):**
  - RunPod: H100 SXM $2.69–3.99/hr; H200 $3.59–5.29; **B200 $5.98–7.99**; **B300 $6.94–8.99**; A100 ~$1.19–1.79; RTX 4090 $0.34–0.89 (https://www.runpod.io/pricing).
  - Lambda: B200 $6.69–6.99/GPU-hr; H100 SXM $3.99–4.29; A100 $1.99–2.79 (https://lambda.ai/service/gpu-cloud).
  - Reserved, contract prices are lower.
- **Trends:** disaggregated prefill/decode, inference-specific chips (TPU 8i, Groq LPX, Maia 200, Inferentia, Rubin CPX), and NVL72-scale expert parallelism for giant MoE models. NVIDIA's own GTC framing is "tokens per watt" and "cost per token."

### 4.12 Export controls and geopolitics (timeline)

- **Oct 7, 2022:** BIS controls on advanced AI chips (A100/H100 class) and on chipmaking equipment to China. Fabs making ≤16/14 nm logic, ≤18 nm DRAM or ≥128-layer NAND are restricted (https://en.wikipedia.org/wiki/United_States_New_Export_Controls_on_Advanced_Computing_and_Semiconductors_to_China).
- **Oct 2023:** Rules tightened using TPP and "performance density" thresholds. This blocked China-specific A800/H800, and NVIDIA responded with the H20.
- **Dec 2024:** HBM exports to China were restricted and more equipment controls added.
- **Jan 2025:** The "AI Diffusion" rule set three country tiers. It was **rescinded in May 2025** before taking effect.
- **2025, H20 back-and-forth:**
  - An April license requirement effectively halted H20 sales.
  - In July–Aug the US reversed course in exchange for a 15% revenue share.
  - Chinese regulators then discouraged purchases of NVIDIA China-specific chips, and China's market regulator found NVIDIA violated anti-monopoly law (Sept 2025) [verify details].
- **Dec 8, 2025:** President Trump announced H200 sales to approved Chinese customers.
- **Jan 13–15, 2026:** A BIS rule moved **H200, AMD MI325X and equivalents** (TPP < 21,000 or DRAM bandwidth < 6,500 GB/s) from presumption-of-denial to **case-by-case** review for China/Macau. Conditions:
  - exports per model capped at **50% of US sales** of that model;
  - certifications that US supply is unaffected;
  - KYC, physical security, and no remote access for restricted parties;
  - a **25%** charge, collected via mandatory US lab testing plus a Section 232 tariff (Jan 14, 2026 proclamation).
  - Blackwell and newer were not covered.
  - Sources: https://www.cfr.org/articles/new-ai-chip-export-policy-china-strategically-incoherent-and-unenforceable ; https://www.iaps.ai/research/bis-licensing-policy-for-h200s
- **2026 outcome:**
  - NVIDIA said in March 2026 it had received licenses, but China reportedly restricted imports.
  - In Q2 FY27, H200 sales to China were **<1% of data-center revenue**, and NVIDIA's guidance assumes zero China data-center compute revenue.
  - Reports in March 2026 described a draft *global* licensing framework for AI chips. As of Oct 19, 2026 no replacement rule had been announced [verify].
  - On Oct 16, 2026 China proposed its own export controls on 40 technologies, including AI.
- **China's domestic stack:**
  - **Huawei Ascend** roadmap (Huawei Connect 2025 and 2026): 950PR (Q1 2026) and 950DT (Q4 2026), using Huawei's self-developed HBM.
  - At Huawei Connect 2026, the **960DT was pulled forward to Q1 2027** and the 960PR to Q3 2027, with the 970 in 2028 and 980 in 2029.
  - The **Atlas 950 SuperPoD** is in commercial use, and a 256,000-card SuperCluster is being deployed.
  - The **Atlas 960E SuperPoD** offers 4,096 NPUs, 8 EF FP8 and 1 PB HBM. SuperClusters reach up to 512k NPUs (1M with multi-rail).
  - Sources: https://www.crnasia.com/news/2026/artificial-intelligence/huawei-outlines-ascend-960-roadmap-and-million-processor-ai ; https://www.datacenterdynamics.com/en/news/huawei-announces-annual-release-cadence-for-three-new-ascend-ai-chips-unveils-supernode-offering-company-says-will-outperform-nvidias-nvl144/
  - Huawei's strategy is *many weaker chips, bound together with lots of optics and power*. SMIC manufactures at 7 nm-class (and reportedly 5 nm-class) using DUV multi-patterning, without EUV [verify 5 nm].
- **US industrial policy:**
  - The CHIPS Act (2022) provides $52.7B, including ~$39B in manufacturing incentives. The advanced-manufacturing investment tax credit was raised from 25% to 35% in 2025 [verify].
  - Government equity in Intel (9.9%); Section 232 semiconductor tariffs (2026).
- **Taiwan concentration:** Most of the world's leading-edge logic (and nearly all AI accelerators, including every NVIDIA, AMD, Google and AWS AI chip listed above) is fabbed and CoWoS-packaged by TSMC in Taiwan, with Arizona ramping. This concentration is a central geopolitical risk.

### 4.13 Edge and on-device AI

- **Apple:** the Neural Engine (since A11, 2017). The M5 (Oct 2025) added a "Neural Accelerator" in each GPU core. On-device foundation models run at ~3B parameters [verify].
- **Windows:** Microsoft "Copilot+ PC" requires a 40+ TOPS NPU (Qualcomm Snapdragon X, Intel Lunar Lake/Panther Lake, AMD Ryzen AI). NVIDIA/Microsoft RTX Spark arrived in 2026 (Q2 FY27 release).
- **Google:** Tensor G5 (TSMC, Pixel 10, 2025) runs Gemini Nano on-device [verify node].
- **Qualcomm:** also entered data-center inference with the AI200 (2026) and AI250 (2027) cards using large LPDDR pools [verify].
- **Robotics/edge:** NVIDIA Jetson Thor (2025) [verify specs].
- **The edge limit is memory:** an 8B-parameter model at 4 bits needs ~4–5 GB, and speed is roughly memory bandwidth ÷ model size.

---

## 5. Diagram ideas (28)

1. **The scale ladder: transistor → AI factory.** A horizontal staircase of 10 boxes, each labeled with a count and a size.
   - The steps: Transistor (~50 nm features) → Logic gate (~10 transistors) → Tensor core → SM (streaming multiprocessor) → GPU die (~100B+ transistors) → Package (2 dies + 8 HBM stacks) → Superchip/tray (CPU + 2 GPUs) → Rack (NVL72: 72 GPUs, ~130 kW) → Pod/cluster (thousands of racks) → Campus (≥1 GW, 1M+ GPUs).
   - Under each box: a "zoom ×1,000" arrow and a real-world size comparison (virus, grain of sand, fingernail, pizza box, refrigerator, football field).
2. **Transistor as a valve.** Side-by-side panels: a garden hose with a pinch clamp labeled "gate" next to a cross-section of a transistor (source, drain, gate, channel), with current arrows on and off. A third panel shows FinFET vs. gate-all-around nanosheet in 3D, with the gate wrapping 3 sides vs. 4.
3. **Gates to multiplier.** Flow: NOT/AND/OR symbols → a half-adder → a 4-bit adder → a multiply-accumulate unit, captioned "everything is switches."
4. **CPU vs. GPU floor plan.**
   - Left: a CPU die with 8 big cores, a large cache and a control-logic box ("few smart workers").
   - Right: a GPU die with 100+ tiny SM tiles, each holding a mini grid of cores and a tensor-core block ("an army of simple workers").
   - Annotate each with a typical core count, clock and FLOPS.
5. **Matrix multiplication by hand → by hardware.** A 3×3 × 3×3 multiply with one output cell highlighted and its 3 MACs drawn. An arrow leads to a tensor core box doing a 4×4×4 multiply in "1 clock."
6. **Systolic array animation storyboard.** A 4×4 grid of MAC cells. Weights are preloaded, activations flow left→right, partial sums flow top→bottom. Time steps t=1…7 show numbers pulsing through, with the caption "each number is reused many times without going back to memory."
7. **The precision ladder.** Stacked horizontal bars for FP32 (1|8|23), TF32 (1|8|10), BF16 (1|8|7), FP16 (1|5|10), FP8 E4M3 (1|4|3), E5M2 (1|5|2), FP4 E2M1 (1|2|1), with sign/exponent/mantissa colored.
   - On the right: relative throughput (1×, 2×, 4×, 8×) and memory per 1B parameters (4 GB, 2 GB, 1 GB, 0.5 GB).
   - Inset: the full list of FP4 values on a number line, and a block of 16 values sharing one scale (NVFP4) vs. 32 (MXFP4).
8. **Memory hierarchy pyramid.** A pyramid from top to bottom: registers (KB, <1 ns) → SRAM/L1/L2 (MB, ~1–10 ns, tens of TB/s) → HBM (hundreds of GB, ~100s ns, ~8–22 TB/s) → CPU DRAM/LPDDR (TB, ~100 GB/s–1 TB/s) → local NVMe SSD (TB, ~10 GB/s) → network storage (PB). Width = capacity, color = speed, with a "cost per GB" annotation.
9. **The memory wall chart.** A log-scale line chart from 2000 to 2026 with three lines: peak FLOPS per chip, DRAM/HBM bandwidth per chip, and interconnect bandwidth. The widening gap is shaded "the memory wall" (data: Gholami et al. 2024; Epoch).
10. **Roofline plot.** X-axis: arithmetic intensity (FLOP/byte, log). Y-axis: achievable FLOPS. A sloped line for the memory-bandwidth limit meets a flat line for the compute peak at the "ridge point" (~295 FLOP/byte for H100 BF16). Plot dots for "LLM decode, batch 1" (far left, memory-bound), "decode, batch 256" (middle) and "prefill/training matmul" (right, compute-bound).
11. **Inside a Blackwell/Rubin package (cross-section and top view).**
    - Top view: two big GPU dies joined by a die-to-die link, surrounded by 8 HBM stacks.
    - Side view: substrate → interposer/CoWoS-L bridges → dies; HBM stack shown as 12–16 thin DRAM layers on a base die, with TSVs as vertical lines.
    - Labels: "reticle limit ~858 mm² per die," "8 stacks × 36 GB = 288 GB."
12. **GB300/VR NVL72 rack exploded view.** 18 compute trays (each 2 superchips = 4 GPUs + 2 CPUs) top and bottom, 9 NVLink switch trays in the middle, a copper spine cartridge at the back (~5,000 cables), power shelves, a liquid-cooling manifold, and the stamp "~120–140 kW (GB300)." A callout says "all 72 GPUs see each other at full NVLink speed = one giant GPU."
13. **Scale-up vs. scale-out.** Two nested circles.
    - The inner circle is the "NVLink domain (72 GPUs), ~1–3.6 TB/s per GPU, nanosecond-to-microsecond latency."
    - The outer ring is "InfiniBand/Ethernet, 0.4–1.6 Tb/s per GPU (≈50–200 GB/s), microseconds."
    - Arrows show which parallelism lives where: TP/EP inside, PP/DP outside.
14. **Network topologies side by side.** A 3-tier fat-tree/Clos (leaf, spine, core), a rail-optimized cluster (8 rails), Google's 3D torus (a cube with wrap-around links), and TPU 8i's Boardfly/dragonfly (groups fully connected). For each, label the number of hops and the typical use.
15. **Optics evolution.** Three panels: (a) GPU → copper → NIC → pluggable optical transceiver → fiber; (b) a switch with co-packaged optics where lasers sit next to the switch chip; (c) a future GPU with optical I/O on-package. Annotate watts per 800G link for each [use vendor numbers].
16. **The four (five) parallelisms.** A grid of GPUs drawn as boxes:
    - DP: same model, different data slices.
    - TP: one matrix split in column strips across 4 GPUs.
    - PP: layers 1–20 / 21–40 / … on successive GPUs, with a pipeline bubble Gantt chart beneath.
    - CP/SP: a long sequence split into chunks.
    - EP: experts E1–E8 on different GPUs with a router sending tokens.
    - Color-code which network tier each uses.
17. **Ring all-reduce step-by-step.** 4 GPUs in a ring, each holding a gradient vector split into 4 chunks. Show the reduce-scatter steps (3) then the all-gather steps (3), with arrows and running sums; caption "each GPU sends ~2× its data regardless of ring size."
18. **Training memory budget stacked bar.** For a 70B model: weights BF16 (140 GB) + gradients (140 GB) + Adam states and FP32 master weights (840 GB) + activations (variable), about 1.1 TB+. A line marks "one H100 = 80 GB; one B300 = 288 GB," and a second bar shows the same budget sharded with ZeRO-3 across 64 GPUs.
19. **Failure timeline at scale.** A 54-day horizontal timeline (Llama 3) with 419 red ticks for unexpected interruptions, a sawtooth of "progress since last checkpoint," a pie of causes (GPU, HBM3, network, software, host), and the label "goodput >90%."
20. **Prefill vs. decode.** Two panels. Prefill: the whole prompt (N tokens) enters as one big matrix → GPU busy (compute-bound). Decode: a single token at a time → for each token the GPU re-reads all weights from HBM (memory-bound). A KV-cache box grows with every token. TTFT and inter-token latency are marked on a timeline.
21. **Interactivity vs. throughput Pareto curve.** X-axis: tokens/sec per user. Y-axis: tokens/sec per GPU (or per MW). Curves for H100, B200, GB300 NVL72, Vera Rubin, and Vera Rubin + LPX, showing that "fast for one user" and "cheap for everyone" trade off.
22. **Cost-per-token waterfall.** Start with "$ per GPU-hour" (capex amortization + power + cooling + network + facility + staff), divide by tokens per hour, and arrive at "$ per million tokens." Side boxes show the levers: utilization, batch size, precision, speculative decoding, chip generation.
23. **How a chip is made (fab flow).** Sand → polysilicon → ingot → wafer → [loop ×N: deposit → coat resist → expose (EUV scanner) → develop → etch → strip → implant → CMP polish] → test → dice → package (CoWoS) → final test → board. The loop is drawn as a circular arrow labeled "repeated for 60–100+ layers; ~3 months fab-in to fab-out [verify]."
24. **Lithography optics.** DUV (193 nm, lenses, in air/water) vs. EUV (13.5 nm, tin droplet + CO₂ laser → plasma → collector mirror → multilayer mirrors → reflective mask → wafer, in vacuum), plus High-NA with a bigger final mirror. Show the light-wavelength comparison bar and resolution numbers (38 nm, 13 nm, 8 nm).
25. **Yield vs. die size.** Two identical wafers with the same 20 random defect dots. The left is cut into many small dies (few ruined, most good); the right is cut into a few huge dies (most ruined). A formula strip reads "Yield ≈ e^(−Area × Defect density)," and an arrow points to "chiplets."
26. **The AI chip supply chain map.** A left-to-right flow of companies and countries:
    - EDA (US: Synopsys, Cadence, Siemens) + IP (UK: Arm) → chip designers (US: NVIDIA, AMD, Google+Broadcom, AWS+Marvell…) → foundry (Taiwan: TSMC; Korea: Samsung; US: Intel) ← equipment (Netherlands: ASML; US: AMAT, Lam, KLA; Japan: TEL) ← materials (Japan: wafers, resists).
    - Memory (Korea: SK hynix, Samsung; US: Micron) → packaging (TSMC CoWoS; ASE/Amkor) → server ODMs (Taiwan: Foxconn, Quanta, Wistron) → clouds/labs.
    - Red "choke point" markers on EUV, CoWoS, HBM and power.
27. **Export-control timeline.** A horizontal timeline 2022 → 2026 with US actions above the line (Oct 2022, Oct 2023, Dec 2024, Jan 2025 Diffusion rule, May 2025 rescission, H20 swings, Dec 2025 H200 announcement, Jan 2026 rule) and China's responses below (Huawei Ascend roadmap, SMIC progress, purchase discouragement, NVIDIA antitrust finding, Oct 2026 Chinese export-control proposal). Chips allowed vs. banned are shown as icons.
28. **Roadmap swimlanes 2024–2028.** One lane each for NVIDIA (Blackwell → Blackwell Ultra → Vera Rubin → Rubin Ultra/Kyber → Feynman), AMD (MI325X → MI355X → MI455X/Helios → MI500), Google (Trillium → Ironwood → TPU 8t/8i), AWS (Trn2 → Trn3 → Trn4), Huawei (910C → 950 → 960 → 970), and HBM (HBM3E → HBM4 → HBM4E). Each lane shows its process node and rack power.

---

## 6. Practical exercises (easy → hard)

*None require programming skill. Exercises marked "spreadsheet" need only Google Sheets or Excel. Cloud exercises cost $0 (free tiers) to about $10.*

**E1. Count in binary with your fingers (10 min).**
- Steps: Hold up fingers as bits (thumb = 1, index = 2, middle = 4, ring = 8, pinky = 16). Make 5, 13 and 31.
- Then answer: how many distinct values can 4 bits hold (16)? 8 bits (256)?
- Learn: why FP4 can represent only 16 values, and why fewer bits means less detail.

**E2. Powers of ten flash cards (15 min, spreadsheet).**
- Steps: Make a column with 10^3 … 10^27 and fill in the names (kilo, mega, giga, tera, peta, exa, zetta, yotta).
- Add real examples next to each: your phone NPU (~10^13 ops/s), one H100 (~10^15 FLOP/s BF16), a GB300 NVL72 rack (~10^18), Llama 3.1 405B training (3.8×10^25 FLOP), and frontier 2026 runs (~10^26–10^27).
- Learn: comfort with the scientific notation used everywhere in AI compute.

**E3. Read a spec sheet like a detective (20 min).**
- Steps: Open NVIDIA's GB300 NVL72 page and the Vera Rubin NVL72 page. For each FLOPS number, write down the precision, whether it is dense or sparse (check the footnotes), and whether it is per GPU or per rack.
- Compute per-GPU values by dividing by 72.
- Learn: headline numbers can differ by 2× (sparsity) or 4× (precision), and 72× (rack vs. chip).

**E4. See a real GPU in Google Colab (15 min, free).**
- Steps: Go to colab.research.google.com → New notebook → Runtime → Change runtime type → choose a GPU (often a T4). In a cell type `!nvidia-smi` and press the play button.
- Record the GPU name, memory (e.g., 15 GB), driver/CUDA version and power draw.
- Run it again after loading a small model (copy-paste a 5-line Hugging Face example) and watch memory use and power rise.
- Learn: a GPU is a physical device with finite memory and power, and "out of memory" is the most common AI error.

**E5. Measure tokens per second on your own computer (30 min).**
- Steps: Install LM Studio or Ollama (point-and-click). Download a ~1B and a ~8B model in 4-bit quantization. Ask each the same question and note the tokens/sec it reports.
- Learn: bigger models are slower, and quantization makes local AI possible. Your laptop is doing *decode*, which is memory-bound.

**E6. Predict your laptop's speed from memory bandwidth (30 min, spreadsheet).**
- Steps: Look up your computer's memory bandwidth (e.g., Apple M-series spec page: ~100–550 GB/s; typical DDR5 laptop: ~60–120 GB/s). Note the model file size from E5 (e.g., 4.7 GB).
- Predicted max tokens/s ≈ bandwidth ÷ model size (e.g., 120 ÷ 4.7 ≈ 25 tok/s). Compare to what you measured.
- Learn: generation speed is set by how fast weights stream from memory, not by FLOPS. This is the memory wall in action.

**E7. How much memory does a model need? (20 min, spreadsheet.)**
- Steps: Use the formula bytes = parameters × bytes per parameter (FP32 = 4, BF16 = 2, FP8 = 1, 4-bit = 0.5). Compute 8B, 70B, 405B and 1T-parameter models at each precision.
- Check: does 70B in BF16 (140 GB) fit on one H100 (80 GB)? On one B300 (288 GB)?
- Learn: why quantization and big-memory GPUs matter, and why multi-GPU serving exists.

**E8. Dies per wafer and cost per chip (45 min, spreadsheet).**
- Steps: Wafer area = π × 150² ≈ 70,686 mm². Use the die area of an H100 (814 mm²).
- Dies per wafer ≈ 70,686/814 − (π × 300)/√(2 × 814) ≈ 63.
- Yield ≈ e^(−area_cm² × D0) with D0 = 0.1 defects/cm² → e^(−0.814) ≈ 44% → ~28 good dies.
- At an assumed ~$17–20k wafer price, that is ~$600–700 of silicon per good die. Compare to the GPU's ~$25k+ price.
- Repeat with a 100 mm² chiplet.
- Learn: big dies are expensive because of yield, chiplets help, and silicon is a small part of an AI chip's price (packaging, HBM, margins and software are the rest).

**E9. Estimate training compute with 6·N·D (30 min, spreadsheet).**
- Steps: FLOP = 6 × parameters × tokens.
  - GPT-3: 6 × 175e9 × 300e9 ≈ **3.2×10^23**.
  - Llama 3.1 405B: 6 × 405e9 × 15.6e12 ≈ **3.8×10^25** (matches Meta's figure).
  - A "Chinchilla-optimal" 1T model (20 tokens per parameter): 6 × 1e12 × 2e13 = **1.2×10^26**.
- Learn: the training budget scales with both model size and data, and frontier runs are 10^26+.

**E10. How long and how many GPUs? (45 min, spreadsheet.)**
- Steps: Time (seconds) = FLOP ÷ (number of GPUs × peak FLOPS × MFU).
  - Llama 3.1 405B on 16,384 H100s at 989e12 BF16 and 40% MFU → ≈ 5.9×10^6 s ≈ **68 days**.
  - A 10^27 FLOP run on 100,000 Blackwell GPUs at 2.5e15 dense BF16 and 40% MFU → 10^7 s ≈ **116 days**.
  - Then try it at FP8 (double the FLOPS).
- Learn: why labs buy 100k–1M GPUs, why precision and MFU matter as much as chip count, and why training runs last months.

**E11. Price a training run (30 min, spreadsheet).**
- Steps: GPU-hours = GPUs × hours from E10. Multiply by rental prices (H100 ~$2–4/hr; B200 ~$6–8/hr list, lower on contract).
  - Llama-3-scale: 16,384 × 1,632 hours ≈ 26.7M GPU-hours × $2.50 ≈ **$67M** at rental rates.
- Learn: where "hundred-million-dollar" and "billion-dollar" training runs come from, and that owned hardware and contracts change the math.

**E12. Rent a cloud GPU for one hour (60 min, ~$3–8).**
- Steps: Create an account on a GPU marketplace (RunPod, Lambda, Vast.ai). Launch the cheapest H100 or A100 "PyTorch" template, open the web terminal, and run `nvidia-smi`, `nvidia-smi topo -m` (shows how GPUs connect) and `nvidia-smi -q | head -50`.
- Shut it down when done and check the bill.
- Learn: what "renting compute" means, the hourly economics, and that GPUs, NVLink and NICs are real things you can inspect. **Always stop the instance.**

**E13. The roofline by hand (45 min, spreadsheet).**
- Steps: Ridge point = peak FLOPS ÷ bandwidth.
  - H100: 989e12 ÷ 3.35e12 ≈ **295 FLOP/byte**.
  - Rubin: 4e15 BF16 ÷ 19.2e12 ≈ 208. At NVFP4 dense: 35e15 ÷ 19.2e12 ≈ 1,800.
- Then compute decode at batch 1 for a 70B BF16 model: 2 FLOP per parameter per token ÷ 2 bytes per parameter = 1 FLOP/byte. That is far below the ridge, so it is memory-bound.
- Learn: why batching helps (it raises FLOP per byte) and why lower precision makes chips even hungrier for bandwidth.

**E14. Max decode speed of a big GPU (20 min).**
- Steps: For a 70B model in FP8 (70 GB) on one H200 (4.8 TB/s): 4,800 ÷ 70 ≈ **69 tokens/s** upper bound for a single user.
- On a B300 (8 TB/s): ≈114. On a Rubin (19–22 TB/s): ≈275–315.
- Learn: the link between HBM bandwidth and the speed you feel in a chatbot.

**E15. Cost per million tokens (30 min, spreadsheet).**
- Steps: $ per M tokens = ($ per GPU-hour) ÷ (tokens per second × 3,600) × 10^6.
  - $3/hr at 1,000 tok/s (batched) → **$0.83**.
  - At 5,000 tok/s → **$0.17**.
- Compare with an API price list for a model you use.
- Learn: inference margins depend on batching and utilization, and why providers love bigger batches while users want speed.

**E16. Energy per token (20 min).**
- Steps: Assume one GPU plus its share of overhead ≈ 1.5 kW, producing 2,000 tokens/s. Energy per token = 1,500 J/s ÷ 2,000 tok/s = 0.75 J per token.
- A 500-token answer ≈ 375 J ≈ 0.1 Wh. Compare to a 10 W LED for ~37 seconds.
- Learn: per-query energy is small, but aggregate demand is huge, and efficiency (tokens per watt) is now a headline metric.

**E17. Training memory budget (30 min, spreadsheet).**
- Steps: Mixed-precision Adam needs ~16 bytes per parameter (2 BF16 weights + 2 gradients + 12 for FP32 master weights and two Adam moments). For 70B that is 1.12 TB, before activations.
- Divide by 80 GB (H100) → at least 14 GPUs just to *hold* state, with ZeRO-3/FSDP sharding.
- Learn: memory, not just speed, forces multi-GPU training, and it motivates ZeRO/FSDP.

**E18. Simulate an all-reduce with people or playing cards (30 min, group).**
- Steps: 4 people each hold 4 numbered cards (their "gradients"). In round 1, each passes one chunk to the right and the receiver adds it. Repeat 3 rounds (reduce-scatter) until each person has one fully summed chunk. Pass for 3 more rounds (all-gather) until everyone has all sums.
- Time it, then add one slow person (a "straggler").
- Learn: how collective communication works, and why the slowest link sets the pace for 100,000 GPUs.

**E19. Failures at scale (20 min, spreadsheet).**
- Steps: If one GPU fails on average once every 5 years (~43,800 hours), a 100,000-GPU cluster sees a failure about every 43,800/100,000 h ≈ **26 minutes**.
- Compare with Llama 3's 419 unexpected interruptions in 54 days (one every ~3 hours at 16k GPUs).
- Model checkpoint frequency: if each checkpoint takes 2 minutes and failures come every 30 minutes, how much work is lost?
- Learn: why reliability engineering, checkpointing and goodput are frontier skills.

**E20. Pick the right parallelism (40 min, paper).**
- Steps: Given a 400B MoE model, 8,192 GPUs in NVL72 racks, and a 128k context, assign tensor/expert parallelism (inside the rack), pipeline parallelism (across racks), context parallelism (long sequences) and data parallelism (everything else). Draw it using Diagram 16.
- Learn: the logic of matching communication-heavy work to the fastest links.

**E21. Compare accelerators per dollar (45 min, spreadsheet).**
- Steps: Build a table: chip, dense BF16 or FP8 FLOPS, HBM GB, HBM TB/s, rental $/hr (from RunPod/Lambda).
- Compute FLOPS per $, GB per $ and TB/s per $ for A100, H100, H200, B200 and B300.
- Learn: no single "best" chip exists. It depends on whether your workload is compute-, memory-capacity- or bandwidth-bound.

**E22. Benchmark quantization quality vs. speed (60 min).**
- Steps: In LM Studio/Ollama, download the same 8B model at 8-bit, 4-bit and 2–3-bit. Ask 10 fixed questions (math, facts, reasoning). Score correctness and record tokens/s and memory use.
- Learn: precision trades quality for speed and memory, and the "knee" is usually around 4 bits for inference.

**E23. Map the supply chain of one GPU (60 min, research).**
- Steps: For an NVIDIA B300 or Rubin GPU, find and list the designer, EDA tools, foundry and node, HBM supplier(s), packaging technology, server ODM, the countries involved, and one choke point at each step. Turn it into Diagram 26.
- Learn: why geopolitics and export controls center on a few companies (ASML, TSMC, SK hynix).

**E24. Read an export-control threshold (45 min).**
- Steps: TPP ≈ (dense peak TOPS or TFLOPS at a given bit length) × (bit length). For example, ~1,979 TFLOPS dense FP8 × 8 ≈ 15,800 for an H100 (H200 is the same compute).
- Compare to the Jan 2026 threshold (TPP < 21,000) and ask why a B200/B300 would exceed it.
- Learn: how policy is written in hardware terms, and why chips get "cut down" for specific markets.

**E25. Plan a 1-gigawatt cluster on a napkin (60 min, spreadsheet, capstone).**
- Steps: Assume ~1.8 kW per GPU all-in at the IT level (VR/GB300 class) and PUE 1.2.
  - GPUs per GW ≈ 1e9 ÷ (1,800 × 1.2) ≈ **460,000**.
  - At ~$40B per GW (Epoch: ~$38B capex/GW), estimate the cost per GPU-slot.
  - Peak dense FP8 = GPUs × ~5–17.5 PF depending on generation.
  - How long would a 10^27 FLOP run take at 40% MFU?
- Learn: how chips, power, money and time connect into one system. This is the bridge to the data-center chapter.

---

## 7. Areas of opportunity

### 7.1 Careers and skills in demand
- **GPU kernel and performance engineers.** These people write and tune CUDA, Triton, CUTLASS or Pallas kernels (e.g., attention, MoE routing, FP4 GEMMs). It is among the scarcest, best-paid skills in AI because every 10% speedup is worth millions at cluster scale. Path: Python → PyTorch → Triton → CUDA → profiling tools (Nsight).
- **ML systems / distributed training engineers.** They design parallelism layouts, debug NCCL hangs, chase MFU and handle failures at 10k–1M GPU scale. Megatron-LM, DeepSpeed, PyTorch FSDP/TorchTitan, JAX/Pathways.
- **Inference optimization engineers.** They work with vLLM, SGLang, TensorRT-LLM and Dynamo, plus quantization, speculative decoding, KV-cache management and disaggregated serving. Demand is exploding as inference outgrows training.
- **Compiler engineers.** MLIR, XLA, Triton, TVM and hardware back-ends for new accelerators. Every new chip needs them.
- **Chip design and verification.** RTL design, physical design, verification and DFT. AI is also changing EDA itself (AI-assisted layout, as OpenAI said it used for its Broadcom chip).
- **Hardware/network engineers for AI clusters.** InfiniBand/Ethernet fabric design, optics, RDMA tuning and cluster bring-up. Data-center technicians who can service liquid-cooled racks are in short supply.
- **Reliability/SRE for AI clusters.** Failure detection, straggler mitigation, checkpoint systems and fleet health telemetry.
- **Semiconductor manufacturing.** Process, yield, lithography, packaging (CoWoS/hybrid bonding) and equipment field engineers, especially in the US, Japan and Europe as fabs reshore. Technician roles need two-year degrees, not PhDs.
- **Non-engineering roles.** Compute procurement and capacity planning, GPU finance (leasing, depreciation modeling, GPU-backed debt), export-control compliance (KYC for chips, license applications), policy analysis (compute governance), technical sales/solutions architects for accelerators, and analysts who can read spec sheets (this chapter's skill set).

### 7.2 Business opportunities
- **Neoclouds and GPU marketplaces:** renting capacity, brokering idle GPUs, and specializing (e.g., inference-only, sovereign/regulated clouds).
- **Inference-as-a-service on cheaper or alternative silicon:** a cost advantage from TPUs, Trainium, AMD MI355X/MI455X, or older GPUs for smaller models.
- **Optimization consultancies:** cutting customers' GPU bills through quantization, batching, routing and caching. The ROI is easy to prove.
- **Observability and FinOps for GPUs:** utilization dashboards, cost attribution and scheduling across clusters (many enterprises run GPUs at low utilization).
- **Edge AI products:** on-device assistants, private local AI appliances (DGX Spark-class desktops), NPUs in industrial and medical devices, and robotics compute.
- **Secondary markets:** refurbishing, reselling and recycling A100/H100s as they depreciate. "Compute futures" and GPU financing products (NVIDIA's Q2 FY27 release mentions platforms aiming to mobilize $500B+ of third-party capital).
- **Picks and shovels:** liquid-cooling components, power conversion (800 V DC), optical interconnect, test and burn-in, cluster-health software.

### 7.3 Open problems (research and engineering frontiers)
- **The memory wall:** bandwidth and capacity per FLOP keep falling. Possible answers include HBM4E/5, custom base dies, processing-near-memory, SRAM-heavy designs (Groq/Cerebras/TPU 8i), CXL memory pooling and better KV-cache compression.
- **Interconnect energy and reach:** copper is running out of reach at 200–400 Gb/s per lane. Co-packaged optics, optical I/O chiplets and optical circuit switching are maturing, and reliability at million-link scale remains unsolved.
- **Low-precision training stability:** making FP4 (NVFP4/MXFP4) pre-training robust at frontier scale; numerics research is hot.
- **Reliability at 1M chips:** silent data corruption, fault-tolerant training, elastic jobs, multi-datacenter training over long-haul links.
- **Software portability:** breaking CUDA lock-in via PyTorch/Triton/JAX back-ends, so that buyers can mix NVIDIA, AMD, TPU and Trainium in one fleet.
- **Inference efficiency for agents and reasoning:** very long contexts, many parallel agents, and huge KV caches. This pushes disaggregated serving and new memory tiers.
- **Power and heat:** 600 kW racks, direct liquid cooling at scale, and grid-interactive training (smoothing tens-of-megawatt power swings).
- **Manufacturing:** High-NA EUV economics, backside power, 3D-stacked logic (Feynman-style), hybrid-bonding yields and HBM supply.
- **Verification and governance:** on-chip location verification and usage attestation (proposed in US "chip security" legislation), and compute accounting for AI regulation.
- **New paradigms (longer term, speculative):** analog/in-memory compute, photonic matrix multiplication, neuromorphic chips, and reversible/low-energy computing. None is yet competitive at frontier scale.

---

## 8. Common misconceptions to correct

1. **"AI runs on the cloud, so hardware doesn't matter."** Every chatbot answer is billions to trillions of physical multiplications on real chips in a real building drawing real power. Hardware sets cost, speed and what is even possible.
2. **"A GPU is just a faster CPU."** It is a different design: thousands of simple cores doing the same operation on lots of data, vs. a few clever cores doing varied work. GPUs are terrible at many tasks CPUs excel at.
3. **"More GHz = faster AI."** Clock speeds have hovered around 1–3 GHz for 20 years. AI speed comes from parallelism, tensor cores, lower precision and, above all, memory bandwidth.
4. **"FLOPS is the number that matters."** For chatbot generation, memory bandwidth and capacity usually matter more. For big training runs, networking and reliability matter as much as raw FLOPS.
5. **"The headline PFLOPS number is what you'll get."** Headline numbers are often *sparse*, *lowest-precision* and *per rack*. Real workloads achieve maybe 30–60% of *dense* peak.
6. **"3 nm means something is 3 nanometers wide."** Node names are marketing labels. Actual transistor features (gate pitch, metal pitch) are tens of nanometers.
7. **"Moore's Law is dead, so progress has stopped."** Single-thread CPU speed growth has slowed, but AI compute per chip and per dollar keeps rising fast. Gains come from precision, specialization, packaging, multi-die designs and networking. Epoch measures AI-chip price-performance at ~1.5× per year and energy efficiency at ~1.34× per year.
8. **"Lower precision means worse AI."** With careful scaling (BF16, FP8, block-scaled FP4), models train and run at nearly the same quality. Precision is a tool, not a downgrade.
9. **"NVIDIA makes its chips."** NVIDIA *designs* chips. TSMC manufactures them, SK hynix/Samsung/Micron make the memory, and Taiwanese ODMs build the servers. Almost every major AI chip (NVIDIA, AMD, Google, AWS, Microsoft) is made by TSMC.
10. **"The chip is the product."** Today the *rack* (NVL72, Helios, TPU pod) or even the whole data center is the unit of design and sale. The networking and software around a chip matter as much as the chip.
11. **"CUDA is just a programming language."** It is an ecosystem of compilers, libraries, tools, documentation and millions of developers built up over ~20 years. That ecosystem is the moat, more than any single chip.
12. **"Google and Amazon chips will make NVIDIA irrelevant soon."** Custom ASICs are growing fast (TPUs for Anthropic, Trainium, Maia, MTIA). But NVIDIA still books ~$89B of data-center revenue *per quarter* and is supply-constrained. The market is growing fast enough for several winners.
13. **"Bigger cluster = proportionally faster training."** Communication overhead, stragglers and failures mean scaling is sub-linear. At 100k+ GPUs, something fails every few minutes to hours.
14. **"Inference is cheap; training is the expensive part."** Per query, yes. In aggregate, inference spending now rivals or exceeds training at major labs, which is why 2026 chips are splitting into training and inference variants (TPU 8t/8i, Rubin + LPX).
15. **"Export controls stopped China's AI."** They slowed access to the best chips and tools. China responded with Huawei Ascend SuperPoDs (many weaker chips bound together), DUV multi-patterning, domestic HBM, and algorithmic efficiency (e.g., DeepSeek's FP8 training on export-compliant H800s). Policy is also volatile (H20 and H200 reversals).
16. **"Quantum computers will soon replace GPUs for AI."** Quantum computers are not general AI accelerators today. Neural-network training and inference run on classical chips, and there is no near-term path to quantum frontier-model training.
17. **"My phone runs ChatGPT."** Phone apps mostly send your request to data-center GPUs. Only small models (a few billion parameters, quantized) run fully on-device, limited by memory and battery.
18. **"Rack and chip names are consistent."** NVL144 vs. NVL72 for the same Rubin generation (dies vs. packages), "B300" vs. "GB300," TOPS vs. FLOPS: names and units are slippery, so always check what is being counted.

---

## 9. Analogies that work for beginners

- **Transistor = a light switch (or a faucet) controlled by electricity instead of a finger.** Billions of them flipping billions of times a second.
- **CPU vs. GPU = a few master chefs vs. a stadium of line cooks.** The chefs can cook anything and improvise. The line cooks each chop one vegetable, but there are 20,000 of them all chopping at once. AI is a mountain of chopping.
- **Tensor core = a muffin tin instead of one muffin pan.** It does a whole tray of small multiplications in one "bake."
- **Systolic array = a bucket brigade or a factory conveyor grid.** Numbers are passed hand to hand and used at each station, so nobody walks back to the warehouse (memory).
- **Memory hierarchy = your desk, your bookshelf, the library downstairs, the warehouse across town.** Registers and SRAM are the desk (tiny, instant), HBM the bookshelf, DRAM the library, SSD the warehouse. Most AI slowness is time spent walking to fetch books.
- **Memory wall = a chef who can chop 10× faster every few years while the pantry door only gets ~1.3× wider.** The chef ends up waiting at the door.
- **HBM = a skyscraper of memory built right next door with a 2,048-lane highway**, instead of a suburb across town on a two-lane road.
- **Precision = a ruler with fewer tick marks.** FP32 marks millimeters, FP8 centimeters, FP4 only a handful of marks. Fewer marks make measuring faster and smaller. With a smart "zoom" (block scaling) you can still measure what matters.
- **Decode = reading an entire encyclopedia to write one word, then reading it again for the next word.** That's why memory speed sets chatbot speed and why batching (writing many people's words per read) is efficient.
- **KV cache = sticky notes summarizing everything said so far**, so the model doesn't re-read the whole conversation. The more you talk (and the more people), the more sticky notes you need.
- **Parallelism strategies = ways to split a giant book-translation project.** Data parallel: each team translates different chapters with the same dictionary, then they reconcile the dictionary. Tensor parallel: each sentence is split among four translators. Pipeline parallel: an assembly line where one team does chapters' first drafts, the next edits, and the next proofreads. Expert parallel: specialists (law, medicine, poetry) get routed the passages they're best at.
- **All-reduce = a group of friends splitting a restaurant bill.** Everyone shares their numbers until each person knows the total, and one slow friend holds up the whole table.
- **NVLink vs. InfiniBand/Ethernet = talking across a desk vs. phoning another building.** Inside the NVL72 "room," 72 GPUs talk instantly. Across racks, they call.
- **Checkpointing = saving your video game before the boss fight.** With 100,000 players in one game, someone's console crashes every half hour.
- **MFU = the fraction of a factory's rated capacity actually turning out product.** The rest is idle time, changeovers and waiting for parts.
- **Lithography = a slide projector printing a city map onto a fingernail**, layer after layer, with features smaller than a virus. EUV = switching from a flashlight to a much finer "pen" of light.
- **Yield = baking cookies on a tray with a few burnt spots.** Small cookies mean only a few are ruined; one giant cookie the size of the tray is almost certainly ruined. Hence chiplets.
- **Advanced packaging = building a city block where the GPU "office tower" and HBM "apartment towers" share underground tunnels (the interposer)**, instead of separate cities connected by highways.
- **Fabless + foundry = a book author and a printing press.** NVIDIA writes the book; TSMC prints it. ASML builds the printing presses, and only ASML can build the most advanced ones.
- **Export controls = controlling who can buy the best ovens and the machines that make ovens.** China has responded by building many more ordinary ovens and wiring them together.
- **Cost per token = the cost per page of a printing business.** It depends on the price of the press, the electricity, how many hours a day it runs, and how many pages it prints per hour.
- **Edge vs. cloud AI = a pocket calculator vs. a call to a math department.** Local is private and instant but limited. The cloud is vast but needs a connection.

---

## Source list (primary and high-quality URLs consulted)

- NVIDIA Q2 FY2027 results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- NVIDIA Q2 FY27 summary: https://theenergymag.com/news/market-news/nvidia-q2-revenue-hits-96-2-b-as-data-center-surges-117-and-vera-rubin-ramps
- NVIDIA GB300 NVL72 specs: https://www.nvidia.com/en-us/data-center/gb300-nvl72/
- NVIDIA Vera Rubin NVL72 specs: https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/
- CES 2026 Rubin launch coverage: https://www.storagereview.com/news/nvidia-launches-vera-rubin-architecture-at-ces-2026-the-vr-nvl72-rack ; https://www.techbriefs.com/component/content/article/54442-ces-2026-nvidia-unveils-new-six-chip-rubin-ai-platform
- GTC 2025 roadmap: https://www.networkworld.com/article/3848394/nvidia-details-its-gpu-cpu-and-system-roadmap-for-the-next-three-years.html
- GTC 2026 keynote: https://www.eetimes.com/gtc-2026-keynote-long-live-the-inference-king/ ; https://www.jonpeddie.com/news/nvidia-gtc-2026-keynote/
- NVIDIA–Groq: https://www.fierce-network.com/cloud/heres-why-nvidia-dropping-20b-groqs-ai-tech ; https://www.constellationr.com/insights/news/nvidias-groq-deal-acquisition-acquihire-or-creative-licensing-deal
- AMD MI355X: https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html ; https://www.theregister.com/2025/06/12/amd_mi355x/
- AMD MI400/Helios/MI500: https://www.theregister.com/2026/01/07/mi500x_amd_ai/ ; https://www.datacenterfrontier.com/machine-learning/news/55399746/amd-helios-takes-ai-infrastructure-fight-to-rack-scale ; https://www.digitalcitizen.life/amd-instinct-mi455x-brings-432gb-of-hbm4-and-40-pflops-of-ai-compute-to-helios/
- Google TPU 8: https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next26 ; https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive
- Google Ironwood: https://www.theregister.com/2025/04/10/googles_7thgen_ironwood_tpus_debut/ ; https://www.theregister.com/2025/11/06/googles_ironwood_tpus_ai/
- TPU history: https://en.wikipedia.org/wiki/Tensor_Processing_Unit
- Anthropic–Google TPUs: https://www.maginative.com/article/anthropic-secures-1m-google-tpus-while-keeping-amazon-as-primary-training-partner/
- AWS Trainium3: https://aws.amazon.com/ai/machine-learning/trainium/ ; https://press.aboutamazon.com/2025/12/trainium3-ultraservers-now-available-enabling-customers-to-train-and-deploy-ai-models-faster-at-lower-cost ; https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap
- Microsoft Maia 200: https://www.trendforce.com/news/?p=52402 ; https://tbreak.com/microsoft-maia-200-a-custom-ai-accelerator/
- Meta–Rivos: https://www.barchart.com/story/news/35149291/meta-meta-expands-ai-chip-ambitions-with-2-billion-rivos-acquisition
- OpenAI–Broadcom: https://www.maginative.com/article/openai-and-broadcom-to-co-design-custom-ai-chips-deploy-10-gw-by-2029/
- Intel (government stake, NVIDIA investment): https://en.wikipedia.org/wiki/Intel
- Cerebras: https://www.cerebras.ai/chip
- HBM generations: https://en.wikipedia.org/wiki/High_Bandwidth_Memory
- Memory wall paper: https://arxiv.org/abs/2403.14123
- TSMC N2/A16: https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm
- EUV / High-NA: https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography ; https://www.asml.com/en/products/euv-lithography-systems/twinscan-exe-5200b
- Epoch AI trends: https://epoch.ai/trends ; models >1e25 FLOP: https://epoch.ai/data-insights/models-over-1e25-flop ; inference prices: https://epoch.ai/data-insights/llm-inference-price-trends
- Llama 3 infrastructure and failures: https://arxiv.org/html/2407.21783v3
- GPU rental prices: https://www.runpod.io/pricing ; https://lambda.ai/service/gpu-cloud
- Export controls: https://en.wikipedia.org/wiki/United_States_New_Export_Controls_on_Advanced_Computing_and_Semiconductors_to_China ; https://www.cfr.org/articles/new-ai-chip-export-policy-china-strategically-incoherent-and-unenforceable ; https://www.iaps.ai/research/bis-licensing-policy-for-h200s
- Huawei Ascend: https://www.crnasia.com/news/2026/artificial-intelligence/huawei-outlines-ascend-960-roadmap-and-million-processor-ai ; https://www.datacenterdynamics.com/en/news/huawei-announces-annual-release-cadence-for-three-new-ascend-ai-chips-unveils-supernode-offering-company-says-will-outperform-nvidias-nvl144/

**Items flagged [verify] for the fact-check pass:**
- exact HBM market shares;
- wafer and rack prices;
- High-NA tool price;
- TSMC foundry share and Arizona total;
- Rubin CPX status;
- Maia 300 timing;
- OpenAI–NVIDIA deal restructuring;
- Anthropic–Microsoft–NVIDIA figures;
- Project Rainier chip count;
- Intel 18A/Panther Lake and Crescent Island dates;
- SMIC 5 nm-class status;
- CHIPS ITC rate change;
- PCIe 7.0 date;
- edge-device specs (M5, Tensor G5, Jetson Thor, DGX Spark, Qualcomm AI200);
- details of China's 2025 regulatory actions against NVIDIA.
