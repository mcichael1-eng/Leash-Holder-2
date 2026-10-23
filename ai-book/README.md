# The AI Field Guide

*Everything about artificial intelligence, built up from nothing. October 2026 edition.*

A complete book for someone with almost no computer-science background who uses AI chatbots every day and wants to understand all of it: how computers work, the math, how machines learn, neural networks and Transformers, how frontier labs build large language models, how to build with AI, chips and compute, data centers and energy, every major branch of AI, safety, law and society, and the skills, careers and opportunities that come with it.

- **10 parts, 66 chapters, 6 appendices**
- **3,694 terms** in a searchable glossary (every term is defined where it first appears)
- **533 diagrams**, plus tables and hand-worked numeric examples
- **659 exercises** from Easy to Challenge, none of which require prior coding experience
- About **1,040,000 words**

## How to read it

- **Online:** https://claude.ai/artifact/YZmhMT1K8T6v12mx3uaefh (contents sidebar, every diagram drawn, searchable glossary, reading progress).

- **Offline:** open `site/index.html` in a browser after building (see below), or read the Markdown chapters in `chapters/` directly on GitHub, which also renders the diagrams.
- Read in order if you are new: each chapter assumes only the ones before it. Chapter 1 maps the whole field and suggests three reading paths.
- Look for the boxes: **Definition** (every term), **Key idea**, **Analogy**, **Try it** (a one-minute experiment), **At the frontier (2026)** (what leading labs do now) and **Watch out** (common mistakes).

## Contents

### Part I: Foundations: How Computers Work and the Math Behind AI

*What a computer is, how everything becomes numbers, how your message reaches a data center, the math every model uses, and the 180-year story of AI.*

1. [What AI Is: A Map of the Whole Field](chapters/01-what-ai-is.md)
2. [How Computers Work: Bits, Transistors and Processors](chapters/02-how-computers-work.md)
3. [Software, Code and Data: How Everything Becomes Numbers](chapters/03-software-code-data.md)
4. [The Internet and the Cloud: How Your Message Reaches a Data Center](chapters/04-internet-and-cloud.md)
5. [The Math of AI, Part 1: Functions, Vectors and Matrices](chapters/05-math-vectors-matrices.md)
6. [The Math of AI, Part 2: Probability, Statistics and Learning by Slopes](chapters/06-math-probability-gradients.md)
7. [A History of AI: 1843 to 2026](chapters/07-history-of-ai.md)

### Part II: How Machines Learn

*How a computer can learn a rule from examples instead of being told it, how to tell whether it learned anything, the classic algorithms, and the data that feeds them.*

8. [Learning From Examples: What Machine Learning Really Is](chapters/08-learning-from-examples.md)
9. [Is the Model Any Good? Evaluation, Overfitting and Metrics](chapters/09-evaluation-and-metrics.md)
10. [The Classical Machine Learning Toolkit](chapters/10-classical-ml-toolkit.md)
11. [Data: The Fuel of AI](chapters/11-data-the-fuel.md)

### Part III: Neural Networks and Deep Learning

*The artificial neuron, how networks learn, and the architectures that power modern AI, from convolutional networks to the Transformer, diffusion and mixture of experts.*

12. [Neural Networks From Scratch](chapters/12-neural-networks-from-scratch.md)
13. [Training Deep Networks: Optimizers, Tricks and Why Depth Works](chapters/13-training-deep-networks.md)
14. [Seeing and Remembering: CNNs, RNNs, Embeddings and the Deep Learning Boom](chapters/14-cnns-rnns-embeddings.md)
15. [The Transformer, Piece by Piece](chapters/15-the-transformer.md)
16. [Generative Models: Autoencoders, GANs, Diffusion and Flow](chapters/16-generative-models.md)
17. [Beyond the Transformer: Mixture of Experts, State Space Models and New Architectures](chapters/17-beyond-the-transformer.md)

### Part IV: Large Language Models: How Frontier Models Are Made

*How the chatbots you use every day are actually built: tokens, pretraining, post-training, reasoning, multimodality, serving, and the 2026 model landscape.*

18. [How a Large Language Model Works](chapters/18-how-llms-work.md)
19. [Pretraining: Data, Scale and Scaling Laws](chapters/19-pretraining-and-scaling.md)
20. [Post-Training: Turning a Text Predictor Into an Assistant](chapters/20-post-training.md)
21. [Reasoning Models and Reinforcement Learning](chapters/21-reasoning-models.md)
22. [Multimodal Models: Seeing, Hearing and Speaking](chapters/22-multimodal-models.md)
23. [Inference: Making Models Fast and Cheap](chapters/23-inference.md)
24. [The 2026 Model Landscape and How to Read Benchmarks](chapters/24-model-landscape-benchmarks.md)

### Part V: Using and Building With AI

*From expert prompting to APIs, retrieval, tools, agents, coding agents, fine-tuning, local models and shipping reliable, secure AI products.*

