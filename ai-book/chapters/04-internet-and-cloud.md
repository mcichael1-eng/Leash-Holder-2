# Chapter 4: The Internet and the Cloud: How Your Message Reaches a Data Center

*By the end of this chapter you will be able to follow one chatbot message from your thumb to a GPU in a distant building and back, step by step, with real numbers for time, distance, energy and cost.*

## What you'll learn

- What a network is, how the internet connects billions of devices, and why messages travel as small packets.
- The physical internet: radio, copper, fiber-optic glass and the undersea cables that carry nearly all traffic between continents, and how the speed of light sets a hard floor on delay.
- How IP addresses and DNS find the right computer, and how HTTP, URLs and status codes work.
- What HTTPS encryption protects, and what it does not.
- Clients, servers, data centers, the cloud and the hyperscalers, at the level you need for the rest of the book.
- What an API is, why it is how programs (and chatbot apps) talk to AI models, and what a message costs.
- The difference between latency and bandwidth, and why your chatbot pauses before the first word and then streams.
- The full 12-step journey of one chatbot message, with a timing, energy and cost budget.

## Before you start

Chapter 2 (How Computers Work: Bits, Transistors and Processors) explains bits, bytes, processors and GPUs. Chapter 3 (Software, Code and Data: How Everything Becomes Numbers) explains how your words become UTF-8 bytes and JSON, what a server's operating system is, and why your chatbot app is only a thin front end. This chapter picks up the moment your message leaves your phone.

## One message, one second, half a continent

You type "Plan a 3-day trip to Lisbon for under 600 euros" and tap Send. About a second later, words start appearing, then stream in at a steady pace until the plan is done. In that second, your message was split into pieces, turned into flashes of light, carried through glass fibers, possibly across a state or an ocean, checked, queued, read by a model spread across several GPUs that draw as much power as a small neighborhood, and answered one token at a time.

Most people never think about any of this, and that is a sign of how well it works. But if you want to understand AI's costs, its speed, its privacy and its physical footprint, you need to see the whole trip. This chapter builds it piece by piece and then puts it together in one diagram.

> **Key idea:** Your chatbot is not in your phone. Every message makes a round trip to a data center, and every part of that trip, from radio waves to glass cables to GPUs, adds time, uses energy and costs money.

## Networks and the internet

A network is simply computers connected so they can exchange data. Your home Wi-Fi is a small network: your phone, laptop, TV and smart speaker all connect to one box, the router, which passes data between them and out to the wider world.

> **Definition — Network:** Two or more computers connected so they can exchange data, by cable or by radio.

> **Definition — Router:** A device that forwards data between networks, choosing where each piece should go next. Your home Wi-Fi box is a router; the internet has millions more.

Your router connects to an internet service provider, the company you pay for internet access. Your ISP connects to bigger networks, which connect to other big networks at meeting points called internet exchange points. The very largest long-distance links, the high-capacity fiber routes between cities and continents, are called the backbone. The internet is not one network owned by anyone. It is tens of thousands of independent networks that have agreed to pass each other's traffic.

> **Definition — ISP (Internet service provider):** The company that connects your home or phone to the internet, such as a cable, fiber or mobile phone company.

> **Definition — Internet:** The worldwide network of networks, linked by shared rules so that any connected device can reach any other.

> **Definition — Internet exchange point (IXP):** A building where many networks meet and hand traffic directly to each other, so data does not have to take long detours.

> **Definition — Backbone:** The highest-capacity long-distance links of the internet, mostly fiber-optic cables between major cities and across oceans.

```mermaid
flowchart LR
  PH["Your phone"] --> WIFI["Home Wi-Fi router<br/>or cell tower"]
  WIFI --> ISP["Your internet<br/>service provider"]
  ISP --> IXP["Internet exchange point<br/>where networks meet"]
  IXP --> BB["Backbone fiber<br/>between cities"]
  BB --> CLOUD["The AI provider's<br/>own network"]
  CLOUD --> DC["Data center<br/>with GPU servers"]
```

