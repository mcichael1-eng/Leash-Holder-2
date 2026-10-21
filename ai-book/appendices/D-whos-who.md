# Appendix D: Who's Who: Companies, Labs, Products and People

*A quick reference to the organizations and people named in this book, grouped by where they sit in the AI stack.*

How to use this appendix: each row gives one or two plain-English lines and the chapter where the topic is covered in depth. Model names, products and job titles are as of October 2026 and change quickly; check the company's own site before relying on them. Revenue, valuation and deal figures are deliberately left out here, because they go stale within weeks; Chapter 61 and Chapter 43 discuss them with dates and sources.

## Frontier labs and their flagship models

| Lab | Who they are | Flagship models and products, as of October 2026 | More in |
|---|---|---|---|
| OpenAI | San Francisco lab founded in 2015 as a nonprofit; its for-profit arm became OpenAI Group PBC, controlled by the OpenAI Foundation, in 2025. Maker of ChatGPT. | GPT-6 Astra, GPT-6 Sol and Luna, GPT-6.1 Sol; open-weight gpt-oss-120b and gpt-oss-20b; Codex coding agent | Chapter 24 |
| Anthropic | San Francisco lab founded in 2021 by former OpenAI researchers, including Dario and Daniela Amodei; a public benefit corporation with a safety focus. | Claude Fable 5.1 and Mythos 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5; Claude Code; created the Model Context Protocol (MCP) | Chapter 24 |
| Google DeepMind | Google's AI lab, formed in 2023 by merging DeepMind (founded in London in 2010, bought by Google in 2014) with Google Brain. | Gemini 4 Argon, Gemini 3.8 Flash; open-weight Gemma 4; Genie 3 world model; AlphaFold | Chapter 24 |
| Meta Superintelligence Labs (MSL) | Meta's AI organization, formed in mid-2025; includes the FAIR research lab and TBD Lab. | Muse Wonder and Wonder Full, Muse Spark, open-weight Muse Glimmer; the earlier Llama family (last: Llama 4, 2025) | Chapter 24 |
| SpaceXSI (formerly xAI) | Founded by Elon Musk in 2023; acquired by SpaceX on February 2, 2026, and renamed SpaceXSI in October 2026. | Grok 4.7; the Colossus supercomputers in Memphis | Chapter 24 |
| Microsoft AI | Microsoft's in-house AI group; Microsoft was OpenAI's earliest large backer and is also an Anthropic compute partner. | Copilot assistants in Windows and Office; in-house models | Chapter 61 |
| Amazon | Builds its own Nova models and the Bedrock platform that serves many labs' models; Anthropic's main cloud and training partner. | Nova models; Bedrock; Alexa | Chapter 61 |
| DeepSeek | Hangzhou lab founded in 2023 by Liang Wenfeng and funded by the quantitative hedge fund High-Flyer; known for efficient open-weight models. | DeepSeek V4-Pro, V4-Flash, V4.1-Flash (MIT license); the R1 reasoning model (2025) | Chapter 21 |
| Alibaba Qwen | The model team of Alibaba Cloud; Qwen is one of the most widely used open-weight families. | Qwen3.8-Max (closed); Qwen3.8-2.4T-A95B and Qwen3.8-27B (open) | Chapter 24 |
| Moonshot AI | Beijing startup founded in 2023 by Yang Zhilin; maker of the Kimi assistant. | Kimi K3 (open weights, 2.8 trillion parameters) | Chapter 17 |
| Z.ai (formerly Zhipu AI) | Beijing lab that grew out of Tsinghua University research. | GLM-5.3 (open weights) | Chapter 24 |
| MiniMax | Shanghai company making language, speech and video models. | MiniMax models; Hailuo video app | Chapter 47 |
| Xiaomi | Chinese phone and electronics maker that also trains large models. | MiMo-V2.6-Pro, the top open-weight model on the Artificial Analysis index in October 2026 | Chapter 24 |
| StepFun | Shanghai model startup. | Step 5 | Chapter 24 |
| Mistral AI | Paris lab founded in 2023 by Arthur Mensch, Guillaume Lample and Timothée Lacroix; Europe's leading model maker. | Mistral Large 4 (preview), Medium 3.5, Large 3 (Apache-2.0); Le Chat assistant | Chapter 24 |
| Cohere | Toronto company founded in 2019, co-founded by Transformer co-author Aidan Gomez; builds models for business use. | Command model family | Chapter 61 |
| Thinking Machines Lab | Founded in 2025 by former OpenAI chief technology officer Mira Murati; publishes research on post-training. | Inkling model; Tinker fine-tuning service | Chapter 20 |
| Safe Superintelligence (SSI) | Founded in 2024 by Ilya Sutskever and colleagues to build safe superintelligence before shipping products. | No public product | Chapter 60 |
| Reflection AI | US startup founded by former Google DeepMind researchers. | Beam 1.0 | Chapter 24 |
| Ai2 (Allen Institute for AI) | Seattle nonprofit founded by Paul Allen; releases fully open models with their data and code. | OLMo models | Chapter 30 |
| Advanced Machine Intelligence Labs | Founded by Yann LeCun after he left Meta in November 2025, to pursue world models beyond LLMs. | Research stage | Chapter 47 |

