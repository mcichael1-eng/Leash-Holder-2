# 01 — Foundations: Computing, Math for AI, and the History of AI

Research notes for *Everything About AI: From Zero to the Frontier*. Reader profile: near-zero computer-science background, but a daily chatbot user for over a year. The chatbot they already use (ChatGPT, Claude, Gemini) should be the running example. Each new idea gets tied back to "what is happening when I type a message and get an answer".

Date of research: October 21, 2026. Time-sensitive facts are sourced in Section 4. Items seen only on a Wikipedia page flagged for factual verification were left out.

---

## 1. Topic map (teaching order, simplest to most advanced)

### Part A — Orientation: what we mean by "AI"
1. **AI as a goal, not a single thing.** Define artificial intelligence as "getting machines to do things that need intelligence when people do them". Explain that the field has tried many approaches: hand-written rules, statistics, and learning from data.
2. **Your chatbot as the running example.** A chatbot is a program running on computers in a distant building. It turns your text into numbers, does trillions of multiplications, and turns the result back into text. The rest of the foundations part explains each word in that sentence.
3. **Three ways to make a computer do something.**
   - *Rules:* a person writes every step.
   - *Learning:* the machine adjusts itself from examples.
   - *Learning plus feedback:* the machine also learns from rewards or ratings.
   Use a spam filter as the example for all three.

### Part B — Numbers and scale (taught early because everything uses it)
4. **Big numbers.** Cover thousand, million, billion, trillion, quadrillion, and quintillion. Use time to make them concrete: a million seconds is about 11.6 days, a billion seconds about 31.7 years, a trillion seconds about 31,700 years.
5. **Powers of ten and scientific notation.** 10³, 10⁶, 10⁹, 10¹², and how to read 2×10²⁵. Explain that the exponent counts the zeros.
6. **Metric prefixes.** Kilo, mega, giga, tera, peta, exa, plus milli, micro, and nano for small things. They come back later in gigabytes, teraflops, nanometers, milliseconds, and gigawatts.
7. **Orders of magnitude and rough estimation.** "Is it closer to a thousand or a million?" Teach estimation as a core AI-literacy skill.
8. **Rates.** Per second, per token, per watt, per dollar. AI costs and speeds are almost always given as rates.

### Part C — Information as numbers
9. **Bits.** A bit is one yes/no or on/off choice. Two bits give 4 combinations, 8 bits give 256. Each extra bit doubles the possibilities.
10. **Binary counting.** Count to 15 on four "light switches". Place value in base 2 compared with base 10.
11. **Bytes and file sizes.** 8 bits make a byte. Then KB, MB, GB, and TB. Explain the 1000 vs 1024 confusion briefly.
12. **Text as numbers.** Characters map to numbers: ASCII ("A" = 65), then Unicode and UTF-8 for every language and for emoji. A text file is a list of numbers.
13. **Images as numbers.** A picture is a grid of pixels, and each pixel holds three numbers (red, green, blue), each from 0 to 255. Resolution is the number of pixels. Uncompressed size is width × height × 3 bytes.
14. **Audio as numbers.** Sound is a wave that gets measured thousands of times per second (sampling). CD quality is 44,100 samples per second. Bit depth sets how precise each measurement is.
15. **Video as numbers.** A video is a sequence of images (frames per second) plus audio.
16. **Files and formats.** A file is a named sequence of bytes. The format (.txt, .jpg, .png, .mp3, .mp4, .pdf, .csv, .json) is an agreement about what the bytes mean.
17. **Compression.** Lossless compression (zip, PNG) loses nothing. Lossy compression (JPEG, MP3) throws away detail people barely notice. Link this to the idea that "a model is a compressed summary of its training data", with care, since that is only partly true.
18. **Everything becomes numbers, so AI can handle any medium.** This sets up tokens, embeddings, and multimodal models.

### Part D — The physical computer
19. **Transistors.** A transistor is a tiny electrically controlled switch: the same on/off idea as a bit, but physical. Today's chips hold tens to hundreds of billions of them; Nvidia's B200 package has 208 billion. Explain manufacturing scale and that "3 nm" is a marketing name, not a literal size.
20. **Logic gates.** AND, OR, and NOT, built from a few transistors. Use doorbell, light-switch, and alarm-system examples. Show that gates combine into an adder, so arithmetic is just arranged switches.
21. **The CPU.** The CPU is the general-purpose "brain": it fetches an instruction, decodes it, executes it, and repeats. Cover clock speed (gigahertz means billions of ticks per second), cores, and the arithmetic logic unit.
22. **Memory (RAM).** Fast working space that is wiped when the power goes off. Use the desk-versus-filing-cabinet analogy.
23. **Storage (SSD and HDD).** Slow but permanent. Introduce the memory hierarchy (registers, cache, RAM, SSD, network) with rough speeds that differ by factors of thousands.
24. **The GPU.** Thousands of simple cores doing the same math in parallel. It was built for video-game graphics and turned out to be perfect for AI. Specialized AI chips (TPUs and other accelerators) belong here too. Introduce high-bandwidth memory (HBM).
25. **Moving data costs more than math.** The "memory wall": chips can often compute faster than they can be fed data. This matters for why chatbots stream text at the speed they do.
26. **Power and heat.** Every operation uses energy and makes heat. That is why data centers need power plants and cooling, which bridges to the compute and data center chapter.
27. **Measuring compute.** FLOP means one floating-point operation (one multiply or add). FLOP/s measures speed. Scale runs from teraflops to exaflops, where an exaflop is 10¹⁸ operations per second.

### Part E — Software
28. **Programs and instructions.** A program is a precise recipe that a computer follows literally. Computers do exactly what they are told, not what you meant.
29. **Algorithms.** An algorithm is a step-by-step method for solving a problem, independent of any language. Examples: sorting a deck of cards, looking up a word in a dictionary by halving (binary search), following GPS directions. Mention efficiency, the idea that some methods take far fewer steps.
30. **Code and programming languages.** Code is human-readable instructions. Cover the ladder from machine code to assembly to high-level languages. A compiler translates a whole program ahead of time; an interpreter translates as it goes.
31. **Python at a conceptual level.** Why Python dominates AI: readable, a huge library ecosystem, and it calls fast C/C++/CUDA code underneath. Concepts to cover:
   - variables
   - data types (integers, decimals/floats, text strings, booleans, lists, dictionaries)
   - `if` statements and loops
   - functions
   - libraries and `import`
   - errors and tracebacks
   - notebooks (Jupyter, Google Colab)
   Mention the key AI libraries by name only: NumPy, pandas, PyTorch, JAX, Hugging Face Transformers.
32. **Bugs and debugging.** Errors are normal. Teach how to read an error message and how to ask a chatbot to help fix code.
33. **Operating systems.** The OS is the "building manager" that shares the CPU, memory, files, and devices among apps. Cover Windows, macOS, Linux, Android, and iOS. Note that almost all servers and supercomputers run Linux.
34. **Apps and the stack.** Hardware, then OS, then libraries, then apps. Your chatbot app is a thin "front end"; the real work happens elsewhere.
35. **Open source.** Code anyone can read, use, and modify under a license (MIT, Apache 2.0, GPL). Introduce GitHub and version control (Git). Distinguish open-source code from **open-weight** AI models: the weights are downloadable, but the training data and code often are not. Mention the Open Source Initiative's Open Source AI Definition 1.0 (October 2024).
36. **Data and databases.** Tables, rows and columns, spreadsheets as a gateway, CSV and JSON. Datasets are the raw material of AI.

### Part F — Networks, the internet, and the cloud
37. **Networks and the internet.** A network is connected computers; the internet is a network of networks. Data travels as small **packets** over copper, fiber optic, radio, and undersea cables.
38. **Addresses and names.** IP addresses are the numeric addresses. DNS is the phone book that turns `claude.ai` into an IP address.
39. **The web and HTTP/HTTPS.** Cover browsers, URLs, requests and responses, and status codes (200, 404, 500). HTTPS encryption is a padlock that only the endpoints can open.
40. **Clients and servers.** Your phone is the client. A server is a computer that waits for requests. A server is just a computer without a screen, sitting in a rack.
41. **Data centers.** Buildings full of servers, networking, power, and cooling. AI data centers are packed with GPUs and are now measured in megawatts and gigawatts. Hand off to the compute chapter.
42. **The cloud.** "Someone else's computer, rented by the minute." Cover the hyperscalers (AWS, Microsoft Azure, Google Cloud) and the difference between paying per hour and buying hardware.
43. **APIs.** An Application Programming Interface is the menu and waiter that let one program ask another for something. Cover API keys, JSON requests, pricing per million tokens, and rate limits. Chatbot apps and AI agents are built on APIs.
44. **Latency and bandwidth.** Latency is how long the trip takes; bandwidth is how much fits through the pipe. Explain why the first word takes a moment to appear and the rest then streams.

### Part G — Capstone: how a chatbot request travels
45. **End-to-end journey.** Follow one message:
    1. You type and tap send.
    2. The app packages the conversation into an HTTPS request.
    3. DNS lookup.
    4. Encrypted packets travel through the cell tower or Wi-Fi, the internet service provider, and the internet backbone.
    5. The request reaches the provider's edge and load balancer.
    6. The API gateway checks your account, rate limits, and safety filters.
    7. The text is tokenized.
    8. The request is scheduled onto a GPU server.
    9. "Prefill" reads the whole conversation; "decode" then generates one token at a time, keeping a KV cache.
    10. The model may call tools (search, code) along the way.
    11. Tokens stream back and are turned into text on your screen.
    12. The conversation is saved to storage.
    Total time: about a second to the first word, then tens of tokens per second.

### Part H — The math needed for AI (intuitive, no proofs)
46. **Functions.** A function is a machine that turns an input into an output, like f(x) = 2x + 1. An AI model is one giant function: text in, probabilities for the next token out. Introduce inputs, outputs, and parameters (the adjustable knobs).
47. **Graphs, coordinates, and lines.** Points on a grid, the slope of a line as "rise over run", and fitting a line to data points. This is the simplest "machine learning".
48. **Vectors.** A vector is an ordered list of numbers. It can be read as a point or an arrow in space, or as a description (a house as [bedrooms, size, age, price]). Its **dimension** is how many numbers it has. You can picture 2D and 3D; 4,096 dimensions works the same way but can't be pictured.
49. **Embeddings (preview).** Words, images, and users become vectors where similar things sit close together. The classic example: king − man + woman ≈ queen.
50. **The dot product.** Multiply matching entries and add them up. Read it as a "compatibility score" or "weighted vote". Cosine similarity is a dot product scaled to ignore length. This is the heart of attention and of search.
51. **Matrices.** A matrix is a table (grid) of numbers. Its shape is rows × columns. It can hold a dataset (rows are examples, columns are features) or a transformation that turns one vector into another.
52. **Matrix-vector and matrix-matrix multiplication.** Each output number is a dot product of a row and a column. Do it by hand with 2×2 examples. Cost: (m×n) times (n×p) takes m·n·p multiply-adds. Because GPUs do this in parallel, matrix multiplication is the workhorse.
53. **Tensors.** Stacks of matrices with more than two dimensions, such as a batch of color images. "Tensor" is a fancy word for a multi-dimensional array.
54. **Why AI is mostly multiplying big tables of numbers.** A neural-network layer does three things:
    1. Multiply the input vector by a weight matrix.
    2. Add a bias.
    3. Apply a simple nonlinear "squash" (activation).
    Stack many layers. **Parameters** are all the numbers in those matrices. Rule of thumb: generating one token costs about 2 × (number of parameters) operations, and training costs about 6 × parameters × training tokens.