*Figure 4.1: The internet is a network of networks. Your message hops from your home network to your ISP, through exchange points and backbone links, into the AI provider's network.*

All these networks can work together only because they follow the same protocols, agreed rules for how to format and exchange data. The key ones date back decades: the ARPANET, the internet's ancestor, sent its first messages in 1969; the TCP/IP protocols that define today's internet became its standard in 1983; and the World Wide Web, invented by Tim Berners-Lee in 1989, went public in 1991.

> **Definition — Protocol:** An agreed set of rules for how computers communicate, like etiquette for machines. TCP/IP, HTTP and TLS are protocols.

The internet now reaches most of humanity, but not all of it. The International Telecommunication Union reported in 2025 that almost three quarters of the world's people are online and about 2.2 billion remain offline, mostly in low- and middle-income countries. For them, cloud AI is out of reach.

## Packets: big messages in small pieces

The internet never sends a big message in one piece. It chops every message into small chunks called packets, each usually up to about 1,500 bytes. Every packet carries a label, its header, with the sender's address, the destination's address and its position in the sequence. Routers read each header and pass the packet one step, or "hop", closer to its destination.

> **Definition — Packet:** A small chunk of data, usually up to about 1,500 bytes, sent across a network with a label saying where it came from and where it is going. Big messages are split into many packets and reassembled.

Why chop things up? Because it makes the network resilient and fair. If one link is congested or broken, routers send later packets another way. No single giant file can hog a cable; packets from millions of users take turns, interleaved like cars merging on a highway.

Worked example: how many packets?

- Your chat request, with a few thousand tokens of conversation history, is roughly 8 to 10 KB of text. At up to 1,500 bytes per packet, that is about 6 or 7 packets.
- A 3 MB photo you upload is 3,000,000 ÷ 1,500 = about 2,000 packets.
- A 4 GB open-weight model download is about 2.7 million packets.

Packets can arrive out of order, and occasionally one is lost. A protocol called TCP numbers every packet, puts them back in order at the destination and asks for any missing ones to be sent again. Your app never sees the chaos; it receives a clean stream of bytes. (A newer protocol called QUIC, used by HTTP/3, does the same job with fewer round trips, and many large sites use it.)

> **Definition — TCP (Transmission Control Protocol):** The protocol that makes packet delivery reliable: it numbers packets, reassembles them in order and resends any that are lost.

```mermaid
flowchart LR
  S["Your message<br/>split into packets 1, 2, 3"] --> R1["Router A"]
  R1 -->|"packet 1"| R2["Router B"]
  R1 -->|"packets 2 and 3"| R3["Router C"]
  R2 --> R4["Router D"]
  R3 --> R4
  R4 --> D["Destination puts<br/>1, 2, 3 back in order"]
```

*Figure 4.2: Packets from one message may take different routes and arrive out of order. TCP reassembles them.*

> **Analogy:** Sending a message over the internet is like mailing a long letter as numbered postcards. Each postcard has the from and to addresses. They may travel by different trucks and arrive in any order, but the numbers let the recipient put the letter back together, and ask for any missing card.

## The physical internet: radio, copper, glass and the ocean floor

The internet is a physical thing. Your message travels through four kinds of medium.

- **Radio.** From your phone to your Wi-Fi router, or to a cell tower (4G or 5G), your data travels as radio waves. This "last hop" is often the slowest and least reliable part of the trip.
- **Copper.** Some homes still connect over copper telephone or cable TV wires, which carry data as electrical signals.
- **Fiber-optic cable.** Almost all long-distance traffic travels as pulses of light inside strands of glass thinner than a hair. A single fiber can carry enormous amounts of data, and a cable bundles many fibers.
- **Satellites.** Some links, especially in remote areas, go through satellites.

> **Definition — Fiber-optic cable:** A cable of hair-thin glass strands that carry data as pulses of light. It carries far more data, over far longer distances, than copper.