*Table D.1: Frontier and near-frontier model labs, as of October 2026.*

## Chips and memory

| Company | Who they are and why they matter | More in |
|---|---|---|
| NVIDIA | Dominant maker of AI chips, founded in 1993 and led by Jensen Huang. Sells GPUs (H100, H200, B200, B300, Rubin) and whole racks (GB200/GB300 NVL72, Vera Rubin NVL72), plus the CUDA software platform; also publishes open Nemotron models. | Chapter 35 |
| AMD | The second GPU maker, led by Lisa Su. Instinct MI300X, MI355X and MI455X accelerators, the Helios rack and ROCm software; signed a multi-gigawatt GPU deal with OpenAI in 2025. | Chapter 35 |
| Google (TPU) | Has designed its own Tensor Processing Units since 2015; Ironwood (TPU v7) and the 2026 TPU 8t (training) and TPU 8i (inference). Anthropic is a major TPU customer. | Chapter 35 |
| Amazon Web Services (Annapurna Labs) | Amazon's chip unit, bought in 2015; designs Trainium (training) and Inferentia (inference) chips. Trainium3 (2025) is AWS's first 3-nanometer AI chip. | Chapter 35 |
| Microsoft (Maia) | Designs Maia accelerators for its own data centers; Maia 200 launched in January 2026. | Chapter 35 |
| Meta (MTIA) | Designs MTIA inference chips for its recommendation and AI systems; bought the RISC-V chip startup Rivos in 2025. | Chapter 35 |
| Broadcom | Co-designs custom AI chips for Google (TPUs), Meta and OpenAI, and makes Ethernet switch chips such as Tomahawk. | Chapter 35 |
| Marvell | Custom chip and networking partner for cloud companies, including AWS and Microsoft. | Chapter 35 |
| Intel | The classic PC and server CPU maker; Gaudi AI accelerators, the 18A process and Intel Foundry. The US government took a 9.9% stake in 2025, and NVIDIA invested $5 billion. | Chapter 36 |
| Arm | British company, majority-owned by SoftBank, whose CPU designs are licensed by others; NVIDIA's Grace and Vera, Google's Axion and Apple's chips use Arm designs. | Chapter 32 |
| Qualcomm | Snapdragon chips with neural processing units for phones and Copilot+ PCs; also entering data-center inference. | Chapter 53 |
| Apple | Designs its own phone and Mac chips with a Neural Engine (since the A11 in 2017) for on-device AI. | Chapter 53 |
| Cerebras | Builds a single chip the size of a whole silicon wafer (WSE-3: 4 trillion transistors, 900,000 cores), strong at very fast inference. | Chapter 35 |
| Groq | Designs LPU inference chips that keep model weights in on-chip memory; NVIDIA licensed its technology and hired its leaders in a reported deal in December 2025. | Chapter 35 |
| SambaNova | Reconfigurable "dataflow" AI chips (SN40L) with several memory tiers. | Chapter 35 |
| Etched | Startup building Sohu, a chip hard-wired for Transformer inference. | Chapter 35 |
| Tenstorrent | AI chips built on open RISC-V cores with open-source software, led by veteran chip architect Jim Keller. | Chapter 35 |
| d-Matrix | Inference chips that compute inside memory (Corsair). | Chapter 35 |
| Huawei | China's leading AI chip designer: Ascend processors and Atlas SuperPoD clusters built from many chips linked by optics. | Chapter 36 |
| Cambricon | Chinese AI chip designer, one of several domestic alternatives to NVIDIA. | Chapter 36 |
| SK hynix | South Korean memory maker; the leading supplier of high-bandwidth memory (HBM) and NVIDIA's primary HBM source. | Chapter 33 |
| Samsung Electronics | Korean giant making DRAM, HBM and flash memory, and contract chips through Samsung Foundry. | Chapter 33 |
| Micron | US memory maker; the third major HBM supplier. | Chapter 33 |
| Lightmatter, Ayar Labs, Celestial AI | Startups using light (photonics) to move data between chips faster and with less energy. | Chapter 35 |