55. **Number precision.** Computers store decimals in fixed sizes: FP32 (4 bytes), BF16/FP16 (2), FP8 (1), FP4 (half a byte). Fewer bits means faster and cheaper but less precise. **Quantization** shrinks a model this way. Memory math: 70 billion parameters × 2 bytes = 140 GB.
56. **Exponentials.** Repeated multiplication: doubling, compound interest, and why "grows 5× per year" becomes 3,125× in five years. Also exponential decay.
57. **Logarithms.** The inverse of an exponential: "how many times do I multiply?" or "how many zeros?". Log scales on charts, why scaling-law plots are straight lines on log-log axes, and log-probabilities.
58. **Probability basics.** Probabilities run from 0 to 1. Cover events, complements, independence, and the "and"/"or" rules.
59. **Probability distributions.** A list of all outcomes with their probabilities, adding to 1, like a loaded die. A language model outputs a distribution over its vocabulary for the next token.
60. **Sampling and temperature.** Picking from the distribution, like drawing marbles from a bag. Temperature flattens or sharpens the distribution; top-p sampling is a related control. This explains why the same question gets different answers.
61. **Softmax.** Turns any list of scores into probabilities that add to 1, using exponentials. A one-paragraph intuition is enough.
62. **Conditional probability.** P(A | B) is "the probability of A given that B happened". The model computes P(next token | everything so far). This is the single most important probability idea for understanding chatbots.
63. **Bayes' rule, intuitively.** Update beliefs with evidence. Use the medical-test example with natural frequencies: out of 1,000 people, 10 sick, 9 true positives, about 89 false positives, so a positive test means only about 9% chance of being sick. Ties in to base rates and to hallucination and calibration.
64. **Descriptive statistics.** Mean, median, mode; spread (range, variance, standard deviation); percentiles. Outliers.
65. **The normal distribution and randomness.** The bell curve, noise, and why model weights start as random numbers.
66. **Correlation versus causation, bias in samples, and overfitting.** Cover training, validation, and test splits ("don't grade yourself on the answer key"), and generalization.
67. **Rates of change and slope.** Speed is the rate of change of distance. The derivative is the slope at a point: "if I nudge the input a little, how much does the output move?"
68. **Partial derivatives and the gradient.** With many knobs, the gradient is the list of slopes, one per knob. It points uphill.
69. **The chain rule, intuitively.** Effects pass through a chain of steps (gears turning gears). Backpropagation is the chain rule applied efficiently backward through layers.
70. **Loss functions.** A single number measuring "how wrong" the model is. For language models it is cross-entropy: how surprised the model was by the real next token, which is a log-probability.
71. **Optimization and gradient descent.** Walk downhill in fog by feeling the slope.
    - The learning rate is the step size: too big overshoots, too small is slow.
    - Stochastic gradient descent uses small random batches.
    - Cover local minima and plateaus. Optimizers such as Adam are smarter walkers.
72. **Putting it together.** A training loop:
    1. Predict.
    2. Measure the loss.
    3. Compute the gradients by backprop.
    4. Nudge the parameters.
    5. Repeat trillions of times.
    "Inference" is using the finished model. This bridges to the machine-learning and deep-learning chapters.

### Part I — History of AI (narrative, with dates)
73. **Pre-history (1830s–1940s).**
    - Babbage's Analytical Engine and Ada Lovelace's notes (1843).
    - Turing's 1936 paper on computable numbers (the Turing machine).
    - McCulloch and Pitts' artificial neuron (1943).
    - ENIAC and the von Neumann architecture (1945).
    - The transistor, Bell Labs (1947).
    - Shannon's information theory and the "bit" (1948).
74. **Birth of the field (1950–1956).**
    - Turing's "Computing Machinery and Intelligence" (1950) and the imitation game, now called the Turing test.
    - The Dartmouth proposal (1955) and summer workshop (1956), where John McCarthy coined "artificial intelligence".
    - The Logic Theorist (Newell, Shaw, Simon, 1956).
75. **Early optimism and symbolic AI (1956–early 1970s).**
    - Rosenblatt's perceptron (1957–58).
    - Arthur Samuel's checkers program and the phrase "machine learning" (1959).
    - Lisp (1958).
    - ELIZA (mid-1960s).
    - Shakey the robot (late 1960s).
76. **First AI winter (~1974–1980).**
    - Minsky and Papert's *Perceptrons* (1969).
    - The UK Lighthill report (1973).
    - Funding cuts.
77. **Expert systems boom (1980s).**
    - MYCIN (1970s).
    - XCON at Digital Equipment Corporation.
    - Japan's Fifth Generation project (1982).
    - The 1987 Lisp-machine market collapse.
78. **Second AI winter (~late 1980s–mid 1990s).** Brittle rule systems that were costly to maintain.
79. **Connectionism quietly continues.**
    - Backpropagation popularized by Rumelhart, Hinton, and Williams in *Nature* (1986).
    - LeCun's convolutional networks for handwritten digits (1989; LeNet-5 in 1998).
    - LSTM (1997).
80. **Statistical machine learning era (1990s–2000s).**
    - Spam filters, recommendation systems, support vector machines, and search engines.
    - Deep Blue beats Kasparov (1997).
    - The web supplies data; cheap storage arrives.
81. **Ingredients of the deep learning boom (2006–2011).**
    - Hinton's "deep belief nets" (2006).
    - Nvidia CUDA (2007) makes GPUs programmable.
    - ImageNet dataset (2009).
    - IBM Watson wins *Jeopardy!* (2011).
    - Siri (2011).
82. **The deep learning boom (2012–2016).**
    - AlexNet wins ImageNet (2012) with about half the errors of the runner-up, trained on two gaming GPUs.
    - word2vec (2013).
    - Google acquires DeepMind (2014).
    - GANs (2014).
    - ResNet (2015).
    - OpenAI founded (2015).
    - TensorFlow (2015) and PyTorch (2016).
    - AlphaGo beats Lee Sedol 4–1 (March 2016).
83. **The Transformer and the scaling era (2017–2022).**
    - "Attention Is All You Need" (June 2017).
    - GPT-1 (2018) and BERT (2018).
    - Turing Award to Bengio, Hinton, and LeCun (2018 award).
    - GPT-2 (2019).
    - Scaling laws (2020).
    - GPT-3 (2020, 175 billion parameters).
    - AlphaFold 2 (2020).
    - GitHub Copilot (2021).
    - DALL·E 2 and Stable Diffusion (2022).
    - InstructGPT/RLHF (2022).
    - ChatGPT (November 30, 2022).
84. **The chatbot era (2023–2024).**
    - GPT-4 and the first Claude (March 14, 2023).
    - Llama and the open-weight wave.
    - Gemini (December 2023).
    - Multimodal models (GPT-4o, May 2024).
    - Long context.
    - Nobel Prizes for AI pioneers (October 2024).
    - Computer use (October 2024).
    - MCP (November 2024).
85. **The reasoning and agents era (September 2024 to now).**
    - OpenAI o1 (September 12, 2024) introduced "thinking before answering".
    - DeepSeek-R1 (January 2025) showed cheap open reasoning.
    - Agents: Operator, Claude Code, ChatGPT agent, and browsers with built-in agents.
    - Math olympiad gold (July 2025).
    - GPT-5 (August 2025).
    - The Claude 4.x/5.x and GPT-5.x/6 generations in 2026, and restricted-access cyber-capable models (Claude Mythos Preview, GPT-6 Astra).
    - Gigawatt-scale data centers.
    Details are in Section 4.
