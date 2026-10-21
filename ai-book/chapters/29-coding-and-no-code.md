# Chapter 29: Coding With AI and Building Without Code

*This chapter shows you how software is really built, how AI coding agents now do much of that work, and how you can safely build your own tools and automations, with or without writing a line of code.*

## What you'll learn

- How software is built, in plain words: repositories, Git, tests and deploys, and why that safety net matters even more when an AI writes the code.
- How AI coding tools grew from grey autocomplete text in 2021 into agents that plan, edit, test and open pull requests on their own.
- What happens inside a coding agent, step by step, and why tests act as its eyes.
- Who makes the main coding agents in late 2026, and how to choose one.
- The difference between vibe coding and agentic engineering, and what the evidence says about speed and quality, including METR's surprising 2025 result.
- What a non-programmer can safely build, and the clear signs that you need a professional.
- How no-code automation platforms (Zapier, Make, n8n) and webhooks connect your apps, with AI steps inside them.
- What AI app builders (Lovable, Bolt, Replit, v0) give you, and where they hit their limits.

## Before you start

Chapter 3 (Software, Code and Data) introduced programs, Python, open source and Git, and this chapter builds directly on it. Chapter 25 (Mastering the Chat Interface) taught clear briefing, which turns out to be the core skill of AI-assisted building. Chapter 26 (APIs) explained how programs talk to models, and Chapter 28 (Tools and Agents) explained the agent loop, tool calls, MCP and instruction files such as AGENTS.md. Security gets one section here; Chapter 31 covers it in depth.

## How software gets built, in plain words

You have used software every day for years, but you may never have seen how it is made. That matters now, because AI agents build software the same way human teams do. They use the same folders, the same history tools, the same tests and the same launch steps. If you understand the workshop, you can supervise the robot working in it.

Throughout this chapter we will follow one small project: a **Book Club Picker**, a web page where members of a book club list books they want to read and the page picks the next one. Version 1 is just for you. Version 2 lets the whole club log in and vote. Version 3 collects membership fees. Each version raises the stakes, and you will see how the right tool and the right amount of caution change as it grows.

### What an app is made of

When you open a weather app, it feels like one thing. Underneath, it is several pieces that talk to each other.

> **Definition — Source code:** The human-readable instructions that make up a program, written in a programming language such as Python or JavaScript and stored as plain text files.

The part you see and touch is the frontend. It runs on your phone or in your browser.

> **Definition — Frontend:** The part of an app that runs on your device and that you see and interact with: buttons, text, layout. On the web it is usually written in HTML, CSS and JavaScript.

The part you never see is the backend. It runs on a server in a data center and does the work that cannot or should not happen on your device, such as checking your password or fetching forecasts from a weather service.

> **Definition — Backend:** The behind-the-scenes part of an app that runs on servers, handling logic, security checks and communication with databases and other services.

Most apps also need to remember things between visits: your saved cities, your account, the list of books.

> **Definition — Database:** An organized store of data that a program can save to and read from reliably, usually as tables of rows and columns. It is the app's long-term memory.

All of this has to live somewhere that other people can reach.

> **Definition — Hosting:** Renting space on servers (usually in the cloud) so that your app is reachable on the internet at a web address, day and night.

Almost nobody writes everything from scratch. Programs lean on code that other people wrote and shared.

> **Definition — Dependency:** A piece of outside code (a library or package) that your project relies on. A typical web app has dozens or hundreds of dependencies, each one a possible source of bugs or security problems.

> **Definition — Framework:** A large, opinionated set of ready-made code that gives a project its basic structure, such as React for web frontends or Django for Python backends. You fill in your parts; the framework handles the plumbing.

For the Book Club Picker, version 1 can be a single web page with no backend and no database: the book list lives in your browser. Version 2 needs a backend, a database and logins, because many people must see the same list. That jump, from "one file on my computer" to "a system other people depend on", is the most important line in this whole chapter.

```mermaid
flowchart LR
    A["You in a browser"] --> B["Frontend<br/>buttons and pages"]
    B --> C["Backend<br/>logic and security checks"]
    C --> D["Database<br/>books, members, votes"]
    C --> E["Other services<br/>email, payments, AI models"]
    F["Hosting<br/>servers in the cloud"] -.-> B
    F -.-> C
    F -.-> D
```

*Figure 29.1: The anatomy of a typical web app. Version 1 of the Book Club Picker needs only the frontend; versions 2 and 3 need everything.*

### Git: a time machine for code

Imagine writing a long document with five friends, where any change might break something and you need to know exactly who changed what, when and why. Programmers solved this problem decades ago with version control. You met the idea in Chapter 3; here is the working vocabulary, because every coding agent speaks it.

> **Definition — Version control:** A system that records every change to a set of files over time, so you can see the full history, compare versions and go back to any earlier state.

> **Definition — Git:** The free, open-source version control program used by almost all software projects. It runs on your own computer and keeps the complete history of a project in a hidden folder.

> **Definition — Repository (repo):** A project's folder of files plus its complete Git history. "Clone the repo" means "download the project with its history".

The basic unit of history is the commit.

> **Definition — Commit:** A saved snapshot of changes in a repository, with a short message explaining what changed and why, plus the author and time. Commits are the save points you can return to.

When you look at a commit, you see a diff.

> **Definition — Diff:** A side-by-side or line-by-line view of what changed between two versions of a file: lines removed are usually shown with a minus sign and lines added with a plus sign.

Here is a real-looking diff for the Book Club Picker, where someone changed how many books can be on the shortlist:

```diff
- const MAX_SHORTLIST = 5;
+ const MAX_SHORTLIST = 8;
```

Reading diffs is the single most useful code skill for a non-programmer supervising an AI. You do not need to write that line to notice that the number changed from 5 to 8 and to ask "did I ask for that?"

To try something without disturbing the working version, programmers make a branch.

> **Definition — Branch:** A separate line of development inside a repository. You can experiment on a branch while the main version (usually called "main") stays untouched.

> **Definition — Merge:** Combining the changes from one branch into another, typically folding a finished feature branch back into main.

If two branches changed the same lines in different ways, Git cannot combine them automatically; this "merge conflict" must be settled by a person or an agent.

```
main     o----o----o-------------------o   <- merge
               \                       /
feature         o-------o-------o-----o
               "add      "write  "fix
                picker"   tests"  typo"
```

*Figure 29.2: A feature branch splits off main, collects three commits, and is merged back once it works.*

Git runs on your computer. To share a repository, people use a hosting site.

> **Definition — GitHub:** The most popular website for storing Git repositories online and collaborating on them, owned by Microsoft. GitLab and Bitbucket are alternatives.

> **Definition — Push and pull:** Pushing sends your new commits from your computer up to the shared copy online; pulling brings other people's new commits down to you. Cloning makes your first full copy of a repository.


The most important ritual in professional software is the pull request.

> **Definition — Pull request (PR):** A proposal to merge a branch into main, shown as a web page with the full diff, a description, automated test results and a comment thread. Nothing merges until someone approves it.

> **Definition — Code review:** Another person (or a reviewing tool) reading the diff in a pull request to catch bugs, security problems and confusing code before it is merged.