*Table D.2: Chip and memory companies.*

## Foundries and equipment

| Company | Who they are and why they matter | More in |
|---|---|---|
| TSMC | Taiwan Semiconductor Manufacturing Company, founded in 1987 by Morris Chang. Manufactures nearly every leading AI accelerator and packages them with its CoWoS technology; also building fabs in Arizona. | Chapter 36 |
| Samsung Foundry | Samsung's contract chipmaking arm; first to ship gate-all-around transistors, at 3 nanometers in 2022. | Chapter 36 |
| Intel Foundry | Intel's manufacturing business, offering the 18A process (new transistors plus backside power) and EMIB and Foveros packaging. | Chapter 36 |
| SMIC | China's largest chip foundry; makes 7-nanometer-class chips without EUV machines. | Chapter 36 |
| ASML | Dutch company that is the only supplier of extreme-ultraviolet (EUV) lithography machines, which cost around $180 million each. | Chapter 36 |
| Carl Zeiss SMT | German optics maker that builds the ultra-precise mirrors inside ASML's EUV machines. | Chapter 36 |
| Applied Materials, Lam Research, Tokyo Electron, KLA | The big makers of machines that deposit, etch, clean and inspect the layers on a chip. | Chapter 36 |
| Synopsys, Cadence | Makers of electronic design automation (EDA) software that engineers use to design chips. | Chapter 36 |
| ASE, Amkor | The largest outsourced chip packaging and testing companies. | Chapter 36 |
| Foxconn, Quanta, Wistron | Taiwanese manufacturers that assemble AI servers and full racks for NVIDIA and cloud companies. | Chapter 34 |
| Dell, Supermicro, HPE | Server makers that sell GPU systems to companies, clouds and governments. | Chapter 34 |

*Table D.3: Foundries, equipment makers and server builders.*

## Clouds and neoclouds

| Company | Who they are and why they matter | More in |
|---|---|---|
| Amazon Web Services (AWS) | The largest cloud provider; offers Bedrock, Trainium chips and NVIDIA GPUs, and built Project Rainier in Indiana for Anthropic. | Chapter 42 |
| Microsoft Azure | Microsoft's cloud; OpenAI's long-time compute partner; builds "Fairwater" AI data centers in Wisconsin and Atlanta. | Chapter 42 |
| Google Cloud | Google's cloud, renting TPUs and NVIDIA GPUs and serving Gemini through Vertex AI. | Chapter 42 |
| Oracle Cloud Infrastructure (OCI) | Oracle's cloud; operates the Stargate campus in Abilene, Texas, for OpenAI. | Chapter 42 |
| Alibaba Cloud | China's largest cloud provider and home of the Qwen models. | Chapter 42 |
| CoreWeave | The largest "neocloud" (a cloud specializing in GPUs); went public in March 2025; Microsoft and Meta are major customers. | Chapter 43 |
| Nebius | Amsterdam-based neocloud spun out of Yandex in 2024, with large Microsoft and Meta contracts. | Chapter 43 |
| Lambda | GPU cloud popular with researchers and startups. | Chapter 43 |
| Crusoe | Builds and runs AI data centers; constructed the Stargate Abilene campus. | Chapter 42 |
| Together AI | Cloud for running and fine-tuning open-weight models. | Chapter 30 |
| Nscale | UK neocloud and partner in Stargate Norway. | Chapter 42 |
| Fluidstack | Builds and operates GPU and TPU data centers, including a large US build-out for Anthropic. | Chapter 42 |
| IREN, Cipher Mining, TeraWulf, Core Scientific | Former bitcoin miners converting their powered sites into AI data centers. | Chapter 42 |
| G42 | Abu Dhabi AI company and partner in Stargate UAE. | Chapter 42 |
| Humain | Saudi Arabia's national AI company, owned by the Public Investment Fund and founded in 2025. | Chapter 42 |
| OpenRouter | A marketplace that lets developers call hundreds of models from many providers through one API. | Chapter 26 |

*Table D.4: Cloud providers and GPU clouds.*

## Data-center builders and energy