Between continents, the internet runs along the ocean floor. Several hundred undersea cables, many no thicker than a garden hose in the deep ocean, carry nearly all intercontinental internet traffic. Powered repeaters spaced along the cable boost the light as it fades. When you chat with a model served from another continent, your words almost certainly travel through one of these cables, not through space.

> **Definition — Undersea (subsea) cable:** A fiber-optic cable laid on the ocean floor between continents. Such cables carry nearly all intercontinental internet traffic.

### The speed of light sets a floor on delay

Light in a vacuum travels about 300,000 km per second. Inside glass it is slower, roughly 200,000 km per second. That works out to about 5 microseconds (millionths of a second) per kilometer of fiber, or 5 milliseconds per 1,000 km. No engineering can beat this; it is physics. Real cables also zigzag rather than going in straight lines, and every router along the way adds a little extra delay.

Worked examples (one-way, light in fiber, straight line, no delays):

| Trip | Rough distance | Minimum one-way time | Minimum round trip |
|---|---|---|---|
| Across a big city | 50 km | 0.25 ms | 0.5 ms |
| Chicago to Virginia | 1,000 km | 5 ms | 10 ms |
| New York to London | 5,600 km | 28 ms | 56 ms |
| Sydney to Los Angeles | 12,000 km | 60 ms | 120 ms |
| Up to a geostationary satellite and down | 72,000 km (at light speed in space) | about 240 ms | about 480 ms |

*Figure 4.3: The speed of light sets a minimum delay no technology can beat. Real round trips are always somewhat longer.*

The last row explains why traditional satellite internet feels sluggish: geostationary satellites orbit about 36,000 km up. Newer low-orbit satellite networks fly a few hundred kilometers up, which is why their delays are far smaller.

> **Watch out:** It is tempting to picture the internet as wireless, or as something in the sky. Apart from the first and last few hundred meters of radio, your data almost always travels through glass cables buried under streets, strung along railways and laid across ocean floors.

## Addresses and names: IP and DNS

To deliver a packet, the network needs an address. Every device on the internet has an IP address, a number that works like a postal address. The older version, IPv4, uses 32-bit addresses written as four numbers from 0 to 255, such as 203.0.113.42. That gives 2 to the power 32, about 4.3 billion, possible addresses: fewer than the number of devices on Earth. So your home router usually shares one public address among all your devices, and the newer IPv6 uses 128-bit addresses, about `3.4 × 10^38` of them, enough to never run out.

> **Definition — IP address:** A number that identifies a device on the internet so packets can be delivered to it, such as 203.0.113.42. IP stands for Internet Protocol.

Nobody wants to remember numbers, so we use domain names like claude.ai, chatgpt.com or gemini.google.com. The Domain Name System (DNS) is the internet's phone book: it turns a name into an IP address. When your app needs to reach a server it hasn't contacted recently, it asks a DNS resolver (usually run by your ISP or a public service), which may ask a chain of other servers: the root servers, then the servers for the ending (.ai, .com), then the servers for the specific name.

> **Definition — Domain name:** A human-readable name for an internet address, such as claude.ai. The ending (.com, .ai, .org) is called the top-level domain.

> **Definition — DNS (Domain Name System):** The internet's phone book, which turns names like claude.ai into the numeric IP addresses computers use.

A fun detail: .ai is the country-code ending of Anguilla, a small Caribbean territory. Like .tv for Tuvalu, it became popular for reasons its owners never planned, and the AI boom turned it into valuable real estate.

```mermaid
sequenceDiagram
  participant P as Phone
  participant R as Resolver
  participant T as Ai registry
  participant A as NameServer
  P->>R: What is the address of claude.ai?
  R->>T: Who handles names ending in .ai?
  T-->>R: Ask this name server
  R->>A: What is the address of claude.ai?
  A-->>R: Here is the IP address
  R-->>P: Here is the IP address, keep it for a while
```

*Figure 4.4: A DNS lookup. Answers are cached, so most lookups are answered instantly from memory instead of repeating this chain.*

