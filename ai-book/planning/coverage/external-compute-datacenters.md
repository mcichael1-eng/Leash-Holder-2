# External-standard coverage audit: compute and data centers

Audit of the book (Chapters 1–66, with Chapters 32–44 as the main home) against three external standards, October 21, 2026. Topic lists were first reconstructed from the auditor's knowledge of each work, without web access, and then verified online the same day against the published contents (publisher pages, Crossref chapter records, the open-access fourth edition of Barroso et al., the publisher's official lecture slides for Hennessy and Patterson, and the live scaling-book site); see "Verified online (October 21, 2026)" at the end. Rows corrected by that check carry a bracketed "[Verified Oct 21: ...]" note; the original wording is kept for the record. Where a section title is uncertain, the row names the topic the standard covers rather than an exact section title. "Status before" is the book's state before this audit's edits. Statuses: COVERED (explained at beginner level), THIN (mentioned but not explained), MISSING, OUT OF SCOPE (too specialized; reason given).

## Standard 1: Barroso, Hölzle and Ranganathan, *The Datacenter as a Computer* (3rd edition, 2019)

Known chapter structure: 1 Introduction; 2 Workloads and Software Infrastructure; 3 WSC Hardware Building Blocks; 4 Data Center Basics (building, power, cooling); 5 Energy and Power Efficiency; 6 Modeling Costs; 7 Dealing with Failures and Repairs; 8 Closing Remarks. Rows below are topics within those chapters; exact section titles are not reproduced. [Verified Oct 21: all eight third-edition chapter titles confirmed exactly (Crossref; "Data Center Basics: Building, Power, and Cooling"). A fourth edition now exists (Springer, December 2025, open access, retitled *The Data Center as a Computer*, 12 chapters); it was audited section by section in the final section. The third edition itself dates from 2018 (the fourth edition's preface says June 2018), not 2019 as the heading says.]

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
| Ch 2: information security at warehouse scale | COVERED | Ch 38 "Physical security"; Ch 4 HTTPS; Ch 56 model-weight security | None; hardware roots of trust judged OUT OF SCOPE as a detail [Verified Oct 21: the fourth edition gives root of trust and confidential computing their own sections (10.2.3, 10.2.5); re-audited as MISSING and added to Ch 38] |
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
| Ch 8: "the attack of the killer microseconds", software-defined infrastructure | OUT OF SCOPE | Not named | None: systems-software research topics a general reader will not meet [Verified Oct 21: the fourth edition makes software-defined infrastructure a whole chapter (Ch 7); its parts were re-audited separately below and software-defined networking was added to Ch 34; killer microseconds stays OUT OF SCOPE] |

## Standard 2: Hennessy and Patterson, *Computer Architecture: A Quantitative Approach* (6th edition), Chapters 7 and 6

Known structure. Chapter 7, Domain-Specific Architectures: introduction; guidelines for DSAs; the DNN domain; Google's TPU (an inference data-center accelerator); Microsoft Catapult (a flexible data-center accelerator); Intel Crest (a training accelerator); Pixel Visual Core (a phone image-processing unit); cross-cutting issues; CPUs versus GPUs versus DNN accelerators; fallacies and pitfalls. Chapter 6, Warehouse-Scale Computers to Exploit Request-Level and Data-Level Parallelism: programming models and workloads; WSC architecture; efficiency and cost; cloud computing as utility computing; cross-cutting issues; a Google WSC; fallacies and pitfalls. [Verified Oct 21: Elsevier's official sixth-edition lecture slides confirm the Chapter 7 sequence Introduction, Guidelines for DSAs, Example: Deep Neural Networks, Tensor Processing Unit, Microsoft Catapult, Intel Crest, Pixel Visual Core, Fallacies and Pitfalls, and the Chapter 6 title and topics (Programming Models and Workloads for WSCs; Computer Architecture of WSC; Physical Infrastructure and Costs of WSC; Cloud Computing; Fallacies and Pitfalls). Elsevier's shop page lists Chapter 6 as "The Warehouse-Scale Computer". The cross-cutting, "a Google WSC" and CPU-versus-GPU-versus-DNN-accelerator sections could not be confirmed from the sources fetched. A seventh edition exists (2025); see the final section.]

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
| Ch 7: fallacies and pitfalls (throughput without latency, cost of a custom chip) [Verified Oct 21: the actual list has five items: "It costs $100 million to design a custom chip"; "Performance counters added as an afterthought"; "Architects are tackling the right DNN tasks"; "For DNN hardware, inferences per second (IPS) is a fair summary performance metric"; "Being ignorant of architecture history when designing a DSA". The first and fourth are this row; the other three are new rows below] | THIN | Spec-sheet skepticism in Ch 32 and Ch 34; chip design cost in Ch 35; throughput-latency curve in Ch 37 | Added Watch out on "inferences per second is a fair summary metric" (Ch 32) |
| Ch 6: request-level parallelism and WSC workloads | COVERED | Ch 23 replicas and batching; Ch 37 serving | None |
| Ch 6: programming models (MapReduce, Hadoop) | MISSING | Not discussed | Added MapReduce (Hadoop, Spark) definition (Ch 34) |
| Ch 6: WSC architecture and its memory/storage hierarchy | COVERED | Ch 33 hierarchy; Ch 34 network tiers | Distributed storage added (Ch 34) |
| Ch 6: efficiency and cost of WSCs (PUE, capex, opex, amortization) [Verified Oct 21: the slides title this "Physical Infrastructure and Costs of WSC", with "Efficiency and Cost of WSC" on its opening slide] | COVERED | Ch 39 and Ch 40 PUE; Ch 43 capex, opex, depreciation | None |
| Ch 6: cloud computing as utility computing, economies of scale | COVERED | Ch 4; Ch 43 | None |
| Ch 6: cross-cutting issues (network bottlenecks, energy inside the server) | COVERED | Ch 38 non-blocking back end; Ch 34; Ch 39 conversion losses | None |
| Ch 6: a Google WSC put together (power, cooling, racks, network, servers) | COVERED | Ch 38 walking tour; Ch 39; Ch 40; Ch 34 | None |
| Ch 6: availability, outages, the nines | COVERED | Ch 38 Tiers, nines, SLA; Ch 34 and Ch 37 failure rates | None |
| Ch 6: fallacies (inactive versus active low-power modes, skipping ECC, microsecond delays, flash for disks) [Verified Oct 21: "flash for disks" is not in the published list and was a reconstruction error; the real list has nine items, the six not named here are new rows below] | THIN | None of the specific points discussed | Added DVFS (Ch 39), idle power and energy proportionality (Ch 40), ECC (Ch 37); microsecond-delay and flash-versus-disk points judged OUT OF SCOPE |

## Standard 3: Google DeepMind, "How to Scale Your Model" (2025)

Known structure (part titles approximately): rooflines; how to think about TPUs; sharded matrices and how to multiply them; all the Transformer math you need; parallelizing a Transformer for training; training LLaMA 3 on TPUs; Transformer inference; serving LLaMA 3 on TPUs; profiling TPU programs; programming TPUs in JAX; how to think about GPUs (a later addition); conclusions. [Verified Oct 21: topics and order correct except the last two, which are reversed: Conclusions and Further Reading is Chapter 11 and How to Think About GPUs is Chapter 12 (added August 18, 2025; the book itself is dated February 4, 2025, by Jacob Austin and colleagues at Google DeepMind). Exact titles are in the final section.]

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
| Collectives and their costs [Verified Oct 21: the standard treats AllGather, ReduceScatter, AllToAll and compute-communication overlap as separate subsections; split out as a new row below] | COVERED | Ch 37 Table 37.7, ring all-reduce by hand, 2 × (N − 1) ÷ N | None |
| Transformer math (parameters, 2N and 6N FLOPs, training memory, KV cache size) | COVERED | Ch 5, Ch 19, Ch 33, Ch 37 | None |
| Attention FLOPs versus the 6ND rule at long context | THIN | Ch 15 quadratic attention scores, never related to 6ND | Added note after the 6ND rule (Ch 37) |
| Activation checkpointing (rematerialization) | COVERED | Ch 37 | None |
| Gradient accumulation | MISSING | Not discussed | Added paragraph and definition (Ch 37) |
| Training parallelism (data, FSDP/ZeRO, tensor, pipeline, mixed) mapped to network tiers | COVERED | Ch 37 "Splitting the work" | None |
| Worked training example (Llama 3 405B) [Verified Oct 21: the standard's Chapter 6 works LLaMA 3-70B, not 405B; the book's Ch 37 uses Meta's published 405B layout, which teaches the same skill] | COVERED | Ch 37 TP 8 × PP 16 × DP 128, MFU 38–43% | None |
| Inference basics (prefill versus decode, latency versus throughput, memory-bound decode, KV cache) | COVERED | Ch 23; Ch 33; Ch 37 | None |
| Inference techniques (continuous batching, prefix caching, speculative decoding, quantization, disaggregation) | COVERED | Ch 23; Ch 37 | None |
| Worked serving example [Verified Oct 21: the standard's Chapter 8 is "Serving LLaMA 3-70B on TPUs"] | COVERED | Ch 37 Table 37.9; Ch 33 users-per-GPU example | None |
| Profiling (profilers, traces, exposed communication) | THIN | Named only in Ch 33 and Ch 35 opportunity and moat bullets | Added Ch 37 "Finding the lost time: profiling" with Figure 37.14 (illustrative trace) |
| Compiler stack (JAX, XLA, kernel fusion) | COVERED | Ch 35 ML compiler definition; Ch 33 tiling and fusion; Ch 13 JAX | None; XLA's internal HLO format OUT OF SCOPE |
| Programming TPUs in JAX (jit, shard_map, sharding annotations) | OUT OF SCOPE | JAX and XLA are named and defined (Ch 13, Ch 35) | None: code-level material beyond this reader |

## Summary

All OUT OF SCOPE topics are explained in plain words in Appendix F (The Advanced Shelf).

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

## Verified online (October 21, 2026)

The three topic lists above were checked against the real published contents. Corrections to existing rows are marked in place with "[Verified Oct 21: ...]". New rows below cover topics the reconstruction missed or merged; each was audited the same way as the original rows (grep the book, read the passage, then decide), and every THIN or MISSING in-scope topic was filled in its owning chapter per OUTLINE.md.

### Standard 1: Barroso, Hölzle and Ranganathan

URLs fetched:
- https://api.crossref.org/works/10.1007/978-3-031-01761-2_1 through _8 (third-edition chapter titles)
- https://ieeetcca.org/2018/11/19/new-book-the-datacenter-as-a-computer-designing-warehouse-scale-machines-third-edition/ (third-edition contents, chapter level)
- https://link.springer.com/book/10.1007/978-3-031-99489-0 (fourth edition: contents, dates, "About this book")
- https://api.crossref.org/works/10.1007/978-3-031-99489-0_1 through _12 (fourth-edition chapter titles and pages)
- https://www.repository.gctu.edu.gh/files/original/fda39897b5038ec6884c65fdb461cd3b.pdf (a copy of the Springer PDF, which is CC BY 4.0; used for the section-level outline and the passages behind the fills)
- Fill sources: https://deepmind.google/discover/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-by-40/ ; https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/availability-zones.html ; https://ghgprotocol.org/sites/default/files/standards/ghg-protocol-revised.pdf ; https://www.nvidia.com/en-us/data-center/solutions/confidential-computing/
- Not reachable: OAPEN's open-access third-edition record (403), a library contents record (503) and Springer's third-edition chapter pages (abstracts only), so third-edition section titles remain unverified.

What differed:
- The third-edition chapter list was exactly right.
- A fourth edition exists: *The Data Center as a Computer* (Springer, Synthesis Lectures on Computer Architecture; eBook December 27, 2025, copyright 2026; open access under CC BY 4.0). It has 12 chapters instead of 8: 1 Introduction; 2 Overview of WSC Architecture; 3 Overview of WSC Workloads; 4 WSC Software: Distributed Systems Infrastructure; 5 WSC Hardware: Data Center Infrastructure; 6 WSC Hardware: Computing Building Blocks; 7 Software-Defined Infrastructure; 8 Performance and Costs; 9 Energy and Sustainability; 10 Trusted Computing: Reliability, Availability, Security, Privacy; 11 A Twenty Five Year WSC Journey; 12 A Selection of 25 Top Papers for 25 Years of WSC. The original rows map onto it as: old Ch 2 → new Ch 3 and 4; old Ch 3 → new Ch 6; old Ch 4 → new Ch 5; old Ch 5 → new Ch 9; old Ch 6 → new Ch 8; old Ch 7 → new Ch 10; old Ch 8 → new Ch 11.
- The fourth edition was audited section by section; the rows below are its topics that the original 42 rows did not already cover.
- The book's four "Going deeper" entries for this title (Ch 34, 38, 40, 44) said "Morgan & Claypool, free online"; they now point to the open-access fourth edition.

| Topic (fourth-edition section) | Status before | Where in the book | Action |
|---|---|---|---|
| Regions and zones; zonal and regional failures (2.1, 10.1.9) | THIN | Ch 4 defined only "Region (cloud)"; Ch 38 geographic redundancy | Added Availability zone definition and a 2-zone versus 3-zone capacity worked example (200 versus 150 servers) to Ch 4 |
| AI workloads: training, inference, LLMs (3.3) | COVERED | Ch 19, 23, 37 | None |
| Public-cloud VM platform case study: verified boot, tiered offloads, provisioning, live migration (3.4) | OUT OF SCOPE | Ch 4 virtual machines; Ch 34 DPUs | None: cloud-platform internals; the root-of-trust idea is now in Ch 38 |
| Data processing services and structured storage (BigQuery, Dataflow, Bigtable, Spanner) (3.5, 4.2.3) | COVERED | Ch 11 warehouses, lakes, pipelines; Ch 34 MapReduce and distributed storage | None; named Google systems OUT OF SCOPE |
| Error codes and integrity checking: replication math, erasure codes, background scrubbing; storage errors (3.6.2, 10.1.5) | THIN | Ch 34 "chunks kept, with copies"; Ch 37 ECC | Added to Ch 34: worked replication example (2% → 0.0008% with three copies), Erasure coding definition (6 + 3 pieces at 1.5× cost), checksums and background sweeps |
| Brownouts (3.6.3) | COVERED | Ch 38 graceful degradation | None |
| Health monitoring and canaries (3.6.4) | COVERED | Ch 10 canary release; Ch 37 health checks; Ch 44 staged rollout | None |
| Consensus (3.6.6) | MISSING | Not discussed | Added Consensus definition to Ch 34 (Chubby 2006, ZooKeeper, etcd; why majorities favor groups of three) |
| Compression and encryption (3.6.7) | COVERED | Ch 3 compression; Ch 4 encryption and HTTPS | None |
| WAN and edge networking (4.2.4, 6.4.7) | COVERED | Ch 4 backbone and CDN; Ch 38 DCI and AI WANs | None |
| Infrastructure management: provisioning, configuration, observability, DevOps and SRE; operational practices (4.3, 10.1.11) | COVERED | Ch 31 observability; Ch 63 SRE; Ch 38 NOC and causes of outages; Ch 44 staged rollout | None |
| Cloud and AI implications for data center design (5.1.4) | COVERED | Ch 38 throughout | None |
| Power microgrids and future opportunities (5.2.5) | COVERED | Ch 41 microgrid; Ch 39 800 V DC | None |
| Modular data center design (5.4.1) | COVERED | Ch 38 modular data centers; Ch 42 prefabricated power skids and cooling modules | None |
| Economic models: the five envelopes (5.4.2) | COVERED | Ch 38 business models (self-build, powered land, powered shell, colocation, layer-by-layer table); Ch 42 lifecycle | None; the framework's name is not used |
| Physical automation in the data center (5.4.3) | MISSING | Not discussed | Added Ch 38 paragraph (rack-moving robot, about five times faster, part tracking for drives with user data) |
| Individual servers as distributed systems (multi-node servers) (6.2.3) | COVERED | Ch 34 superchips, compute trays, NVL72 | None |
| Video accelerators and VCU systems (6.3.3) | MISSING | Not discussed | Added Ch 32 paragraph and Transcoding definition (VCU, 8 to 20 times software-encoding throughput) |
| Spine-less networking; optics in WSCs (6.4.4, 6.4.5) | THIN | Ch 34 OCS for TPU pods only | Added Ch 34 paragraph on Jupiter replacing the spine layer with optical circuit switches |
| Storage hardware: media, diskless servers, disk and flash appliances, smart storage (6.5) | COVERED | Ch 2 and Ch 33 media; Ch 34 distributed storage | None; appliance designs OUT OF SCOPE |
| Software-defined servers and memory: compiler and library tuning, platform-aware scheduling, far memory (7.1) | OUT OF SCOPE | Ch 33 CXL memory tiers; Ch 35 ML compilers | None: fleet-efficiency engineering beyond this reader |
| Software-defined networks: Jupiter, B4, bandwidth enforcement (7.3) | MISSING | Not discussed (no mention of SDN) | Added Software-defined networking (SDN) definition and B4 to Ch 34 |
| Software-defined storage, power and fleet (7.4, 7.5) | COVERED | Ch 39 power capping and oversubscription | None; storage tiering details OUT OF SCOPE |
| Self-driving systems: ML to run and design WSCs (7.6, 11.3.5) | MISSING | Not discussed | Added Ch 40 paragraph on ML-controlled cooling (DeepMind 2016: 40% less cooling energy, about 15% lower PUE overhead; worked 1.12 → 1.10) and the fourth edition's note that it is still uncommon. AI-designed chip layouts not added: only the vendor's own blog was fetched |
| Fleetwide workload characterization and performance modeling (8.1) | OUT OF SCOPE | Ch 37 profiling | None: general-fleet profiling ("data center tax") is beyond this reader |
| Beyond PUE to SPUE (9.2.5) | COVERED | Ch 39 Watch out on server losses; Ch 40 fan trick | None; the acronym SPUE is not used |
| Measuring energy efficiency (9.3.1) | COVERED | Ch 23 tokens per watt; Ch 37 FLOPs per watt; Ch 35 MLPerf | None |
| Power stranding (9.5.1) | COVERED | Ch 38 stranded capacity | None |
| Intermittent energy supply (9.5.5) | COVERED | Ch 41 variable power, batteries, flexible loads | None |
| Emissions: Scope 1, 2, 3 (9.6.1) | THIN | Ch 40 embodied carbon and CUE; scopes never named | Added Emission scopes definition to Ch 41, with Google's 1% Scope 1, the 3:1 Scope 3 to Scope 2 ratio and why the accounting clocks differ (TPU lifecycle about 70% electricity) |
| Carbon-aware scheduling (9.6.2) | THIN | Ch 39 opportunity bullet; Ch 41 frontier callout | Added Carbon-aware computing definition and time- and place-shifting paragraph to Ch 41 |
| Water (9.6.3) | COVERED | Ch 40 WUE and "Water, done carefully" | None |
| Other sustainability: low-carbon materials, reuse and recycling (9.6.4) | COVERED | Ch 40 embodied carbon | None; building-material details OUT OF SCOPE |
| Energy usage of AI (9.7) | COVERED | Ch 39, 40, 41, 44 | None |
| Energy usage of the internet and cryptocurrency (9.8) | OUT OF SCOPE | Data center share of electricity in Ch 39 and 41 | None: crypto and whole-internet energy are outside an AI book's scope |
| Silent data corruptions and corrupt execution errors (10.1.10) | COVERED | Ch 37 silent data corruption | None |
| Security of servers; silicon root of trust (10.2.2, 10.2.3) | MISSING | Not discussed (the original audit had judged it OUT OF SCOPE) | Added Root of trust definition to Ch 38 |
| Confidential computing (10.2.5) | MISSING | Not discussed | Added Confidential computing definition to Ch 38 (CPUs from AMD, Intel, Arm; NVIDIA Hopper, Blackwell and Rubin per NVIDIA) |
| CPU vulnerabilities; secure service deployment (10.2.6, 10.2.7) | OUT OF SCOPE | Not discussed | None: security engineering detail |
| A twenty-five-year WSC journey: epochs and lessons (11) | OUT OF SCOPE | General lessons (scale, specialization, co-design) in Ch 32 and 35 | None: company history |
| A selection of 25 top papers (12) | OUT OF SCOPE | Several of the papers are cited in Ch 34, 37, 40 | None: an annotated bibliography, not a topic |

### Standard 2: Hennessy and Patterson

URLs fetched:
- https://shop.elsevier.com/books/computer-architecture/hennessy/978-0-12-811905-1 and https://www.inspectioncopy.elsevier.com/book/details/9780128119051 (sixth edition, chapter level)
- https://www.sigarch.org/other-announcements/book-release-6th-edition-of-computer-architecture-a-quantitative-approach/ (sixth-edition announcement)
- https://cse.buffalo.edu/~rsridhar/cse490-590/lec/ch7-2025.pdf and https://cse.buffalo.edu/~rsridhar/cse490-590/lec/ch6.pdf (Elsevier's official sixth-edition lecture slides, "Copyright 2019 Elsevier", hosted on a University at Buffalo course page; the only section-level source found, and secondary)
- https://shop.elsevier.com/books/computer-architecture/hennessy/978-0-443-15406-5 and https://library.naist.jp/opac/en/volume/264553 (seventh edition)

What differed:
- Chapter 7 structure was right, including Intel Crest (the SIGARCH announcement calls it "a short description of the Intel Nervana Neural Network Processor").
- Chapter 6: the reconstructed long title matches the slides; Elsevier's shop page lists it as "The Warehouse-Scale Computer". "Efficiency and cost" appears as "Physical Infrastructure and Costs of WSC".
- Both fallacy rows were merged or partly invented: Chapter 7 has five fallacies and pitfalls, Chapter 6 has nine; "flash for disks" is not among them.
- A seventh edition exists: Hennessy, Patterson and new co-author Christos Kozyrakis (Morgan Kaufmann; Elsevier lists October 24 and December 2, 2025; catalogs give 2026). Its chapters: 1 Fundamentals of Quantitative Design and Analysis; 2 Memory Hierarchy Design; 3 Instruction-Level Parallelism and Its Exploitation; 4 Data-Level Parallelism in Vector, SIMD, and GPU Architectures; 5 Thread-Level Parallelism; 6 Warehouse-Scale Systems for Utility Computing; 7 Domain-Specific Architectures. The publisher says it adds coverage of GPU and CPU architectures, domain-specific architectures, systems on chip and heterogeneous computing, with a "Putting It All Together" section per chapter. UNRESOLVED: no public section-level contents were found for its Chapters 6 and 7, and this round's web-search budget ran out, so what its AI material covers below chapter level is unverified.

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Ch 7 pitfall: performance counters added as an afterthought | OUT OF SCOPE | Ch 37 profiling explains why measurement matters | None: chip-design practice |
| Ch 7 fallacy: architects are tackling the right DNN tasks | OUT OF SCOPE | Ch 35 MLPerf; Ch 24 benchmarks | None: a 2017 point about which networks dominated data-center workloads |
| Ch 7 pitfall: being ignorant of architecture history when designing a DSA | OUT OF SCOPE | Ch 32 traces systolic arrays to Kung and Leiserson (1978) | None |
| Ch 6 fallacy: cloud computing providers are losing money | OUT OF SCOPE | Ch 43 cloud and chain economics | None: a dated 2017 business claim |
| Ch 6 pitfall: focusing on average performance instead of 99th-percentile performance | COVERED | Ch 37 tail latency; Ch 6 percentiles | None |
| Ch 6 pitfall: using too wimpy a processor to improve WSC cost-performance | COVERED | Ch 36 worked example "many weaker chips"; Ch 32 | None |
| Ch 6 pitfall: inconsistent measure of PUE by different companies | COVERED | Ch 40 "What PUE hides" | None |
| Ch 6 fallacy: capital costs of the WSC facility are higher than for the servers it houses | COVERED | Ch 43 cost per MW (building versus IT equipment several times larger) | None |
| Ch 6 fallacy: turning off hardware during periods of low activity improves the cost-performance of a WSC | THIN | Ch 40 idle power; Ch 39 DVFS; no direct discussion | Added Ch 40 paragraph (wake-up penalty, purchase price dominates, prefer active low-power modes and filling quiet hours) |

The Chapter 7 "$100 million custom chip" fallacy stays in the original row as COVERED: Ch 35 and 36 discuss design cost, though they quote several hundred million dollars for a leading-edge 2026 chip, a different claim from the textbook's 2017 argument, whose wording was not available.

### Standard 3: How to Scale Your Model

URLs fetched: https://jax-ml.github.io/scaling-book/ and its chapter pages roofline/, tpus/, sharding/, transformers/, training/, applied-training/, inference/, applied-inference/, profiling/, jax-stuff/, conclusion/, gpus/ (all under https://jax-ml.github.io/scaling-book/).

What differed:
- Real structure (two numberings on the site): Part 1 Preliminaries: 1 A Brief Intro to Roofline Analysis (page title "All About Rooflines"), 2 How to Think About TPUs, 3 Sharded Matrices and How to Multiply Them. Part 2 Transformers: 4 All the Transformer Math You Need to Know, 5 How to Parallelize a Transformer for Training, 6 Training LLaMA 3 on TPUs, 7 All About Transformer Inference, 8 Serving LLaMA 3-70B on TPUs. Part 3 Practical Tutorials: 9 How to Profile TPU Programs, 10 Programming TPUs in JAX. Part 4 Conclusions and Bonus Content: 11 Conclusions and Further Reading, 12 How to Think About GPUs. The site menu numbers the same pages Part 0 (Introduction) to Part 12.
- The reconstruction had Conclusions and GPUs in the wrong order, and its worked examples are LLaMA 3-70B rather than 405B (rows annotated).
- Section level adds MoE math, FlashAttention, separate collective primitives, sharded-inference layouts, the JetStream engine, GPU collectives with in-network reduction, and GB200 notes.

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Sparsity and mixture-of-experts math; expert parallelism (Ch 4, Ch 12) | COVERED | Ch 17 MoE and expert parallelism; Ch 37 expert parallelism and all-to-all; Ch 19 active parameters in 6ND | None |
| FlashAttention (Ch 4 appendix) | COVERED | Ch 15 | None |
| Collective primitives in depth (AllGather, ReduceScatter, AllToAll) and overlapping communication with compute (Ch 3) | COVERED | Ch 37 collectives table, FSDP diagram, overlap and exposed communication in the profiling section; Ch 17 all-to-all | None |
| Sharded inference layouts: sharding the KV cache, 2D weight-stationary sharding, latency-bound collectives (Ch 7 and appendices) | OUT OF SCOPE | Ch 37 tensor-parallel serving; Ch 33 KV cache memory | None: practitioner layout detail |
| An inference engine implementation, JetStream (Ch 7) | OUT OF SCOPE | Ch 23 serving engines (vLLM, SGLang, TensorRT-LLM, Dynamo) | None: one named implementation |
| Achieved versus advertised link bandwidth (Ch 12) | COVERED | Ch 32 peak versus achieved; Ch 34 spec-sheet detective | None |
| In-network reductions, NVIDIA SHARP (Ch 12) | OUT OF SCOPE | Not discussed | None: the standard itself measures only about 30% gain and calls pure all-reduces rare in LLMs |
| How GB200 NVL72 changes the GPU picture (Ch 12 appendix) | COVERED | Ch 34 NVL72 "one giant GPU" | None |

### Updated counts

| Standard | Rows | COVERED before | THIN before | MISSING before | OUT OF SCOPE | Covered after edits |
|---|---|---|---|---|---|---|
| Barroso, Hölzle and Ranganathan (3rd ed. rows plus 4th ed. additions) | 42 + 41 = 83 | 30 + 22 = 52 | 5 + 5 = 10 | 6 + 7 = 13 | 1 + 7 = 8 | 75 of 75 in scope (90% of all 83) |
| Hennessy and Patterson (6th ed.), Ch 7 and Ch 6 | 21 + 9 = 30 | 13 + 4 = 17 | 3 + 1 = 4 | 4 + 0 = 4 | 1 + 4 = 5 | 25 of 25 in scope (83% of all 30) |
| How to Scale Your Model (2025) | 21 + 8 = 29 | 16 + 5 = 21 | 3 + 0 = 3 | 1 + 0 = 1 | 1 + 3 = 4 | 25 of 25 in scope (86% of all 29) |
| **All three** | **142** | **90** | **17** | **18** | **17** | **125 of 125 in scope (88% of all 142)** |

Before both rounds, 90 of 125 in-scope topics (72%) were covered at beginner level; after them, all 125 are.

Edits in this round (9 new definitions, all in STYLE.md format and added to Key terms; validate.py clean on all seven files; check.py OK for Chapters 4, 32, 34, 38, 40, 41, 44):
- Ch 4: zones paragraph, Availability zone, 2-zone versus 3-zone worked example.
- Ch 32: VCU paragraph, Transcoding.
- Ch 34: Jupiter spine-less paragraph, Software-defined networking (SDN), B4; Consensus; replication worked example, Erasure coding, checksums and scrubbing; Going deeper entry updated to the fourth edition.
- Ch 38: physical automation paragraph; Root of trust (silicon root of trust); Confidential computing; Going deeper entry updated.
- Ch 40: ML-controlled cooling paragraph with worked PUE example; "turning off hardware" fallacy paragraph; Going deeper entry updated.
- Ch 41: Emission scopes (Scope 1 to Scope 3) with the accounting-clock comparison; Carbon-aware computing (carbon-intelligent scheduling).
- Ch 44: Going deeper entry updated to the fourth edition.