| Organization | Who they are and why they matter | More in |
|---|---|---|
| Stargate LLC | OpenAI's data-center venture with SoftBank, Oracle and MGX, announced in January 2025 with a target of "up to $500 billion and 10 gigawatts." | Chapter 42 |
| SoftBank | Japanese investment group led by Masayoshi Son; Stargate partner, major OpenAI investor and majority owner of Arm. | Chapter 43 |
| MGX | Abu Dhabi technology investment fund and Stargate partner. | Chapter 43 |
| Vantage Data Centers, STACK Infrastructure, Related Digital | Developers building several Stargate campuses in Texas, Wisconsin, New Mexico and Michigan. | Chapter 42 |
| Equinix, Digital Realty | The largest operators of colocation data centers, where many companies rent space and connect networks. | Chapter 38 |
| Schneider Electric, Vertiv, Eaton | Makers of the power and cooling equipment inside data centers: switchgear, backup power and liquid cooling. | Chapter 39 |
| GE Vernova, Siemens Energy, Mitsubishi Power | The main gas-turbine makers, with multi-year order backlogs driven partly by data centers. | Chapter 41 |
| Constellation Energy | The largest US nuclear plant operator; restarting Three Mile Island Unit 1 (renamed the Crane Clean Energy Center) to power Microsoft. | Chapter 41 |
| Vistra, Talen Energy | Power companies selling nuclear output to Meta (Vistra) and Amazon (Talen, from the Susquehanna plant). | Chapter 41 |
| TerraPower | Advanced nuclear reactor company founded by Bill Gates; its Natrium reactors are part of Meta's 2026 nuclear deals. | Chapter 41 |
| Oklo, Kairos Power, X-energy | Small and advanced reactor developers with deals with Meta (Oklo), Google (Kairos) and Amazon (X-energy). | Chapter 41 |
| Fervo Energy | Enhanced geothermal developer working with Google. | Chapter 41 |
| Bloom Energy | Maker of fuel cells used for fast on-site power at data centers. | Chapter 41 |
| Entergy | Louisiana utility building gas power plants for Meta's Hyperion campus. | Chapter 41 |
| PJM Interconnection | The largest US grid operator (13 states plus Washington, D.C.), where data-center demand drove record capacity prices. | Chapter 41 |
| ERCOT | The operator of most of Texas's power grid, now handling large data-center connection requests under new state rules. | Chapter 41 |
| Blue Owl | Investment firm that financed Meta's Hyperion campus through a joint venture, an example of off-balance-sheet data-center financing. | Chapter 43 |

*Table D.5: Builders, equipment makers, energy companies and grid operators.*

## Tooling, data and infrastructure companies

| Company or project | Who they are and why they matter | More in |
|---|---|---|
| Scale AI | Data-labeling and evaluation company; Meta took a 49% stake in 2025 and founder Alexandr Wang joined Meta. | Chapter 11 |
| Surge AI | Provider of expert human data for training and evaluating models. | Chapter 11 |
| Mercor | Marketplace that hires domain experts (doctors, lawyers, coders) to create AI training data. | Chapter 11 |
| Hugging Face | The "GitHub of AI": hosts open models, datasets and demos, and maintains the Transformers library. | Chapter 30 |
| LangChain | Open-source framework for building LLM apps; LangGraph for agents and LangSmith for tracing and evals. | Chapter 28 |
| LlamaIndex | Framework for connecting models to your documents and data (retrieval). | Chapter 27 |
| Pinecone, Weaviate, Qdrant, Chroma | Vector databases that store embeddings for semantic search and RAG. | Chapter 27 |
| Databricks | Data and AI platform from the creators of Apache Spark; bought MosaicML in 2023. | Chapter 10 |
| Snowflake | Cloud data warehouse that has added AI features. | Chapter 11 |
| Weights & Biases | Experiment-tracking tools for model training; bought by CoreWeave in 2025. | Chapter 13 |
| Braintrust, Arize, Langfuse | Evaluation and observability tools for monitoring LLM apps in production. | Chapter 31 |
| vLLM, SGLang | Open-source engines for serving models fast; vLLM introduced PagedAttention. | Chapter 23 |
| Ollama, LM Studio, llama.cpp | Free tools for running open-weight models on your own computer. | Chapter 30 |
| Zapier, Make, n8n | No-code automation platforms that connect apps and now include AI agents. | Chapter 29 |
| Agentic AI Foundation | Linux Foundation body launched in December 2025 to steward open agent standards, including MCP and AGENTS.md. | Chapter 28 |

*Table D.6: Tooling, data and infrastructure companies and projects.*

## Application companies