Because answers are saved (cached) for minutes or hours, most lookups take no time at all. An uncached lookup typically takes tens of milliseconds. DNS is also a tool for traffic control: big services return different IP addresses to different users, steering each person toward a nearby, healthy entrance to their network.

> **Try it:** On Windows, open Command Prompt and type `nslookup chatgpt.com`; on a Mac, open Terminal and type the same. You will see one or more IP addresses. Try `nslookup claude.ai` and `nslookup gemini.google.com` too, and notice that big services often return several addresses.

## The web's language: URLs, HTTP and status codes

Once your app knows the server's address, it needs to say what it wants. On the web, that conversation uses HTTP, the Hypertext Transfer Protocol. HTTP is a simple request-and-response pattern: the client sends a request, the server sends back a response.

> **Definition — HTTP (Hypertext Transfer Protocol):** The protocol browsers and apps use to request things from servers and receive responses. Nearly every website and AI API speaks it.

A request is aimed at a URL, a web address that names the protocol, the server and the specific thing you want:

```text
https://api.example.com/v1/messages?stream=true
  |          |              |          |
scheme     domain          path      query
(how)      (which server)  (what)    (options)
```

*Figure 4.5: The anatomy of a URL.*

> **Definition — URL (Uniform Resource Locator):** A web address, such as https://claude.ai/new. It names the protocol, the server and the specific page or resource.

A request also has a method (GET to fetch something, POST to send something, such as your chat message), headers (labels with extra information, such as your login token and the format of the data) and, for POST, a body (the data itself, for a chatbot usually the JSON from Chapter 3). The response comes back with a three-digit status code, its own headers and a body.

> **Definition — Request and response:** The two halves of a web conversation. The client sends a request (what it wants, plus any data); the server sends a response (a status code plus the result).

> **Definition — Status code:** A three-digit number at the start of every HTTP response summarizing what happened: 200 means OK, 404 means not found, 429 means too many requests.

| Code | Meaning | When you might see it in AI |
|---|---|---|
| 200 | OK | Your message was accepted and answered |
| 301 | Moved permanently | An old web address redirects to a new one |
| 400 | Bad request | The request was malformed, such as broken JSON |
| 401 | Unauthorized | Missing or wrong API key |
| 402 | Payment required | Long unused; revived in 2025 for pay-per-crawl (see below) |
| 403 | Forbidden | You are identified but not allowed |
| 404 | Not found | Wrong URL or a model name that does not exist |
| 429 | Too many requests | You hit a rate limit; wait and retry |
| 500 | Internal server error | Something broke on the provider's side |
| 503 | Service unavailable | The service is overloaded or down for maintenance |

*Figure 4.6: Common HTTP status codes. The first digit tells you the family: 2 is success, 4 is your side's problem, 5 is the server's problem.*

Some providers add their own codes. Anthropic's API, for example, uses 529 to signal that its servers are temporarily overloaded.

> **At the frontier (2026):** The web's plumbing is being rewired around AI. On July 1, 2025, Cloudflare, which sits in front of a large share of websites, began blocking known AI crawlers by default for new domains and launched "Pay Per Crawl", which revives the long-dormant HTTP status code 402 Payment Required so sites can charge AI companies for access. Chapter 11 covers how this affects AI training data.

## HTTPS and encryption: the locked briefcase

Your chat travels through your Wi-Fi router, your ISP, exchange points and backbone links owned by companies you have never heard of. Anyone along the way could, in principle, read raw packets. HTTPS prevents that. It is HTTP wrapped in encryption, so that only your device and the server can read what is inside.

> **Definition — Encryption:** Scrambling data with a secret key so that only someone with the right key can unscramble and read it.

> **Definition — HTTPS:** HTTP with encryption (the S stands for secure). The padlock icon in your browser means the connection uses it.

There is a puzzle at the heart of this. To encrypt, both sides need the same secret key. But you have never met the server, and any key you send over the internet could be copied by an eavesdropper. The solution, public-key cryptography, is one of the great inventions of the 20th century.