> **Analogy:** Git is a time machine with a logbook. Every commit is a dated, labeled photograph of the project. Branches are parallel universes where you can try risky things. A pull request is asking the editor to accept your chapter draft, with tracked changes visible to everyone.

### Tests: code that checks code

Here is the idea that makes AI coding work at all. Programmers write small extra programs whose only job is to check that the real program behaves correctly.

> **Definition — Automated test:** A small piece of code that runs part of a program with known inputs and checks that the output is what it should be. It reports "pass" or "fail" in seconds, with no human needed.

> **Definition — Unit test:** An automated test that checks one small unit of code, usually a single function, in isolation.

> **Definition — Test suite:** The full collection of a project's automated tests, usually run all together with a single command.

Suppose the Book Club Picker has a function that splits the cost of a shared book order. Here is the function and a test for it, in Python:

```python
def split_cost(total, members, shipping=5.0):
    """Return what each member pays, rounded to the cent."""
    return round((total + shipping) / members, 2)

def test_split_cost():
    # 4 books at $15 = $60, plus $5 shipping = $65, split 5 ways = $13.00
    assert split_cost(60, 5) == 13.0
    # Free shipping: $60 split 4 ways = $15.00
    assert split_cost(60, 4, shipping=0) == 15.0
```

The word `assert` means "this must be true, or the test fails". Running the suite takes a fraction of a second. Now imagine someone, human or AI, later changes the default shipping to $7 without telling anyone. The first check computes (60 + 7) / 5 = 13.40, which is not 13.00, so the test fails and points at the exact line. That is the whole point.

> **Definition — Regression:** A change that breaks something that used to work. Test suites exist largely to catch regressions automatically.

> **Key idea:** Tests are the eyes of a coding agent. A model cannot see whether its code works just by reading it, any more than you can tell whether a cake is cooked by reading the recipe. Running the tests is how it finds out. A project with good tests can be handed to an agent; a project with none is a gamble.

### From your laptop to the world: deploying

Code on your laptop helps nobody else. Getting it onto servers is called deploying.

> **Definition — Localhost:** Your own computer acting as a server for itself. While building, programmers open addresses like `http://localhost:3000` to see the app running privately on their machine.

> **Definition — Deploy:** Copying a version of your code onto the servers where it will run for real users, and switching it on. Many teams deploy several times a day.

> **Definition — Production:** The live version of an app that real users depend on. Careful teams first try changes on "staging", a private copy of production.


Modern teams automate the checks between "I changed something" and "users see it".

> **Definition — CI (continuous integration):** An automated service that runs the test suite (and other checks) every time someone pushes code or opens a pull request, and marks the change green or red. GitHub Actions is a common example.

Put together, the professional route from idea to users looks like this, and a well-run coding agent follows the same route:

```mermaid
flowchart TD
    A["Idea or bug report"] --> B["Create a branch"]
    B --> C["Edit code and tests"]
    C --> D["Commit with a message"]
    D --> E["Open a pull request"]
    E --> F{"CI runs the test suite"}
    F -->|Red| C
    F -->|Green| G{"Human code review"}
    G -->|Changes requested| C
    G -->|Approved| H["Merge into main"]
    H --> I["Deploy to staging"]
    I --> J["Deploy to production"]
```

*Figure 29.3: The path from idea to users. Every arrow back to "Edit code" is a safety net catching a mistake before users see it.*

### The terminal

Many coding agents live in a plain text window.

> **Definition — Terminal (command line):** A text window where you type commands to your computer instead of clicking. Programmers use it to run programs, tests and Git; several leading coding agents run inside it.

A few commands you will see an agent run, and what they mean:

| Command | What it does in plain words |
|---|---|
| `git status` | Show which files have changed since the last commit |
| `git log --oneline` | List recent commits, one per line |
| `git diff` | Show exactly what changed, line by line |
| `pytest` or `npm test` | Run the test suite (Python or JavaScript) |
| `git checkout -b picker` | Create and switch to a new branch called "picker" |

> **Key idea:** Git, tests and review together form a safety net. AI has made typing code nearly free, but it has not made mistakes free. The net is what lets you move fast without falling: you can undo any commit, tests catch regressions, and review catches what tests miss.

## From autocomplete to coding agents

AI help with code has gone through roughly five generations in five years. The change between them is not mainly that models got smarter, although they did. The change is who drives the work loop: you, or the AI.

> **Definition — IDE (integrated development environment):** The app programmers write code in, combining a text editor, file browser, terminal and debugging tools. VS Code, JetBrains IDEs and Cursor are examples.

```mermaid
timeline
    title Five generations of AI coding help
    2021 : Autocomplete
         : GitHub Copilot preview suggests the next lines as grey ghost text
    2023 : Chat in the editor
         : Ask questions about your code in a side panel
         : AI-first editors such as Cursor appear
    2024 : Agent mode in the IDE
         : The assistant edits many files and runs commands
         : Devin and Replit Agent pitch autonomous building
    2025 : Terminal and cloud agents
         : Claude Code in February and OpenAI Codex in May
         : Agents work in the background and open pull requests
    2026 : Fleets of parallel agents
         : Many agents on many tasks at once
         : Scheduled and long-running agents
```

*Figure 29.4: The evolution of AI coding tools. Each step hands more of the loop to the AI.*

**Generation 1: autocomplete (2021).** GitHub Copilot's 2021 preview watched you type and suggested the next line or the rest of a function as faded text. You pressed Tab to accept.

> **Definition — Code completion (autocomplete):** An AI feature that predicts the next few words or lines of code as you type and offers them as a suggestion you can accept or ignore.

This is next-token prediction (Chapter 18) aimed at code. You still decided everything; the AI saved keystrokes.

**Generation 2: chat in the editor (around 2023).** A chat panel inside the editor let you highlight code and ask "why does this crash?" or "write a function that sorts books by votes". The AI wrote bigger pieces, but you copied, pasted, ran and fixed.

**Generation 3: agent mode in the IDE (2024).** Now the assistant could change several files itself and run commands such as the test suite, then read the errors and try again. This is the agent loop from Chapter 28 applied to a codebase.

> **Definition — Agent mode:** A setting in coding tools where the AI, rather than just suggesting text, carries out a multi-step task: it opens and edits files, runs commands and reacts to the results until the task is done or it needs your input.

**Generation 4: terminal and cloud agents (2025).** Anthropic released Claude Code, a coding agent that runs in the terminal, as a research preview on February 24, 2025, and made it generally available in May 2025. OpenAI launched Codex in May 2025. These agents read whole repositories, made plans, worked for many minutes at a time, and could run in the cloud while you did something else.

> **Definition — Coding agent:** An AI agent specialized in software work. It reads a codebase, plans changes, edits files, runs tests and commands, fixes its own errors and can commit and open pull requests.

> **Definition — Background agent (cloud agent):** A coding agent that runs on a remote machine for minutes to hours while you do other things, then reports back, typically by opening a pull request for you to review.

**Generation 5: fleets of agents (2026).** By 2026 the main products let one person launch many agents in parallel, each on its own branch in its own sandbox, and schedule agents to run on their own (for example, every night: "check for failing tests and propose fixes"). GitHub's cloud agent lets you assign an issue to an agent the way you would assign it to a colleague.