| Company | Who they are and why they matter | More in |
|---|---|---|
| Cursor (Anysphere) | AI-first code editor; agreed in June 2026 to be acquired by SpaceX in an all-stock deal reported at about $60 billion. | Chapter 29 |
| Cognition | Maker of Devin, an autonomous coding agent; bought the Windsurf code editor in 2025. | Chapter 29 |
| GitHub (Microsoft) | Copilot (2021) was the first mass-market AI coding assistant; now includes cloud coding agents. | Chapter 29 |
| Replit | Browser-based coding platform with Replit Agent for building apps from descriptions. | Chapter 29 |
| Lovable | Stockholm-based app builder that turns plain-English descriptions into web apps. | Chapter 29 |
| Vercel (v0), StackBlitz (Bolt) | AI app and website builders for developers and non-developers. | Chapter 29 |
| Perplexity | AI "answer engine" that searches the web and cites sources. | Chapter 51 |
| Character.AI | Companion-chatbot app founded by former Google researchers; faced lawsuits and restricted open-ended chats for teens. | Chapter 58 |
| Harvey | AI assistant and agents for law firms and legal departments. | Chapter 53 |
| Sierra, Decagon | Customer-service AI agents; Sierra charges per resolved conversation (outcome-based pricing). | Chapter 53 |
| Midjourney | Independent lab making a leading image generator. | Chapter 47 |
| Black Forest Labs | German maker of the Flux image models, founded by creators of Stable Diffusion. | Chapter 47 |
| Stability AI | Company behind the 2022 public release of Stable Diffusion. | Chapter 47 |
| Runway | Video generation and editing tools for creators and studios. | Chapter 47 |
| Kuaishou (Kling), ByteDance (Seedance) | Chinese tech companies with leading video-generation models. | Chapter 47 |
| ElevenLabs | Voice synthesis, voice cloning and dubbing. | Chapter 46 |
| Suno, Udio | AI music generators sued by major record labels in 2024; several labels settled and moved to licensing in 2025–26. | Chapter 46 |
| Waymo | Alphabet's self-driving company, grown from Google's 2009 project; runs driverless robotaxis in several US cities. | Chapter 50 |
| Tesla | Electric-car maker with Full Self-Driving software, a Robotaxi service and the Optimus humanoid robot. | Chapter 50 |
| Zoox, Baidu Apollo Go, Pony.ai, WeRide | Robotaxi developers in the US (Zoox, owned by Amazon) and China. | Chapter 50 |
| Aurora | Self-driving trucks. | Chapter 50 |
| Figure AI | Humanoid robot maker; its robots work on parts handling at BMW using its Helix model. | Chapter 49 |
| Physical Intelligence | Builds general "robot brain" models, the π0 family. | Chapter 49 |
| Unitree, AgiBot | Chinese robot makers that led humanoid shipments in 2025. | Chapter 49 |
| Boston Dynamics, Agility Robotics, Apptronik, 1X | Makers of the Atlas, Digit, Apollo and NEO robots. | Chapter 49 |
| Isomorphic Labs | Google DeepMind spin-out (2021) using AI for drug discovery. | Chapter 52 |
| Insilico Medicine | Drug-discovery company whose AI-designed drug rentosertib reached a Phase IIa trial in 2025. | Chapter 52 |

*Table D.7: Companies that build products on top of AI models.*

## Safety, policy and evaluation organizations