> **Definition — Public-key cryptography:** Encryption that uses a pair of keys: a public key that anyone can use to lock (encrypt) data, and a private key, kept secret, that alone can unlock it. It lets strangers set up a shared secret over an open network.

> **Analogy:** Public-key cryptography is like a server handing out thousands of open padlocks. Anyone can snap one shut on a box, but only the server holds the key that opens them. You put a fresh secret inside a box, lock it with the server's padlock and send it. Eavesdroppers see only a locked box.

In practice, the protocol called TLS uses public-key methods for a quick handshake, in which the two sides agree on a fresh shared key, and then switches to fast ordinary encryption for the actual conversation. During the handshake, the server also proves its identity with a certificate, a digital document vouched for by a trusted certificate authority. That stops an impostor from pretending to be claude.ai. The modern version, TLS 1.3, completes the handshake in a single round trip.

> **Definition — TLS (Transport Layer Security):** The protocol that encrypts HTTPS connections. It verifies the server's identity and sets up a shared secret key during a short handshake.

> **Definition — Certificate (digital):** An electronic document, vouched for by a trusted certificate authority, that proves a server really belongs to the name it claims, such as claude.ai.

```mermaid
sequenceDiagram
  participant P as Phone
  participant S as Server
  P->>S: Hello, here are the encryption methods I support
  S-->>P: Here is my certificate proving I am claude.ai
  Note over P,S: Both sides compute the same fresh secret key
  P->>S: Encrypted request with your chat
  S-->>P: Encrypted response, streamed back
```

*Figure 4.7: A simplified TLS handshake. After one round trip, everything else is encrypted with a shared key that was never sent over the network.*

It is just as important to know what HTTPS does not hide.

| Who | Can see | Cannot see |
|---|---|---|
| The owner of the café Wi-Fi | That your device connected to the AI provider, when, and roughly how much data moved | Your messages, the answers, your password |
| Your ISP and the networks in between | The same as above | The same as above |
| The AI provider | Everything you send and receive, once decrypted at its servers | Nothing in your chat is hidden from it |

*Figure 4.8: What HTTPS protects. It hides content from everyone in between, but not from the service you are talking to.*

> **Watch out:** HTTPS is not end-to-end encryption in the sense used by messaging apps such as Signal, where even the company cannot read your messages. A chatbot provider must decrypt your text, because its model has to read it to answer. Your privacy with an AI service depends on the provider's policies and settings, not on the padlock (Chapter 58).

> **Definition — End-to-end encryption:** Encryption where only the people communicating can read messages, not even the company running the service. Chatbots cannot work this way, because the provider's model must read your text.

## Clients and servers

Every exchange in this chapter has two roles. The client asks; the server answers. Your phone's chatbot app is a client. The computer that receives its request is a server.

> **Definition — Client:** A device or program that sends requests to another computer, such as your phone's chatbot app or your web browser.

> **Definition — Server:** A computer that waits for requests and answers them. It usually has no screen or keyboard and sits in a rack in a data center.

There is nothing magical about a server. It is a computer like your laptop, usually more powerful, with no screen, running Linux (Chapter 3), and built to run day and night. One web server can handle thousands of clients at once. An AI server is a special case: a heavy box with several GPUs, which can cost as much as a house and draw as much power as several homes.

> **Analogy:** A server is a shop that never closes and a client is a customer. A data center is a mall of thousands of such shops, with its own power plant and air conditioning.

## Data centers: where the servers live

Servers live in data centers: buildings packed with racks of servers, network equipment, power gear and cooling. A rack is a standard metal cabinet, about the size of a tall refrigerator, holding servers stacked like pizza boxes. Rows of racks fill large halls. Outside sit the substation, backup generators and cooling equipment.

> **Definition — Data center:** A building packed with servers, network equipment, power systems and cooling. Your chatbot's model runs in one.

> **Definition — Rack:** A standard metal cabinet that holds servers and network gear in data centers. A 2026 AI rack can draw around 120 to 140 kilowatts, about as much as 100 homes.

