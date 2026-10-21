# Freshness check: Part VIII (Chapters 45–54), web-verified

Checked October 21, 2026 against the live web. Scope: every "At the frontier (2026)" box in Chapters 45–54, every 2024–2026 claim about a named system, company, fleet, deployment or benchmark, and the main historical numbers.

How to read the Source column:

- A URL means the page was fetched (or, where marked "via search", its content was confirmed in a web-search result) during this round.
- "n.r." (not re-fetched) means the claim matches the long-established public record and the canonical source is named, but it was not fetched again this round. The shared web-search budget (200 searches across all agents) ran out partway through, so the remaining checks went straight to known primary URLs. 2026 claims and frontier boxes came first.
- Secondary sources (Wikipedia, trade press) were used only where no primary page could be reached. The book says "reported" wherever it now relies on one.

| Claim | Chapter and section | Verdict | Source URL | Change made |
|---|---|---|---|---|
| SAM (April 2023), SA-1B dataset of about 1.1 billion masks on 11 million images | 45, Segment Anything | CONFIRMED | n.r.: https://arxiv.org/abs/2304.02643 | None |
| SAM 2 adds video (July 2024) | 45, Segment Anything | CONFIRMED | n.r.: https://ai.meta.com/blog/segment-anything-2/ | None |
| SAM 3 concept prompts and SAM 3D released together (November 19, 2025) | 45, Segment Anything; 47, 3D | CONFIRMED | https://ai.meta.com/blog/segment-anything-model-3/ (concept prompts, SAM 3D in the same announcement; the exact day comes from the public record) | None |
| SAM 3.1 (March 27, 2026): follows up to 16 objects per pass, 16 to 32 frames per second on one H100 | 45, Segment Anything | ADDED | https://ai.meta.com/blog/segment-anything-model-3/ | New bullet in the SAM family list |
| AlexNet top-5 error 15.3% vs 26.2%; ResNet about 3.6%; Karpathy about 5% | 45, Image classification | CONFIRMED | n.r.: ILSVRC 2012/2015 results; Karpathy 2014 blog | None |
| CLIP about 76% zero-shot on ImageNet (2021) | 45, Image classification | CONFIRMED | n.r.: https://arxiv.org/abs/2103.00020 | None |
| YOLO at about 45 frames per second (2015–16); DETR 2020; COCO 80 classes | 45, Object detection | CONFIRMED | n.r.: https://arxiv.org/abs/1506.02640 | None |
| Hawk-Eye in tennis since 2006; Wimbledon electronic line calling in 2025 | 45, Tracking | CONFIRMED | n.r.: Wimbledon/AELTC announcement, October 2024 | None |
| Kinect 2010, OpenPose 2017, 17 COCO keypoints, about 21 hand keypoints | 45, Pose estimation | CONFIRMED | n.r. | None |
| LeNet read over a tenth of US checks; Tesseract (HP 1980s, open-sourced 2005) | 45, OCR | CONFIRMED | n.r. | None |
| Viola–Jones 2001; DeepFace 2014; FaceNet 2015 (128 numbers) | 45, Faces | CONFIRMED | n.r. | None |
| Face ID false match about 1 in 1,000,000 | 45, Faces | CONFIRMED | n.r.: https://support.apple.com/en-us/102381 | None |
| Gender Shades: 34.7% vs 0.8% error | 45, Accuracy gaps | CONFIRMED | n.r.: http://gendershades.org | None |
| NIST 2019 test of 189 algorithms, 10–100× false-match gaps | 45, Accuracy gaps | CONFIRMED | n.r.: https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8280.pdf | None |
| Robert Williams arrest (January 2020) and 2024 Detroit settlement | 45, Accuracy gaps | CONFIRMED | n.r.: ACLU, June 2024 | None |
| EU AI Act face-scraping and emotion-recognition bans from February 2, 2025 | 45, Surveillance and the law | CONFIRMED | n.r.: https://artificialintelligenceact.eu/implementation-timeline/ | None |
| BIPA (2008); Facebook $650 million settlement (2021); San Francisco ban (2019) | 45, Surveillance and the law | CONFIRMED | n.r. | None |
| NeRF 2020; Gaussian splatting 2023; Depth Anything 2024 | 45, 3D | CONFIRMED | n.r. | None |
| Panda to gibbon at 99.3% (2014); stop-sign stickers (2018); wolf/husky (2016); pneumonia hospital shortcut (2018) | 45, How vision fails | CONFIRMED | n.r. | None |
| IDx-DR (April 2018), first FDA-authorized autonomous AI diagnostic | 45, Industry tour; 52, Medicine | CONFIRMED | n.r.: FDA press release, April 11, 2018 | None |
| Be My Eyes "Be My AI" on GPT-4 (2023); Amazon Just Walk Out (2018, scaled back 2024) | 45, Industry tour | CONFIRMED | n.r. | None |
| FDA list of AI-enabled devices: about 1,451 to end-2025; 1,614 by June 29, 2026 (secondary); about three-quarters radiology | 45, Industry tour; 52, Medicine | UNVERIFIABLE | https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices (returned 401) | None; the text already labels the 1,614 count as a secondary analysis |
| At the frontier: liveness detection against deepfake selfies | 45, Faces | CONFIRMED | General statement, no specific figures | None |
| At the frontier: vision converging on promptable general models (SAM 3, SAM 3D, VLA backbones, NPUs) | 45, At the frontier | CONFIRMED | https://ai.meta.com/blog/segment-anything-model-3/ ; https://deepmind.google/models/gemini-robotics/ | None |
| Whisper (September 2022): 680,000 hours; 117,000 hours in 96 other languages; 125,000 hours of translation | 46, Whisper | CONFIRMED | n.r.: https://arxiv.org/abs/2212.04356 | None |
| Microsoft 5.9% WER on Switchboard (2016) | 46, Deep learning turn | CONFIRMED | n.r. | None |
| Koenecke et al. PNAS 2020: WER 0.35 vs 0.19 | 46, Fairness | CONFIRMED | n.r.: https://www.pnas.org/doi/10.1073/pnas.1915768117 | None |
| "Careless Whisper" (2024): about 1% of transcripts with hallucinated phrases | 46, When transcripts invent words | CONFIRMED | n.r.: https://arxiv.org/abs/2402.08021 | None |
| Gemini 3.5 Transcribe (August 26, 2026): 85+ languages; 4.0% streaming and 2.6% pre-recorded WER (Artificial Analysis, per Google) | 46, Measuring WER | ADDED | https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/ | New paragraph with a worked figure (about 230 errors in a one-hour meeting) |
| WaveNet (September 2016); parallel WaveNet about 1,000× faster (2017); Tacotron 2 | 46, Text-to-speech | CONFIRMED | n.r.: https://deepmind.google/research/breakthroughs/wavenet/ | None |
| VALL-E (January 2023), 3-second voice prompt | 46, Text-to-speech | CONFIRMED | n.r.: https://arxiv.org/abs/2301.02111 | None |
| Apple Personal Voice (2023), about 15 minutes of recordings | 46, Voice cloning | CONFIRMED | n.r. | None |
| $243,000 voice fraud (2019); Arup about $25 million deepfake (2024) | 46, Harms | CONFIRMED | n.r. (press-reported; the text says "reportedly") | None |
| Biden robocall (January 2024); FCC ruling (February 2024); ELVIS Act (March 2024) | 46, Harms | CONFIRMED | n.r. | None |
| Voicebox withheld (2023); Voice Engine 15-second sample (March 2024) | 46, Harms | CONFIRMED | n.r. | None |
| McDonald's ended AI drive-thru test at 100+ restaurants (June 2024) | 46, Voice agents | CONFIRMED | n.r. | None |
| Intermountain Health: 27% less time on notes per appointment | 46, Voice agents; 52, Scribes | UNVERIFIABLE | https://www.abridge.com/press (no such figure) | None; already attributed to Intermountain |
| At the frontier: Gemini 3.8 Live released September 15, 2026; Kyutai Moshi (2024) as early full-duplex | 46, Voice agents | CONFIRMED | https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/ ; https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live ; https://www.kyutai.org/ (Moshi release post dated 2024-09-18) | None |
| At the frontier: native omni models, live translation, licensed music models, on-device recognition | 46, At the frontier | CONFIRMED | As above; the Suno v6 licensed models (see below) | None |
| Jukebox (2020, about 9 hours per minute); MusicLM (January 2023); MusicGen (June 2023); Suno and Udio full songs (2024) | 46, Music | CONFIRMED | n.r. | None |
| "Now and Then" (November 2023) won a Grammy in 2025 | 46, Tools musicians use | CONFIRMED | n.r. | None |
| Veo 3 (May 2025) generates synchronized sound | 46, Music; 47, Video | CONFIRMED | https://deepmind.google/models/veo/ | None |
| Labels sued Suno and Udio (June 2024) | 46, The law | CONFIRMED | https://en.wikipedia.org/wiki/Suno_AI ; https://en.wikipedia.org/wiki/Udio (citing The Verge and Billboard, June 24, 2024) | None |
| Universal settled with Udio (October 2025) and planned a licensed platform | 46, The law | CONFIRMED | https://en.wikipedia.org/wiki/Udio (citing LA Times, October 30, 2025) | None |
| Warner settled with Suno (November 2025); Suno to launch licensed models in 2026 | 46, The law | CONFIRMED | https://en.wikipedia.org/wiki/Suno_AI | None |
| Warner–Udio (November 2025), Udio–Merlin (January 2026), Udio–Kobalt (April 2026) | 46, The law | UNVERIFIABLE | Not in any page reached | None |
| "As of mid-2026, Sony was still litigating" | 46, The law; Answers Q7 | CORRECTED | https://en.wikipedia.org/wiki/Suno_AI (secondary: Music Business Worldwide, court filings) | Updated: Suno launched licensed v6 models (September 2026, built with Warner, BMG and others); Universal and Sony still suing Suno and filed a second suit over about 60,000 recordings in September 2026 (reported). Q7 now says "late 2026" and the answer is updated |
| Music timeline: "Licensed music models promised" (2026) | 46, Figure 46.12 | CORRECTED | https://en.wikipedia.org/wiki/Suno_AI | Now "Suno launches licensed v6 models in September" |
| US Copyright Office report on human authorship (January 2025) | 46, The law | CONFIRMED | n.r.: https://www.copyright.gov/ai/ | None |
| AudioSet (2017): about 2 million clips, 527 classes; iPhone Sound Recognition (2020) | 46, Audio understanding | CONFIRMED | n.r. | None |
| Chicago ended ShotSpotter (2024) | 46, Audio understanding | CONFIRMED | n.r. | None |
| Merlin Sound ID (2021); Project CETI (2024) | 46, Bioacoustics | CONFIRMED | n.r. | None |
| WHO: 1.5 billion with hearing loss, 430 million disabling | 46, Accessibility | CONFIRMED | n.r.: https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss | None |
| Phonak DNN-chip hearing aid (2024); OTC hearing-aid rule (2022); AirPods Pro 2 hearing aid (September 2024) | 46, Accessibility | CONFIRMED | n.r. | None |
| Image timeline 2021–2025 (DALL·E, Midjourney, Stable Diffusion, Firefly, SD3, FLUX.1, GPT-4o images March 2025, Nano Banana August 2025, FLUX.2 and Nano Banana Pro November 2025) | 47, Image history | CONFIRMED | https://bfl.ai/blog/flux-2 (November 25, 2025); https://en.wikipedia.org/wiki/GPT_Image (GPT-4o images March 25, 2025); others n.r. | None |
| gpt-image-2 (April 2026) | 47, Image history; Table 47.1 | CONFIRMED | https://en.wikipedia.org/wiki/GPT_Image (secondary; the text already says "according to press coverage") | None |
| GPT Image 2.5 (September 8, 2026) | 47, Image history; Table 47.1; Figure 47.1 | ADDED | https://en.wikipedia.org/wiki/GPT_Image (secondary) | Added to the history paragraph (marked "reported"), the table row and the timeline |
| FLUX.2 has an open-weight [dev] tier and closed [pro]/[flex] tiers | 47, Table 47.1 | CONFIRMED | https://bfl.ai/blog/flux-2 | None |
| At the frontier: Gemini Omni (announced May 2026) turns any input into generated or edited video by conversation; FLUX.2 open tier; Wan | 47, Image landscape | CONFIRMED | https://deepmind.google/models/gemini-omni/ ; https://en.wikipedia.org/wiki/Google_Gemini (announced May 19, 2026 at Google I/O) | None |
| Sora preview (February 2024); subscribers (December 2024); Kling (June 2024); Veo (May 2024), Veo 2 (December 2024) | 47, Video history | CONFIRMED | https://en.wikipedia.org/wiki/Kling_AI (June 10, 2024); others n.r. | None |
| Veo 3.1 (October 2025) still DeepMind's leading video model in 2026; up to 4K | 47, Video history; Table 47.2 | CONFIRMED | https://deepmind.google/models/veo/ (lists Veo 3.1 as newest; 1080p or 4K) | None |
| Sora 2 (September 30, 2025); shutdown announced March 2026; app closed April 26, 2026; API "scheduled to end" September 24, 2026 | 47, Sora 2 and the app that closed | CORRECTED | https://en.wikipedia.org/wiki/Sora_(text-to-video_model) (citing the OpenAI Help Center) | API end changed to past tense ("ended on September 24, 2026") |
| "OpenAI described Sora as continuing as a world-model research effort" (three places) | 47, Sora 2; two At the frontier boxes | HEDGED | No primary source reachable (help.openai.com returned 403) | Now "was reported to continue", "reportedly how OpenAI framed", "OpenAI reportedly describes" |
| Kling 3.0 is the current Kling | 47, Table 47.2 | CORRECTED | https://en.wikipedia.org/wiki/Kling_AI (secondary) | Row now "Kling 3.0 and 4.0"; Kling 4.0 launched globally October 2026 with 30-second clips and 4K (reported) |
| Seedance 2.0 is the current Seedance | 47, Table 47.2 | CORRECTED | https://en.wikipedia.org/wiki/Seedance (secondary) | Row now "Seedance 2.0 and 2.5"; 2.5 (July 2026) makes clips with sound of up to 30 seconds (reported) |
| Runway Gen-4.5 | 47, Table 47.2 | CONFIRMED | https://en.wikipedia.org/wiki/Runway_(company) (infobox) | None |
| Gemini Omni 1.1 Flash (August 27, 2026): scenes extended to 40 seconds, output up to 4K | 47, Table 47.2 | ADDED | https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/ | Added to the Gemini Omni row |
| At the frontier: sound expected; editing by conversation (Gemini Omni); labs frame video as a step to world models | 47, Video landscape | HEDGED | https://deepmind.google/models/veo/ ; https://deepmind.google/models/gemini-omni/ | Sora clause hedged (see above) |
| DreamFusion (2022); Hunyuan3D; SAM 3D (November 2025) | 47, 3D | CONFIRMED | n.r. | None |
| VASA-1 (April 2024) withheld | 47, Avatars | CONFIRMED | n.r. | None |
| GameNGen (2024, about 20 fps); Genie (2024); Genie 2 (December 2024) | 47, World models | CONFIRMED | n.r. | None |
| Genie 3 (August 2025): 720p, about 24 frames per second, consistent for minutes, promptable world events | 47, World models; 49, World models | CONFIRMED | https://deepmind.google/models/genie/ ("20-24 frames per second", 720p, "a few minutes") | None |
| Project Genie (January 29, 2026), US Google AI Ultra, about 60-second sessions | 47, World models; 49, World models | UNVERIFIABLE | https://deepmind.google/models/genie/ (describes it as a research prototype, gives no date or terms) | None |
| NVIDIA Cosmos (January 2025), open license, "about 20 million hours of video" | 47, World models | CONFIRMED | https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-world-foundation-model-platform-to-accelerate-physical-ai-development (January 6, 2025; open model license; the press release ties "20 million hours" to its data-curation pipeline) | None; the text already says "NVIDIA ... says" |
| World Labs Marble; LeCun left Meta (November 2025) for AMI Labs; V-JEPA 2 (2025) | 47, World models | CONFIRMED | n.r. | None |
| At the frontier: DeepMind "folded Genie into Gemini Omni" | 47, World models | CORRECTED | https://deepmind.google/models/gemini-omni/ ; https://deepmind.google/models/genie/ (separate models) | Now "offers Gemini Omni alongside them" |
| C2PA founded 2021 | 47, Provenance | CONFIRMED | n.r. | None |
| China's labeling rules from September 1, 2025 | 47, Labels and law | CONFIRMED | n.r. | None |
| EU AI Act Article 50 marking applies from August 2026, with a grace period to December 2026 for systems already on the market | 47, Labels and law | CONFIRMED | https://artificialintelligenceact.eu/implementation-timeline/ (compliance with Article 50(2) by December 2, 2026); https://artificialintelligenceact.eu/article/50/ | None |
| TAKE IT DOWN Act (May 2025), 48-hour removal | 47, Labels and law | CONFIRMED | n.r. | None |
| Grok sexualized-image scandal (late 2025 to early 2026) | 47, Everyday harms | CONFIRMED | n.r. | None |
| Getty v Stability: UK High Court (November 2025) | 47, Training | CONFIRMED | n.r. | None |
| Getty's US claims survived dismissal (April 2026) | 47, Training | UNVERIFIABLE | Not reached | None |
| Disney and Universal sued Midjourney (June 2025) | 47, Training | CONFIRMED | n.r. | None |
| At the frontier: licensed, controllable, labeled generation | 47, Creative work | CONFIRMED | Article 50 timeline above | None |
| Dijkstra (1959), A* (1968), STRIPS (1971), PDDL (1998), Remote Agent (1999) | 48, Search and planning | CONFIRMED | n.r. | None |
| Deep Blue (May 1997, 3.5–2.5, about 200 million positions per second); Stockfish neural evaluation (2020) | 48, Game trees | CONFIRMED | n.r. | None |
| Checkers solved (2007), about 5 × 10^20 positions | 48, Games table | CONFIRMED | n.r. | None |
| DQN (2013; Nature 2015, 49 games) | 48, Deep RL | CONFIRMED | n.r. | None |
| AlphaGo: Fan Hui 5–0 (October 2015), Lee Sedol 4–1 (March 2016), Move 37 at 1 in 10,000 | 48, AlphaGo | CONFIRMED | n.r. | None |
| AlphaGo Zero 100–0 after 3 days; AlphaZero (2017/2018); MuZero (2020) | 48, AlphaGo Zero to MuZero | CONFIRMED | n.r. | None |
| OpenAI Five (45,000 years of play, beat OG in April 2019); AlphaStar above 99.8% (October 2019) | 48, Real-time games | CONFIRMED | n.r. | None |
| Libratus (January 2017, 120,000 hands); Pluribus (2019, about 8 days on 64 cores, under $150) | 48, Poker | CONFIRMED | n.r. | None |
| Sutton and Barto, 2024 Turing Award (announced March 2025) | 48, TD learning | CONFIRMED | n.r.: https://awards.acm.org/about/2024-turing | None |
| Data-center cooling up to 40% (2016); AlphaChip (2021); tokamak control (2022); Swift drone (2023) | 48, RL outside games | CONFIRMED | n.r. | None |
| DeepSeek R1-Zero (January 2025); AlphaProof 28/42 (2024); AlphaTensor (2022); AlphaDev (2023); AlphaEvolve (May 2025) | 48, Games to reasoning | CONFIRMED | n.r. | None |
| At the frontier: RL scaled on LLMs in many environments | 48, Games to reasoning | CONFIRMED | General statement | None |
| DeepMind–EVE Online research partnership (August 21, 2026): offline game as a testbed for memory, long-horizon planning and many agents | 48, At the frontier | ADDED | https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games/ | One sentence appended to the At the frontier box |
| At the frontier: Gemini Robotics 2 (July 30, 2026), whole-body control; Figure's Helix 02 runs Figure 03 at BMW | 49, Learning to walk | CONFIRMED | https://deepmind.google/models/gemini-robotics/ ; https://www.therobotreport.com/google-deepmind-says-gemini-robotics-2-enables-full-body-control/ ; https://www.therobotreport.com/bmw-group-deploys-figure-03-humanoid-after-tests-previous-version/ (via search) | None |
| Gemini Robotics 2: light bulb and knot tying; partners Apptronik, Agile Robots and Boston Dynamics; 100+ trusted testers | 49, Hands; lineage | CONFIRMED | https://deepmind.google/models/gemini-robotics/ | None |
| NVIDIA Isaac GR00T reference humanoid (June 2026): Unitree H2 Plus, Sharpa hands, Jetson Thor; Ai2, ETH Zurich, Stanford and UC San Diego | 49, Hands; lineage | CONFIRMED | https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-NVIDIA-Isaac-GR00T-Reference-Humanoid-Robot-for-Academic-Research (June 1, 2026, via search) | None |
| Rudin et al. 2021; Dactyl (2019); ANYmal (2019–20) | 49, Learning to walk | CONFIRMED | n.r. | None |
| RT-1 (2022: about 130,000 demonstrations, 13 robots, 17 months); Open X-Embodiment (1M+ episodes, 22 robot types); ALOHA (about $20,000); UMI (2024) | 49, Data gap | CONFIRMED | n.r.: https://arxiv.org/abs/2212.06817 ; https://arxiv.org/abs/2310.08864 | None |
| OpenAI wound down robotics (2021) | 49, Data gap | CONFIRMED | n.r. | None |
| Physical Intelligence timeline: π0 (October 31, 2024), open-sourced (February 4, 2025), π0.5 (April 22, 2025), real-time chunking (June 9, 2025), π*0.6 (November 17, 2025), human-to-robot (December 16, 2025), MEM (March 3, 2026), RL Token (March 19, 2026), π0.7 (April 16, 2026) | 49, Data sources; lineage | CONFIRMED | https://www.pi.website/blog | None |
| At the frontier: labs combine six data sources (PI timeline items) | 49, Data sources | CONFIRMED | https://www.pi.website/blog | None |
| RT-2 (2023, 256 action bins); Gemini Robotics (March 2025); Gemini Robotics 1.5 (September 25, 2025); GR00T N1 (March 2025); Figure Helix (2025) | 49, Robot foundation models | CONFIRMED | n.r. | None |
| At the frontier: PI's Pi API beta (October 13, 2026, "Frontier Models for Every Robot"); Gemini Robotics-ER 2 in preview | 49, Robot foundation models | CONFIRMED | https://www.pi.website/blog ; https://www.therobotreport.com/google-deepmind-says-gemini-robotics-2-enables-full-body-control/ | None |
| Gemini 4 Argon for Robotics (October 13, 2026) | 49, At the frontier box | ADDED | https://developers.googleblog.com/gemini-4-argon-for-robotics | One clause added to the box |
| Omdia: 13,318 humanoids shipped in 2025; AgiBot 5,168; Unitree 4,200 (Unitree says 5,500+) | 49, Units shipped | CONFIRMED | https://technode.com/2026/01/09/chinas-agibot-leads-global-humanoid-robot-shipments-in-2025-omdia-says/ ; https://en.jiemian.com/article/13924474.html (via search) | None |
| Counterpoint: about 16,000 installations, China over 80% | 49, Units shipped | UNVERIFIABLE | Not reached | None |
| Figure 02 at BMW: 11 months, 10-hour shifts, 90,000+ parts, 1,250+ hours | 49, Table 49.3 | CONFIRMED | https://www.humanoidsdaily.com/news/figure-retires-the-f-02-battle-scarred-robots-30-000-bmws-and-hard-lessons-learned (company figures, via search) | None; already labeled company claims |
| Figure 03 began parts sequencing at BMW in 2026, using Helix 02 | 49, Table 49.3 | CONFIRMED | https://www.therobotreport.com/bmw-group-deploys-figure-03-humanoid-after-tests-previous-version/ (July 2026, via search) | None |
| Agility Digit: 9 sites, 65,000+ hours, customers; "company claims in an SEC filing" | 49, Table 49.3 | CORRECTED | https://interestingengineering.com/ai-robotics/us-digit-robot-maker-agility (June 25, 2026) | Figures confirmed; source label changed to "Company claims, from its June 2026 listing announcement", and the June 2026 merger to become a listed company added |
| GXO: Digit moved 100,000 totes (November 2025) | 49, Table 49.3; 53, Logistics | CONFIRMED | https://oodaloop.com/briefs/technology/agility-robotics-digit-humanoid-passes-100000-tote-milestone-in-live-gxo-implementation (via search) | None |
| Boston Dynamics production Atlas at CES (January 2026); Hyundai Georgia plant from 2028; Gemini partnership | 49, Table 49.3 | CONFIRMED | https://en.wikipedia.org/wiki/Atlas_(robot) (secondary; the exact January 5 date and the DeepMind deliveries are not in it) | None |
| Tesla Optimus V3: production "slated to begin at Fremont in mid-2026", Texas 2027 | 49, Table 49.3 | CORRECTED | https://electrek.co/2026/04/22/tesla-optimus-production/ | Now: Musk said on the April 2026 call that Fremont production would start in late July or August 2026, slowly and at an unpredictable rate, with Texas around summer 2027; label "Company statements; output unconfirmed" |
| 1X NEO: pre-orders October 28, 2025 at $20,000 or $499 a month; 100,000+ a year by end-2027; no confirmed consumer deliveries | 49, Table 49.3 | CONFIRMED | https://letsdatascience.com/news/1x-ships-neo-humanoid-robots-to-us-homes-774b7a74 (May 1, 2026: deliveries still "planned for 2026") | None |
| 1X Hayward factory began full-scale production (April 30, 2026) | 49, Table 49.3 | ADDED | https://macaubusiness.com/1x-opens-neo-factory-in-hayward-ca-americas-first-vertically-integrated-humanoid-robot-factory-with-consumer-shipments-planned-for-2026/ (via search) | Added to the 1X row (company claim) |
| Waymo about 500,000 paid rides a week (spring 2026) | 49, Worked example; 50, Waymo | CONFIRMED | https://www.sherwood.news/tech/waymos-now-serving-more-than-500-000-paid-robotaxi-rides-every-week/ ; https://driveteslacanada.ca/news/waymo-driverless-rides-denver-san-diego-tampa/ (via search; still the latest figure in September 2026) | None |
| About 40,000 US road deaths a year, about 3 trillion miles, about 1.3 deaths per 100 million miles | 50, Why driving is hard | CONFIRMED | https://en.wikipedia.org/wiki/Motor_vehicle_fatality_rate_in_U.S._by_year (1.27 to 1.35 in 2022–23; the 2025 early estimate is lower, about 1.14) | None; the round figures hold for "a typical recent year" |
| NHTSA "94 percent" critical-reason note (2015); SAE J3016 (2014) | 50, Levels | CONFIRMED | n.r. | None |
| Mercedes Drive Pilot first US Level 3 (Nevada and California, 2023), up to about 40 mph | 50, Levels; history | CONFIRMED | n.r. | None |
| DARPA 2004/2005 (Stanley, 132 miles)/2007 (Boss); Google 2009, Waymo 2016, Waymo One 2018, driverless 2020 | 50, History | CONFIRMED | n.r. | None |
| Uber Tempe crash (March 2018) and NTSB findings; sale to Aurora (2020) | 50, Two crashes | CONFIRMED | n.r.: https://www.ntsb.gov/investigations/Pages/HWY18MH010.aspx | None |
| Cruise drag (October 2023); GM ended robotaxis (December 2024) | 50, Two crashes | CONFIRMED | n.r. | None |
| Tesla Robotaxi launched in Austin (June 2025) with safety monitors | 50, History; Tesla | CONFIRMED | n.r. | None |
| Waymo up from 250,000 (April 2025); target 1 million a week by end-2026 | 50, Waymo | CONFIRMED | https://techcrunch.com/2025/02/27/waymo-has-doubled-its-weekly-robotaxi-rides-in-less-than-a-year/ ; Bloomberg interview via https://www.sherwood.news/tech/waymos-now-serving-more-than-500-000-paid-robotaxi-rides-every-week/ | None |
| Waymo "more than 20 million cumulative trips" | 50, Waymo | UNVERIFIABLE | Not reached | None |
| Waymo fleet "about 3,500 vehicles" | 50, Waymo; Table 50.3; worked example | CORRECTED | https://www.ttnews.com/articles/waymo-halts-atlanta-robotaxi (Bloomberg, May 21, 2026: 3,791 vehicles recalled) | Now about 3,800. Worked example now 500,000 ÷ 3,800 ≈ 132 rides per vehicle per week, about 19 a day. Exercise 8 starts at 19 |
| Waymo 271.3 million rider-only miles to June 2026; 95% (94.82%), 82%, 93%, 82% fewer crashes | 50, Waymo; Applying the method | CONFIRMED | https://waymo.com/safety/impact/ (data through June 2026; still current at Waymo's September 24, 2026 update) | None |
| Waymo cities: "a March 2026 expansion brought driverless service to 10 metro areas ... Las Vegas went fully driverless on July 8, 2026, with Denver, San Diego and Tampa named as next" | 50, Waymo; Figure 50.6; Table 50.3; In plain English | CORRECTED | https://waymo.com/rides/ ; https://blog.waymo.com/blog/shorts/ro-den-lv-sd-tmpa/ (July 8, 2026: all four cities); https://waymo.com/blog/2026/10/waymo-closes-5-billion-debt-financing ("fifteenth U.S. city last month") | Now: 15 US metros serving riders as of October 2026, all listed; Las Vegas, Denver, San Diego and Tampa went driverless in July 2026 (employees first) and opened to the public from September. Timeline, table and recap updated (11 to 15) |
| Waymo abroad: London targeted for 2026; Tokyo for 2027; no paid rides outside the US | 50, Waymo | CONFIRMED | https://waymo.com/rides/ (London and Tokyo listed as "Up Next") | Wording updated to "up next" |
| Waymo Madrid (first riders targeted 2027) and Toronto (targeted 2028), announced October 2026 | 50, Waymo | ADDED | https://waymo.com/blog/2026/10/waymo-in-madrid-region ; https://waymo.com/blog/2026/10/waymo-in-toronto | Added to the Abroad bullet |
| Waymo May 2026 flood software recall (3,791 vehicles), storm pauses, freeway pause in four cities | 50, Waymo | ADDED | https://www.ttnews.com/articles/waymo-halts-atlanta-robotaxi ; https://techcrunch.com/2026/05/21/waymo-halts-freeway-rides-after-robotaxis-struggle-in-construction-zones/ | New "Setbacks" bullet, with "recall" explained inline |
| Tesla: unsupervised rides in Austin, Dallas, Houston, later Florida; September 2026 report of 1 million+ unsupervised miles and about 200+ vehicles; Musk on unsupervised FSD in Q4 2026; about 12 billion supervised FSD miles (Q2 2026 call) | 50, Tesla | UNVERIFIABLE | https://www.tesla.com/fsd/safety (returned 403); no other primary source reached | None; the text already labels these as company or single secondary figures |
| Zoox: about 2 million autonomous miles and 350,000+ riders (March 2026) | 50, Zoox | UNVERIFIABLE | Not reached (zoox.com journal pages returned 404) | None |
| Zoox: NHTSA's first commercial exemption for a purpose-built robotaxi (July 30, 2026), capped at 2,500 a year | 50, Zoox; Regulation | UNVERIFIABLE | https://en.wikipedia.org/wiki/Zoox_(company) records only the August 2025 demonstration exemption | None |
| Zoox paid rides in Las Vegas from August 10, 2026 | 50, Zoox | CONFIRMED | https://en.wikipedia.org/wiki/Zoox_(company) (citing CNBC, August 5, 2026) | None |
| Baidu Apollo Go: 20M+ rides (February 2026); 300,000+ weekly peak (Q4 2025); about 3.2 million driverless rides (Q1 2026) | 50, China | UNVERIFIABLE | https://ir.baidu.com (returned 403) | None |
| Apollo Go driverless commercial service in Dubai | 50, China | CONFIRMED | https://en.wikipedia.org/wiki/Apollo_Go (citing Baidu's April 2026 release) | None |
| Apollo Go driverless commercial service in Abu Dhabi; London road tests | 50, China | UNVERIFIABLE | https://en.wikipedia.org/wiki/Apollo_Go lists Abu Dhabi only as announced | None |
| Pony.ai: 1,975 vehicles (June 30, 2026), 3,500+ targeted | 50, China | UNVERIFIABLE | https://ir.pony.ai (returned 403) | None |
| Kusano et al., 56.7 million miles (Traffic Injury Prevention) | 50, Applying the method | CONFIRMED | n.r. | None |
| RAND "Driving to Safety" (2016): 1.09 per 100 million; about 275 million miles | 50, Rule of three | CONFIRMED | n.r.: https://www.rand.org/pubs/research_reports/RR1478.html | None |
| NHTSA Standing General Order (2021); UK Automated Vehicles Act 2024 | 50, Regulation | CONFIRMED | n.r. | None |
| At the frontier: the modular and end-to-end camps have blurred | 50, End-to-end | CONFIRMED | General statement | None |
| At the frontier: race to scale; Waymo 1 million target; exemption caps; first paid driverless rides in Europe | 50, Landscape | CONFIRMED | https://waymo.com/rides/ ; https://waymo.com/blog/2026/10/waymo-in-madrid-region (no European paid rides yet) | None |
| Netflix about 80% of hours from recommendations (2015); YouTube 70%+ (2018) | 51, Introduction | CONFIRMED | n.r. | None |
| Amazon item-to-item (2003); Netflix Prize (about 100 million ratings, 480,000 users, 17,770 films) | 51, Collaborative filtering | CONFIRMED | n.r. | None |
| Twitter/X recommendation code (March 2023, about 1,500 candidates); YouTube two-stage paper (2016) | 51, The funnel | CONFIRMED | n.r. | None |
| At the frontier: Meta "generative recommenders" (2024) with power-law scaling; Google semantic IDs | 51, Two-tower | CONFIRMED | https://arxiv.org/abs/2402.17152 (ICML 2024; quality "scales as a power-law of training compute"); https://arxiv.org/abs/2305.05065 (Semantic IDs, NeurIPS 2023) | None |
| YouTube watch time (2012); Facebook "meaningful social interactions" (2018); WSJ (2021) | 51, What to optimize | CONFIRMED | n.r. | None |
| 2023 Science/Nature Facebook and Instagram election experiments | 51, Polarization | CONFIRMED | n.r. | None |
| NY SAFE for Kids Act (2024); DSA non-profiling feed | 51, Teens | CONFIRMED | n.r. | None |
| At the frontier: "worth your time" surveys; bridging ranking in Community Notes | 51, Teens | CONFIRMED | General statement; n.r. | None |
| Lookalike audiences (2013); Performance Max (2021); Advantage+ (2022); ATT (April 2021); Meta's $10 billion estimate (2022); Chrome cookies decisions (2024, 2025) | 51, Ads | CONFIRMED | n.r. | None |
| At the frontier: OpenAI announced ChatGPT ads (January 2026), seen by March 2026; Agentic Commerce Protocol with Stripe (September 2025) | 51, Ads | CONFIRMED | https://en.wikipedia.org/wiki/ChatGPT (announcement January 2026; "Ads started to be seen by March 2026"); ACP n.r. | None |
| PageRank (1998); Knowledge Graph (2012); RankBrain (2015); BERT in 1 in 10 US English searches (October 2019); AI Overviews (May 2024); AI Mode (2025) | 51, Search | CONFIRMED | n.r. | None |
| Pew (March 2025 browsing): 8% vs 15% clicks; 1% inside the summary | 51, SEO to GEO | CONFIRMED | n.r.: https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/ | None |
| GEO paper (2023, arXiv:2311.09735); llms.txt discussed since 2024 | 51, SEO to GEO | CONFIRMED | n.r. | None |
| AlphaFold 2 at CASP14 (median about 92); database (2021); 200 million+ (2022) | 52, Proteins | CONFIRMED | n.r. | None |
| AlphaFold DB over 260 million predictions; October 2026 links from residues and mutations to papers | 52, Proteins; timeline | CONFIRMED | https://alphafold.ebi.ac.uk/ | None |
| 2024 Nobel Prizes (Baker, Hassabis, Jumper; Hopfield, Hinton) | 52, Proteins | CONFIRMED | n.r.: https://www.nobelprize.org/prizes/chemistry/2024/summary/ | None |
| AlphaFold 3 (May 2024), code for academics (late 2024) | 52, Proteins | CONFIRMED | n.r. | None |
| RFdiffusion (2023); antivenom proteins (Nature 2025); designed-nanoparticle COVID vaccine (South Korea 2022) | 52, Protein design | CONFIRMED | n.r. | None |
| ESM3 (2024): esmGFP about 58% identity, "500 million years" | 52, Protein language models | CONFIRMED | n.r. | None |
| Microsoft-led Science paper (2025) on AI-redesigned toxins slipping past screening | 52, Watch out | CONFIRMED | n.r. | None |
| AlphaMissense (2023): about 71 million variants, 89% classified | 52, Genomics | CONFIRMED | n.r. | None |
| Evo 2 (2025): about 9 trillion letters, 100,000+ species, about 1 million context | 52, Genomics | CONFIRMED | n.r. | None |
| AlphaGenome (2025): up to 1 million letters | 52, Genomics | CONFIRMED | n.r. | None |
| AlphaGenome Atlas (September 8, 2026): about 9 billion single-letter variants; free for academics; not for clinical use | 52, Genomics; timeline | ADDED | https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/ | One sentence added after the AlphaGenome paragraph; timeline entry |
| At the frontier: genomics moving toward "virtual cell" models | 52, Genomics | CONFIRMED | General statement | None |
| Clinical success rates 2011–2020 (about 52%, 29%, 58%, 91%) | 52, Drug pipeline | CONFIRMED | n.r.: BIO/Informa/QLS 2021 report | None |
| AI-discovered molecules: 80–90% pass Phase I, about 40% Phase II (2024 analysis) | 52, Drug pipeline | CONFIRMED | n.r. | None |
| Halicin (2020), over 100 million compounds screened | 52, Drug examples | CONFIRMED | n.r. | None |
| Rentosertib Phase IIa (Nature Medicine, 2025): 71 patients, 12 weeks | 52, Drug examples | CONFIRMED | https://en.wikipedia.org/wiki/Rentosertib | None (the FVC figures, +98.4 mL vs −20.3 mL, were not re-checked because the paper redirected to a login) |
| Isomorphic Labs had not dosed a human by May 2026; first-in-human expected by end-2026 | 52, Drug examples | CONFIRMED | https://www.isomorphiclabs.com/news ; https://www.isomorphiclabs.com/articles/building-a-new-path-to-make-medicines-with-ai (September 29, 2026) | Added that in late September 2026 the company still described its work as preclinical ("gear up for clinical developments") |
| No AI-designed drug approved as of late 2026; AI drugs at "mid-stage" trials | 52, Drug examples | UNVERIFIABLE | https://en.wikipedia.org/wiki/Rentosertib says rentosertib was in a Phase 3 trial in 2026, citing a secondary drug-information site | None; flagged for a follow-up check |
| GNoME (November 2023): 2.2 million crystals, about 380,000 stable; A-Lab 41 of 58 in 17 days; 2024 critiques | 52, Materials | CONFIRMED | n.r. | None |
| Coscientist (Nature 2023) | 52, Materials | CONFIRMED | n.r. | None |
| GraphCast (2023) arithmetic; GenCast (December 2024, about 97% of targets); AIFS operational (February 2025); WeatherNext 2 (November 2025) | 52, Weather; Table | CONFIRMED | n.r.; WeatherNext 2's 25 km grid is confirmed in the WeatherNext 3 post | None |
| WeatherNext 3 (September 3, 2026): hourly forecasts from raw satellite data, 5 km temperature and moisture, used in Search, Gemini and Maps | 52, Weather table; "What AI weather models still depend on" | ADDED | https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-weathernext-3/ | New table row; one sentence noting it starts from raw satellite observations |
| DeepMind cyclone model: Nature paper (August 6, 2026); three-day forecasts as good as earlier two-day ones; helped the Hurricane Center with Melissa (2025) | 52, Weather | ADDED | https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/ | One sentence added after the 2025 Hurricane Center evaluation sentence |
| AlphaGeometry (January 2024: 25 of 30, 100 million synthetic examples); AlphaProof and AlphaGeometry 2 (28 of 42, 2024) | 52, Mathematics; 54, Neuro-symbolic | CONFIRMED | n.r. | None |
| Gemini Deep Think 35/42 at IMO 2025, officially graded; OpenAI 35/42 graded by former medalists | 52, Mathematics; 54, Neuro-symbolic | CONFIRMED | n.r. | None |
| IMO 2026: claims of perfect AI scores not officially certified | 52, Mathematics | UNVERIFIABLE | https://www.imo-official.org/ (no statement on AI results) | None; already hedged |
| AlphaEvolve: 4 × 4 complex matrices in 48 multiplications; August 2026 preprint brings ω to about 2.371177 | 52, Mathematics; 54, Evolution (At the frontier) | CONFIRMED | https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication (bound "as of August 2026", citing Dupont et al., "Improving the Matrix Multiplication Exponent with Modern Optimization and AlphaEvolve") | None |
| Erdős-problems episode (October 2025); FunSearch (2023) | 52, Mathematics | CONFIRMED | n.r. | None |
| AI Index 2026: IMO-gold model reads analog clocks right about half the time | 52, Mathematics | CONFIRMED | https://hai.stanford.edu/ai-index/2026-ai-index-report ("50.1% of the time") | None |
| Google AI co-scientist (February 2025) | 52, AI scientists | CONFIRMED | n.r. | None |
| At the frontier: agents connected to cloud labs | 52, AI scientists | CONFIRMED | General statement | None |
| LHC about 40 million crossings a second; Kepler-90i (2017) | 52, Physics and astronomy | CONFIRMED | n.r. | None |
| MASAI (about 80,000 women): 20% more cancers, 44% less reading work (2023); Paige Prostate (2021) | 52, Medical imaging | CONFIRMED | n.r. | None |
| IDx-DR pivotal study: 900 people, 10 sites, sensitivity 87.2%, specificity 90.7% | 52, Medical imaging | CONFIRMED | n.r. | None |
| Epic sepsis model evaluation (JAMA IM 2021); TREWS (2022) | 52, Sepsis | CONFIRMED | n.r. | None |
| Abridge Best in KLAS (2025 and 2026); Dragon Copilot (March 2025) | 52, Scribes | CONFIRMED | https://www.abridge.com/press ; Dragon Copilot n.r. | None |
| ChatGPT about 900 million weekly users (February 2026); ChatGPT Health (January 2026) | 52, Chatbots and health | CONFIRMED | https://en.wikipedia.org/wiki/ChatGPT (January 7, 2026 launch; 900 million in February 2026) | None |
| Med-PaLM 2 86.5% (2023); Oxford study with about 1,300 participants (2025); Microsoft diagnostic system (mid-2025) | 52, Chatbots and health | CONFIRMED | n.r. | None |
| At the frontier: generalist medical models and administrative agents | 52, Medicine | CONFIRMED | General statement | None |
| Flash Crash (May 6, 2010); Knight Capital (August 1, 2012, about $440 million in 45 minutes); ECOA (1974) | 53, Finance | CONFIRMED | n.r. | None |
| At the frontier: banks moving from fraud scores to investigation agents | 53, Finance | CONFIRMED | General statement | None |
| Stanford 2024 legal-RAG study (about one in six or worse wrong); Mata v. Avianca ($5,000, 2023); TAR accepted since 2012 | 53, Law | CONFIRMED | n.r. | None |
| Bloom 2 sigma (1984); Stanford detector bias study (2023); OpenAI detector withdrawn (2023); Turkish GPT-4 field experiment | 53, Education | CONFIRMED | n.r. | None |
| AI Index 2026: over 80% of US high-school and college students use AI for school | 53, Education | CONFIRMED | https://hai.stanford.edu/ai-index/2026-ai-index-report | None |
| Brynjolfsson, Li and Raymond (5,000+ agents, +14%, +34%); Klarna (February 2024, 2.3 million chats, about 700 agents; 2025 reversal); Moffatt v. Air Canada (2024); FTC fake-review rule (2024) | 53, Customer service and marketing | CONFIRMED | n.r. | None |
| UPS ORION about 100 million miles a year; Deere bought Blue River (2017) | 53, Logistics; Agriculture | CONFIRMED | n.r. | None |
| DoD Directive 3000.09 (2012, 2023); CCW talks since 2014; UNGA resolution (December 2023); treaty call for 2026 | 53, Defense | CONFIRMED | n.r. | None |
| Big Sleep SQLite bug (November 2024); AIxCC finals (August 2025) | 53, Cybersecurity | CONFIRMED | n.r. | None |
| Anthropic disrupted a Chinese state-sponsored campaign using Claude Code (November 2025): about 30 targets, 80–90% of tactical work by AI | 53, Cybersecurity | CONFIRMED | https://www.anthropic.com/news/disrupting-AI-espionage | None |
| At the frontier: Claude Mythos Preview and Project Glasswing (April 2026); "thousands of high-severity vulnerabilities" in major OSes and browsers; restricted access | 53, Cybersecurity | CONFIRMED | https://www.anthropic.com/glasswing (announced April 7, 2026) | None |
| Industry table: wind forecasts +20% value (2019); Colorado insurance law (2021); Zillow Offers (2021); Amazon résumé tool (2018); NYC bias audits (2023); Robodebt (2023); Dutch benefits scandal (2021); AP earnings stories (2014); CNET (2023); semi-automated offside (2022) | 53, Other industries | CONFIRMED | n.r. | None |
| Copilot+ PCs 40 TOPS (2024); Neural Engine since A11 (2017) | 53, Edge chips | CONFIRMED | n.r. | None |
| Apple M5 (October 2025) has a Neural Accelerator in each GPU core | 53, Edge chips | CONFIRMED | https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/ | None |
| Apple about 3B on-device model; Private Cloud Compute (2024); "Hey Siri" two-stage detector (2017); Gboard federated learning (2017); Apple Watch fall detection and ECG (2018) | 53, Edge | CONFIRMED | n.r. | None |
| Gemini Robotics On-Device (June 2025) and On-Device 2 (July 2026) | 53, Edge examples | CONFIRMED | https://www.therobotreport.com/google-deepmind-says-gemini-robotics-2-enables-full-body-control/ | None |
| At the frontier: DGX Spark "reportedly with 128 GB" | 53, Edge | CORRECTED | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ ("64 GB or 128 GB") | "reportedly" removed; now "with up to 128 GB of unified memory" |
| Domingos's five tribes (2015); MYCIN; XCON; Cyc (1984); Prolog (1972) | 54, Rules | CONFIRMED | n.r. | None |
| Knowledge Graph (2012); Wikidata (2012), more than 100 million items | 54, Knowledge graphs | CONFIRMED | n.r.: https://www.wikidata.org/wiki/Wikidata:Statistics | None |
| Pearl's Turing Award (2011); Pathfinder; Kalman filter (1960); fuzzy logic (1965); Sendai Namboku Line (1987) | 54, Uncertainty | CONFIRMED | n.r. | None |
| Karl Sims (1994); ant colony optimization; particle swarm optimization (1995); boids (1987) | 54, Evolution | CONFIRMED | n.r. | None |
| At the frontier: AlphaEvolve (see Chapter 52 row) | 54, Evolution | CONFIRMED | As above | None |
| Asthma paradox (Caruana 2015); Google Flu Trends (2008, overestimate 2012–13, closed 2015) | 54, Causality | CONFIRMED | n.r. | None |
| At the frontier: formal verification as a training ground | 54, Neuro-symbolic | CONFIRMED | General statement | None |
| Georgetown–IBM (January 7, 1954; 60+ sentences, about 250 words, 6 rules); ALPAC (1966); IBM statistical MT (1990); GNMT (2016); NLLB-200 (2022) | 54, Language before LLMs | CONFIRMED | n.r. | None |
| Cheapest major-lab LLM tier about $0.10 per million input tokens (late 2026) | 54, Classic NLP tasks | CONFIRMED | https://ai.google.dev/gemini-api/docs/pricing (Gemini 2.5 Flash-Lite, $0.10 standard; $0.05 batch) | None |
| About 86 billion neurons and 20 watts; Hubel and Wiesel (Nobel 1981); Schultz, Dayan and Montague (1997); TrueNorth (2014); Loihi (2017), Loihi 2 (2021) | 54, The brain | CONFIRMED | n.r. | None |
| BrainGate (2006); 2023 Stanford and UCSF speech decoders (about 60–80 words a minute); UC Davis NEJM 2024 (about 97%) | 54, BCIs | CONFIRMED | n.r. | None |
| Neuralink: "a February 2026 report put the number of participants ... at 21 or more (a secondary source)" | 54, BCIs | CORRECTED | https://en.wikipedia.org/wiki/Neuralink ("In January 2026, Neuralink said it had 21 participants enrolled in trials worldwide") | Now "said in January 2026 that 21 participants were enrolled in its trials worldwide (as reported)" |
| Neuralink Blindsight still awaiting a first human implant (mid-2026) | 54, BCIs | UNVERIFIABLE | https://neuralink.com/updates/ (no content returned) | None |
| UT Austin semantic decoder (2023, about 16 hours per person); Chile (2021); Colorado (2024) and California neural-data laws | 54, BCIs | CONFIRMED | n.r. | None |
| At the frontier: speech neuroprostheses | 54, BCIs | CONFIRMED | General statement | None |