| Organization | Who they are and why they matter | More in |
|---|---|---|
| METR | Berkeley nonprofit (Model Evaluation and Threat Research) that tests frontier models before release and measures AI "time horizons." | Chapter 57 |
| Apollo Research | London organization testing models for deception and "scheming." | Chapter 57 |
| Redwood Research | Nonprofit that pioneered "AI control": safety measures that work even if a model is misaligned. | Chapter 56 |
| Alignment Research Center (ARC) | Theory-focused alignment nonprofit founded by Paul Christiano in 2021. | Chapter 56 |
| ARC Prize Foundation | Runs the ARC-AGI benchmarks and prizes, co-founded by François Chollet and Mike Knoop. | Chapter 24 |
| Epoch AI | Research group tracking AI compute, costs, data centers and capabilities; runs FrontierMath and the Epoch Capabilities Index. | Chapter 24 |
| Artificial Analysis | Independent company benchmarking models on intelligence, price and speed. | Chapter 24 |
| LMArena | Crowdsourced blind comparisons of chatbots; began as Chatbot Arena at UC Berkeley. | Chapter 24 |
| Center for AI Safety (CAIS) | Nonprofit led by Dan Hendrycks; co-created Humanity's Last Exam and organized the 2023 statement on extinction risk. | Chapter 60 |
| MIRI (Machine Intelligence Research Institute) | One of the oldest AI-risk organizations, co-founded by Eliezer Yudkowsky; now focused on warning about catastrophic risk. | Chapter 60 |
| FAR.AI, Palisade Research | Research nonprofits studying robustness, misuse and behaviors such as shutdown resistance. | Chapter 55 |
| Transluce, Goodfire | Interpretability organizations (a nonprofit lab and a startup) building tools to look inside models. | Chapter 57 |
| Eleos AI | Research nonprofit studying whether AI systems could have morally relevant welfare. | Chapter 60 |
| UK AI Security Institute (AISI) | UK government body that tests frontier models; renamed from the AI Safety Institute in 2025. | Chapter 59 |
| US Center for AI Standards and Innovation (CAISI) | US government body at NIST that evaluates frontier models; replaced the US AI Safety Institute in 2025. | Chapter 59 |
| NIST | US standards agency; publishes the AI Risk Management Framework. | Chapter 59 |
| EU AI Office | European Commission office enforcing the EU AI Act's rules for general-purpose AI models. | Chapter 59 |
| Cyberspace Administration of China (CAC) | China's internet regulator, which runs the registry for algorithms and generative AI services. | Chapter 59 |
| International AI Safety Report | Global scientific review of AI risks, chaired by Yoshua Bengio, with reports from 2025. | Chapter 59 |
| GovAI, CSET, RAND, IAPS | Policy research institutes; RAND defined the SL1–SL5 security levels for protecting model weights. | Chapter 56 |
| Ada Lovelace Institute, AI Now Institute, Center for Democracy and Technology | Research and advocacy groups focused on AI's effects on people and rights. | Chapter 58 |
| DAIR, Algorithmic Justice League | Organizations founded by Timnit Gebru and Joy Buolamwini studying bias and harms. | Chapter 58 |
| Future of Life Institute | Nonprofit led by Max Tegmark; organized the 2023 open letter calling for a pause on giant AI experiments. | Chapter 60 |
| AI Futures Project | Group led by Daniel Kokotajlo that published the "AI 2027" scenario. | Chapter 60 |
| LawZero | Nonprofit founded by Yoshua Bengio in 2025 to build "safe-by-design" AI. | Chapter 60 |
| Frontier Model Forum | Industry body founded in 2023 by Anthropic, Google, Microsoft and OpenAI to share safety practices. | Chapter 56 |
| Partnership on AI | Multi-stakeholder nonprofit (2016) of companies, academics and civil society. | Chapter 59 |
| MLCommons | Engineering consortium behind the MLPerf hardware benchmarks and the AILuminate safety benchmark. | Chapter 35 |
| C2PA | Industry coalition behind Content Credentials, a standard for labeling where images and videos came from. | Chapter 58 |
| MATS, ARENA, BlueDot Impact | Training programs that bring newcomers into AI safety research. | Chapter 65 |

*Table D.8: Safety, policy and evaluation organizations.*

## People

### Pioneers

| Person | Why they matter | More in |
|---|---|---|
| Ada Lovelace (1815–1852) | Wrote notes on Charles Babbage's Analytical Engine in 1843, including what is often called the first published computer program, and asked whether machines could create. | Chapter 7 |
| Alan Turing (1912–1954) | Defined what computers can compute (1936) and proposed the "imitation game," now called the Turing test, in 1950. | Chapter 7 |
| Claude Shannon | Founded information theory (1948), the math of bits; co-organized the 1956 Dartmouth workshop. | Chapter 2 |
| John McCarthy | Coined the term "artificial intelligence" in the 1955 Dartmouth proposal and created the Lisp language. | Chapter 7 |
| Marvin Minsky | Dartmouth co-organizer and MIT AI pioneer; co-wrote *Perceptrons* (1969), which cooled interest in neural networks. | Chapter 7 |
| Herbert Simon and Allen Newell | Built the Logic Theorist (1956), an early reasoning program, and championed symbolic AI. | Chapter 54 |
| Frank Rosenblatt | Invented the perceptron (1958), the first learning artificial neuron. | Chapter 12 |
| Arthur Samuel | Coined "machine learning" in 1959 with a checkers program that improved by playing itself. | Chapter 8 |
| Joseph Weizenbaum | Created ELIZA (1966), the first famous chatbot, and later warned about over-trusting machines. | Chapter 7 |
| Judea Pearl | Developed Bayesian networks and a mathematics of cause and effect; Turing Award 2011. | Chapter 54 |
| Geoffrey Hinton | Helped popularize backpropagation (1986) and, with students, built AlexNet (2012); Turing Award 2018 and Nobel Prize in Physics 2024; left Google in 2023 to speak about AI risks. | Chapter 12 |
| Yann LeCun | Pioneered convolutional neural networks (LeNet); Turing Award 2018; long-time Meta chief AI scientist who left in 2025 to start a world-model company. | Chapter 14 |
| Yoshua Bengio | Deep learning pioneer and Turing Award 2018 winner; now chairs the International AI Safety Report and founded LawZero. | Chapter 14 |
| Sepp Hochreiter and Jürgen Schmidhuber | Invented the LSTM (1997), the memory-cell network that dominated sequence modeling before Transformers. | Chapter 14 |
| Richard Sutton and Andrew Barto | Founders of modern reinforcement learning; won the Turing Award for 2024. Sutton wrote "The Bitter Lesson" (2019). | Chapter 48 |
| Fei-Fei Li | Created ImageNet (2009), the dataset behind the deep learning boom; co-directs Stanford HAI and founded World Labs. | Chapter 11 |
| Andrew Ng | Co-founded Google Brain and Coursera; founded DeepLearning.AI, whose courses taught millions. | Chapter 65 |
| Alex Krizhevsky and Ilya Sutskever | With Hinton, built AlexNet, whose 2012 ImageNet win launched the deep learning era. | Chapter 14 |
| Ashish Vaswani, Noam Shazeer and co-authors | The eight Google authors of "Attention Is All You Need" (2017), which introduced the Transformer. | Chapter 15 |
| Demis Hassabis and John Jumper | Led AlphaFold, which predicts protein structures; shared the 2024 Nobel Prize in Chemistry with David Baker. | Chapter 52 |
| David Silver | Led the AlphaGo and AlphaZero projects at DeepMind. | Chapter 48 |