AI data centers are measured not in square meters but in power. The largest are approaching 1 gigawatt, roughly enough electricity for 800,000 to a million US homes. Epoch AI estimates that building one costs about $38 billion per gigawatt of IT power and takes about two years. As of October 20, 2026, Epoch's data center tracker followed 95 large AI data centers with about 14.2 GW of IT power between them. The largest known, according to Epoch, is xAI's Colossus 2 in Memphis, at roughly 1.1 million H100-equivalent chips. Altogether, the International Energy Agency estimated that the world's data centers (AI and everything else) used about 415 terawatt-hours of electricity in 2024, about 1.5% of global electricity, and projected about 945 TWh by 2030.

Your traffic enters a data center through fiber cables from several network carriers, which meet the building's own network in a secure room called a meet-me room. From there it flows over the building's front-end network, the one that handles user traffic and storage. Separate, much faster networks link the GPUs to each other so that a model too big for one chip can run across many (Chapter 34). Part VII of this book (Chapter 38 to Chapter 43) tours the building, its power, its cooling, its energy sources and its economics.

> **Watch out:** "The cloud" sounds weightless, but it is concrete, steel, copper, glass, water pipes and gas turbines in specific towns. Every chatbot answer comes from a real machine drawing real electricity in a real building.

## The cloud and the hyperscalers

Before about 2006, a company that wanted servers bought them, installed them in its own building and hired people to run them. Then Amazon Web Services launched in 2006 and offered something new: rent computers by the hour over the internet, start them in minutes, and switch them off when you are done. That is cloud computing.

> **Definition — Cloud computing:** Renting computing power, storage and software over the internet, paying for what you use, instead of owning and running the machines yourself.

The biggest cloud providers are called hyperscalers: Amazon Web Services (AWS), Microsoft Azure and Google Cloud, with Oracle growing fast. Meta builds giant data centers too, but mainly for its own services. During the AI boom, a newer group of "neoclouds" such as CoreWeave, Nebius, Lambda, Crusoe and Together AI specialize in renting GPUs for AI. The major AI labs rent enormous amounts of capacity from these companies, and increasingly build their own sites with partners (Chapter 42).

> **Definition — Hyperscaler:** A giant cloud provider operating huge data centers worldwide, such as Amazon Web Services, Microsoft Azure or Google Cloud.

> **Definition — Neocloud:** A newer cloud company that specializes in renting GPUs for AI, such as CoreWeave, Nebius or Lambda.

Cloud providers organize their data centers into regions, such as "US East" or "Europe West", each a cluster of buildings in one geographic area. Regions matter for speed (closer is faster) and for law: some customers must keep data inside a particular country or bloc. AI providers charge for this; OpenAI, for example, adds a 10% uplift for regional processing on models released since March 2026.

> **Definition — Region (cloud):** A geographic area where a cloud provider runs a group of data centers, such as US East or Europe West. Choosing a region affects speed, price and which country's laws apply to your data.

Clouds sell at three levels. You can rent bare machines (often virtual machines, software slices of a physical server) and manage everything yourself; rent a platform where the provider handles the servers; or simply use finished software through a browser or app.

> **Definition — Virtual machine:** A software imitation of a whole computer, running alongside others on one physical server. Clouds rent them so many customers can share a machine safely.

| Level | What you rent | Who manages the servers | AI example |
|---|---|---|---|
| Infrastructure as a service (IaaS) | Raw machines, GPUs, storage | You | Renting eight H100 GPUs by the hour to fine-tune a model |
| Platform as a service (PaaS) | A ready platform to run your code or models | Mostly the provider | Calling a hosted model through a cloud AI platform |
| Software as a service (SaaS) | A finished application | The provider | Your ChatGPT, Claude or Gemini subscription |

*Figure 4.9: The three levels of cloud service. A chatbot subscription is software as a service.*

Worked example: renting GPUs. In October 2026, Lambda listed on-demand H100 GPUs at about $3.99 to $4.29 per GPU-hour, and RunPod listed them from about $2.69 to $3.99 (in 2025 they were widely available for $2 to $3). At $4 per hour:

- 8 GPUs for a 10-hour fine-tuning experiment: 8 × 10 × $4 = $320.
- 8 GPUs running all month (about 730 hours): 8 × 730 × $4 = about $23,000.
- 8 GPUs for a full year (8,760 hours): about $280,000.

Renting is ideal for short or unpredictable jobs. Companies that will keep GPUs busy around the clock for years sign much cheaper long-term contracts, or buy and run their own (Chapter 43).

> **Analogy:** The cloud is like using taxis and rental cars instead of owning a car: you pay only for the trips you take, and someone else handles maintenance. A hyperscaler is a city that owns its own buildings; a neocloud is a hotel chain renting rooms (GPUs) by the night or the year.

Clouds also run content delivery networks: thousands of small edge sites close to users that keep copies of popular content, such as images, videos and the code of web apps, so it loads quickly. AI providers use the edge to accept your connection close to you and then carry your request over their own fast private network to a data center. The answer itself cannot be cached at the edge, because every response is generated fresh.

> **Definition — CDN (content delivery network) and edge:** A network of many small sites near users, called the edge, that keeps copies of popular content and accepts connections close to you, making websites and apps faster.

## APIs: how programs order from each other

Your chatbot app does not talk to the model directly. It talks to an API, an Application Programming Interface: a published menu of requests one program can make of another, with exact rules for how to ask and what comes back. AI companies sell access to their models through APIs, and their own apps use APIs behind the scenes too.

> **Definition — API (Application Programming Interface):** A defined way for one program to request services from another, like a restaurant menu and a waiter. AI companies sell model access through APIs.

> **Analogy:** An API is a waiter with a menu. You order only what is on the menu, in the expected way ("one Sonnet, 1,000 tokens max, here is the conversation"). The kitchen is hidden, and the waiter brings back your dish (the response) or tells you the kitchen is too busy (a 429).

An API lives at an endpoint, a specific URL. Anthropic's main model endpoint, for example, is https://api.anthropic.com/v1/messages. A program sends a POST request there with JSON describing the model and the conversation, plus an API key in the headers to prove who is paying.

> **Definition — Endpoint:** The specific URL where an API receives a particular kind of request, such as https://api.anthropic.com/v1/messages.

> **Definition — API key:** A secret code, like a password, that identifies who is using an API so they can be billed and limited. Anyone who gets your key can spend your money.

```mermaid
flowchart LR
  APP["Your program<br/>or chatbot app"] -->|"HTTPS POST: JSON request<br/>plus API key"| API["API endpoint<br/>the waiter"]
  API --> CHK["Check key, plan<br/>and rate limits"]
  CHK --> MOD["Model on GPU servers<br/>the kitchen"]
  MOD --> API
  API -->|"JSON response<br/>text plus token counts"| APP
```

*Figure 4.10: An API call. The program never touches the model directly; it orders through a strict menu.*

APIs charge by the token, usually quoted per million tokens, with output (what the model writes) priced higher than input (what it reads). Worked example using Anthropic's list prices as of October 2026 for Claude Sonnet 5.5, $2 per million input tokens and $10 per million output tokens:

- A chat turn that sends 2,000 tokens of conversation and gets 600 tokens back:
  - Input: 2,000 × $2 ÷ 1,000,000 = $0.004.
  - Output: 600 × $10 ÷ 1,000,000 = $0.006.
  - Total: about $0.01, one cent.
- A thousand such turns cost about $10.

APIs also enforce rate limits: caps on requests or tokens per minute, so no single customer can swamp the service. Exceed one and you get status code 429; well-written programs wait a moment and try again, waiting longer after each failure. Chapter 26 shows you how to make API calls yourself, and Chapter 28 explains how agents are built as API calls in a loop.

> **Definition — Rate limit:** A cap on how many requests or tokens you may send in a period of time, such as per minute. Going over it returns a 429 error.

## Latency and bandwidth

Two words describe the speed of any network connection, and people mix them up constantly.