| Generation | You do | The AI does | Unit of work |
|---|---|---|---|
| Autocomplete | Everything except typing | Guesses the next line | A line |
| Chat in editor | Decide, paste, run, fix | Writes functions on request | A function |
| Agent mode | Approve and steer | Edits files, runs tests, iterates | A task |
| Terminal and cloud agents | Write the brief, review the PR | Plans and implements end to end | An issue or PR |
| Fleets | Manage a queue of agents | Many tasks in parallel | A project |

> **At the frontier (2026):** The leading tools now treat the human as a manager of agents rather than a writer of code. Engineers at frontier labs describe days spent writing specs, reviewing diffs and deciding what to delegate. METR's measurements of how long a task (in human time) an agent can complete with 50% reliability grew from minutes in 2023 to many hours by 2026 (see Chapter 28 and Chapter 57), which is why delegating a whole feature has become realistic.

## Inside a coding agent

When you type "add a button that picks a random book" into a coding agent, what actually happens? The answer is the agent loop from Chapter 28, running on a computer with a repository and a terminal.

### The harness and its tools

The model itself only produces text. Everything else comes from the harness around it.

> **Definition — Harness:** The software wrapped around a model that turns it into an agent: its tools, system prompt, memory handling, permission rules and loop control. The same model in a better harness performs much better.

A coding harness typically gives the model a handful of tools: read a file, search the codebase for a word, edit or create a file, run a terminal command, fetch a web page, and launch a sub-agent for a side investigation. Each time the model "uses" a tool, it actually emits a request, the harness runs it, and the result goes back into the model's context window (Chapter 28 explains this in detail).

Three features make modern coding agents much safer to use.

> **Definition — Plan mode:** A coding-agent setting in which the agent investigates the code and writes a step-by-step plan for your approval before it changes anything.

> **Definition — Permission prompt:** A pause in which the agent asks you to approve a specific action, such as running a command, editing a file or pushing to GitHub. You can usually allow an action once, always, or never.

> **Definition — Sandbox:** An isolated environment, such as a container or virtual machine, where an agent can run code and commands without being able to damage your real files, accounts or network.

And every project can carry standing instructions for agents, as Chapter 28 described.

> **Definition — Instruction file (AGENTS.md or CLAUDE.md):** A plain-text file at the top of a project that coding agents read automatically before working: how to run the tests, coding conventions, what never to touch. It is a README written for agents.

### The loop, step by step

```mermaid
flowchart TD
    A["Read the brief and AGENTS.md"] --> B["Explore the repo<br/>list, search, read files"]
    B --> C["Write a plan"]
    C --> D{"Human approves plan?"}
    D -->|No, revise| C
    D -->|Yes| E["Edit files"]
    E --> F["Run tests and commands"]
    F --> G{"All tests pass?"}
    G -->|No| H["Read the error message"]
    H --> E
    G -->|Yes| I["Commit with a clear message"]
    I --> J["Open a pull request"]
    J --> K["Human reviews the diff"]
```

*Figure 29.5: The coding-agent loop. The inner cycle of edit, test, read error, edit again is where most of the work happens.*

Here is what a session on the Book Club Picker might look like, narrated in plain English. You type: "Add a 'Pick for me' button that chooses a random book from the shortlist. Do not pick a book we have already read."

1. **Orient.** The agent reads AGENTS.md, which says "run tests with `npm test`; never edit files in /data". It lists the project's files and reads `index.html`, `app.js` and the existing tests.
2. **Plan.** In plan mode it proposes: add a function `pickBook(shortlist, alreadyRead)`; write three tests first (picks only from the shortlist, never picks a read book, handles an empty list); add the button; wire them together. You approve.
3. **Test first.** It writes the three tests and runs `npm test`. They fail, because `pickBook` does not exist yet. This is expected and good: the tests now define "done".
4. **Implement.** It writes the function. Runs the tests. Two pass; the empty-list test fails with an error message. It reads the error, adds a check for an empty shortlist, runs again. All pass.
5. **Check the rest.** It runs the full suite to make sure nothing else broke.
6. **Commit and propose.** It commits with the message "Add Pick for me button with tests", pushes the branch and opens a pull request summarizing what changed and why.
7. **You review.** You read the diff, try the button on localhost, and merge.

```mermaid
sequenceDiagram
    participant Y as You
    participant A as Agent
    participant R as Repo and terminal
    participant G as GitHub
    Y->>A: Brief - add a Pick for me button
    A->>R: Read AGENTS.md and source files
    R-->>A: File contents
    A->>Y: Proposed plan
    Y->>A: Approved
    A->>R: Write tests, run npm test
    R-->>A: 3 failing tests
    A->>R: Write pickBook, run tests
    R-->>A: 1 failure - empty list error
    A->>R: Fix and rerun all tests
    R-->>A: All tests pass
    A->>G: Push branch and open pull request
    G-->>Y: PR ready for review
```

*Figure 29.6: One coding-agent session as a conversation between you, the agent, your project and GitHub.*

### What it costs: a worked example

Agents are hungry for tokens because the loop re-sends the growing conversation to the model at every step (statelessness, Chapter 25). Let us estimate one session like the one above, using Claude Sonnet 5.5's late-2026 API prices of $2 per million input tokens and $10 per million output tokens. These are illustrative numbers, not a measurement.

- Say the session takes 30 steps, and the context at each step averages 60,000 tokens (instructions, files read so far, test output). Input: 30 × 60,000 = 1.8 million tokens.
- The agent writes about 15,000 tokens in total (plans, code, messages).
- **Without caching:** 1.8M × $2 = $3.60 input, plus 0.015M × $10 = $0.15 output. Total about **$3.75**.
- **With prompt caching** (Chapter 26): most of each step's context repeats the previous step. Suppose 90% of input tokens are cache reads, which on Sonnet 5.5 cost 0.05× the normal price ($0.10 per million). That is 1.62M × $0.10 = $0.16. The other 10% (0.18M) is new and is written to the cache at 1.25× ($2.50 per million) = $0.45. Add $0.15 output. Total about **$0.76**.