## Summary

**Counts (one row can group several closely related claims):**

| Verdict | Rows |
|---|---|
| CONFIRMED | 190 (53 checked against a page fetched or a search result this round; 12 frontier-box or cross-reference rows with no figures to check; 125 matching the long-established record, marked n.r.) |
| CORRECTED | 12 |
| HEDGED | 2 (the Sora world-model wording, in three places) |
| UNVERIFIABLE | 16 |
| ADDED | 12 |
| **Total** | **232** |

All 26 "At the frontier (2026)" boxes in Chapters 45–54 were checked. Two Chapter 47 boxes were changed: "folded Genie into Gemini Omni" was corrected, and the Sora world-model clause was hedged in both. Two boxes gained a sourced sentence: Chapter 48 (the EVE Online research partnership) and Chapter 49 (Gemini 4 Argon for Robotics). Chapter 53's DGX Spark figure is now stated from NVIDIA's own spec. The rest were confirmed, or are general statements with no figures to check.

**Main corrections:**

- **Waymo (Chapter 50, also the Chapter 50 recap, timeline and table).** The book said 10 metros in March, with Las Vegas driverless on July 8 and Denver, San Diego and Tampa "next". In fact all four started driverless operation in July, and by October 2026 Waymo listed 15 US metros serving the public. The fleet figure is now about 3,800 (3,791 vehicles were recalled in May 2026), and the rides-per-car worked example and Exercise 8 were updated to match. Added: Madrid (riders 2027) and Toronto (2028), and a short "Setbacks" bullet on the May 2026 flood recall and service pauses.
- **Music law (Chapter 46).** Suno launched licensed v6 models in September 2026. Universal and Sony are still suing Suno and filed a second suit in September 2026. The timeline and the answer to Question 7 were updated.
- **Generative media (Chapter 47).** The Sora API end date is now past tense. "Folded Genie into Gemini Omni" was unsupported and is corrected. The Sora world-model framing is hedged. The video table now includes Kling 4.0, Seedance 2.5 and Gemini Omni 1.1 Flash, and the image section adds GPT Image 2.5.
- **Robotics (Chapter 49).** Agility's figures come from its June 2026 announcement that it is becoming a listed company; no SEC filing was located, so the label is fixed. Tesla's Optimus start date is now quoted exactly from the April 2026 call. Added: the 1X factory start and Gemini 4 Argon for Robotics.
- **Smaller fixes.** DGX Spark memory is now stated from NVIDIA's own spec. The Neuralink participant count is now dated January 2026.