25. [Mastering the Chat Interface: Prompting and Context Engineering](chapters/25-prompting-and-context.md)
26. [APIs: Talking to Models With Code](chapters/26-apis.md)
27. [Retrieval: Giving AI Your Knowledge](chapters/27-retrieval-rag.md)
28. [Tools and Agents: From Function Calling to MCP](chapters/28-tools-and-agents.md)
29. [Coding With AI and Building Without Code](chapters/29-coding-and-no-code.md)
30. [Customizing Models: Fine-Tuning, Open Weights and Running AI Locally](chapters/30-fine-tuning-and-local.md)
31. [Shipping AI: Evals, Reliability, Security and Product Design](chapters/31-evals-security-product.md)

### Part VI: Compute: The Machines Behind AI

*The machines behind AI: GPUs and TPUs, memory, networks, the chip industry, how chips are made, and how training and serving work at the scale of 100,000 chips.*

32. [From Transistor to Accelerator: CPUs, GPUs, TPUs and FLOPs](chapters/32-cpus-gpus-tpus.md)
33. [Memory and the Memory Wall](chapters/33-memory-wall.md)
34. [Wiring Thousands of Chips Together: Servers, Racks, Networks and Clusters](chapters/34-servers-racks-networks.md)
35. [The AI Chip Industry: NVIDIA, AMD, Google, Custom Silicon and Startups](chapters/35-ai-chip-industry.md)
36. [How Chips Are Made: Fabs, Lithography, Packaging and Geopolitics](chapters/36-how-chips-are-made.md)
37. [Training and Serving at Scale: The Math of Compute](chapters/37-training-serving-at-scale.md)

### Part VII: Data Centers and Energy

*The buildings, power plants, cooling systems and money behind AI, and how every layer from sand to your screen comes together.*

38. [Inside a Data Center](chapters/38-inside-a-data-center.md)
39. [Power: From the Grid to the GPU](chapters/39-power.md)
40. [Cooling: Where the Heat Goes](chapters/40-cooling.md)
41. [Energy for AI: Grids, Gas, Nuclear and Renewables](chapters/41-energy-for-ai.md)
42. [The Great Buildout: Hyperscalers, Neoclouds and Megaprojects](chapters/42-the-buildout.md)
43. [The Economics of AI Compute](chapters/43-economics-of-compute.md)
44. [How It All Comes Together: The Life of a Prompt and the Making of a Frontier Model](chapters/44-how-it-all-comes-together.md)

### Part VIII: The Branches of AI

*AI beyond chatbots: vision, speech, generative media, games, robots, self-driving cars, recommenders, science, medicine and every major industry.*

45. [Computer Vision](chapters/45-computer-vision.md)
46. [Speech, Audio and Music](chapters/46-speech-audio-music.md)
47. [Generative Media: Images, Video, 3D and World Models](chapters/47-generative-media.md)
48. [Reinforcement Learning, Games and Planning](chapters/48-rl-games-planning.md)
49. [Robotics and Physical AI](chapters/49-robotics.md)
50. [Self-Driving Vehicles](chapters/50-self-driving.md)
51. [Recommenders, Search and Ads: The AI You Use Without Noticing](chapters/51-recommenders-search-ads.md)
52. [AI for Science and Medicine](chapters/52-science-and-medicine.md)
53. [AI Across Industries and at the Edge](chapters/53-industries-and-edge.md)
54. [Other Paths to Intelligence: Symbolic AI, Language Before LLMs, Evolution, Bayes, Causality and Brains](chapters/54-other-paths.md)

### Part IX: Safety, Ethics, Law and Society

*What can go wrong, how labs try to make AI safe, how we look inside models, misuse and harms, the law, and AI's effect on work and society.*

55. [What Can Go Wrong: Reliability and the Alignment Problem](chapters/55-alignment-problem.md)
56. [How Labs Make AI Safer: Alignment Techniques, Safety Frameworks and Control](chapters/56-making-ai-safer.md)
57. [Interpretability and Evaluations: Looking Inside and Testing](chapters/57-interpretability-and-evals.md)
58. [Misuse, Security and Everyday Harms](chapters/58-misuse-and-harms.md)
59. [AI Law and Policy Around the World](chapters/59-law-and-policy.md)
60. [AI, Work, the Economy and the Big Debates](chapters/60-work-economy-debates.md)

### Part X: Your Path: Skills, Careers and Opportunity

*Who makes money in AI, every skill and role, where the opportunities are, a learning roadmap, and what comes next.*

61. [The AI Industry Map: Who Makes Money and How](chapters/61-industry-map.md)
62. [The Complete AI Skills Map](chapters/62-skills-map.md)
63. [Careers in AI: Every Role Explained](chapters/63-careers.md)
64. [Opportunities: Where You Can Win](chapters/64-opportunities.md)
65. [Your Learning Roadmap and How to Stay Current](chapters/65-learning-roadmap.md)
66. [The Road Ahead: Open Problems and the Future of AI](chapters/66-the-road-ahead.md)

### Reference

