# External-standard coverage audit: compute and data centers

Audit of the book (Chapters 1–66, with Chapters 32–44 as the main home) against three external standards, October 21, 2026. Topic lists come from the auditor's knowledge of each work; web search was unavailable. Chapter-level structure is given with confidence; where a section title is uncertain, the row names the topic the standard is known to cover rather than an exact section title. "Status before" is the book's state before this audit's edits. Statuses: COVERED (explained at beginner level), THIN (mentioned but not explained), MISSING, OUT OF SCOPE (too specialized; reason given).

## Standard 1: Barroso, Hölzle and Ranganathan, *The Datacenter as a Computer* (3rd edition, 2019)

Known chapter structure: 1 Introduction; 2 Workloads and Software Infrastructure; 3 WSC Hardware Building Blocks; 4 Data Center Basics (building, power, cooling); 5 Energy and Power Efficiency; 6 Modeling Costs; 7 Dealing with Failures and Repairs; 8 Closing Remarks. Rows below are topics within those chapters; exact section titles are not reproduced.

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Ch 1: the warehouse-scale computer idea (a whole building programmed as one computer) | THIN | Book title cited in "Going deeper" of Ch 34, 38, 40, 44; Ch 34 "one giant GPU"; Ch 37 "Collectives are how a cluster acts as one machine" | Added Ch 34 "The software that turns a cluster into one computer" with a WSC definition |
| Ch 1: cost efficiency at scale; one data center versus several | COVERED | Ch 4 "The cloud and the hyperscalers"; Ch 38 "Between data centers" and geographic redundancy; Ch 42 multi-site training | None |
| Ch 2: platform-level software (firmware, OS, drivers) | COVERED | Ch 3 operating systems; Ch 35 software stack (Figure 35.3) | None |
| Ch 2: cluster resource management and scheduling (Borg, Kubernetes, Slurm) | THIN | Ch 62 defines Kubernetes and Slurm only as skills; Ch 38 failure diagram shows an undefined "Job scheduler" | Added cluster scheduler and gang scheduling (Ch 34) |
| Ch 2: distributed storage (GFS/Colossus, object stores) | THIN | Storage appears only as a box in Ch 34 and Ch 38 network diagrams | Added distributed storage definition and a checkpoint-bandwidth worked example (Ch 34) |
| Ch 2: application frameworks (MapReduce and successors) | MISSING | Spark appears only in a Ch 63 careers table | Added MapReduce (Hadoop, Spark) definition tied to pretraining data processing (Ch 34) |
| Ch 2: application workloads (search, video, ML training and serving) | COVERED | Whole book; Ch 23, Ch 37, Ch 51 | None |
| Ch 2: monitoring (dashboards, tracing, health monitoring) | COVERED | Ch 31 LLMOps and tracing; Ch 38 BMS, DCIM, NOC and the GPU-failure sequence diagram | None (Ch 37 profiling addition extends it) |
| Ch 2: performance and availability toolbox (replication, sharding, load balancing, health checks, staged rollout) | COVERED | Ch 4 and Ch 44 load balancer; Ch 23 replica; Ch 37 sharding, hot spares, health checks; Ch 44 staged rollout | None |
| Ch 2: tail latency and tail-tolerant design ("The Tail at Scale", hedged requests) | THIN | Ch 34 one sentence on "tail latency"; Ch 6 defines p99; Ch 23 SLO and goodput | Added Ch 37 "Tail latency: why the slowest server sets your wait" (fan-out math 1 − 0.99^100, hedged requests, queueing delay, Table 37.11) |
| Ch 2: latency numbers engineers should know | COVERED | Ch 33 "Latency at human scale"; Ch 38 speed of light about 5 µs/km; Ch 44 time budget | None |
| Ch 2: buy versus build | COVERED | Ch 35 "Why build your own chip?"; Ch 38 business models; Ch 43 renting versus owning | None |
| Ch 2: cloud computing, virtual machines, containers | COVERED | Ch 4 (virtual machine definition); Ch 43 GPU-hour rental | None |
| Ch 2: information security at warehouse scale | COVERED | Ch 38 "Physical security"; Ch 4 HTTPS; Ch 56 model-weight security | None; hardware roots of trust judged OUT OF SCOPE as a detail |
| Ch 3: server and rack hardware | COVERED | Ch 34 rungs 3–4; Ch 38 "Inside the rack" | None |
| Ch 3: brawny versus wimpy cores (few strong versus many weak processors) | COVERED | Ch 32 CPU "few brilliant workers" versus GPU armies; Ch 36 "Worked example: many weaker chips" (more network, power and failures) | None (term itself not used) |
| Ch 3: accelerators in the WSC | COVERED | Ch 32, Ch 35 | None |
| Ch 3: cluster and host networking (fat tree, oversubscription, NICs/DPUs) | COVERED | Ch 34 "Switches and the fat tree", rail-optimized designs, DPU; Ch 38 non-blocking back end versus shared cloud networks | None |
| Ch 3: storage devices (disk, flash) | COVERED | Ch 2 storage; Ch 33 memory hierarchy | None |
| Ch 3: balanced designs | COVERED | Ch 33 ridge points; Ch 38 stranded capacity | None |
| Ch 4: tiers and building basics | COVERED | Ch 38 tour, Tiers I–IV, nines, SLA | None |
| Ch 4: power distribution (UPS, PDUs, AC versus DC, redundancy) | COVERED | Ch 39 power chain and 800 V DC; Ch 38 N+1 and 2N | None |
| Ch 4: cooling (CRACs, chillers, towers, free cooling, airflow, liquid, containers) | COVERED | Ch 40 throughout; Ch 38 modular data centers | None |
| Ch 5: PUE and its pitfalls; facility losses | COVERED | Ch 39 "What gets lost along the way"; Ch 40 "What PUE hides" | None |
| Ch 5: losses inside the server (beyond PUE) | COVERED | Ch 39 Watch out on power-supply and regulator losses; Ch 40 fan trick | None |
| Ch 5: energy efficiency of computing | COVERED | Ch 37 FLOPs-per-watt trends; Ch 23 tokens per watt | None |
| Ch 5: server utilization profile | COVERED | Ch 43 "Utilization" (60–80% of power capacity); Ch 42 | None |
| Ch 5: energy proportionality and idle power | MISSING | Not discussed | Added Ch 40 "Idle power and energy proportionality" (Barroso and Hölzle 2007, worked 1,000 W server example, Watch out) |
| Ch 5: low-power modes and DVFS | MISSING | Ch 32 gives power ≈ C × V² × f but never applies it to running chips | Added DVFS definition and worked 15% slowdown example (Ch 39) |
| Ch 5: energy efficiency through specialization | COVERED | Ch 32 accelerator zoo | None (DSA addition strengthens it) |
| Ch 5: power provisioning and oversubscription | MISSING | Nameplate and average-load facts only (Ch 39, Ch 42) | Added Ch 39 "Power budgets: oversubscription and capping" with a 30 MW worked example and the training-versus-inference contrast |
| Ch 5: power capping | MISSING | Not discussed | Added in the same Ch 39 section |
| Ch 5: energy storage for power management | COVERED | Ch 39 capacitors and batteries smoothing GPU swings | None |
| Ch 6: capital and operating costs, TCO | COVERED | Ch 43 capex/opex, cost per MW, TCO | None |
| Ch 6: case studies; partially filled data centers | COVERED | Ch 43 100 MW model; Ch 40 partial-load PUE; Ch 38 stranded capacity | None |
| Ch 6: cost of public clouds | COVERED | Ch 43 GPU-hour prices, neoclouds versus hyperscalers | None |
| Ch 7: software fault tolerance; failures as normal | COVERED | Ch 34 "Failures at scale"; Ch 37 checkpoints and goodput; Ch 38 training-hall redundancy | None |
| Ch 7: causes of service-level faults (software, configuration, people versus hardware) | MISSING | Not discussed | Added Ch 38 "What actually takes services down" with graceful degradation and availability-product Watch out |
| Ch 7: machine-level failure statistics (MTBF, memory errors, ECC, silent corruption) | THIN | Ch 37 MTBF, Llama 3 interruptions, silent data corruption; no ECC or memory-error data | Added ECC definition and the 2009 Google memory-error finding (Ch 37) |
| Ch 7: predicting faults, repairs and spares | COVERED | Ch 37 health checks and hot spares; Ch 38 failure-to-repair sequence, remote hands | None |
| Ch 8: Amdahl's law, end of Moore's law, accelerators | COVERED | Ch 32 Amdahl, Moore, Dennard; Ch 35 "Physics limits and the long bets" | None |
| Ch 8: "the attack of the killer microseconds", software-defined infrastructure | OUT OF SCOPE | Not named | None: systems-software research topics a general reader will not meet |