> **Definition — Latency:** How long it takes for data to get from one place to another, or for a request to get its first response. It is measured in milliseconds.

> **Definition — Bandwidth:** How much data can move per second, like the width of a pipe. Internet speeds are quoted in megabits per second (Mbps).

> **Analogy:** Latency is how long the drive is; bandwidth is how many lanes the highway has. Adding lanes lets more cars travel at once, but it does not make a 500-kilometer trip shorter.

A measure you will see often is round-trip time: how long a tiny message takes to go somewhere and come back. The `ping` command measures it.

> **Definition — Round-trip time (RTT):** The time for a small message to travel to a destination and for the reply to come back, often measured with the ping command. It is the basic unit of network delay.

One unit trap first. Internet speeds are quoted in megabits per second (Mbps), but file sizes are in megabytes (MB). A byte is 8 bits, so divide by 8: a 100 Mbps connection moves 12.5 MB per second.

Worked examples:

- **Downloading a 4 GB open-weight model on 100 Mbps:** 4 GB = 4,000 MB = 32,000 megabits. 32,000 ÷ 100 = 320 seconds, about 5 minutes. Here bandwidth is everything; a 1,000 Mbps connection would take 32 seconds.
- **Sending a 10 KB chat request on the same connection:** 10 KB = 80,000 bits. 80,000 ÷ 100,000,000 = 0.0008 seconds, under a millisecond. But the request still needs perhaps 20 to 40 milliseconds to reach a data center 1,000 km away. Here latency is everything.
- **Receiving a streamed answer:** a model writing 50 tokens per second, at roughly 4 bytes of text per token, sends about 200 bytes of text per second. Even with the wrapping and labels around each chunk, that is a few kilobytes per second at most. HD video streaming uses about 5 megabits per second, hundreds of times more.

```mermaid
quadrantChart
  title What each activity needs from the network
  x-axis Low bandwidth --> High bandwidth
  y-axis Delay is fine --> Needs low latency
  quadrant-1 Heavy and urgent
  quadrant-2 Light but urgent
  quadrant-3 Light and patient
  quadrant-4 Heavy but patient
  Video call: [0.55, 0.9]
  Online game: [0.15, 0.95]
  Voice assistant: [0.25, 0.8]
  Chatbot text: [0.08, 0.55]
  Movie streaming: [0.8, 0.3]
  Model download: [0.95, 0.08]
  Email: [0.05, 0.1]
```

*Figure 4.11: Different activities stress different things. Chatbot text needs almost no bandwidth; its speed is set by latency and by the data center.*

This is why your chatbot behaves as it does. Before the first word appears, there is a pause made of network round trips plus waiting and reading time inside the data center. After that, words stream at a pace set mostly by the GPUs, not by your connection. The two numbers that describe this are time to first token and tokens per second.

> **Definition — Time to first token (TTFT):** How long you wait after sending a message until the first piece of the answer appears. It dominates how fast an AI app feels.

> **Definition — Tokens per second:** How fast a model writes once it has started, often tens of tokens per second for a chatbot. Divide the answer length by it to estimate how long a reply takes.

> **Definition — Streaming:** Sending a response piece by piece as it is produced, instead of all at once at the end. It is why chatbot answers appear word by word.

The streaming itself usually uses a simple web technique called server-sent events: the server keeps the HTTPS connection open and pushes each new chunk of text down it as soon as it exists.

> **Definition — Server-sent events (SSE):** A web technique where a server keeps a connection open and pushes a stream of small updates to the client. Most AI APIs use it to stream tokens.

> **Key idea:** Your Wi-Fi is almost never the reason a chatbot types slowly. A chat answer needs only a few kilobytes per second. The pause before the first word comes from distance, queues and the model reading your conversation; the typing speed after that comes from the GPUs in the data center.

> **Try it:** Open fast.com or speedtest.net. Note two numbers: your download speed (bandwidth, in Mbps) and your latency or "ping" (in milliseconds). Then compute how long a 4 GB file would take to download at your speed.