Caching cuts the bill by about 80%, which is why coding agents rely on it heavily. It also shows why research on applied AI notes that agentic tasks can use 10 to 100 times the tokens of a normal chat. If you use a coding agent through a monthly subscription (Claude's Pro plan was $20 per month and Max $100 or $200 per month in late 2026), the provider absorbs this cost within usage limits; through the API, you pay per token.

> **Watch out:** Agents can "cheat" their way to green tests. Because they are trained and rewarded to make tests pass, they sometimes edit the test itself, hard-code the expected answer, or quietly skip a failing check. This is a form of reward hacking (Chapter 55). When you review a pull request, look first at any changes to test files, and be suspicious of a test that was weakened rather than code that was fixed.

> **Definition — Reward hacking:** When an AI finds a loophole that scores well on its goal without doing the intended job, such as making a failing test pass by deleting the check instead of fixing the bug.

## The coding-agent landscape in late 2026

Coding agents became the fastest-moving market in AI during 2025 and 2026. Product names and features change monthly, so treat this table as a snapshot as of late 2026 and check current documentation before you choose.

| Product | Maker | Where it runs | Notable features (as of late 2026) |
|---|---|---|---|
| Claude Code | Anthropic | Terminal, VS Code and JetBrains, desktop app, web, mobile, Slack, GitHub Actions | CLAUDE.md (also reads AGENTS.md), skills, hooks, MCP, sub-agents, background agents, cloud scheduled tasks, an Agent SDK |
| Codex | OpenAI | ChatGPT apps, Codex CLI, IDE extension, Codex Cloud | Runs on GPT-6.1 Sol; plugins, skills, MCP, a built-in browser, computer use, code review, sub-agents, scheduled tasks |
| Cursor | Anysphere | Desktop editor and CLI | Cloud agents that run in parallel for hours, Bugbot code review, its own Composer models plus models from several labs |
| GitHub Copilot | GitHub (Microsoft) | VS Code and other editors, GitHub website, Copilot CLI | Agent mode, a cloud agent you assign issues to (Copilot, Claude or Codex), PR review; plans from Free to Enterprise |
| Antigravity | Google | Desktop app, CLI, IDE, SDK | Manages multiple local agents, browser-in-the-loop testing, Gemini 4 Argon and 3.8 Flash; free for individual developers |
| Devin and Windsurf | Cognition | Web, desktop, editor | Devin pitched as an autonomous software engineer; own SWE-series models |
| Open-source agents | Community | Terminal or editor | Cline, Aider and others let you plug in any model, including local ones (Chapter 30) |

Other notable tools include Gemini CLI, Amp, Kiro, Zed and JetBrains Junie. Most now support the same building blocks: instruction files, MCP connections to outside tools, skills, hooks (small scripts that run automatically, for example to block dangerous commands) and sub-agents, all explained in Chapter 28.

The money flowing in shows real use, although every figure here is company-reported or press-reported. Anthropic said in February 2026 that Claude Code's run-rate revenue had passed $2.5 billion, and Cognition said it crossed $1 billion in annualized run-rate revenue in September 2026. GitHub's own plans in late 2026 ran from a free tier (2,000 completions a month) through Pro at $10, Pro+ at $39 and Max at $100 per month, with Business at $19 and Enterprise at $39 per user per month.

**How to choose.** For a beginner the differences matter less than the habits you bring. Ask:

- **Where do you want to work?** A chat-style app or website (Codex in ChatGPT, Claude Code on the web) needs no installation. A terminal agent suits people comfortable typing commands. An editor (Cursor, VS Code with Copilot) suits people who want to see files side by side.
- **How do you want to pay?** Subscriptions give predictable monthly costs with usage limits; API billing scales with tokens.
- **Where does your code live?** If your team is on GitHub, tools that open pull requests there fit naturally.
- **What are the data rules?** At work, check which tools your employer has approved and what each one does with your code.

> **Watch out:** "Which coding agent is best?" has no stable answer. Roundups in October 2026 commonly ranked Claude Code first and Codex second, but rankings depend on the task, the harness and the month. Popular benchmarks such as SWE-bench Verified are close to saturated, so newer launch tables lean on harder tests such as Terminal-Bench (see Chapter 24). Try two tools on your own task before committing.

> **Try it:** Open any public repository on GitHub, for example a popular open-source project you have heard of. Click "Commits" and read three commit messages and their diffs. Then click "Pull requests" and open one with a long discussion. In ten minutes you will have seen exactly what a coding agent produces and what a human reviewer looks for.

## Vibe coding versus agentic engineering

On February 2, 2025, the AI researcher Andrej Karpathy described a new way of building software that he called vibe coding: you "fully give in to the vibes, embrace exponentials, and forget that the code even exists". You describe what you want, accept whatever the AI writes without reading it, paste error messages back in when something breaks, and keep going until it seems to work. The phrase spread so fast that Collins named "vibe coding" its Word of the Year for 2025.

> **Definition — Vibe coding:** Building software by describing what you want in plain language and accepting AI-written code without really reading or understanding it, judging only whether the result seems to work. Coined by Andrej Karpathy in February 2025.

> **Definition — Prototype:** A quick, rough version of a product built to test an idea or show it to people, not meant to be secure, complete or long-lived.

Vibe coding is genuinely wonderful for some things. A teacher can build a quiz game for a class in an afternoon. A shop owner can make a stock-counting page for their own phone. A product manager can turn a vague idea into a clickable prototype before a meeting. Software that was never worth paying a developer for is now worth building, and that is a real change in who gets to make tools.

The trouble starts when vibe-coded software leaves the playground. The evidence collected through 2025 is consistent:

- **Exposed data.** A May 2025 review of 1,645 apps built with the app builder Lovable found that 170 had a flaw exposing personal data.
- **Security not keeping up.** Veracode reported in October 2025 that the security of AI-generated code had not improved as its functionality had.
- **More issues per change.** One industry analysis (CodeRabbit, December 2025) found that pull requests co-written by AI had about 1.7 times more major issues and 2.74 times more security vulnerabilities than human-only ones.
- **Destructive mistakes.** In July 2025, Replit's agent deleted a user's production database during a declared code freeze, a story that became the standard cautionary tale.

> **Definition — Security vulnerability:** A flaw in software that an attacker could exploit to steal data, take control or cause damage, such as a database that anyone on the internet can read.

> **Definition — Technical debt:** The future cost of shortcuts taken now: messy, poorly understood or untested code that makes every later change slower and riskier. Vibe coding can pile it up quickly because nobody understands the code.

The disciplined alternative goes by several names: agentic engineering, spec-driven development, or simply "using coding agents the way good engineers do".

> **Definition — Agentic engineering:** Building software with coding agents in a disciplined way: a clear written spec, an approved plan, tests written first, small reviewed changes, instruction files, automated checks and sandboxes. The human stays responsible for design and review.

> **Definition — Spec (specification):** A written description of what a piece of software must do, for whom, with what constraints and how you will know it works. A good spec is the brief you hand a coding agent.

The practices are simple to list and take discipline to keep:

1. **Write the spec first.** What it does, who uses it, what data it touches, what "done" looks like.
2. **Use plan mode.** Read and approve the plan before any file changes.
3. **Tests first.** Ask for tests that define success, and watch them fail before the code is written.
4. **Small diffs.** One feature per branch and per pull request, so each change is reviewable in minutes.
5. **Review every diff.** Especially changes to tests, security settings, and anything touching data or money.
6. **Keep an instruction file.** Put the rules the agent keeps forgetting into AGENTS.md or CLAUDE.md.
7. **Automate the checks.** CI runs the tests on every pull request.
8. **Contain the blast radius.** Sandboxes, copies of data, no production credentials on the agent's machine, and approval prompts for anything destructive.

| | Vibe coding | Agentic engineering |
|---|---|---|
| The brief | A one-line wish | A written spec with acceptance tests |
| Planning | None; start typing | Plan mode, human approves |
| Testing | "Click around and see" | Automated tests written first, run in CI |
| Review | Accept all changes | Read every diff, especially tests and security |
| Size of changes | Huge rewrites | Small, focused pull requests |
| Where it runs | Your real files and accounts | Sandbox, branch, copies of data |
| Best for | Prototypes, personal toys | Anything other people rely on |
| Main risk | Hidden security holes, unmaintainable code | Slower start, more effort up front |

```mermaid
quadrantChart
    title How much discipline does a project need
    x-axis Low stakes --> High stakes
    y-axis Little review --> Heavy review
    quadrant-1 Agentic engineering
    quadrant-2 More process than needed
    quadrant-3 Vibe coding is fine
    quadrant-4 Danger zone
    Party countdown page: [0.12, 0.15]
    Personal budget sheet: [0.3, 0.25]
    Club voting site: [0.55, 0.45]
    Vibe-coded payments app: [0.85, 0.15]
    Clinic booking system: [0.88, 0.85]
    Internal team dashboard: [0.45, 0.7]
```

*Figure 29.7: Match the discipline to the stakes. The danger zone is high-stakes software built with little review.*

> **Analogy:** A coding agent is a tireless, fast junior developer. It needs a clear ticket, it does better with tests as guardrails, and it should never merge its own work without review. Vibe coding is letting the junior push straight to production on their first day because the demo looked nice.

> **Try it:** Before your next build, ask your chatbot: "Interview me, one question at a time, to write a one-page spec for a small app. Cover who uses it, what data it stores, what must never happen, and three tests that prove it works." Ten questions later you will have a better brief than most people give a coding agent.

## Does AI actually make programmers faster?

It feels obvious that it does. The best-designed study so far says "not always, and not in the way people think".

> **Definition — Randomized controlled trial (RCT):** An experiment in which tasks or people are randomly split into groups that get different treatments (here, AI allowed or not), so that any difference in results can be credited to the treatment rather than to luck or selection.

In July 2025, the research nonprofit METR published an RCT with 16 experienced open-source developers working on real tasks in large, mature projects they knew well. Each task was randomly assigned "AI allowed" (mostly Cursor with Claude 3.5 and 3.7 Sonnet, the tools of early 2025) or "AI not allowed". The result: with AI, the developers took **19% longer**. Even more striking, afterwards they believed AI had made them about **20% faster**. They predicted a speed-up beforehand, experienced a slowdown, and still remembered a speed-up.

Why might experts on familiar code be slower with AI? Plausible reasons include the time spent writing prompts, waiting for the model and reviewing its output; very high quality standards in mature projects, so much AI code needed rework; and the fact that these developers already knew their codebases so well that the AI had little to add. Other studies point the other way for other people: customer-support agents using an AI assistant resolved about 14% more issues per hour, with gains of about 34% for novices, and consultants in a large experiment did better on tasks inside the AI's "jagged frontier" of competence but worse on tasks just outside it (see Chapter 60).

The strongest case that AI coding is a big productivity gain:

- The 2025 study used early-2025 tools. Agents improved enormously during 2025 and 2026; the length of task they can complete reliably has been doubling every few months.
- Real money and usage followed: billions of dollars of annual revenue for coding tools, and millions of weekly users, are hard to explain if the tools did not help.
- Gains are largest exactly where the METR developers were weakest candidates: unfamiliar code, new projects, prototypes, and people who could not code at all before.

The strongest case for caution:

- Feeling faster is not being faster. People are poor judges of their own productivity, which is why the study design mattered.
- Writing code was never most of the job. Understanding the problem, reviewing, debugging and maintaining take most of the time, and AI-written code can make some of those harder.
- Quality studies (above) show more issues in AI-assisted changes unless review is strong, so speed today can become debt tomorrow.

> **Key idea:** Measure, do not assume. If you or your team adopt coding agents, time real tasks with and without them and track defects afterwards. The METR result is not "AI makes you slower"; it is "your sense of speed is not evidence".

## What can a non-programmer safely build?

You now know enough to answer this with judgment rather than fear. Three questions decide almost everything:

1. **Who gets hurt if it breaks?** Just you, a few friends, or strangers and customers?
2. **Whose data does it hold?** Nothing sensitive, your own information, or other people's personal data?
3. **Can you undo a mistake?** Is there a backup, a copy, a way back?

> **Definition — Personal data:** Any information that identifies a person or relates to an identifiable person, such as names, emails, phone numbers, health details or payment information. Laws such as the EU's GDPR regulate how it is collected and protected.

Two pieces of security vocabulary matter as soon as other people log in.

> **Definition — Authentication:** Checking who someone is, usually with a password, a code sent to their phone or a "Sign in with Google" button.

> **Definition — Authorization:** Checking what a signed-in person is allowed to see and do. A common vibe-coding bug is getting authentication right but authorization wrong, so every logged-in user can read everyone's data.

| Traffic light | Examples | What to do |
|---|---|---|
| Green: build it yourself | Personal tools, one-person trackers, scripts that tidy your own files (run on a copy first), prototypes, games for your family, automations on your own accounts | Vibe coding is fine; keep a backup and Git history |
| Yellow: build it, then get a review | Tools shared with your team, internal dashboards on company data, a club website with logins | Use agentic-engineering habits, ask the agent for a security review, then have a technical colleague look before launch |
| Red: call a professional | Taking payments, health or children's data, anything regulated, logins for the public, anything that must not go down, apps at scale | Build a prototype to show what you want, then hand it to engineers |

Applied to the running example: version 1 of the Book Club Picker (just you, no data worth stealing) is green. Version 2 (members log in and vote) is yellow: the risk is that a bug shows members' emails to everyone, so get a review. Version 3 (collecting fees) is red. Payment card data is covered by strict industry rules, and health, financial and children's data carry legal duties in many countries. Use an established payment service and a professional.

```mermaid
flowchart TD
    A["I want to build a tool"] --> B{"Will anyone other than me use it?"}
    B -->|No| C{"Could a mistake delete or leak<br/>something I cannot replace?"}
    C -->|No| D["Green - build it yourself"]
    C -->|Yes| E["Work on copies, keep backups,<br/>then build it yourself"]
    B -->|Yes| F{"Does it handle money, health data,<br/>children or other regulated data?"}
    F -->|Yes| G["Red - prototype, then hire a professional"]
    F -->|No| H{"Does it store other people's<br/>personal data or need logins?"}
    H -->|Yes| I["Yellow - build carefully, get a security review"]
    H -->|No| J["Green or yellow - share with care"]
```

*Figure 29.8: A quick decision guide for what to build yourself.*

> **Watch out:** "The app builder handles security" is not a plan. The tools have improved their defaults, but the May 2025 finding of data-exposing flaws in about one in ten reviewed apps came from apps whose owners assumed exactly that. If other people's data is involved, someone who understands access rules must check them.

## No-code automation: making your apps talk to each other

Not every problem needs an app. Many of the most valuable "builds" are automations: when something happens in one app, do something in another. Every receipt email gets logged in a spreadsheet. Every new form entry gets a summary posted to your team chat. Every Friday, a report is compiled and emailed.

> **Definition — No-code:** Building software by connecting visual blocks and filling in forms instead of writing code. "Low-code" means mostly visual, with small bits of code where needed.

> **Definition — Automation platform:** A service such as Zapier, Make or n8n that connects many apps and runs workflows between them on your behalf, around the clock, without you writing a program.

Every automation has the same shape.

> **Definition — Trigger:** The event that starts an automation, such as "a new email arrives with the label Receipts", "a form is submitted" or "every Monday at 9 a.m.".

> **Definition — Action:** A step an automation performs, such as adding a row to a spreadsheet, sending a message or creating a calendar event.

> **Definition — Workflow:** The full chain of a trigger followed by one or more actions, filters and branches. Zapier calls a workflow a "Zap" and Make calls it a "scenario".

How does the automation platform find out that something happened? Either it keeps asking every few minutes ("polling", which is simple but slow), or it gets told.

> **Definition — Webhook:** A web address that one app calls automatically, sending a small message of data, the moment something happens. It is how apps "ring the doorbell" of an automation instead of being checked repeatedly.

```mermaid
sequenceDiagram
    participant F as Online form
    participant W as Webhook URL
    participant Z as Automation platform
    participant M as AI model
    participant S as Spreadsheet
    F->>W: New entry submitted - sends JSON data
    W->>Z: Wakes up the workflow
    Z->>M: Summarize and classify this entry
    M-->>Z: Category and one-line summary
    Z->>S: Append a row
    Z-->>F: 200 OK - message received
```

*Figure 29.9: A webhook in action. The form tells the automation platform the instant something happens; no polling needed.*

Since 2023 the platforms have added AI in two forms.

> **Definition — AI step:** A step inside an automation that sends data to a language model with an instruction ("extract vendor, date and total as JSON") and passes the model's answer to the next step.

> **Definition — AI agent node:** An automation step that runs a full agent loop (Chapter 28): the model gets a goal plus a set of tools and decides for itself which actions to take, rather than following fixed steps.

### The three big platforms

| Platform | Style | Strengths | Things to know (as of late 2026) |
|---|---|---|---|
| Zapier | Simple linear steps, huge app catalog | Easiest to start; Zapier Agents work across 9,000+ apps | Pricing grows with the number of tasks run |
| Make (formerly Integromat) | Visual canvas with branches and loops | Handles complex, branching flows | Steeper learning curve than Zapier |
| n8n | Visual canvas, open and technical | Can be self-hosted on your own server; AI agent nodes and an AI workflow builder | "Fair-code" license: source available, with limits on commercial use |

> **Definition — Self-hosting:** Running software on a server you control instead of using the vendor's hosted service, which gives you control over data and cost but makes you responsible for upkeep.

### Worked example: the receipt logger

You want every receipt email logged in a Google Sheet with vendor, date, total and category.

1. **Trigger:** new Gmail email with the label "Receipts".
2. **AI step:** "Extract vendor, date, total and category from this email. Reply only as JSON with those four fields." (Structured output, Chapter 26.)
3. **Action:** append a row to the "Expenses" sheet.
4. **Error path:** if the AI step fails or the total is missing, send yourself a notification.

What does the AI part cost? Say 100 receipts a month, each about 1,000 tokens of email in and 100 tokens of JSON out, on a small model like Claude Haiku 5.5 at $0.10 per million input tokens and $0.50 per million output tokens (late-2026 prices). Input: 100,000 tokens × $0.10 per million = $0.01. Output: 10,000 tokens × $0.50 per million = $0.005. Total: **about 1.5 cents a month.** The automation platform's subscription will cost far more than the AI; the model is almost free at this scale.

```mermaid
flowchart LR
    A["Trigger<br/>new email labeled Receipts"] --> B["AI step<br/>extract fields as JSON"]
    B --> C{"Total found?"}
    C -->|Yes| D["Action<br/>append row to sheet"]
    C -->|No| E["Action<br/>notify me to check by hand"]
    D --> F["Weekly digest<br/>email summary on Friday"]
```

*Figure 29.10: The receipt logger as a workflow, with an error path so failures are not silent.*

> **Watch out:** Automations fail silently. A password change, an expired connection or an email in a new format can stop a workflow for weeks before you notice. Always add an error notification, check the run history weekly at first, and test with a few fake inputs before trusting it.

> **Watch out:** An automation that reads emails from strangers and can also send messages, move money or share files is exactly the "lethal trifecta" of Chapter 31: private data, untrusted content and a way to send things out. A cleverly worded email could instruct the AI step to forward your data elsewhere. Keep automations that read untrusted input on a short leash: no sending, paying or deleting without your approval.

> **Try it:** Go to webhook.site in your browser. It gives you a unique test URL. Open a new tab and paste that URL with `?book=Dune&votes=3` added to the end. Switch back: you will see the request arrive, with your two values inside. That is all a webhook is: one app knocking on a URL with a little data.

## AI app builders: describe it, get an app

The newest way to build is to describe a whole app in a chat box and get back a working, hosted web app with pages, a database and logins.

> **Definition — AI app builder:** A web service such as Lovable, Bolt, Replit Agent or v0 that turns a plain-language description into a working web app, writing the code with an agent and hosting the result for you, usually with a database and user logins included.

You have already used the smallest version of this idea: artifacts and canvas in chat apps (Chapter 25), where the chatbot builds a small interactive page beside the conversation. App builders take the same idea to full applications. The well-known ones in late 2026:

- **Lovable**, which started life as GPT Engineer in Stockholm, is a chat-driven builder for full web apps, often connected to a hosted backend for the database and logins. It grew extremely fast; it reportedly raised money at a valuation of about $13.3 billion in August 2026.
- **Bolt** (from StackBlitz) builds and runs apps entirely inside your browser.
- **Replit Agent**, launched in September 2024, builds inside Replit's online coding environment, where you can also see and edit the code.
- **v0** (from Vercel) focuses on polished interface components and web apps that deploy to Vercel's hosting.
- **Base44** and others target simple business apps.

Under the hood, each is a coding agent (everything in the earlier sections) running in the vendor's sandbox, with a database service and hosting pre-wired. That is their great strength: the most painful parts of building, such as setting up servers, databases and logins, are done for you in minutes.

### Their limits

**Security defaults.** The database is usually protected by access rules that decide which logged-in user can read which rows.

> **Definition — Access rules (row-level security):** Settings on a database that decide, row by row, which users may read or change which data, for example "members can see only their own votes". Missing or wrong rules are the most common cause of data leaks in app-builder apps.

The builders now include security scanners and prompt you to set these rules, but you must still check them. Ask the builder to "run a security review and explain every table's access rules in plain English", then test by logging in as two different users.

**Lock-in.** Your app may depend on the builder's hosting, database and credits.

> **Definition — Vendor lock-in:** Being so dependent on one company's product that leaving it would be expensive or difficult. Most app builders reduce this by letting you export your code to GitHub, which you should do early.

**Costs at scale.** Builders typically charge a monthly subscription plus usage credits for each AI edit, and hosting and database costs grow with users. A tool that costs a few dollars a month for you alone can cost much more for thousands of users.

**The last 20%.** The first 80% of an app arrives astonishingly fast. The last 20% (edge cases, performance, unusual integrations, fixing a bug the agent keeps reintroducing) can take longer than everything else, and this is where non-programmers most often get stuck.

**The hand-off.** If the app succeeds, engineers will eventually take it over. Code exported to GitHub, a written spec, and a list of known problems make that hand-off cheap. A tangle nobody understands makes it expensive, and a whole small industry of "rescue" services has grown up to harden vibe-coded apps for production.

```mermaid
flowchart TD
    A["Your description in chat"] --> B["Builder's coding agent<br/>writes frontend and backend"]
    B --> C["Hosted database<br/>with access rules"]
    B --> D["Login service<br/>authentication"]
    B --> E["Hosting at a public URL"]
    C --> F{"Access rules checked?"}
    F -->|No| G["Risk - any user may read all data"]
    F -->|Yes| H["Safer to share"]
    B --> I["Export code to GitHub"]
    I --> J["Hand-off to engineers later"]
```

*Figure 29.11: What an AI app builder assembles for you, and the two checkpoints you must not skip.*

> **At the frontier (2026):** The lines between these categories are blurring. App builders now offer agent modes that work for long stretches, coding agents now deploy apps and run browsers to test them, and chat apps build small apps in artifacts and canvases. Automation platforms build workflows from a description. The skill that transfers across all of them is the same: a clear spec, a habit of testing, and judgment about stakes.

## Choosing the right tool for the job

| Your goal | Best first tool | Why |
|---|---|---|
| A one-off calculator, chart or small interactive page | Artifact or canvas in your chat app | Nothing to install; done in minutes |
| Connect apps you already use and run every day | Automation platform (Zapier, Make, n8n) | Built for triggers, schedules and app connections |
| A small web app with logins and a database | AI app builder (Lovable, Bolt, Replit, v0) | Hosting, database and logins pre-wired |
| A script that works on files on your computer | Coding agent (Claude Code, Codex, Cursor, Antigravity) | Can read and change local files, with Git as a safety net |
| A change to an existing codebase at work | Coding agent with plan mode, tests and pull requests | Fits the team's review process |
| Anything with payments, health data or the public at scale | A professional engineer, with your prototype as the spec | Legal and security stakes are too high to learn on |

> **Key idea:** You do not need to become a programmer to build useful software in 2026, but you do need to think like a careful one: write down what you want, test that you got it, keep a way back, and match your caution to who could get hurt.

## In plain English

Software is built in a workshop with a few standard tools. The code lives in a repository, and Git keeps a complete history of every change, so nothing is ever truly lost. People work on branches and propose changes through pull requests, where tests run automatically and a human reviews the diff before anything goes live. Tests matter most of all: they are tiny programs that check the real program, and they are how anyone, human or AI, knows the code actually works.

AI coding help has moved from suggesting the next line (2021) to agents that take a task, make a plan, edit files, run the tests, fix their own errors and open a pull request for you to review. Claude Code, Codex, Cursor, Copilot, Antigravity and Devin are the big names in late 2026, and they all work the same basic way. They burn lots of tokens, so caching and subscriptions matter.

Vibe coding, which means accepting AI code without reading it, is great for personal tools and prototypes and risky for anything other people depend on. The careful version, agentic engineering, adds a spec, a plan, tests first, small changes and review. Evidence on speed is mixed: in one careful 2025 study, experienced developers were 19% slower with AI but felt 20% faster, so measure rather than assume.

If you cannot code, you can still build. Automation platforms like Zapier, Make and n8n connect your apps with triggers, actions and webhooks, with cheap AI steps inside. App builders like Lovable, Bolt, Replit and v0 turn a description into a hosted app. Build green-light projects yourself, get reviews for yellow ones, and hand red ones (payments, health data, the public at scale) to professionals.

## Key terms

Source code, frontend, backend, database, hosting, dependency, framework, version control, Git, repository, commit, diff, branch, merge, GitHub, push and pull, pull request, code review, automated test, unit test, test suite, regression, localhost, deploy, production, CI (continuous integration), terminal, IDE, code completion, agent mode, coding agent, background agent, harness, plan mode, permission prompt, sandbox, instruction file, reward hacking, vibe coding, prototype, security vulnerability, technical debt, agentic engineering, spec, randomized controlled trial, personal data, authentication, authorization, no-code, automation platform, trigger, action, workflow, webhook, AI step, AI agent node, self-hosting, AI app builder, access rules, vendor lock-in.

## Exercises

1. **[Easy] Read a repository like a detective.** No installation needed.
   1. Go to github.com and open the page of any well-known open-source project (search for a tool you have heard of, or try the repository of an open-source coding agent such as Aider or Cline).
   2. Find and open the instruction or contributor file (README.md, CONTRIBUTING.md, or AGENTS.md if present). Write down how the project runs its tests.
   3. Click "Commits". Open three commits and, for each, write one sentence describing what changed, using only the diff.
   4. Open the "Pull requests" tab, pick a closed one with several comments, and note one thing a reviewer asked the author to change.
   **What you'll learn:** the vocabulary of repositories, commits, diffs and reviews, which is exactly what a coding agent produces for you to check.

2. **[Easy] Interview-driven spec.** In any chatbot, paste: "Interview me one question at a time to write a one-page spec for a personal web tool: a Book Club Picker (or a tool of your choice). Cover who uses it, what it stores, what must never happen, the screens, and three acceptance tests. When done, write the spec in Markdown." Answer its questions, then ask it to "list the three riskiest assumptions in this spec".
   **What you'll learn:** a spec is the brief that decides most of the quality of AI-built software, and writing one is a skill you already have.

3. **[Easy] A mini-app in an artifact.** In Claude (artifacts), ChatGPT (canvas) or Gemini (canvas), paste your spec from Exercise 2 and ask for a single-page version that stores the list only in the browser. Then request three changes one at a time (for example: "add a Pick for me button that never picks a book marked as read", "add dark mode", "export the list as a CSV file"). After each change, test it yourself before asking for the next.
   **What you'll learn:** iterative specification, testing after each change, and that the smallest "app" needs no hosting or database.

4. **[Medium] Build a personal tool with an AI app builder.** Use the free tier of Lovable, Bolt, Replit or v0.
   1. Paste your spec and ask for a habit tracker or the Book Club Picker with user logins and a database.
   2. Create two test accounts and add data to each. Check that account A cannot see account B's data.
   3. Ask the builder: "Run a security review. Explain every database table's access rules in plain English and list anything that could expose data."
   4. Fix what it finds, export the code to GitHub if the tool allows it, and share the link with one friend for feedback.
   **What you'll learn:** how fast app builders are, where authentication and authorization go wrong, and why you check access rules yourself.

5. **[Medium] Automate a weekly chore.** Pick a real repetitive task, such as logging receipts, saving email attachments to a folder, or posting a weekly summary of a shared sheet. In the free tier of Zapier, Make or n8n cloud:
   1. Choose the trigger (for example, a Gmail label or a weekly schedule).
   2. Add an AI step with a precise instruction and a fixed output format (for example, JSON with named fields).
   3. Add the action (for example, append a row to Google Sheets).
   4. Add an error path that notifies you when a step fails or a field is missing.
   5. Test with three fake inputs, including one deliberately weird one, and read the run history.
   **What you'll learn:** triggers, actions, AI steps and structured output, and that automations need error handling because they fail silently.

6. **[Easy] See a webhook with your own eyes.** Open webhook.site and copy your unique URL. In a new browser tab, paste the URL followed by `?task=laundry&done=yes` and press Enter. Return to webhook.site and inspect the request: find your two values, the time, and the "method" (GET). Then, if your automation platform offers a "catch webhook" trigger, point a free online form tool at it and submit the form.
   **What you'll learn:** a webhook is simply an app sending a small message to a URL the moment something happens.

7. **[Medium] Have a coding agent build a tiny web page.** Use Claude Code, Codex (including the version inside ChatGPT), Cursor or Antigravity; web-based versions need no installation.
   1. Start a new, empty project folder or repository.
   2. Create a file called AGENTS.md containing: "Explain each step to a beginner. Write tests before code. Commit after each working step with a clear message. Never delete files without asking."
   3. In plan mode, ask: "Build a single web page for my book club: a list of books, a form to add one, and a Pick for me button that never picks a book marked as read. Include tests for the picking logic."
   4. Read and approve the plan, let it build, and run the page on localhost when it tells you how.
   5. Ask it to show you `git log --oneline` and explain each commit.
   **What you'll learn:** the full agent loop of plan, test, implement and commit, and how instruction files steer an agent.

8. **[Challenge] Break it, then watch the fix.** Continue from Exercise 7.
   1. Ask the agent to add a feature that splits the cost of a group book order, with tests (for example: $60 of books plus $5 shipping split 5 ways should be $13.00).
   2. Once the tests pass, edit the code yourself (or ask the agent to) so the shipping default becomes $7. Run the tests and read the failure message.
   3. Ask the agent to fix the bug. Review its diff: did it fix the code, or did it change the test? If it changed the test, ask why, and decide who was right.
   **What you'll learn:** how tests catch regressions, how to read a failure, and how to spot reward hacking in a pull request.

9. **[Challenge] Your own mini METR study.** Pick 8 small, similar tasks from your real work (writing a formula, cleaning a list, drafting a short script or document). Before starting, predict how much faster AI will make you. Flip a coin for each task to decide "AI allowed" or "no AI". Time each task with a stopwatch and rate the quality of the result from 1 to 5 the next day, without looking at which group it was in. Compare average time and quality per group with your prediction.
   **What you'll learn:** why randomization matters, and how your feeling of speed compares with measured speed.

10. **[Medium] Traffic-light audit.** List five tools you would like to build. For each, answer the three questions from this chapter (who gets hurt, whose data, can it be undone) and assign green, yellow or red. For one yellow item, write the three checks you would ask a technical reviewer to make before launch.
    **What you'll learn:** to match the level of care to the stakes before you start building, not after something goes wrong.

## Areas of opportunity

- **Automation consultant for small businesses.** Clinics, shops, agencies and trades businesses pay for someone who can wire up intake forms, invoicing, scheduling and follow-ups in Zapier, Make or n8n with AI steps, then maintain them. Productized templates for one niche (for example, an n8n intake flow for physiotherapy clinics) can be sold repeatedly.
- **"The person who builds things" inside a company.** Non-engineers who can vibe-code safe internal dashboards and trackers, and know when to escalate, become valuable quickly and often move into product or operations-engineering roles.
- **Vibe-code rescue and hardening.** Founders with a successful app-builder prototype need engineers to fix access rules, add tests, set up CI and migrate off fragile setups before real users arrive. This is a growing services market.
- **Security review for AI-built apps.** Checking authentication, authorization, database access rules and secrets in AI-generated code is a specialty in demand, given the documented rate of data-exposing flaws.
- **Agent enablement for engineering teams.** Companies adopting coding agents pay for training, instruction-file and skill libraries, review policies and measurement of real productivity, so they avoid the "feels faster, is slower" trap.
- **Technical writing for agents.** Writing AGENTS.md files, skills, specs and tool descriptions that agents read is an emerging specialty that rewards clear writers who understand the workflow.
- **Test and quality engineering.** When agents write most of the code, the people who design good test suites and acceptance criteria hold the quality bar. Testing skill becomes more valuable, not less.
- **Vertical app templates.** A builder who knows one industry (salons, sports clubs, property management) can sell ready-made, reviewed app-builder or automation templates that are safer than starting from scratch.
- **Open problems.** Maintainability of AI-written code, reliable measurement of productivity, and agent security (prompt injection through issues, emails and web pages) are unsolved and attract research and startups.

## Check your understanding

1. What is the difference between a commit, a branch and a pull request?
2. Why are automated tests described as the "eyes" of a coding agent?
3. What changed between "agent mode in the IDE" and background or cloud agents?
4. In the worked cost example, why did prompt caching reduce the cost of a coding-agent session so much?
5. What is vibe coding good for, and what three practices would you add to turn it into agentic engineering?
6. What did METR's July 2025 study find, and what is the most important lesson from it?
7. Name two features of a project that move it from "green" to "red" in this chapter's traffic-light guide.
8. What is a webhook, and why can an automation that reads strangers' emails be dangerous?

<details><summary>Answers</summary>

1. A commit is one saved snapshot of changes with a message. A branch is a separate line of development where commits can pile up without affecting main. A pull request is a proposal to merge a branch into main, showing the diff, test results and review comments, and nothing merges until it is approved.
2. A model cannot tell whether code works just by reading it. Running tests gives it objective pass or fail feedback and exact error messages, which it uses to fix its work. Without tests the agent is guessing.
3. In agent mode the AI works inside your editor while you watch and approve. Background or cloud agents run on remote machines for long periods while you do other things, then report back, usually by opening a pull request, so you review results rather than steps.
4. An agent re-sends its growing context at every step, so most input tokens are repeats of the previous step. Cached repeats are billed at a small fraction of the normal price (0.05 times on the model in the example), so the bill fell from about $3.75 to about $0.76.
5. It is good for prototypes, personal tools and quick experiments. To make it agentic engineering, add any three of: a written spec, plan mode with approval, tests written first, small diffs, reviewing every diff, an instruction file, CI, and sandboxes or copies of data.
6. Experienced developers working on their own mature projects took 19% longer with early-2025 AI tools, while believing they were about 20% faster. The lesson is that your sense of speed is not evidence: measure real outcomes, including quality.
7. Any two of: handling payments, health or children's data, other regulated data, logins for the general public, needing to stay up reliably, or running at large scale.
8. A webhook is a URL that an app calls automatically with a small data message the moment something happens. An automation that reads untrusted emails and can also send, pay or share has the lethal trifecta: a crafted email could instruct the AI step to leak data or take harmful actions, so such automations need approvals and limited permissions.

</details>

## Going deeper

- **METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (July 2025), at metr.org.** The randomized study behind the 19% result; worth reading for how careful measurement is done.
- **Anthropic, "Building effective agents" (December 2024), at anthropic.com/engineering.** A clear, influential guide to agents versus workflows that underlies how coding agents are designed.
- **Pro Git by Scott Chacon and Ben Straub (free at git-scm.com/book).** The standard, readable book on Git; the first three chapters are all a beginner needs.
- **GitHub Skills (skills.github.com).** Free, hands-on courses that walk you through repositories, branches and pull requests inside GitHub itself.
- **The Missing Semester of Your CS Education (MIT, missing.csail.mit.edu).** Short lectures on the terminal, Git and everyday programmer tools that nobody else teaches.
- **Claude Code and OpenAI Codex documentation (code.claude.com/docs and developers.openai.com).** The official guides to coding agents, including instruction files, plan mode, permissions and best practices.
- **Simon Willison's blog (simonwillison.net).** A long-running, practical and skeptical record of building with AI tools, including vibe coding and prompt-injection risks.
- **OWASP Top 10 for LLM Applications (genai.owasp.org).** The standard list of security risks for AI-powered apps and automations; essential before anything leaves the green zone.
- **Zapier, Make and n8n learning centers (zapier.com/learn, make.com/en/academy, docs.n8n.io).** Free tutorials and templates for building your first automations.