*Table D.9: Pioneers of computing and AI.*

### Lab and company leaders

Roles are as of October 2026; leadership changes are frequent.

| Person | Role and why they matter | More in |
|---|---|---|
| Sam Altman | Co-founder and CEO of OpenAI. | Chapter 61 |
| Greg Brockman | OpenAI co-founder and president. | Chapter 61 |
| Jakub Pachocki | OpenAI's chief scientist. | Chapter 24 |
| Dario Amodei | Co-founder and CEO of Anthropic; formerly led research at OpenAI. | Chapter 61 |
| Daniela Amodei | Co-founder and president of Anthropic. | Chapter 61 |
| Jared Kaplan | Anthropic co-founder and chief science officer; lead author of the 2020 scaling-laws paper. | Chapter 19 |
| Demis Hassabis | Co-founder of DeepMind and CEO of Google DeepMind. | Chapter 24 |
| Sundar Pichai | CEO of Google and its parent company Alphabet. | Chapter 61 |
| Mark Zuckerberg | Founder and CEO of Meta. | Chapter 61 |
| Alexandr Wang | Founder of Scale AI; leads TBD Lab, the language-model group inside Meta Superintelligence Labs. | Chapter 24 |
| Elon Musk | Founded xAI in 2023 and runs SpaceX and Tesla; an OpenAI co-founder who left its board in 2018. | Chapter 24 |
| Satya Nadella | CEO of Microsoft. | Chapter 61 |
| Mustafa Suleyman | DeepMind co-founder who has led Microsoft AI since 2024. | Chapter 61 |
| Jensen Huang | Co-founder and CEO of NVIDIA since 1993. | Chapter 35 |
| Lisa Su | CEO of AMD since 2014. | Chapter 35 |
| Morris Chang and C.C. Wei | TSMC's founder (1987) and its current chairman and CEO. | Chapter 36 |
| Masayoshi Son | Founder and CEO of SoftBank; key backer of OpenAI and Stargate. | Chapter 43 |
| Liang Wenfeng | Founder of DeepSeek and co-founder of the hedge fund High-Flyer. | Chapter 24 |
| Yang Zhilin | Founder of Moonshot AI. | Chapter 24 |
| Arthur Mensch | Co-founder and CEO of Mistral AI. | Chapter 24 |
| Mira Murati | Former OpenAI chief technology officer; founded Thinking Machines Lab in 2025. | Chapter 24 |
| Ilya Sutskever | OpenAI co-founder and former chief scientist; co-founded Safe Superintelligence in 2024. | Chapter 60 |
| Aidan Gomez | Transformer co-author; co-founder and CEO of Cohere. | Chapter 61 |
| Clem Delangue | Co-founder and CEO of Hugging Face. | Chapter 30 |

*Table D.10: Lab and company leaders, as of October 2026.*

### Researchers

