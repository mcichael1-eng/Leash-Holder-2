# Coverage report: 01-foundations.md (topic map, section 1)

Audited October 21, 2026 against `ai-book/chapters/`. Each of the 86 items was located by searching for its key terms and every named sub-item, then reading the passage. "COVERED" means explained at beginner level, not just mentioned.

| Item | Status before | Where covered (chapter and section) | Action taken |
|---|---|---|---|
| A1. AI as a goal, not a single thing (rules, statistics, learning) | COVERED | Ch 1 "What is AI? A definition that actually works" (goal definition, many approaches, "medicine" analogy, AI effect) | None |
| A2. Your chatbot as the running example | COVERED | Ch 1 "Start with what you already know" (the one-paragraph answer unpacked phrase by phrase, "How much math is in one answer?"); Ch 1 "What happens when you press Enter: the first look" | None |
| A3. Three ways to make a computer do something (spam filter) | COVERED | Ch 1 "Three ways to make a computer do something" (Way 1 rules, Way 2 learned word scores worked, Way 3 feedback/RL/RLHF) | None |
| B4. Big numbers (thousand to quintillion; seconds) | COVERED | Ch 2 "Big numbers, made concrete with time" (table to quintillion; 11.6 days, 31.7 years, 31,700 years; Figure 2.1) | None |
| B5. Powers of ten and scientific notation | COVERED | Ch 2 "Powers of ten and scientific notation" (exponent counts zeros, 2 × 10^25, adding exponents) | None |
| B6. Metric prefixes | COVERED | Ch 2 "Metric prefixes" (kilo to exa, milli/micro/nano, AI-example table) | None |
| B7. Orders of magnitude and estimation | COVERED | Ch 2 "Estimation: is it closer to a thousand or a million?" (Fermi estimate worked: your chat text vs Llama 3 data) | None |
| B8. Rates | COVERED | Ch 2 "Rates: per second, per token, per watt, per dollar" (speed, price, energy examples) | None |
| C9. Bits | COVERED | Ch 2 "Bits: the atoms of information" (doubling table to 64 bits, light-switch analogy) | None |
| C10. Binary counting | COVERED | Ch 2 "Counting in binary" (0 to 15 on four switches, converting 41, adding in binary) | None |
| C11. Bytes and file sizes (1000 vs 1024) | COVERED | Ch 2 "Bytes and file sizes" (KB to TB, size table, 140 GB model, "two small traps") | None |
| C12. Text as numbers (ASCII, Unicode, UTF-8) | COVERED | Ch 3 "Text as numbers" (ASCII, Unicode, UTF-8, tokens preview); Ch 2 Figure 2.2 (A = 65) | None |
| C13. Images as numbers | COVERED | Ch 3 "Images as numbers" (pixels, RGB 0–255, resolution, width × height × 3 worked) | None |
| C14. Audio as numbers | COVERED | Ch 3 "Audio as numbers" (sampling, 44,100 per second, bit depth) | None |
| C15. Video as numbers | COVERED | Ch 3 "Video as numbers" (frames per second, per-frame bytes worked) | None |
| C16. Files and formats | COVERED | Ch 3 "Files and formats" (named sequence of bytes, format table incl. .pdf/.csv/.json, file signatures) | None |
| C17. Compression (lossless, lossy, "a model is a compressed summary" with care) | COVERED | Ch 3 "Compression: making data smaller" and "Is a language model a compressed copy of the internet?" | None |
| C18. Everything becomes numbers | COVERED | Ch 3 "The big idea: everything becomes numbers"; "From characters to tokens: a preview"; "Putting it together" | None |
| D19. Transistors (B200 208 billion, "3 nm" is marketing) | COVERED | Ch 2 "Transistors: switches with no moving parts" (Watch out on node names); manufacturing in Ch 36 | None |
| D20. Logic gates and the adder | COVERED | Ch 2 "Logic gates: making decisions with switches" (truth table, everyday examples, series/parallel); "From gates to arithmetic: building an adder by hand" | None |
| D21. The CPU (fetch-decode-execute, clock, cores, ALU) | COVERED | Ch 2 "The clock", "The processor: how a CPU runs a program", "The fetch–decode–execute loop", "Cores" | None |
| D22. Memory (RAM), desk vs filing cabinet | COVERED | Ch 2 "Memory and storage: the desk and the filing cabinet" | None |
| D23. Storage and the memory hierarchy | COVERED | Ch 2 same section (latency table from registers to network, Figure 2.10) | None |
| D24. The GPU, TPUs and accelerators, HBM | COVERED | Ch 2 "GPUs and accelerators: thousands of simple workers" (TPU, accelerator definitions); HBM defined in "Moving data costs more than doing math" | None |
| D25. Moving data costs more than math (memory wall) | COVERED | Ch 2 "Moving data costs more than doing math" and "Why your chatbot types at the speed it does" | None |
| D26. Power and heat | COVERED | Ch 2 "Power and heat" | None |
| D27. Measuring compute (FLOP, FLOP/s, exaflop) | COVERED | Ch 2 "Measuring compute: FLOP and FLOP/s" with "Two worked examples" | None |
| E28. Programs and instructions | COVERED | Ch 3 "Programs: recipes for a very literal cook" | None |
| E29. Algorithms (sorting, binary search, efficiency) | COVERED | Ch 3 "Algorithms: methods that solve problems" (dictionary binary search, selection vs merge sort worked, Figure 3.8) | None |
| E30. Code and languages (machine code, assembly, compiler vs interpreter) | COVERED | Ch 3 "Code and programming languages" (Figure 3.9 ladder, compiler/interpreter definitions) | None |
| E31. Python concepts (variables, types, if/loops, functions, import, errors, notebooks, key libraries) | COVERED | Ch 3 "Why Python runs AI"; "Reading Python: a ten-minute tour" (all sub-items with code); library list incl. NumPy, pandas, PyTorch, JAX, Hugging Face | None |
| E32. Bugs and debugging | COVERED | Ch 3 "Bugs and debugging" (reading a traceback, asking a chatbot to fix code) | None |
| E33. Operating systems | COVERED | Ch 3 "Operating systems: the building manager" (Windows, macOS, Linux, Android, iOS; servers run Linux) | None |
| E34. Apps and the stack | COVERED | Ch 3 "The app stack: from chip to chat" (front end vs back end, Figure 3.11) | None |
| E35. Open source, licenses, Git/GitHub, open weights, OSI Open Source AI Definition 1.0 | COVERED | Ch 3 "Open source, licenses and open weights"; "Git and GitHub: tracking every change" | None |
| E36. Data and databases (tables, CSV, JSON) | COVERED | Ch 3 "Data: tables, CSV, JSON and databases"; depth in Ch 11 | None |
| F37. Networks, the internet, packets, physical media | COVERED | Ch 4 "Networks and the internet", "Packets: big messages in small pieces", "The physical internet: radio, copper, glass and the ocean floor" | None |
| F38. IP addresses and DNS | COVERED | Ch 4 "Addresses and names: IP and DNS" | None |
| F39. The web, HTTP/HTTPS, status codes | COVERED | Ch 4 "The web's language: URLs, HTTP and status codes"; "HTTPS and encryption: the locked briefcase" | None |
| F40. Clients and servers | COVERED | Ch 4 "Clients and servers" | None |
| F41. Data centers | COVERED | Ch 4 "Data centers: where the servers live"; depth in Part VII | None |
| F42. The cloud and hyperscalers | COVERED | Ch 4 "The cloud and the hyperscalers" (AWS, Azure, Google Cloud; renting GPUs by the hour worked) | None |
| F43. APIs (keys, JSON, per-million-token pricing, rate limits) | COVERED | Ch 4 "APIs: how programs order from each other"; depth in Ch 26 | None |
| F44. Latency and bandwidth | COVERED | Ch 4 "Latency and bandwidth"; definitions also in Ch 2 | None |
| G45. End-to-end journey of one chatbot message (12 steps) | COVERED | Ch 4 "The journey of one chatbot message" (Figure 4.12 sequence diagram, steps 1–12, "The budget of one message"); revisited in Ch 44 | None |
| H46. Functions | COVERED | Ch 5 "Functions: machines that turn inputs into outputs" (function machine, knobs/parameters, chatbot as one function) | None |
| H47. Graphs, coordinates, slope, fitting a line | COVERED | Ch 5 "Graphs, slopes and fitting a line" | None |
| H48. Vectors and dimension | COVERED | Ch 5 "Vectors: lists of numbers that describe things" | None |
| H49. Embeddings preview (king − man + woman) | COVERED | Ch 5 "Embeddings: meaning as a location" | None |
| H50. Dot product and cosine similarity | COVERED | Ch 5 "The dot product: the most important calculation in this book"; "Cosine similarity" (both worked by hand) | None |
| H51. Matrices | COVERED | Ch 5 "Matrices: tables of numbers" | None |
| H52. Matrix-vector and matrix-matrix multiplication, m·n·p cost | COVERED | Ch 5 "Matrix multiplication: many dot products at once" (row times column, shape rule, counting the cost) | None |
| H53. Tensors | COVERED | Ch 5 "Tensors: stacks of matrices" | None |
| H54. Why AI is mostly multiplying tables; 2N and 6ND | COVERED | Ch 5 "Why AI is mostly multiplying big tables of numbers"; "Counting the cost: two rules of thumb that size the AI industry" | None |
| H55. Number precision, quantization, memory math | COVERED | Ch 5 "Number precision" (floating point, precision ladder FP32 to FP4, "Memory math: how big is a model?") | None |
| H56. Exponentials (doubling, compound interest, 5× per year = 3,125×, decay) | THIN | Ch 6 "Exponentials: repeated multiplication" covered doubling, 3,125× and decay, but compound interest was absent | Added a compound-interest paragraph in Ch 6 "Powers and doubling" ($1,000 at 7% worked to 10 and 30 years vs simple interest; rule of 72), a "Compound interest" definition and key term |
| H57. Logarithms (log scales, log-log plots, log-probabilities) | COVERED | Ch 6 "Logarithms: counting the multiplications" (log scales, log-log plots and scaling laws); log-probability in "Chaining probabilities for a whole sentence" | None |
| H58. Probability basics (complements, independence, and/or rules) | COVERED | Ch 6 "Probability: a number between 0 and 1" ("The three rules you need") | None |
| H59. Probability distributions | COVERED | Ch 6 "Probability distributions: the shape of uncertainty" | None |
| H60. Sampling, temperature, top-p | COVERED | Ch 6 "Sampling and temperature" (drawing from the bag, temperature, top-p) | None |
| H61. Softmax | COVERED | Ch 6 "Softmax: turning scores into probabilities" (worked with three numbers) | None |
| H62. Conditional probability, P(next token given everything so far) | COVERED | Ch 6 "Conditional probability: the heart of every chatbot" (incl. a counting language model) | None |
| H63. Bayes' rule with natural frequencies | COVERED | Ch 6 "Bayes' rule: updating beliefs with evidence" (1,000-person medical test, about 9%) | None |
| H64. Descriptive statistics (mean, median, mode, range, variance, SD, percentiles, outliers) | THIN | Ch 6 "Descriptive statistics" covered everything except the range | Added a range paragraph with a worked class-scores example and the outlier caveat, plus a "Range (statistics)" definition and key term, in Ch 6 "Spread: variance and standard deviation" |
| H65. Normal distribution, noise, random starting weights | COVERED | Ch 6 "The normal distribution, noise and random starts" | None |
| H66. Correlation vs causation, sample bias, overfitting, splits | COVERED | Ch 6 "Correlation, causation and honest testing"; depth in Ch 9 | None |
| H67. Rates of change and the derivative | COVERED | Ch 6 "Slopes and derivatives: how much does the output move?" | None |
| H68. Partial derivatives and the gradient | COVERED | Ch 6 "Gradients: slopes for many knobs at once" | None |
| H69. The chain rule and backpropagation | COVERED | Ch 6 "The chain rule: gears turning gears" (gears, backpropagation) | None |
| H70. Loss functions and cross-entropy | COVERED | Ch 6 "Loss functions: one number for 'how wrong'" (cross-entropy as surprise, perplexity) | None |
| H71. Gradient descent (learning rate, SGD, local minima, plateaus, Adam) | COVERED | Ch 6 "Gradient descent: walking downhill in fog" ("Choosing the step size", "Valleys, plateaus and smarter walkers") | None |
| H72. The training loop; inference | COVERED | Ch 6 "The training loop: putting it all together" | None |
| I73. Pre-history 1830s–1940s | COVERED | Ch 7 "Era 1: Dreams of thinking machines (1843–1949)" (Lovelace, Turing 1936, McCulloch–Pitts, ENIAC/von Neumann, transistor, Shannon) | None |
| I74. Birth of the field 1950–1956 | COVERED | Ch 7 "Era 2": "'Can machines think?' (1950)", "Dartmouth, 1956: the field gets its name" (Logic Theorist) | None |
| I75. Early optimism and symbolic AI | COVERED | Ch 7 "The perceptron: a machine that learns", "Checkers, ELIZA and Shakey"; Lisp in Figure timeline | None |
| I76. First AI winter | COVERED | Ch 7 "Era 3: The first AI winter" (Perceptrons 1969, Lighthill 1973, funding cuts) | None |
| I77. Expert systems boom | COVERED | Ch 7 "Era 4": "'Knowledge is power': expert systems" (MYCIN, XCON, Fifth Generation, Lisp machine collapse) | None |
| I78. Second AI winter | COVERED | Ch 7 "Why the boom collapsed (1987–1993)" | None |
| I79. Connectionism continues (backprop 1986, LeNet, LSTM) | COVERED | Ch 7 "Meanwhile, the neural network idea comes back" | None |
| I80. Statistical ML era (spam, recommenders, SVMs, search, Deep Blue) | COVERED | Ch 7 "Era 5": "The statistical turn", "Games as yardsticks" | None |
| I81. Ingredients 2006–2011 | COVERED | Ch 7 "The ingredients arrive (2006–2011)" (deep belief nets, CUDA, ImageNet, Watson, Siri) | None |
| I82. Deep learning boom 2012–2016 | COVERED | Ch 7 "Era 6" (AlexNet, word2vec, DeepMind purchase, GANs, ResNet, OpenAI, TensorFlow/PyTorch, AlphaGo) | None |
| I83. Transformer and scaling era 2017–2022 | COVERED | Ch 7 "Era 7" (Transformer, GPT/BERT, Bitter Lesson, scaling laws and GPT-3, AlphaFold 2, Copilot, DALL·E/Stable Diffusion, InstructGPT, ChatGPT) | None |
| I84. Chatbot era 2023–2024 | COVERED | Ch 7 "Era 8" (GPT-4 and Claude on March 14, 2023, Llama, Gemini, GPT-4o, long context, Nobel Prizes); computer use and MCP in Era 9 | None |
| I85. Reasoning and agents era | COVERED | Ch 7 "Era 9" (o1, DeepSeek-R1, Operator, Claude Code, ChatGPT agent, Atlas, IMO gold, GPT-5) and "Era 10" (2026 models, Mythos, Astra, gigawatt campuses) | None |
| I86. Patterns in the history | COVERED | Ch 7 "The patterns: what 180 years of AI history teach" (hype cycles, hardware plus data jumps, the Bitter Lesson, questions to carry forward) | None |

**Summary.** Of the 86 topic-map items, 84 were already COVERED, 2 were THIN and none were MISSING. Part I of the book (Chapters 1–7) follows this research file almost item for item, with worked numbers for nearly every concept, so the only gaps were two named sub-items inside otherwise complete sections: compound interest (H56) and the range as a measure of spread (H64). Both were filled in Chapter 6 with short, worked, beginner-level paragraphs, two new definition callouts in the exact STYLE.md format ("Compound interest", "Range (statistics)") and matching entries in the chapter's Key terms list. Two minor stylistic differences were left as they are because the idea is fully taught: the logic-gate section uses vault, badge-door and hallway-light examples instead of doorbell/alarm ones, and the algorithms section mentions GPS only in passing. Chapter 6 passes validate.py (all diagrams valid) and check.py.