## Standard 2: Hennessy and Patterson, *Computer Architecture: A Quantitative Approach* (6th edition), Chapters 7 and 6

Known structure. Chapter 7, Domain-Specific Architectures: introduction; guidelines for DSAs; the DNN domain; Google's TPU (an inference data-center accelerator); Microsoft Catapult (a flexible data-center accelerator); Intel Crest (a training accelerator); Pixel Visual Core (a phone image-processing unit); cross-cutting issues; CPUs versus GPUs versus DNN accelerators; fallacies and pitfalls. Chapter 6, Warehouse-Scale Computers to Exploit Request-Level and Data-Level Parallelism: programming models and workloads; WSC architecture; efficiency and cost; cloud computing as utility computing; cross-cutting issues; a Google WSC; fallacies and pitfalls.

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Ch 7: why DSAs (end of Dennard scaling, slowing Moore's law, Amdahl limits) | COVERED | Ch 32 "Moore's law, Dennard scaling and the end of free speed", Amdahl's law | Added the term dark silicon (Ch 32) |
| Ch 7: the five guidelines for DSAs | THIN | Ideas appear separately (SRAM, systolic arrays, low precision, compilers) but never as a recipe; "domain-specific" only in Going deeper | Added Ch 32 "The recipe behind the zoo: five rules for domain-specific chips" with Table 32.8 (rule, TPU v1, 2026 echo) |
| Ch 7: DNN primer (MLPs, CNNs, RNNs, training versus inference, batching, quantization) | COVERED | Ch 12–15, Ch 23, Ch 32 | None |
| Ch 7: TPU v1 architecture (systolic array, 8-bit, on-chip buffers, compiler) and its successors | COVERED | Ch 32 systolic array worked with TPU v1 numbers; Ch 35 TPU generations table | Added 28 MiB on-chip memory detail |
| Ch 7: TPU v1 results and the 99th-percentile response-time limit on batch size | MISSING | Not discussed | Added "What the recipe bought" (15–30× speed, 30–80× performance per watt, 7 ms p99 deadline, 15 months) in Ch 32 |
| Ch 7: Microsoft Catapult (FPGAs across a data center) | MISSING | FPGA defined generically in Ch 32 | Added Catapult paragraph (Ch 32) |
| Ch 7: Intel Crest | OUT OF SCOPE | Not named | None: a cancelled 2017-era design; Ch 35 covers Intel's current Gaudi 3 and Crescent Island |
| Ch 7: Pixel Visual Core and image signal processors | MISSING | Not discussed | Added paragraph and ISP definition (Ch 32) |
| Ch 7: heterogeneity, SoCs, open instruction sets | COVERED | Ch 53 SoC definition; Ch 32 "Chips in your pocket"; RISC-V in Ch 32 and Ch 35 | None |
| Ch 7: CPU versus GPU versus accelerator on rooflines | COVERED | Ch 33 roofline and ridge points for 11 chips | None |
| Ch 7: cost-performance, TCO, performance per watt | COVERED | Ch 32 spec tables; Ch 43 TCO and custom-chip claims; Ch 37 FLOPs per watt | None |
| Ch 7: fallacies and pitfalls (throughput without latency, cost of a custom chip) | THIN | Spec-sheet skepticism in Ch 32 and Ch 34; chip design cost in Ch 35; throughput-latency curve in Ch 37 | Added Watch out on "inferences per second is a fair summary metric" (Ch 32) |
| Ch 6: request-level parallelism and WSC workloads | COVERED | Ch 23 replicas and batching; Ch 37 serving | None |
| Ch 6: programming models (MapReduce, Hadoop) | MISSING | Not discussed | Added MapReduce (Hadoop, Spark) definition (Ch 34) |
| Ch 6: WSC architecture and its memory/storage hierarchy | COVERED | Ch 33 hierarchy; Ch 34 network tiers | Distributed storage added (Ch 34) |
| Ch 6: efficiency and cost of WSCs (PUE, capex, opex, amortization) | COVERED | Ch 39 and Ch 40 PUE; Ch 43 capex, opex, depreciation | None |
| Ch 6: cloud computing as utility computing, economies of scale | COVERED | Ch 4; Ch 43 | None |
| Ch 6: cross-cutting issues (network bottlenecks, energy inside the server) | COVERED | Ch 38 non-blocking back end; Ch 34; Ch 39 conversion losses | None |
| Ch 6: a Google WSC put together (power, cooling, racks, network, servers) | COVERED | Ch 38 walking tour; Ch 39; Ch 40; Ch 34 | None |
| Ch 6: availability, outages, the nines | COVERED | Ch 38 Tiers, nines, SLA; Ch 34 and Ch 37 failure rates | None |
| Ch 6: fallacies (inactive versus active low-power modes, skipping ECC, microsecond delays, flash for disks) | THIN | None of the specific points discussed | Added DVFS (Ch 39), idle power and energy proportionality (Ch 40), ECC (Ch 37); microsecond-delay and flash-versus-disk points judged OUT OF SCOPE |

## Standard 3: Google DeepMind, "How to Scale Your Model" (2025)

Known structure (part titles approximately): rooflines; how to think about TPUs; sharded matrices and how to multiply them; all the Transformer math you need; parallelizing a Transformer for training; training LLaMA 3 on TPUs; Transformer inference; serving LLaMA 3 on TPUs; profiling TPU programs; programming TPUs in JAX; how to think about GPUs (a later addition); conclusions.

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Rooflines: arithmetic intensity, compute- versus memory-bound | COVERED | Ch 33 "Arithmetic intensity" and "The roofline model, worked with numbers" | None |
| Critical batch size (batch needed to reach the ridge point) | COVERED | Ch 33 Rubin example (about 456 users), Try it; Ch 37 Table 37.9 | None |
| Communication rooflines (when network time exceeds compute) | THIN | Ch 37 all-reduce timing, not compared with compute time | Added worked example (≈ 5,300 ÷ B tokens rule; Llama 3 layout gives about 4%) and Communication-bound definition (Ch 37) |
| TPU anatomy (MXU systolic arrays, HBM, on-chip memory) | COVERED | Ch 32 systolic arrays and MXU; Ch 35 TPU table | None; VMEM/VPU component names OUT OF SCOPE |
| TPU networking (ICI, wraparound torus, pods, links between pods) | COVERED | Ch 34 ICI, torus, Virgo, pods; scale-across | None |
| GPU anatomy (SMs, warps, tensor cores, shared memory, L2, HBM) | COVERED | Ch 32 "Inside a GPU"; Ch 33 | None |
| GPU networking (NVLink, NVSwitch, NVL72, InfiniBand fat tree) | COVERED | Ch 34 | None |
| Sharded matrices and sharded matrix multiplies | COVERED | Ch 37 tensor-parallel worked example; sharding definition | None; sharding notation OUT OF SCOPE |
| Collectives and their costs | COVERED | Ch 37 Table 37.7, ring all-reduce by hand, 2 × (N − 1) ÷ N | None |
| Transformer math (parameters, 2N and 6N FLOPs, training memory, KV cache size) | COVERED | Ch 5, Ch 19, Ch 33, Ch 37 | None |
| Attention FLOPs versus the 6ND rule at long context | THIN | Ch 15 quadratic attention scores, never related to 6ND | Added note after the 6ND rule (Ch 37) |
| Activation checkpointing (rematerialization) | COVERED | Ch 37 | None |
| Gradient accumulation | MISSING | Not discussed | Added paragraph and definition (Ch 37) |
| Training parallelism (data, FSDP/ZeRO, tensor, pipeline, mixed) mapped to network tiers | COVERED | Ch 37 "Splitting the work" | None |
| Worked training example (Llama 3 405B) | COVERED | Ch 37 TP 8 × PP 16 × DP 128, MFU 38–43% | None |
| Inference basics (prefill versus decode, latency versus throughput, memory-bound decode, KV cache) | COVERED | Ch 23; Ch 33; Ch 37 | None |
| Inference techniques (continuous batching, prefix caching, speculative decoding, quantization, disaggregation) | COVERED | Ch 23; Ch 37 | None |
| Worked serving example | COVERED | Ch 37 Table 37.9; Ch 33 users-per-GPU example | None |
| Profiling (profilers, traces, exposed communication) | THIN | Named only in Ch 33 and Ch 35 opportunity and moat bullets | Added Ch 37 "Finding the lost time: profiling" with Figure 37.14 (illustrative trace) |
| Compiler stack (JAX, XLA, kernel fusion) | COVERED | Ch 35 ML compiler definition; Ch 33 tiling and fusion; Ch 13 JAX | None; XLA's internal HLO format OUT OF SCOPE |
| Programming TPUs in JAX (jit, shard_map, sharding annotations) | OUT OF SCOPE | JAX and XLA are named and defined (Ch 13, Ch 35) | None: code-level material beyond this reader |

## Summary

| Standard | Topics | COVERED before | THIN before | MISSING before | OUT OF SCOPE | Covered after edits |
|---|---|---|---|---|---|---|
| Barroso, Hölzle and Ranganathan (3rd ed.) | 42 | 30 | 5 | 6 | 1 | 41 of 41 in scope (98% of all 42) |
| Hennessy and Patterson (6th ed.), Ch 7 and Ch 6 | 21 | 13 | 3 | 4 | 1 | 20 of 20 in scope (95% of all 21) |
| How to Scale Your Model (2025) | 21 | 16 | 3 | 1 | 1 | 20 of 20 in scope (95% of all 21) |
| **All three** | **84** | **59** | **11** | **11** | **3** | **81 of 81 in scope (96% of all 84)** |

Before this audit, 59 of 81 in-scope topics (73%) were covered at beginner level. The book was already strong on everything chip-, rack-, power-, cooling- and cost-shaped, which is where these standards overlap most with the research files. The gaps were the systems ideas that sit between hardware and service: the software layer that makes a building one computer, tail latency and queueing, power oversubscription and capping, energy proportionality, the causes of real outages, the DSA design recipe with its TPU, Catapult and Pixel Visual Core case studies, and two pieces of practitioner math (communication rooflines and profiling).

Edits (all with definition callouts in STYLE.md format and Key terms updated; 23 new definitions):
- Ch 32: new subsection "The recipe behind the zoo: five rules for domain-specific chips" (Table 32.8; DSA, dark silicon, ISP; TPU v1 results; Catapult; Pixel Visual Core; fallacy Watch out).
- Ch 34: new subsection "The software that turns a cluster into one computer" (WSC, cluster scheduler, gang scheduling, distributed storage, MapReduce; checkpoint-bandwidth worked example).
- Ch 37: attention-versus-6ND note; gradient accumulation; communication-roofline worked example; "Finding the lost time: profiling" (new Figure 37.14, later figures renumbered 37.15–37.18, no in-text references affected); ECC and memory errors; "Tail latency: why the slowest server sets your wait" (Table 37.11).
- Ch 38: new subsection "What actually takes services down" (graceful degradation; availability of a chain of parts).
- Ch 39: new section "Power budgets: oversubscription and capping" (power oversubscription, power capping, DVFS; two worked examples).
- Ch 40: new subsection "Idle power and energy proportionality" (worked example, Watch out).

Sources: all added facts are stable textbook or paper knowledge (Barroso and Hölzle 2007 and 2009; Dean and Barroso 2013; Jouppi et al. 2017; Schroeder, Pinheiro and Weber 2009; Hennessy and Patterson 6th ed.); no new 2025–26 facts were introduced beyond figures already in the chapters. validate.py: 51/51 diagrams valid across Chapters 32, 34, 37, 38, 39, 40. check.py: all six chapters OK.