| Person | Why they matter | More in |
|---|---|---|
| Andrej Karpathy | OpenAI founding member and former head of AI at Tesla; teaches "Neural Networks: Zero to Hero," built nanochat and coined "vibe coding" (2025). | Chapter 29 |
| Alec Radford | Lead author of the original GPT papers and of CLIP and Whisper. | Chapter 18 |
| Noam Shazeer | Transformer co-author and mixture-of-experts pioneer; co-founded Character.AI and returned to Google in 2024. | Chapter 17 |
| Jason Wei | First author of the 2022 chain-of-thought prompting paper. | Chapter 21 |
| Chris Olah | Interpretability pioneer and Anthropic co-founder. | Chapter 57 |
| Jan Leike | Alignment researcher who co-led OpenAI's superalignment team before joining Anthropic. | Chapter 56 |
| Paul Christiano | Co-author of foundational RLHF research (2017); founded the Alignment Research Center and later led safety at the US AI Safety Institute. | Chapter 20 |
| Neel Nanda | Leads mechanistic interpretability work at Google DeepMind. | Chapter 57 |
| Evan Hubinger | Anthropic researcher behind the "sleeper agents" and alignment-faking studies. | Chapter 55 |
| Buck Shlegeris and Ryan Greenblatt | Redwood Research leaders who developed AI control. | Chapter 56 |
| Beth Barnes | Founder of METR. | Chapter 57 |
| Marius Hobbhahn | CEO of Apollo Research. | Chapter 57 |
| Dan Hendrycks | Director of CAIS; created MMLU and co-created Humanity's Last Exam. | Chapter 24 |
| François Chollet | Creator of the Keras library and the ARC benchmark; co-founder of ARC Prize. | Chapter 24 |
| Amanda Askell | Anthropic researcher who shapes Claude's character and constitution. | Chapter 56 |
| Percy Liang and Tatsunori Hashimoto | Stanford researchers who teach CS336, "Language Modeling from Scratch"; Liang led the HELM evaluation project. | Chapter 65 |
| Anca Dragan and Rohin Shah | Lead safety and alignment research at Google DeepMind. | Chapter 56 |
| Kyle Fish | Anthropic's model-welfare researcher. | Chapter 60 |

*Table D.11: Researchers whose work shapes today's models.*

### Safety, ethics and policy voices

| Person | Why they matter | More in |
|---|---|---|
| Stuart Russell | UC Berkeley professor, co-author of the standard AI textbook *Artificial Intelligence: A Modern Approach* and of *Human Compatible* (2019). | Chapter 55 |
| Eliezer Yudkowsky and Nate Soares | MIRI's leading voices on existential risk; co-wrote *If Anyone Builds It, Everyone Dies* (2025). | Chapter 60 |
| Daniel Kokotajlo | Former OpenAI researcher who leads the AI Futures Project and its "AI 2027" scenario. | Chapter 60 |
| Max Tegmark | MIT physicist and president of the Future of Life Institute. | Chapter 60 |
| Helen Toner | Policy researcher at Georgetown's CSET; former OpenAI board member. | Chapter 59 |
| Timnit Gebru | Founder of DAIR; co-author of the Gender Shades and "Stochastic Parrots" papers. | Chapter 58 |
| Joy Buolamwini | Led the Gender Shades study (2018) showing face-analysis systems erred far more on darker-skinned women; founded the Algorithmic Justice League. | Chapter 58 |
| Emily M. Bender | Linguist and co-author of "On the Dangers of Stochastic Parrots" (2021). | Chapter 58 |
| Margaret Mitchell | Lead author of the 2019 "Model Cards" paper; AI ethics researcher at Hugging Face. | Chapter 24 |
| Arvind Narayanan and Sayash Kapoor | Princeton authors of *AI Snake Oil* and the essay "AI as Normal Technology." | Chapter 60 |
| Kate Crawford | Scholar of AI's social and environmental costs; author of *Atlas of AI*. | Chapter 58 |
| Meredith Whittaker | President of the Signal Foundation and co-founder of the AI Now Institute. | Chapter 58 |
| Rumman Chowdhury | Pioneer of algorithmic auditing and public red-teaming events. | Chapter 58 |
| Alondra Nelson | Led the White House's 2022 Blueprint for an AI Bill of Rights. | Chapter 59 |
| Marc Andreessen | Venture capitalist (a16z) and prominent opponent of most AI regulation. | Chapter 59 |
| David Sacks | White House AI and crypto adviser from 2025. | Chapter 59 |
| Michael Kratsios | Director of the White House Office of Science and Technology Policy. | Chapter 59 |
| Scott Wiener | California state senator behind SB 1047 (vetoed in 2024) and SB 53 (signed in 2025). | Chapter 59 |
| Alex Bores | New York assemblymember who sponsored the RAISE Act. | Chapter 59 |
| Robert Long | Co-founder of Eleos AI, which studies AI welfare. | Chapter 60 |

*Table D.12: Voices in safety, ethics and policy debates.*