86. **Patterns in the history.** Hype and winter cycles. Each boom rode a hardware jump plus a data jump. Methods that scale with compute won out over hand-built knowledge (Rich Sutton's "The Bitter Lesson", 2019). Questions to carry forward.

---

## 2. Glossary candidates (plain-English definitions)

**Numbers and scale**
1. **Thousand / million / billion / trillion**: 10³, 10⁶, 10⁹, and 10¹² (1 followed by 3, 6, 9, or 12 zeros). Each step is 1,000 times bigger than the one before.
2. **Quadrillion / quintillion**: 10¹⁵ and 10¹⁸. AI computing speeds are now counted in these units.
3. **Scientific notation**: writing a number as (a number between 1 and 10) × 10 to a power, so 2,000,000 = 2×10⁶. The exponent tells you how many places to move the decimal point.
4. **Order of magnitude**: a factor of ten. "Two orders of magnitude bigger" means about 100 times bigger.
5. **Exponent / power**: how many times a number is multiplied by itself. 2⁵ = 2×2×2×2×2 = 32.
6. **Metric prefixes**: kilo (thousand), mega (million), giga (billion), tera (trillion), peta (quadrillion), exa (quintillion). Small ones: milli (thousandth), micro (millionth), nano (billionth).

**Information and data**
7. **Bit**: the smallest unit of information, a single 0 or 1 (off or on). Every digital thing is built from bits.
8. **Byte**: 8 bits, enough to store a number from 0 to 255 or one basic character.
9. **Binary**: counting with only two digits, 0 and 1. Each place is worth double the one to its right (1, 2, 4, 8, ...).
10. **Kilobyte, megabyte, gigabyte, terabyte (KB, MB, GB, TB)**: about a thousand, a million, a billion, and a trillion bytes. A photo is a few MB; a phone holds hundreds of GB.
11. **Encoding**: an agreed rule for turning something (letters, colors, sounds) into numbers and back again.
12. **ASCII**: an early encoding with 128 characters for English letters, digits, and symbols. "A" is 65.
13. **Unicode / UTF-8**: the modern worldwide encoding that gives a number to every character in every writing system, including emoji. UTF-8 is the most common way to store those numbers as bytes.
14. **Pixel**: one tiny dot of an image, usually stored as three numbers for red, green, and blue brightness.
15. **Resolution**: how many pixels an image or screen has, such as 1920×1080. More pixels means more detail and more data.
16. **RGB**: describing a color as amounts of red, green, and blue light, each typically from 0 to 255.
17. **Sample (audio)**: one measurement of a sound wave's height. Thousands per second (the **sample rate**) recreate the sound.
18. **Frame**: one still image in a video. Videos show many frames per second.
19. **File**: a named chunk of stored bytes, such as a document, a photo, or a program.
20. **File format**: the rulebook for what a file's bytes mean (.jpg, .mp3, .pdf, .csv). The file extension hints at the format.
21. **CSV**: "comma-separated values", a plain-text table where each line is a row and commas separate the columns. Spreadsheets can open it.
22. **JSON**: a plain-text format for structured data using labels and values, like `{"name": "Ada", "age": 36}`. APIs and AI tools use it constantly.
23. **Compression**: making data smaller. Lossless compression can be undone perfectly; lossy compression throws away some detail to save more space.
24. **Metadata**: data about data, such as a photo's date, location, and camera model.
25. **Dataset**: an organized collection of examples (texts, images, labeled records) used to train or test AI.
26. **Database**: organized storage software designed to save, search, and update large amounts of data quickly.

**Hardware**
27. **Transistor**: a microscopic switch controlled by electricity, the basic building block of all chips. Modern chips contain billions.
28. **Semiconductor**: a material (mainly silicon) whose ability to carry electricity can be controlled. It is what makes transistors possible, and "semiconductor" is also the name of the chip industry.
29. **Chip / integrated circuit**: a small slice of silicon with billions of transistors and wires etched onto it.
30. **Logic gate**: a tiny circuit of a few transistors that combines on/off signals by a rule (AND, OR, NOT). Gates combine to do arithmetic.
31. **Moore's Law**: Gordon Moore's 1965 observation that the number of transistors on a chip was doubling regularly (later about every two years). It is a trend, not a law of nature, and it has slowed.
32. **CPU (central processing unit)**: the general-purpose processor that runs programs step by step. Very flexible, but does only a few things at once.
33. **Core**: one independent processing unit inside a CPU or GPU. More cores means more work done at the same time.
34. **Clock speed**: how many basic steps a processor takes per second, measured in gigahertz (billions per second).
35. **GPU (graphics processing unit)**: a processor with thousands of small cores that do the same math on lots of data at once. Built for graphics, it is now the main engine of AI.
36. **Accelerator / TPU**: chips designed specially for AI math. Google's Tensor Processing Unit is the best-known non-GPU example.
37. **Memory / RAM**: fast, temporary working space for data the processor is using right now. It is erased when the power goes off.
38. **HBM (high-bandwidth memory)**: very fast memory stacked right next to an AI chip so it can be fed numbers quickly. It is often the limiting factor for AI.
39. **Storage (SSD / hard drive)**: slower but permanent places to keep files. Data survives power-off.
40. **Cache**: a small, very fast memory that keeps recently used data close at hand so it doesn't have to be fetched again.
41. **Memory hierarchy**: the ladder from tiny, super-fast memory (registers, cache) to big, slow storage. Good programs keep the data they need near the top.
42. **Bandwidth**: how much data can be moved per second, like the width of a pipe.
43. **Latency**: how long one trip takes, from request to the start of a response.
44. **FLOP**: one floating-point operation, a single multiplication or addition of decimal numbers. Used to count how much math a job takes.
45. **FLOP/s (FLOPS)**: floating-point operations per second, a measure of computing speed. Teraflops are trillions and exaflops are quintillions per second.
46. **Server**: a computer that provides a service to other computers over a network. It usually has no screen and sits in a rack in a data center.
47. **Data center**: a building packed with servers, networking gear, power equipment, and cooling. Your chatbot runs in one.
48. **Supercomputer**: a very large group of processors connected to work on one big problem together. The biggest AI training clusters are effectively supercomputers.

**Software**
49. **Program / software**: a set of instructions a computer follows. "Software" is the general term for programs, as opposed to physical hardware.
50. **Instruction**: one basic command a processor understands, such as "add these two numbers" or "move this data".
51. **Algorithm**: a step-by-step method for solving a problem, like a recipe. It can be written in any programming language, or in plain words.
52. **Code / source code**: instructions written in a programming language that humans can read and edit.
53. **Programming language**: a precise artificial language for writing instructions, such as Python, JavaScript, or C++.
54. **Python**: a popular, readable programming language that dominates AI work, largely because of its huge collection of ready-made libraries.
55. **Machine code**: the raw binary instructions a processor actually executes.
56. **Compiler / interpreter**: tools that translate human-written code into something the machine runs. A compiler translates everything first; an interpreter translates and runs line by line.
57. **Variable**: a named box in a program that holds a value, like `price = 20`.
58. **Data type**: the kind of value something is: whole number (integer), decimal (float), text (string), true/false (boolean), list, and so on.
59. **Loop**: an instruction to repeat steps, such as "for each photo, do this".
60. **Function (programming)**: a named, reusable block of code that takes inputs and returns an output.
61. **Library / package**: ready-made code others have written that you can reuse. NumPy and PyTorch are libraries.
62. **Bug / debugging**: a bug is a mistake in code that causes wrong behavior. Debugging is finding and fixing it.
63. **Notebook (Jupyter / Google Colab)**: a document mixing text and runnable code cells. Colab runs it free in your browser on Google's computers.
64. **Operating system (OS)**: the master program (Windows, macOS, Linux, Android, iOS) that manages hardware and lets apps run and share resources.
65. **Linux**: a free, open-source operating system that runs almost all servers, supercomputers, and Android phones.
66. **App / application**: a program made for users to accomplish tasks, like a chatbot app or a web browser.
67. **Front end / back end**: the front end is what you see and touch (the app's screen). The back end is the behind-the-scenes servers doing the work.
68. **Open source**: software whose source code is published so anyone can use, study, change, and share it under a license.
69. **License**: legal terms saying what you may do with code or a model. MIT and Apache 2.0 are permissive; GPL requires sharing changes.
70. **Open-weight model**: an AI model whose trained numbers (weights) can be downloaded and run by anyone. The training data and code may stay private.
71. **Version control / Git / GitHub**: Git tracks every change to code over time. GitHub is a website for storing and collaborating on Git projects.

**Networks, internet, and cloud**
72. **Network**: computers connected so they can exchange data.
73. **Internet**: the worldwide network of networks, linked by shared rules (protocols).
74. **Protocol**: an agreed set of rules for how computers talk, like etiquette for machines. TCP/IP and HTTP are protocols.
75. **Packet**: a small chunk of data sent across a network. Big messages are split into many packets and reassembled.
76. **IP address**: a numeric address identifying a device on the internet, like a postal address.
77. **DNS (Domain Name System)**: the internet's phone book, turning names like `gemini.google.com` into IP addresses.
78. **URL**: a web address, specifying the protocol, the site, and the page.
79. **HTTP / HTTPS**: the protocol browsers and apps use to request and receive web content. HTTPS is the encrypted version.
80. **Encryption**: scrambling data so only someone with the right key can read it.
81. **Client / server**: the client asks (your phone); the server answers (a computer in a data center).
82. **Cloud computing**: renting computing power and storage over the internet instead of owning the machines.
83. **Hyperscaler**: a giant cloud provider operating huge data centers worldwide, such as Amazon Web Services, Microsoft Azure, or Google Cloud.
84. **API (Application Programming Interface)**: a defined way for one program to request services from another, like a menu and a waiter. AI companies sell model access through APIs.
85. **API key**: a secret password-like code identifying who is using an API, so they can be billed and limited.
86. **Rate limit**: a cap on how many requests you may make in a period of time.
87. **Load balancer**: a traffic director that spreads incoming requests across many servers.
88. **Streaming**: sending a response piece by piece as it is produced, which is why chatbot answers appear word by word.
89. **Bandwidth vs latency**: see entries 42 and 43. How much data, versus how long the trip takes.

**Math**
90. **Function (math)**: a rule that turns each input into an output, like f(x) = 2x + 1. An AI model is a huge function.
91. **Variable (math)**: a symbol (x, y) standing for a number that can change.
92. **Parameter**: an adjustable number inside a function or model that shapes its behavior. Modern AI models have billions to trillions of them.
93. **Weight**: the most common kind of parameter. It is a number saying how strongly one input influences an output.
94. **Bias (math)**: a parameter added after multiplying, which shifts the output up or down. Unrelated to unfair bias.
95. **Linear**: a straight-line relationship, where doubling the input doubles the effect. Built from multiplying and adding only.
96. **Nonlinear / activation function**: a bend or squash (like "replace negatives with zero") applied between layers. Without it, stacking layers would add no power.
97. **Coordinate**: a number giving a position along one direction; (3, 5) is a point on a grid.
98. **Vector**: an ordered list of numbers, such as [3, 5, 2]. It can describe a point, an arrow, or a thing's features.
99. **Dimension**: how many numbers a vector has, meaning how many directions its space has. AI uses vectors with thousands of dimensions.
100. **Embedding**: a vector that represents a word, image, or item so that similar things get similar vectors.
101. **Dot product**: multiply two vectors entry by entry and add up the results. A big result means they "point the same way".
102. **Cosine similarity**: a similarity score from −1 to 1 based on the angle between two vectors, ignoring their lengths.
103. **Matrix**: a rectangular table of numbers with rows and columns. Neural network layers are matrices.
104. **Shape**: a matrix or tensor's size, like 3×4 (3 rows, 4 columns). Shapes must match to multiply.
105. **Matrix multiplication**: combining two matrices where each output entry is the dot product of a row and a column. It is the most common operation in AI.
106. **Tensor**: a grid of numbers with any number of dimensions: a vector is 1-D, a matrix 2-D, a stack of images 4-D.
107. **Exponential growth**: growth by repeated multiplying (doubling, tripling), which starts slow and then explodes.
108. **Logarithm**: the reverse of an exponential. It answers "what power do I need?", so the log base 10 of 1,000 is 3.
109. **Log scale**: a chart axis where each step multiplies (1, 10, 100, 1,000) instead of adding. It is used to show huge ranges.
110. **Probability**: a number from 0 (impossible) to 1 (certain) measuring how likely something is.
111. **Probability distribution**: a list of every possible outcome with its probability, all adding up to 1.
112. **Random variable**: a quantity whose value depends on chance, like a die roll.
113. **Sampling**: picking an outcome at random according to a distribution. Chatbots sample each next token.
114. **Temperature**: a setting that makes sampling more predictable (low) or more varied and creative (high).
115. **Softmax**: a formula that turns any list of scores into probabilities that are positive and add to 1.
116. **Conditional probability**: the probability of something given that something else is true, written P(A | B).
117. **Bayes' rule**: a recipe for updating a belief when new evidence arrives, combining how likely the evidence is with how common the thing was to begin with (the base rate).
118. **Base rate**: how common something is before you look at any specific evidence.
119. **Independence**: two events are independent if knowing one tells you nothing about the other.
120. **Expected value**: the long-run average result if you repeated a random process many times.
121. **Mean / median / mode**: the average, the middle value, and the most common value. Three ways to describe a "typical" number.
122. **Variance / standard deviation**: how spread out numbers are around the average. Standard deviation is the square root of variance, in the original units.
123. **Normal distribution (bell curve)**: the common hump-shaped pattern where most values sit near the average and extremes are rare.
124. **Correlation**: two things tending to move together. It does not prove that one causes the other.
125. **Outlier**: a value far from the rest that can distort averages.
126. **Noise**: random variation in data that hides the true pattern.
127. **Overfitting**: when a model memorizes its training examples, including their noise, and does badly on new ones. Like memorizing an answer key.
128. **Generalization**: performing well on new, unseen examples. This is the real goal of learning.
129. **Training / validation / test set**: the data used to learn, the data used to tune choices, and the data held back for a final honest exam.
130. **Rate of change**: how fast one quantity changes as another changes, like miles per hour.
131. **Slope**: steepness of a line, "rise over run". It is positive going up and negative going down.
132. **Derivative**: the slope of a curve at one exact point. It answers "if I nudge the input a tiny bit, how much does the output change?"
133. **Partial derivative**: the slope with respect to one knob while holding all the others still.
134. **Gradient**: the list of all partial derivatives. It points in the direction of steepest increase, so going the opposite way reduces error fastest.
135. **Chain rule**: the rule for finding how a change ripples through several connected steps, by multiplying the step-by-step effects.
136. **Backpropagation (backprop)**: the efficient method for computing every parameter's gradient in a neural network, working backward from the error using the chain rule.
137. **Loss function**: a formula giving one number for how wrong the model's outputs are. Training tries to make it small.
138. **Cross-entropy**: the standard loss for language models. Roughly, it measures how surprised the model was by the correct next token.
139. **Optimization**: finding the parameter values that make something as good (or as small) as possible.
140. **Gradient descent**: optimization by repeatedly taking small steps downhill against the gradient.
141. **Learning rate**: how big each gradient-descent step is.
142. **Stochastic gradient descent / batch**: gradient descent using a small random handful (batch) of examples per step, which is faster and works well.
143. **Local minimum**: a dip that is lower than its surroundings but not the lowest point overall.
144. **Floating point**: the way computers store decimal numbers with a limited number of significant digits, like scientific notation in binary.
145. **Precision (FP32 / BF16 / FP8 / FP4)**: how many bits each number uses (32, 16, 8, or 4). Fewer bits are faster and use less memory but are less exact.
146. **Quantization**: storing a model's numbers with fewer bits to make it smaller and faster, with a small loss of accuracy.

**AI-general terms needed early**
147. **Artificial intelligence (AI)**: the field of making machines do tasks that require intelligence when humans do them.
148. **Machine learning (ML)**: making computers learn patterns from examples instead of following hand-written rules.
149. **Neural network**: a model made of layers of simple units, each computing a weighted sum plus a squash. It is loosely inspired by brain neurons, but it is really stacked matrix math.
150. **Deep learning**: machine learning using neural networks with many layers.
151. **Model**: the trained function, meaning the architecture plus all its learned parameters.
152. **Training**: the process of adjusting a model's parameters using data until it performs well.
153. **Inference**: using an already-trained model to produce outputs. Every chatbot reply is inference.
154. **Token**: a chunk of text (often part of a word) that a language model reads and writes. In English, about four characters or three-quarters of a word on average.
155. **Tokenizer**: the program that splits text into tokens and converts them to numbers (and back).
156. **Context window**: the maximum amount of text (in tokens) a model can consider at once, including the conversation so far.
157. **Large language model (LLM)**: a neural network trained on huge amounts of text to predict the next token. It is the engine inside chatbots.
158. **Transformer**: the neural network design introduced in 2017 that underlies nearly all modern chatbots. Its key ingredient is "attention".
159. **Attention**: a mechanism letting each token look at all the other tokens and decide, using dot products, which ones matter most.
160. **GPT**: "Generative Pre-trained Transformer", OpenAI's model family name. It became a generic term.
161. **Reasoning model**: a model trained to produce a long internal "thinking" process before its final answer, introduced publicly with OpenAI's o1 (September 2024).
162. **Agent**: an AI system that takes actions toward a goal over multiple steps (searching, clicking, running code), not just answering once.
163. **Hallucination**: when a model confidently states something false or made up.
164. **Symbolic AI / GOFAI**: the early approach of programming intelligence as explicit symbols and logical rules ("Good Old-Fashioned AI").
165. **Expert system**: a 1970s–80s program encoding a human expert's knowledge as if-then rules.
166. **Perceptron**: the 1950s single-layer learning machine, a single artificial neuron that learns weights from examples.
167. **AI winter**: a period when disappointment caused funding and interest in AI to collapse (roughly the mid-1970s and the late 1980s to early 1990s).
168. **Turing test**: Alan Turing's 1950 proposal to judge machine intelligence by whether a human judge can tell it apart from a person in text conversation.
169. **Benchmark**: a standard test used to compare AI systems' performance.
170. **Scaling laws**: the observed pattern that models predictably improve as you increase compute, data, and parameters together.
171. **Compute**: shorthand for the amount of computing power (or total operations) used, as in "training compute".
172. **CUDA**: Nvidia's software platform (2007) that lets programmers use GPUs for general math. It is a major reason Nvidia dominates AI.
173. **Vibe coding**: a term coined by Andrej Karpathy in February 2025 for building software by describing what you want to an AI and accepting its code, often without reading it closely. Collins Dictionary's 2025 Word of the Year.
174. **MCP (Model Context Protocol)**: an open standard introduced by Anthropic in November 2024 that lets AI apps connect to outside tools and data in a uniform way, like a USB port for AI.

---

## 3. Prerequisites and dependencies

**Core dependency chains** (A → B means "teach A before B"):

- **Big numbers and scientific notation** → file sizes (KB/MB/GB) → FLOPs and exaflops → model size and parameter counts → training compute and data-center chapters.
- **Bits** → binary counting → bytes → encoding (text, images, audio) → "everything is numbers" → tokens and embeddings.
- **Bits (on/off)** → transistors (physical switches) → logic gates → arithmetic circuits → CPU → GPU (many simple cores) → AI accelerators.
- **CPU, memory, storage** → memory hierarchy → bandwidth and latency → the memory wall → why HBM matters → why chatbots stream at the speed they do.
- **Programs and instructions** → algorithms → programming languages → Python concepts → libraries (NumPy/PyTorch) → running a model in Colab.
- **Operating systems and apps** → client/server → internet and packets → DNS/HTTP(S) → cloud and data centers → APIs → the journey of a chatbot request → agents (which are API calls in a loop).
- **Open source** → open-weight models → the open vs closed model debate (later chapter).
- **Functions** → parameters → "a model is a function with adjustable knobs" → training as knob-tuning.
- **Coordinates and graphs** → slope → line fitting (simplest ML) → derivatives → gradients → gradient descent → backpropagation.
- **Vectors** → dimensions → dot product → cosine similarity → embeddings → semantic search and RAG (later chapter) → attention (Transformer chapter).
- **Dot product** → matrix-vector multiplication → matrix multiplication → layers → neural networks → "AI is multiplying tables" → FLOP counting (2 × params per token) → GPU and compute economics.
- **Exponentials** → logarithms → log scales → scaling-law charts; and exponentials → softmax → probabilities from scores.
- **Probability basics** → distributions → sampling and temperature → "why answers vary" → conditional probability → next-token prediction → Bayes and base rates → hallucination and calibration.
- **Statistics (mean, variance)** → normal distribution → random initialization and noise → overfitting and generalization → train/test splits → benchmarks and evaluation.
- **Loss function** needs probability and logarithms (for cross-entropy) and functions. **Gradient descent** needs derivatives and the loss function. **Backprop** needs the chain rule and matrix multiplication.
- **Number precision (floating point)** needs bits/bytes and scientific notation → quantization → memory math (params × bytes) → which models fit on which devices.
- **History** can be woven in throughout, but its eras map onto concepts:
  - Perceptron needs dot product and weights.
  - The Minsky–Papert critique needs "linear vs nonlinear".
  - Backprop (1986) needs gradients.
  - AlexNet (2012) needs GPUs, datasets, and convolution (a light preview).
  - Transformer (2017) needs vectors, attention, and dot products.
  - ChatGPT (2022) needs tokens, next-token probability, and RLHF (a preview).
  - Reasoning models (2024+) need sampling and "thinking tokens".

**Recommended chapter order for this domain**
1. What AI is, with the chatbot as the example
2. Numbers and scale
3. Bits, bytes, and everything-as-numbers
4. Inside the machine: transistors to GPUs
5. Software, algorithms, and Python
6. Operating systems and open source
7. Internet, cloud, and APIs
8. The journey of a chatbot message
9. Functions and graphs
10. Vectors and dot products
11. Matrices and matrix multiplication
12. Exponentials and logs
13. Probability and sampling
14. Statistics, overfitting, and testing
15. Slopes, gradients, and the chain rule
16. Optimization and the training loop
17. History of AI, 1843–2016
18. History of AI, 2017–2026

History can alternatively go first as a motivating story, with "flash-forward" boxes.

---

## 4. Current state and key facts (2025–2026)

*Dates for 2026 are recent. Where sources disagree, both versions are given. All facts were checked on October 21, 2026.*

### 4.1 Frontier model timeline, 2024–2026

**2024**
- **Sep 12, 2024 — OpenAI o1-preview.** The first widely available "reasoning model", which spends extra computation "thinking" before answering. Epoch AI dates the reasoning-model era from September 2024. https://epoch.ai/trends
- **Oct 8–9, 2024 — Nobel Prizes.**
  - Physics went to John Hopfield and Geoffrey Hinton for foundational work on neural networks.
  - Chemistry went to David Baker, Demis Hassabis, and John Jumper (protein design and AlphaFold).
  https://www.nobelprize.org/prizes/physics/2024/summary/ and https://www.nobelprize.org/prizes/chemistry/2024/summary/
- **Oct 22, 2024 — Claude computer use (public beta).** Claude can move a cursor, click, and type. https://en.wikipedia.org/wiki/Claude_(language_model)
- **Oct 2024 — Open Source AI Definition 1.0** released by the Open Source Initiative. https://opensource.org/ai/open-source-ai-definition

**2025**
- **Jan 20, 2025 — DeepSeek-R1.** An open-weight reasoning model from China. On Jan 27, Nvidia stock fell about 17%. https://en.wikipedia.org/wiki/2025_in_artificial_intelligence , https://en.wikipedia.org/wiki/DeepSeek
- **Jan 21, 2025 — Stargate Project announced.** Up to $500B of AI infrastructure. (same source)
- **Jan 23, 2025 — OpenAI Operator.** A web-browsing agent. (same source)
- **Feb 2, 2025.** Karpathy coins "vibe coding", and OpenAI launches Deep Research. (same source)
- **Feb 24, 2025 — Claude 3.7 Sonnet and Claude Code** (a terminal coding agent). **Feb 27 — GPT-4.5.** (same source)
- **Mar 5, 2025 — Turing Award** to Andrew Barto and Richard Sutton for reinforcement learning. (same source)
- **Mar 25, 2025 — Gemini 2.5 Pro (experimental).** https://en.wikipedia.org/wiki/Google_Gemini
- **May 14, 2025 — AlphaEvolve.** DeepMind's AlphaEvolve found a way to multiply 4×4 complex matrices with 48 scalar multiplications, the first improvement on Strassen's method for that case in 56 years. This makes a great sidebar for the matrix-multiplication chapter. https://en.wikipedia.org/wiki/2025_in_artificial_intelligence
- **May 22, 2025 — Claude Opus 4 and Sonnet 4.** Claude Code generally available. https://en.wikipedia.org/wiki/Claude_(language_model)
- **Jul 9, 2025 — Nvidia reaches $4 trillion** market capitalization, the first public company to do so. **Oct 29 — $5 trillion.** https://en.wikipedia.org/wiki/2025_in_artificial_intelligence
- **Jul 10, 2025 — METR study.** Experienced open-source developers were 19% *slower* with early-2025 AI tools, a useful counterpoint for the misconceptions section. (same source)
- **Jul 19–21, 2025 — Math olympiad gold.** OpenAI and Google DeepMind models reach gold-medal standard at the International Mathematical Olympiad. (same source)
- **Aug 2, 2025 — EU AI Act** obligations for general-purpose AI model providers take effect. (same source)
- **Aug 7, 2025 — GPT-5.** A "system" with a fast model, a reasoning model, and a router that picks between them. https://en.wikipedia.org/wiki/GPT-5
- **Sep 29, 2025 — California SB 53**, the first US law addressing catastrophic risk from frontier AI. https://en.wikipedia.org/wiki/2025_in_artificial_intelligence
- **Oct 2025 — ChatGPT Atlas**, a browser with an agent mode. https://en.wikipedia.org/wiki/ChatGPT
- **Nov 2025 — new flagships.** GPT-5.1 (Nov), Gemini 3 Pro (Nov 18), Claude Opus 4.5 (Nov 24). **Dec 2025 — GPT-5.2.** Sources: ChatGPT, Google Gemini, and Claude Wikipedia pages above.
- **Nov 6, 2025 — "Vibe coding"** named Collins Word of the Year. **Nov 24 — US "Genesis Mission"** executive order for AI-driven science. https://en.wikipedia.org/wiki/2025_in_artificial_intelligence

**2026**
- **Jan 2026 — Claude Cowork** research preview (an agent for non-coding knowledge work). https://en.wikipedia.org/wiki/Claude_(language_model)
- **Feb 2026.**
  - Claude Opus 4.6 (Feb 5; added "agent teams").
  - Gemini 3 Deep Think upgrade (Feb 12).
  - Claude Sonnet 4.6 (Feb 17).
  - Gemini 3.1 Pro preview (Feb 19).
  - GPT-5.3-Codex.
  - GPT-4o retired from ChatGPT (Feb 13).
  Sources: Claude, Gemini, and ChatGPT Wikipedia pages; https://en.wikipedia.org/wiki/2026_in_artificial_intelligence
- **Feb 2026 — ChatGPT reaches about 900 million weekly active users** (up from 800M in October 2025). https://en.wikipedia.org/wiki/ChatGPT
- **Mar 2026 — GPT-5.4.** https://en.wikipedia.org/wiki/ChatGPT
- **Apr 7, 2026 — Project Glasswing and Claude Mythos Preview.** Anthropic's unreleased model, limited to defenders, found "thousands of high-severity vulnerabilities" across every major operating system and web browser. Examples include a 27-year-old OpenBSD bug and a 16-year-old FFmpeg bug that automated testing had hit five million times without catching. Partners include AWS, Apple, Google, Microsoft, Nvidia, and the Linux Foundation. This is a strong real-world example for the operating-system and open-source chapters. https://www.anthropic.com/glasswing
- **Apr 16, 2026 — Claude Opus 4.7.** **Apr 23 — GPT-5.5** (Thinking and Pro; GPT-5.5 Instant became the free default May 5). **Apr 24 — DeepSeek-V4 preview.** https://en.wikipedia.org/wiki/GPT-5.5 , https://en.wikipedia.org/wiki/DeepSeek
- **May 19, 2026 — Gemini 3.5 family** announced at Google I/O. **May 28 — Claude Opus 4.8.** **May 2026 — Nvidia Rubin** (TSMC 3 nm-class, HBM4 memory, 50 petaflops sparse FP4 versus 20 for Blackwell) enters full production, with deployment reported for September 2026. https://en.wikipedia.org/wiki/Google_Gemini , https://en.wikipedia.org/wiki/Rubin_(microarchitecture)
- **Jun 2026.**
  - Claude Mythos 5 (limited) and Claude Fable 5 (public Mythos-tier model with safety restrictions), June 9.
  - GPT-5.6.
  - Claude Sonnet 5 (June 30).
  https://en.wikipedia.org/wiki/Claude_(language_model) , https://en.wikipedia.org/wiki/ChatGPT
- **Jul 24, 2026 — Claude Opus 5.** **Jul 31 / Aug 13 — DeepSeek-V4-Flash and V4-Pro** official releases. Sources: Claude and DeepSeek Wikipedia pages.
- **Sep 3, 2026 — GPT-6 Astra unveiled.**
  - Rolled out in phases, starting with organizations in OpenAI's cybersecurity program.
  - OpenAI said it was its first model to reach its internal "Critical" cybersecurity threshold.
  - OpenAI also said it was its first pretraining run on more than 100,000 GPUs, at its Stargate site in Texas.
  - OpenAI called it a "generational leap". Treat claims that it "is AGI" as marketing or speculation; the Wikipedia article states it only conditionally.
  https://en.wikipedia.org/wiki/GPT-6 , https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html
- **Sep 15, 2026 — Claude Mythos and Fable 5.1** (Anthropic's news page date; Wikipedia lists Sep 1). **Sep 22 — Claude Opus 5.5.** **Sep 28 — Claude Sonnet 5.5.** **Oct 7 — Claude Haiku 5.5.** https://www.anthropic.com/news
- **Sep 22 or Oct 2026 — GPT-6 Sol and GPT-6 Luna.** Wikipedia says Sep 22; OpenAI's Deployment Safety Hub refers to an "October release". **Oct 7–8 — GPT-6 rolls into ChatGPT** (paid, then free). https://en.wikipedia.org/wiki/GPT-6 , https://deploymentsafety.openai.com/gpt-6-october
- **Gemini 4 (status unclear as of Oct 21, 2026).** Late-September reporting quoted DeepMind's Koray Kavukcuoglu saying Gemini 4 was in post-training and would ship well before year-end. Wikipedia's Gemini page lists a "Gemini 4 Argon" in late September or October 2026 but is internally inconsistent. Re-verify before print. https://www.infoworld.com/article/4226642/google-plans-gemini-4-release-before-year-end-2.html
- **Oct 2, 2026 — Claude Frontier Academy.** Anthropic announced $100M to train 10,000 "Frontier Deployed Engineers", a signal for Section 7. https://www.anthropic.com/news

**Writing guidance:** The release cadence is now monthly. For the book, teach the *pattern* (model families with big/medium/small tiers; "thinking" modes; restricted cyber-capable tiers; agents; open-weight challengers from China) rather than freezing a list of version numbers. A dated "as of" table works better than prose.

### 4.2 Compute and hardware numbers useful in the foundations chapters
- **Frontier training compute grows about 5× per year** since 2020 (doubling every 5.2 months). Training cost grows about 3.5× per year. https://epoch.ai/trends (updated Feb 5, 2026)
- **Hardware trends.** AI chip performance per dollar rises about 49% per year. GPU energy efficiency rises about 34% per year (doubling every 2.4 years). GPU memory bandwidth rises only about 28% per year since 2008, which is the "memory wall" made concrete. Same source.
- **Largest AI data centers.** The largest are approaching **1 gigawatt**, about enough to power a million US homes. Construction costs about **$38 billion per gigawatt** of IT power and takes about 2 years. The largest known is Colossus 2 in Memphis (Elon Musk's xAI, listed by Epoch under "SpaceXAI"), at roughly 1.1 million H100-equivalents. Meta's Hyperion is planned to reach about 3.7 million H100-equivalents by January 2028. Same source.
- **Transistors.** Nvidia Blackwell (announced Mar 18, 2024) has **208 billion transistors** across two dies of 104 billion each, on TSMC 4NP, with a B200 with 192 GB of HBM3E. The previous Hopper H100 die has 80 billion. https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)
- **TOP500 supercomputers (June 2026).**
  1. LineShine (China, Shenzhen): 2.198 exaflop/s.
  2. El Capitan (US): 1.809.
  3. Frontier (US): 1.353.
  There are five exascale systems in total; the others are Aurora and Europe's JUPITER Booster. https://top500.org/lists/top500/2026/06/
- **Data center electricity.** The IEA's *Energy and AI* (April 2025) estimated data centers used about 415 TWh in 2024, about 1.5% of world electricity, and projected about 945 TWh by 2030. https://www.iea.org/reports/energy-and-ai
- **Inference cost decline.** The 2025 Stanford AI Index reported that the cost of using a model at GPT-3.5 level fell more than 280-fold between November 2022 and October 2024. https://hai.stanford.edu/ai-index/2025-ai-index-report
- **Rules of thumb for FLOPs.** Inference costs about 2 × parameters FLOPs per token; training costs about 6 × parameters × tokens. Kaplan et al., "Scaling Laws for Neural Language Models" (2020), https://arxiv.org/abs/2001.08361
- **Training cost example.** DeepSeek-V3's technical report (Dec 2024) put its final training run at about 2.79 million H800 GPU-hours, about $5.6M at an assumed $2 per GPU-hour. This excludes research and earlier experiments, a nuance worth teaching. https://arxiv.org/abs/2412.19437

### 4.3 Software, programming, and the internet
- **Python is #1 in the TIOBE index** (October 2026, 19.23%), though down 5.23 points year over year, followed by C, C++, Java, and C#. https://www.tiobe.com/tiobe-index/
- **GitHub Octoverse 2025 (Oct 28, 2025).**
  - 180M+ developers.
  - **TypeScript overtook Python as the most-used language on GitHub in August 2025** by monthly contributors (about 2.64M vs about 2.6M).
  - Python still leads AI repositories (582k AI-tagged repos) and powers nearly half of new AI repos.
  - 4.3M+ AI-related repositories.
  - 1.1M+ public repos import an LLM SDK.
  - India has 21.9M developers (#2 globally).
  https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- **Hugging Face Hub hosts about 3.17 million models** (counter read Oct 21, 2026). https://huggingface.co/models
- **Internet access.** The ITU (2025) says almost three-quarters of the world is online and **2.2 billion people remain offline**, mostly in low- and middle-income countries. https://www.itu.int/itu-d/reports/statistics/facts-figures-2025/
- **Stanford AI Index 2026.**
  - US private AI investment was $285.9B in 2025, versus $12.4B for China.
  - Generative AI reached 53% population adoption within three years; organizational adoption is 88%.
  - The top US model led the top Chinese model by only 2.7% on Arena scores as of March 2026.
  - The US hosts 5,427 data centers.
  - Over 80% of US high school and college students use AI for schoolwork.
  https://hai.stanford.edu/ai-index/2026-ai-index-report

### 4.4 History quick-reference (pre-2024, stable facts for the timeline graphic)
| Year | Event |
|---|---|
| 1843 | Ada Lovelace's notes on Babbage's Analytical Engine |
| 1936 | Turing's "On Computable Numbers" (the Turing machine) |
| 1943 | McCulloch & Pitts artificial neuron |
| 1945 | ENIAC; von Neumann's stored-program design |
| 1947 | Transistor invented (Bell Labs) |
| 1948 | Shannon's information theory (the "bit") |
| 1950 | Turing, "Computing Machinery and Intelligence" (imitation game) |
| 1956 | Dartmouth workshop (proposal written 1955; "artificial intelligence" coined); Logic Theorist |
| 1957–58 | Rosenblatt's perceptron (Mark I Perceptron hardware) |
| 1959 | Arthur Samuel popularizes "machine learning" (checkers) |
| 1965 | Moore's observation; ELIZA built 1964–66 |
| 1969 | Minsky & Papert, *Perceptrons*; ARPANET; Shakey robot |
| 1973 | Lighthill report → first AI winter (~1974–80) |
| 1970s | MYCIN medical expert system |
| 1980–87 | Expert-system boom (XCON at DEC); Japan's Fifth Generation project (1982) |
| 1986 | Rumelhart, Hinton & Williams popularize backpropagation (*Nature*) |
| 1987–early 1990s | Lisp-machine collapse → second AI winter |
| 1989 | LeCun's convolutional network reads handwritten zip codes |
| 1991 | Python first released; Linux; World Wide Web goes public |
| 1997 | Deep Blue defeats Kasparov; LSTM published |
| 2006 | Hinton's deep belief nets; AWS cloud launches |
| 2007 | Nvidia CUDA |
| 2009 | ImageNet dataset |
| 2011 | IBM Watson wins *Jeopardy!*; Siri |
| 2012 | AlexNet wins ImageNet (about half the runner-up's error), trained on 2 GPUs |
| 2013 | word2vec |
| 2014 | GANs; Google buys DeepMind |
| 2015 | ResNet; OpenAI founded; TensorFlow open-sourced |
| 2016 | AlphaGo beats Lee Sedol 4–1 (March); PyTorch |
| 2017 | Transformer, "Attention Is All You Need" (June) |
| 2018 | GPT-1, BERT; Turing Award to Bengio, Hinton, LeCun (announced 2019) |
| 2019 | GPT-2; Sutton's "The Bitter Lesson" |
| 2020 | Scaling-laws paper; GPT-3 (175B parameters); AlphaFold 2 at CASP14 |
| 2021 | GitHub Copilot preview; DALL·E; Anthropic founded |
| 2022 | InstructGPT/RLHF; DALL·E 2; Stable Diffusion; **ChatGPT (Nov 30)** |
| 2023 | LLaMA (Feb); GPT-4 & Claude (Mar 14); Llama 2; Gemini 1.0 (Dec 6); EU AI Act political deal (Dec) |
| 2024 | Claude 3; GPT-4o (May); EU AI Act in force (Aug 1); o1 (Sep 12); Nobel Prizes; MCP (Nov) |

(History facts are standard and well documented. Sources for spot-checks: https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence , https://en.wikipedia.org/wiki/History_of_artificial_intelligence , https://arxiv.org/abs/1706.03762 for the Transformer paper.)

---

## 5. Diagram ideas (24)

1. **"Powers of Ten" ladder.** A vertical ladder from 10⁰ to 10²⁷. Each rung has a label and a real-world anchor:
   - 10³: a thousand words, a short essay.
   - 10⁶: one megapixel; a long novel's characters.
   - 10⁹: transistors in an older phone chip; a 1-billion-parameter model.
   - 10¹²: the training tokens of a modern model, about trillions.
   - 10¹⁵: a petaflop.
   - 10¹⁸: an exaflop (one second of the fastest supercomputer).
   - About 10²⁵: GPT-4-era training compute.
   - 10²⁶ and beyond: frontier training runs.
   A side column shows the matching metric prefix (kilo to exa).
2. **"Seconds to understand scale" bars.** Three horizontal bars on a log axis: 1 million seconds is 11.6 days, 1 billion seconds is 31.7 years, 1 trillion seconds is about 31,700 years. A caption ties it to "a trillion-parameter model".
3. **Binary light switches.** Eight light switches in a row, labeled with place values 128, 64, 32, 16, 8, 4, 2, 1. Switches for 64 and 1 are on, adding to 65. An arrow points to the letter "A" (ASCII 65). Below, the same 8 switches are shown as a "byte".
4. **Everything is numbers.** Four columns, each a left-to-right flow with arrows:
   - Text: "Hi!" → [72, 105, 33] → binary.
   - Image: a zoomed 4×4 pixel grid with RGB triples written in each cell.
   - Audio: a sound wave with dots at regular sample points and their heights listed as numbers.
   - Video: a stack of frames with a "30 per second" label.
   All four arrows converge on a box: "Lists of numbers that AI can process".
5. **From transistor to adder.**
   - Panel 1: a transistor drawn as a faucet (gate = handle, current = water).
   - Panel 2: an AND gate built from two switches in series, an OR gate from two in parallel, with truth tables.
   - Panel 3: gates wired into a "half adder" adding 1+1 = binary 10.
   - Panel 4: "billions of these = a chip".
6. **Anatomy of a computer (kitchen metaphor).** Labeled boxes:
   - CPU = chef, with a "clock" metronome.
   - RAM = countertop.
   - SSD = pantry.
   - GPU = a brigade of 1,000 line cooks doing the same chop.
   - Network card = delivery door.
   - Power supply and fan = stove and vent hood.
   - Arrows show ingredients (data) moving pantry → counter → chef.
7. **Memory hierarchy pyramid.** A pyramid with five tiers, labeled with rough speed and size:
   - Registers: under 1 ns, bytes.
   - Cache: about 1–10 ns, MB.
   - RAM / HBM: about 100 ns, GB.
   - SSD: about 100 µs, TB.
   - Network / other data center: milliseconds.
   One side labeled "faster, smaller, pricier"; the other "slower, bigger, cheaper". A human-scale translation runs alongside: "if a cache read took 1 second, an SSD read would take about a day".
8. **CPU vs GPU.** Left: a few big, complex cores (4–16 boxes) labeled "flexible, sequential". Right: a grid of thousands of tiny cores labeled "same operation on lots of data". Below each, a task icon: "running your web browser" versus "multiplying a 4096×4096 matrix".
9. **The software stack (layer cake).** Bottom to top: hardware (chips) → operating system → libraries (NumPy, PyTorch, CUDA) → applications (chatbot app, browser) → you. Arrows on the side say "requests go down, results come up". A callout shows where "open source" lives (most layers).
10. **Algorithm as recipe and flowchart.** A flowchart for binary search ("find a word in a dictionary"): start → open the middle → "Is the word before this page?" (diamond) → yes/no branches → repeat → found. A side note says "1,000,000 pages found in at most 20 steps".
11. **Python anatomy.** A 6-line Python snippet annotated with callouts: variable, list, loop, function, library import, and a comment. A second panel shows a Colab notebook with a text cell, a code cell, and an output cell.
12. **Internet postcard journey.** A message is split into numbered postcards (packets). Each postcard has a "from IP" and "to IP". They take different routes through router nodes on a world map, including an undersea cable, and get reassembled in order at the destination. A DNS "phone book" box translates `claude.ai` → an IP address.
13. **Client, server, cloud, API.**
    - A phone (client) sends an arrow labeled "HTTPS request (JSON)" to a box labeled "API" (drawn as a waiter with a menu).
    - The API connects to a kitchen labeled "servers in a data center (the cloud)".
    - A response arrow returns labeled "JSON response".
    - A side box shows an actual short JSON request and response.
14. **The journey of a chatbot message (centerpiece).** A horizontal swimlane diagram with lanes: Your phone | Internet | Provider edge | API gateway | GPU cluster | Storage. Numbered steps:
    1. Type and send.
    2. Encrypt (padlock).
    3. DNS.
    4. Packets cross the network.
    5. Load balancer.
    6. Authentication, rate limits, safety check.
    7. Tokenize ("Hello world" → [9906, 1917] style IDs).
    8. Queue to a GPU server.
    9. Prefill (read the whole conversation).
    10. Decode loop (one token at a time, with a circular arrow labeled "repeat ~ tens of times per second").
    11. Optional tool call (search or code sandbox).
    12. Stream tokens back.
    13. Detokenize and display.
    14. Save the conversation.
    A timing bar along the bottom: ~0.1 s network, ~0.5–2 s to first token, then streaming.
15. **A function as a machine with knobs.** A box with an input chute (x), output chute (y), and knobs labeled w and b; inside it reads "y = w·x + b". Below, a giant version: "text in → [box with 1 trillion knobs] → probabilities for the next word out".
16. **Line fitting = simplest machine learning.** A scatter plot of house size versus price with a straight line through it. The vertical gaps from points to line are drawn as red "error" segments. Labels: slope = w, intercept = b, "learning = adjusting w and b to shrink the red lines".
17. **Vectors as points and arrows.** 2D axes labeled "sweetness" and "crunchiness" with fruit plotted as points (apple, banana, carrot, candy). Arrows from the origin; similar foods cluster. An inset shows the classic king/queen/man/woman parallelogram in "embedding space", captioned "real embeddings have thousands of axes".
18. **Dot product as compatibility score.** Two vectors written as rows of colored boxes, such as your movie tastes [action 5, romance 1, comedy 4] and a movie's profile [action 4, romance 0, comedy 5]. Arrows pair matching boxes into "5×4, 1×0, 4×5", summing to 40. A second example with low overlap scores lower. Caption: "attention and search both run on this".
19. **Matrix multiplication step by step.** A 2×3 matrix times a 3×2 matrix produces a 2×2 result. One row of the first and one column of the second are highlighted in the same color, with an arrow to the single output cell they produce (a dot product). A shape rule underneath: (2×3)·(3×2) → (2×2), "inner numbers must match". A cost callout: "m·n·p multiplications".
20. **A neural network layer is a matrix multiply.** Left: the classic circles-and-lines network picture (3 inputs, 4 neurons). Right: the identical thing as input vector × weight matrix + bias → activation (a ReLU curve icon) → output vector. A double-headed arrow says "same thing". Footer: "stack 100 layers, make the matrices 10,000 wide → a large language model".
21. **Exponential vs linear growth, with a log-scale twin.** Two side-by-side charts of the same data. Left (normal axis): a line growing by +5 per year versus a curve growing ×5 per year, which rockets off the chart. Right (log axis): the exponential is now a straight line. Annotation: "this is why AI-progress charts use log scales" and "×5 per year = ×3,125 in 5 years".
22. **Next-token probability bar chart.** Prompt: "The capital of France is". A bar chart over candidate tokens: " Paris" 0.92, " the" 0.03, " a" 0.02, " located" 0.01, other 0.02. Three versions at temperature 0.2 (one giant bar), 1.0 (as shown), and 2.0 (flattened). Caption: "the model outputs a distribution; the app samples from it".
23. **Bayes with 1,000 people (icon array).** A grid of 1,000 person icons:
    - 10 colored "sick".
    - Of those, 9 are outlined "tested positive".
    - Of the 990 healthy, about 89 are also outlined "false positive".
    - A callout: "Positive test → 9 of 98 are actually sick ≈ 9%".
    Link to "why a confident-sounding answer can still be wrong".
24. **Gradient descent: hiking down in fog.** A 3D hilly "loss landscape" surface with a hiker. Small footsteps zig-zag downhill toward a valley; arrows labeled "gradient (steepest uphill)" and "step = −learning rate × gradient". Insets show "learning rate too big: bounces across the valley" and "too small: barely moves". A flag marks a "local minimum" in a smaller dip.
25. **AI history timeline with hype curve (bonus).** A horizontal timeline from 1950 to 2026 with a wavy "enthusiasm/funding" line above it: peaks (1960s, mid-1980s, 2012+, 2022+) and troughs labeled "AI winter 1 (~1974–80)" and "AI winter 2 (~1987–93)". Milestone pins underneath: Turing 1950, Dartmouth 1956, Perceptron 1958, *Perceptrons* 1969, Lighthill 1973, XCON 1980, backprop 1986, Deep Blue 1997, ImageNet 2009, AlexNet 2012, AlphaGo 2016, Transformer 2017, GPT-3 2020, ChatGPT 2022, o1 2024, GPT-5 2025, Claude 5/GPT-6 2026. A second track below shows the "ingredients": compute (transistor counts) and data (web size) rising on a log scale.

---

## 6. Practical exercises (sorted easy → hard)

1. **Big-number time travel (paper and pencil, 10 min).** Convert a million, a billion, and a trillion seconds into days and years: divide by 60, 60, 24, then 365. *Learn:* the gap between "billion" and "trillion" is enormous. Model sizes and token counts will now feel real.

2. **Ask your chatbot to be your binary tutor (chatbot, 10 min).**
   1. Write your age in binary by hand using place values 32/16/8/4/2/1.
   2. Ask a chatbot to check it.
   3. Then ask it to quiz you with five numbers.
   *Learn:* binary is just place value with 2 instead of 10; eight bits cover 0–255.

3. **Spell your name in numbers (free web tool).** Search "text to ASCII converter" or "Unicode code point lookup". Type your name, then an emoji. Note the numbers and how many bytes the emoji takes in UTF-8. *Learn:* text is stored as numbers, and some characters take more bytes than others.

4. **See tokens (free tokenizer page, 10 min).** Open OpenAI's tokenizer page (platform.openai.com/tokenizer) or any "LLM token counter".
   1. Paste a sentence and count characters versus tokens.
   2. Try a rare word, a number like 1234567, a sentence in another language, and some code.
   *Learn:* models read tokens, not letters. This explains why chatbots sometimes miscount letters, and why non-English text can cost more.

5. **A photo is a spreadsheet (phone or computer).** Zoom into a photo as far as possible until you see squares. Use any free "image color picker" website to read RGB values of three pixels. Compute the uncompressed size of your phone's photo: width × height × 3 bytes. Compare with the actual file size. *Learn:* images are grids of numbers, and compression (JPEG) saves a lot.

6. **Count your computer's parts (built-in settings).** On Windows (Settings → System → About, then Task Manager → Performance) or Mac (Apple menu → About This Mac), write down your CPU, number of cores, RAM, and storage. Watch CPU and memory usage jump while you open a heavy website. *Learn:* the abstract parts (CPU, RAM, storage) are real, measurable things on your own device.

7. **Trace the internet route (command line, 10 min).** Open Command Prompt (Windows: `tracert claude.ai`) or Terminal (Mac: `traceroute claude.ai`). Also run `nslookup chatgpt.com`. Count the hops and note the milliseconds. *Learn:* DNS turns names into IP addresses; your message hops through many routers; latency is measurable.

8. **Watch a chatbot request in your browser (DevTools, 15 min).** In Chrome, open any chatbot site, press F12, and go to the Network tab. Send a short message and find the request that streams the answer. Look at the request (your text plus settings, as JSON) and see the response arriving in pieces. *Learn:* the app is a front end talking to an API, and responses stream token by token.

9. **Ask for the same answer five times (chatbot).**
   1. Ask "Give me a one-sentence slogan for a bakery" five times in fresh chats.
   2. Then ask "What is 17 × 23?" five times.
   3. Compare the variation.
   4. Ask the chatbot to explain sampling and temperature.
   *Learn:* outputs are sampled from a probability distribution. Creative tasks vary more; well-determined answers vary little.

10. **Dot product as matchmaking (spreadsheet).**
    1. In Google Sheets, write your movie-taste vector in row 1 (action, romance, comedy, horror, documentary, each scored 0–5).
    2. Write five movie profiles in rows 2–6.
    3. Use `=SUMPRODUCT($B$1:$F$1, B2:F2)` to score each movie and sort.
    *Learn:* a dot product is a compatibility score. Recommendation systems and attention use the same operation.

11. **Matrix multiplication by hand, then check (paper, then spreadsheet).**
    1. Multiply [[1,2],[3,4]] × [[5,6],[7,8]] by hand. The answer is [[19,22],[43,50]].
    2. Verify in Sheets with `=MMULT(A1:B2, D1:E2)`.
    3. Try multiplying a 2×3 by a 2×3 and watch it fail.
    *Learn:* each output cell is a row-times-column dot product, and shapes must line up.

12. **Mean, variance, and the outlier effect (spreadsheet).** Enter 10 salaries, then add one billionaire. Compute `AVERAGE`, `MEDIAN`, and `STDEV.P` before and after. *Learn:* the mean is fragile, the median is robust, and spread matters. These are basic tools for reading AI benchmark claims.

13. **Exponential vs linear in a chart (spreadsheet).**
    1. Column A holds years 0–10.
    2. Column B is linear (+5/year): `=5*A2`.
    3. Column C is exponential (×5/year): `=5^A2`.
    4. Chart both, then switch the vertical axis to a log scale.
    *Learn:* exponentials dwarf linear growth, and a log axis turns exponential growth into a straight line, the way AI-trend charts are drawn.

14. **The medical test and Bayes (paper, chatbot check).** Using 1,000 imaginary people (prevalence 1%, test catches 90% of sick people, 9% false-positive rate), fill in a 2×2 table and compute P(sick | positive). Then ask a chatbot the same question and check whether it gets about 9%. *Learn:* base rates dominate; confidence is not correctness. Also practice checking AI math.

15. **Train an image classifier with no code (Teachable Machine, 20 min).**
    1. Go to teachablemachine.withgoogle.com and make an image project with two classes (e.g., "thumbs up" and "thumbs down") using your webcam: about 50 images each.
    2. Train it, then test it.
    3. Then deliberately train with a messy background for one class only, and see it "cheat".
    *Learn:* learning from examples, training versus testing, and how models pick up unintended shortcuts (bias and overfitting).

16. **Play with a neural network (TensorFlow Playground, 20 min).** Go to playground.tensorflow.org.
    1. Pick the circle dataset with zero hidden layers and press play: it fails, because a straight line can't separate the classes.
    2. Add one hidden layer with 4 neurons: it succeeds.
    3. Raise the learning rate to 3 and watch it go unstable.
    4. Add noise and watch the test loss versus training loss.
    *Learn:* the need for nonlinearity (the 1969 *Perceptrons* critique, live), learning rate, and overfitting.

17. **Gradient descent in a spreadsheet (spreadsheet, 30 min).** Minimize f(x) = (x − 3)². Columns:
    - step
    - x (start x = 10)
    - slope = 2*(x−3)
    - new x = x − 0.1*slope
    Fill down 30 rows and chart x. Try learning rates of 0.01, 0.5, and 1.1. *Learn:* how gradient descent walks downhill, and why the step size matters (too small is slow, too big overshoots or diverges).

18. **Run Python for the first time (Google Colab, 15 min).**
    1. Open colab.research.google.com and choose New notebook.
    2. Paste and run:
       ```python
       name = "Ada"
       numbers = [3, 1, 4, 1, 5, 9]
       print("Hello,", name)
       print("Total:", sum(numbers), "Average:", sum(numbers)/len(numbers))
       for n in numbers:
           print(n, "squared is", n*n)
       ```
    3. Change things and break it on purpose, e.g. remove a quote mark.
    4. Paste the error into a chatbot and ask what it means.
    *Learn:* variables, lists, loops, and functions in practice. Error messages are normal and readable.

19. **An image is an array (Colab).** Paste and run:
    ```python
    import numpy as np, matplotlib.pyplot as plt
    img = np.zeros((8, 8, 3), dtype=np.uint8)   # 8x8 pixels, 3 colors
    img[2:6, 2:6] = [255, 0, 0]                  # a red square
    img[0, :] = [0, 0, 255]                      # a blue top row
    print(img.shape); print(img[3, 3])
    plt.imshow(img); plt.show()
    ```
    Then change the numbers to draw your initial. *Learn:* images really are tensors of numbers with a shape (height × width × 3).

20. **Why GPUs exist: time a big matrix multiply (Colab).** Paste and run:
    ```python
    import numpy as np, time
    for n in [100, 500, 1000, 2000]:
        A = np.random.rand(n, n); B = np.random.rand(n, n)
        t = time.time(); C = A @ B; dt = time.time() - t
        print(f"{n}x{n}: {2*n**3/1e9:.1f} billion operations in {dt:.3f} s")
    ```
    Then use Runtime → Change runtime type → GPU, and repeat with PyTorch (`import torch; A = torch.rand(n, n, device="cuda")`, then `torch.cuda.synchronize()` before timing). *Learn:* matrix multiplication cost grows like n³; GPUs do it far faster. This is "AI is multiplying big tables" in action.

21. **Memory math for real models (paper or chatbot).** For models of 8B, 70B, and 405B parameters, compute memory at FP16 (2 bytes) and FP4 (0.5 bytes). Compare with your laptop's RAM and a 192 GB B200 GPU. Then compute FLOPs per generated token (≈ 2 × params) and per 1,000-token answer. *Learn:* why big models need data-center GPUs, why quantization matters, and how to sanity-check claims.

22. **Simulate probability (Colab).** Paste and run:
    ```python
    import random
    flips = [random.choice("HT") for _ in range(10000)]
    print(flips.count("H")/len(flips))
    words = ["Paris", "Lyon", "the", "a"]; probs = [0.9, 0.04, 0.04, 0.02]
    print(random.choices(words, probs, k=20))
    ```
    Change the probabilities to mimic "high temperature" (flatter numbers). *Learn:* sampling from a distribution, the law of large numbers, and why chatbots vary.

23. **Fit a line with gradient descent in code (Colab, 30 min).** Ask a chatbot: "Write a short Python program for Google Colab that creates 50 noisy points around y = 2x + 1, then uses gradient descent to learn w and b, printing the loss every 100 steps and plotting the final line." Run it, then ask the chatbot to explain each line. Change the learning rate. *Learn:* the full training loop (predict, loss, gradient, update) on the smallest possible "model".

24. **Build a tiny embedding search (Colab plus a free model, harder).** Ask a chatbot for Colab code using the `sentence-transformers` library (model `all-MiniLM-L6-v2`) to:
    1. Embed 10 sentences you write.
    2. Embed a query.
    3. Rank the sentences by cosine similarity.
    Inspect one embedding's length (384 dimensions). *Learn:* text becomes vectors, and "meaning search" is just dot products. This is a preview of RAG.

25. **Make your own AI history timeline (research project).** Using the Section 4.4 table as a skeleton, ask a chatbot to propose 10 more milestones. Then verify each date against a second source (Wikipedia or the original paper) and mark any the chatbot got wrong. Put the result into a Google Sheet timeline chart. *Learn:* the arc of AI history, and the habit of verifying AI output, especially dates.

---

## 7. Areas of opportunity

### Careers and roles where this foundational knowledge pays off
- **AI-literate professionals in every field.** People who understand tokens, probability, and costs can use AI tools more effectively and spot errors. The 2026 AI Index reports 88% organizational adoption of AI, so understanding is now a general workplace skill.
- **Forward/frontier-deployed engineers and AI solutions engineers.** These people translate between AI capabilities and business processes. Anthropic's October 2026 commitment of $100M to train 10,000 "Frontier Deployed Engineers" signals demand.
- **Data roles.** Data analyst, data engineer, data annotator/labeler, AI evaluator ("red-teamer", benchmark builder). Statistics and probability foundations transfer directly.
- **Software development with AI assistance.** Python remains the AI language (TIOBE #1; leading AI repos on GitHub). AI coding agents lower the entry barrier, and "vibe coding" makes prototypes cheap. People who understand fundamentals (APIs, data formats, debugging) can turn prototypes into reliable software.
- **Cloud and infrastructure.** Cloud engineers, site reliability engineers, and AI infrastructure and cost-optimization specialists. The memory-hierarchy, networking, and FLOP-math ideas in this domain are their daily vocabulary.
- **Data center and energy trades.** Electricians, HVAC and liquid-cooling technicians, power engineers, and construction managers. Gigawatt-scale campuses (Epoch estimates about $38B capex per GW) need large skilled workforces. There is a hand-off to the compute chapter.
- **Semiconductors.** Chip design, fabrication, packaging (HBM stacking), and supply chain. Transistor and logic-gate knowledge is the on-ramp.
- **Security.** Glasswing showed AI models finding thousands of high-severity bugs in operating systems and browsers. Defenders who understand operating systems, open source, and networking are in demand, and "AI-assisted vulnerability management" is an emerging specialty.
- **Educators, explainers, and technical writers.** Demand is high for clear AI-literacy teaching. Over 80% of US students use AI for schoolwork, yet only about half of schools have AI policies (2026 AI Index).
- **Policy, law, and history of technology.** Regulation (EU AI Act phases, California SB 53, state lawsuits) needs people who understand the technical basics, and the history of hype cycles informs investment and policy judgment.

### Business opportunities
- **AI-literacy training** for companies, schools, and older adults, built on the "everything is numbers / AI is matrix multiplication / outputs are probabilities" mental model.
- **Local-language and accessibility tools.** 2.2 billion people are still offline, and many languages are under-served by tokenizers and training data, which makes them more expensive and lower quality.
- **Small-business automation** using APIs and agents for invoicing, scheduling, and customer support. This requires understanding APIs, JSON, rate limits, and costs per million tokens.
- **Data preparation services.** Cleaning, labeling, and converting messy files (PDFs, scans, audio) into AI-ready formats.
- **On-device and edge AI.** Quantized small models running on phones and laptops, using the memory math from exercise 21.
- **Verification and fact-checking services** for AI-generated content, using probability, base rates, and source-checking habits.

### Skills in demand (foundation-level)
- Python basics and reading code
- Spreadsheets as data and math tools
- Basic statistics and probability reasoning
- Estimating costs and scale ("napkin math")
- Understanding APIs and JSON
- Using the command line and Git
- Clear technical writing
- Verifying AI outputs

### Open problems connected to this domain
- **The memory wall.** Memory bandwidth improves about 28% per year while compute improves faster, so AI speed is often limited by data movement. New memory technologies, chip packaging, and algorithms that move less data are active research areas.
- **Energy efficiency of computation.** Data center electricity demand is projected to more than double by 2030 (IEA). Lower-precision math (FP8/FP4), better chips, and new computing paradigms (analog, optical, neuromorphic) are open frontiers.
- **Faster matrix multiplication.** AlphaEvolve's 48-multiplication result (2025) shows that even 1960s-era math problems in matrix multiplication still have room, and AI is now helping discover algorithms.
- **Why deep learning generalizes.** Classical statistics says huge models should overfit, but they don't in the expected way. There is still no full mathematical theory.
- **Calibration and uncertainty.** Getting models to output probabilities that match reality, and to say "I don't know" (Bayes and base rates).
- **Tokenization fairness and efficiency.** Some languages need many more tokens for the same meaning, which raises cost and reduces quality.
- **Measuring AI's real productivity effects.** For example, METR's 2025 study found experienced developers 19% slower with early-2025 tools, despite expecting a speed-up. Good measurement is an open methodological problem.
- **Mathematics with AI.** AI systems now produce olympiad-level proofs and claim progress on open problems. The 2026 debates in the math community over credit and verification are unresolved.
- **Open vs closed models.** The 2026 AI Index puts the gap between the best US and Chinese models at only 2.7% on Arena scores, and open-weight models (DeepSeek, Qwen, gpt-oss) keep closing the gap. Questions of definition, licensing, and safety remain open.

---

## 8. Common misconceptions to correct

1. **"The chatbot looks up answers in a giant database."** It generates text token by token from learned parameters. Some products add web search or document retrieval on top, but the core is prediction, not lookup.
2. **"The AI lives in my phone."** For major chatbots the app is a thin front end. The model runs on GPU servers in data centers, and your message travels there and back. (Small on-device models do exist.)
3. **"The cloud is not a physical thing."** The cloud is rows of real computers in real buildings using real electricity and water. AI data centers now approach a gigawatt each.
4. **"Computers understand what they're doing."** At the hardware level, they flip billions of switches by fixed rules. Whatever "understanding" a model has emerges from patterns in numbers. That is a fascinating open question, not a given either way.
5. **"Binary means computers can only do simple yes/no things."** Combinations of bits can represent any number, color, sound, or word. 8 bits give 256 options; 64 bits give about 18 quintillion.
6. **"AI is brand new."** The field was named in 1956, neural networks date to 1943–1958, and backprop was popularized in 1986. What is new since 2012, and especially since 2017–2022, is the scale of data and compute.
7. **"Neural networks work like the brain."** They are loosely inspired by neurons, but they are really stacks of matrix multiplications and simple functions trained by gradient descent, which is very different from biology.
8. **"You need advanced math to understand AI."** The core ideas are multiplication and addition, lists of numbers, slopes, and probabilities. Professionals need more, but the concepts are accessible.
9. **"Bigger numbers are always better" (more parameters, bigger context, higher benchmark scores).** Data quality, training method, and inference-time "thinking" matter a lot. Benchmarks can be saturated or contaminated, and a small, well-trained model can beat an older large one.
10. **"The model learns from my conversation in real time."** A deployed model's parameters don't change while you chat. Apps may add "memory" features (saved notes fed back into the context), and companies may use data for future training depending on settings.
11. **"The AI gives the same answer every time" or "different answers mean it's broken."** Outputs are sampled from probability distributions. Variation is by design, and temperature and settings control it.
12. **"If the AI says it confidently, it's probably true."** Fluency is not accuracy. Models can be confidently wrong (hallucination), and base rates matter (Bayes).
13. **"Correlation in data shows causation."** Models learn correlations, including spurious ones (like Teachable Machine learning the background). This is a statistics basic that carries straight over to AI behavior.
14. **"Moore's Law is a law of physics that guarantees ever-faster computers."** It was an industry trend that has slowed. AI progress now relies as much on more chips, specialized designs, lower precision, and bigger data centers.
15. **"GPUs are just for gaming."** They are now the main engine of AI. Nvidia briefly became the world's most valuable company, reaching $4 trillion (July 2025) and then $5 trillion (October 2025).
16. **"The Turing test is the official measure of AI."** It was a 1950 thought experiment. Modern evaluation uses many benchmarks and real-world task tests, and passing as human in short chats is no longer considered decisive.
17. **"AI progress is a smooth upward line."** History shows two AI winters and hype cycles. Even today, the "jagged frontier" means models can be superhuman at some tasks and fail at simple ones (like counting letters, because of tokens).
18. **"Open-weight means open source and therefore free of restrictions."** Many "open" models release only the weights, sometimes under licenses with use restrictions. The training data and code are often private.
19. **"A model 'reads' words letter by letter like we do."** It reads tokens (word pieces) converted into vectors. That is why spelling and character-counting tasks can be oddly hard.
20. **"A trillion is just a bit more than a billion."** It is a thousand times more. Scale illiteracy leads to bad intuitions about costs and model sizes.
21. **"Reasoning models think in a human way."** "Thinking" means generating extra intermediate tokens before the final answer, trained with reinforcement learning. It helps on many problems but is not a window into human-like thought.
22. **"The AI coding boom means you no longer need to understand computers."** AI lowers the entry barrier, but understanding fundamentals (data formats, APIs, errors, security) is what lets you check and fix AI-generated work. The 2025 METR slowdown result is a reminder.
23. **"Exponential trends will continue forever."** Compute has grown about 5× per year, but power, chip supply, money, and data are physical and economic limits. Exponentials in the real world eventually bend.

---

## 9. Analogies that work well for beginners

**Computing**
- **Bits = light switches.** Each switch is on or off; a row of 8 switches can make 256 patterns, enough to label every letter on a keyboard.
- **Binary = an odometer with only 0 and 1.** When a wheel passes 1 it rolls over to 0 and bumps the next wheel, just like 9 → 10 in decimal.
- **Transistor = a faucet controlled by a small handle.** A tiny signal on the handle (gate) lets a big flow (current) through or stops it.
- **Logic gates = rules for a security door.** AND: both keycards needed. OR: either keycard works. NOT: the door is open unless someone holds the button.
- **Computer = a restaurant kitchen.**
  - CPU = head chef.
  - RAM = countertop, quick to reach but limited and cleared at closing.
  - Storage = pantry/freezer, big but slow.
  - Program = recipe.
  - GPU = 1,000 line cooks who all chop at once but can only do simple repeated tasks.
- **CPU vs GPU = one brilliant professor vs a stadium of students with calculators.** The professor solves anything step by step; the stadium does a million simple sums at once.
- **Memory hierarchy = your desk, your bookshelf, the basement, the city library.** Keep what you need close at hand.
- **Memory wall = a super-fast chef starved by a slow delivery van.** Cooking speed doesn't matter if ingredients arrive slowly.
- **Program = a recipe followed by an extremely literal cook.** If the recipe says "add eggs" without "crack them", in go the shells.
- **Algorithm = the method; code = the written-down recipe in a particular language.** The same lasagna method can be written in English or Italian.
- **Operating system = a building manager.** It assigns rooms (memory), schedules the elevator (CPU time), and keeps tenants (apps) from breaking into each other's apartments.
- **Open source = a published recipe** anyone can cook, tweak, and share. **Open weights = the finished, frozen cake** given away, without the recipe or ingredient list.
- **Internet packets = postcards.** A long letter is split into numbered postcards that may travel different routes and get reassembled in order.
- **IP address = street address; DNS = your phone's contact list** (you tap "Mom", it dials the number).
- **HTTPS = a locked briefcase.** Couriers carry it, but only the sender and receiver have keys.
- **Server = a shop that never closes;** a data center = a mall of thousands of such shops with its own power plant.
- **Cloud = renting a car (or a taxi) instead of buying one.** Pay for what you use, with someone else maintaining it.
- **API = a restaurant waiter with a menu.** You order from the menu (allowed requests) in a fixed format; the kitchen is hidden; the waiter brings back your dish (response).
- **API key = a membership card** that tells the restaurant who to bill.
- **Latency vs bandwidth = how long the drive is vs how many lanes the highway has.**
- **Streaming tokens = a typist reading out each word as they type it,** instead of handing over the finished page.
- **Compression = vacuum-packing clothes.** Lossless packing means everything comes out the same; lossy packing tosses the socks you'll never miss.

**Math**
- **Function = a vending machine.** Put in an input, get a predictable output. **Parameters = the machine's internal settings** the owner can adjust.
- **A model's parameters = knobs on a giant mixing board** (billions of them). Training is the sound engineer turning knobs until the music sounds right.
- **Vector = a recipe's ingredient list** (2 eggs, 1 cup flour, 0.5 cups sugar) or a character sheet in a game (strength 7, speed 3, magic 9). Dimension = how many ingredients or stats.
- **Embedding space = a map where similar things live in the same neighborhood.** Cats live near dogs; tax forms live far away.
- **Dot product = a compatibility score on a dating or movie app.** Multiply how much each side cares about each trait and add it up.
- **Matrix = a spreadsheet of numbers;** multiplying a vector by a matrix = **a currency-exchange board or mixing desk** that turns one set of inputs into a new blended set of outputs.
- **Matrix multiplication = many dot products at once,** like grading every student's answers against every answer key in one go.
- **A neural network = an assembly line of mixing desks** with a "no negatives allowed" filter (the activation) between stations.
- **Exponential growth = rice on a chessboard** (one grain, then double on each square), or a lily pad that doubles daily and covers the pond overnight at the end.
- **Logarithm = "how many doublings?" or "how many zeros?"** The log of a number is roughly its digit count. A log scale is a ruler where each tick means "10 times more".
- **Probability distribution = a bag of marbles,** where the number of each color sets its chance. **Sampling = reaching in blindfolded.**
- **Temperature = how adventurous the diner is.** Low: always orders the favorite. High: tries random dishes.
- **Conditional probability = narrowing the room.** Of everyone in the room, what fraction wear glasses? Now only among people holding books?
- **Bayes = a detective updating a hunch.** Strong evidence matters, but so does how common the suspect type is to begin with. Base rates are "who was in the building".
- **Mean vs median = average wealth in a bar when a billionaire walks in.** The mean skyrockets; the median barely moves.
- **Variance = how scattered darts are around the bullseye.**
- **Overfitting = memorizing last year's exam answers.** Perfect on the practice test, lost on the real one. **Test set = a sealed exam** you never peek at.
- **Derivative = the speedometer reading** at one instant; the slope = the steepness of the road right under your feet.
- **Gradient = an arrow on a hiking map** pointing straight uphill. **Gradient descent = walking downhill in thick fog** by feeling the ground with your feet. **Learning rate = stride length:** giant leaps overshoot the valley, tiny shuffles take forever.
- **Local minimum = a small hollow on the mountainside** that feels like the bottom in the fog.
- **Chain rule / backprop = tracing blame back through a relay team.** If the final time was bad, how much was each runner's fault? Pass the blame backward, leg by leg.
- **Loss function = a score from a strict judge,** where lower is better. Cross-entropy = how surprised the judge is by the right answer.
- **Training vs inference = studying for years vs answering one exam question.** Training is huge and rare; inference happens billions of times a day.
- **Quantization = saving a photo as a smaller JPEG.** Slightly less detail, much smaller and faster.

**History**
- **AI winters = gold rushes followed by ghost towns.** Promises outran results, funding fled, and a few prospectors kept digging until better tools (GPUs, data) arrived.
- **Symbolic AI vs machine learning = writing a rulebook for every situation vs letting someone learn by watching thousands of examples.**
- **The deep learning boom = a three-legged stool:** algorithms (backprop, from 1986), data (the internet, ImageNet), and compute (GPUs). It only stood up once all three legs were long enough, around 2012.
- **"The Bitter Lesson" = the tortoise of brute compute beating the hare of clever hand-built knowledge,** over and over across 70 years.
- **ChatGPT moment = the iPhone moment.** The underlying pieces (Transformers, GPT-3) existed already, but a friendly interface put them in everyone's hands overnight.

---

### Notes on source reliability for the author team
- 2026 model dates come mostly from Wikipedia articles (Claude, ChatGPT, GPT-5.5, GPT-6, DeepSeek, Google Gemini), cross-checked where possible against Anthropic's own news page and Anthropic's Glasswing page. OpenAI's site blocked automated fetches, so OpenAI 2026 details rely on Wikipedia, CNBC, and OpenAI's Deployment Safety Hub.
- Known conflicts:
  - GPT-6 Sol/Luna: Sep 22 vs "October".
  - Claude Mythos/Fable 5.1: Sep 1 (Wikipedia) vs Sep 15 (Anthropic news).
  - Gemini 4: reported as "in post-training" in late September vs listed as released in late September or October.
  Re-verify all three before publication.
- Several dramatic 2026 claims appear on Wikipedia's "2026 in artificial intelligence" page, which is flagged for factual verification: autonomous AI cyberattacks, solutions to famous math problems, and "GPT-6 is AGI". They were deliberately excluded or softened here and should be checked against primary sources by the relevant chapter's researcher.
- The web-search budget for this session ran out partway through. Some stable facts (IEA 2024 data-center figures, AI Index 2025 inference-cost figure, DeepSeek-V3 cost, Nobel and Turing details, pre-2024 history) are from well-established publications listed with their canonical URLs but were not re-fetched today.