- Appendix A: [Numbers and Units Cheat Sheet](appendices/A-numbers-and-units.md)
- Appendix B: [Math Cheat Sheet](appendices/B-math-cheat-sheet.md)
- Appendix C: [AI Timeline, 1843–2026](appendices/C-timeline.md)
- Appendix D: [Who's Who: Companies, Labs, Products and People](appendices/D-whos-who.md)
- Appendix E: [Resources: Courses, Books, Newsletters, Podcasts and Communities](appendices/E-resources.md)
- Appendix F: [The Advanced Shelf](appendices/F-advanced-shelf.md)
- [Glossary](GLOSSARY.md) (generated)

## How it was made

1. **Research.** Ten research agents mapped every area of AI (foundations, machine learning and data, deep learning, large language models, building with AI, compute and chips, data centers and energy, the branches of AI, safety and policy, careers and opportunity), checking 2025–2026 facts against sources.
2. **Outline.** The findings became a 66-chapter outline with a brief for every chapter (`planning/OUTLINE.md`) and a house style (`planning/STYLE.md`).
3. **Writing.** Writer agents drafted two chapters each from the research, then validated every diagram and checked every chapter against the style rules.
4. **Editing.** One editor per Part re-checked worked calculations, facts, cross-references and consistency across chapters, and hedged anything the research could not confirm.
5. **Coverage audit.** Every one of the 832 topics in the research topic maps (including every skill and every role) was traced to the chapter that teaches it. 819 were already fully taught, 13 were thin and none were missing; the 13 were filled. The per-topic tables are in `planning/coverage/`.
6. **Beginner read-through.** A reader-test pass through ten chapters across the difficulty range, from the point of view of someone with no computer-science background, fixed 65 places where that reader would get lost (`planning/coverage/reader-test.md`).
7. **External-standard audit.** The book was then checked against 15 outside references: Russell & Norvig's *Artificial Intelligence: A Modern Approach*, the ACM/IEEE CS2023 AI curriculum, Goodfellow et al.'s *Deep Learning*, *Dive into Deep Learning*, Stanford CS229, CS231n, CS224n and CS336, Chip Huyen's *AI Engineering* and *Designing Machine Learning Systems*, the Hugging Face LLM and Agents courses, Full Stack Deep Learning, *The Datacenter as a Computer*, Hennessy & Patterson on domain-specific architectures, *How to Scale Your Model*, Hendrycks' *AI Safety, Ethics, and Society*, BlueDot's alignment course and the EU AI Act. Of 878 topics, 819 are in scope for this reader (the rest are graduate-level mathematics, named where the reader will meet them). The book taught 541 of the 819 before the audit and teaches all 819 after it. Per-standard tables are in `planning/coverage/external-*.md`.
8. **Verified online.** With web access, every one of those tables of contents was checked against the real published contents and syllabi (including newer editions such as the free 4th edition of *The Data Center as a Computer* and the 2026 Stanford course pages). Topics the first audit had missed were added and taught; the book now covers every in-scope topic of every standard, and every topic judged out of scope is explained in plain words in Appendix F, The Advanced Shelf.
9. **Fact-check against current sources.** Ten fact-checkers, one per Part plus the appendices, checked about 1,200 time-sensitive claims (models, prices, chips, data-center projects, laws, people) against primary sources as of October 2026: about 115 were corrected, about 50 recent developments were added, and claims that only the press supports are marked "reported". Every web link was checked (`planning/coverage/freshness-*.md`). A consistency sweep then made every corrected fact read the same in every chapter (`planning/coverage/consistency-sweep.md`).
10. **Real readers' questions.** 528 questions that people actually ask online (help centers, forums, Hacker News, Stack Exchange, Quora) were checked against the book. It fully answered 421 before and 506 after; the rest are partly answered or depend on facts no primary source settles (`planning/coverage/questions-*.md`).
11. **Every chapter read as a beginner.** Every chapter and appendix was read start to finish from the reader's point of view, fixing about 1,000 places where that reader would get lost, including defining every abbreviation and company name at first use, and testing the exercises (`planning/coverage/reader-test-*.md`, `earliest-use.md`, `code-tests.md`). Every term defined in more than one chapter was checked so the glossary never merges two different meanings (`definitions-*.md`).
12. **Adversarial review.** Everything added in steps 8 to 11 was reviewed twice more, once for facts and arithmetic and once for clarity and integrity, by reviewers told to assume each passage was wrong until checked: about 3,000 passages, about 260 problems fixed (`planning/coverage/adversarial-review.md`). A final completeness critic re-read every report and closed what was still open.

Facts about fast-moving areas (models, chips, data centers, prices, law) reflect sources available on October 23, 2026 and will date. Figures from secondary sources are marked as reported; check the Going deeper lists for primary sources.

## Rebuilding the web version

```bash
cd ai-book/build
npm install                       # mermaid-cli, used to draw the diagrams
python3 gen_extra_terms.py ../planning/research ..   # optional: research glossary terms (needs the research files)
python3 check.py ..               # style checks for every chapter
python3 build.py .. ../site       # writes site/index.html, p1.html ... p10.html, reference, glossary, exercises
```

Needs Python 3, pandoc and Node.js. Set `CHROME_PATH` if Puppeteer cannot find a Chromium to render diagrams with.