**Additions (June–October 2026 developments):** Gemini 3.5 Transcribe WER (August), Suno v6 (September), GPT Image 2.5 (September), Seedance 2.5 (July), Kling 4.0 (October), Gemini Omni 1.1 Flash (August), the DeepMind–EVE Online research partnership (August), Gemini 4 Argon for Robotics (October), Waymo's expansion to 15 metros plus Madrid and Toronto (July to October), WeatherNext 3 (September), the WeatherNext cyclone paper in Nature (August), AlphaGenome Atlas (September), and Isomorphic Labs' September statement that it is still preclinical. SAM 3.1 (March 2026) was also added.

**Unresolved (left unchanged; worth a follow-up with more search budget):**

- The FDA AI-device counts (fda.gov returned 401).
- Tesla Robotaxi and FSD mileage.
- Zoox's July 2026 commercial exemption and its rider and mileage counts.
- Baidu Apollo Go ride counts and Abu Dhabi status.
- Pony.ai's fleet size.
- Udio's deals with Warner, Merlin and Kobalt.
- Project Genie's date and terms.
- Getty's April 2026 US ruling.
- Counterpoint's humanoid estimate.
- Waymo's "20 million cumulative trips".
- The Intermountain 27% figure.
- Neuralink Blindsight.
- Whether any AI-designed drug has reached Phase 3 or approval. A secondary source says rentosertib is in Phase 3; if confirmed, Chapter 52's "mid-stage trials" wording should change to "late-stage".

Chapter 51 needed no changes. All edited files (Chapters 45, 46, 47, 48, 49, 50, 52, 53, 54) pass validate.py and check.py.
