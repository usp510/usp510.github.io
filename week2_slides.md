---
theme: seriph
title: "USP 410/510 Urban Data Science - Week 2"
info: |
  USP 410/510 Urban Data Science
  Spring 2026, Portland State University
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

# LLMs and AI Agents

## USP 410/510 | Spring 2026

Dr. Liming Wang

Portland State University

<!--
Week 2 shifts from setup and Python basics to how students should actually work with LLMs.
The tone should be practical: these tools are useful, but only with good workflow and skepticism.
-->

---
layout: section
---

# Part 1: Why This Matters

---

# Today

<v-clicks>

- What LLMs are good at in practice
- How Karpathy recommends using them (as of 2025)
- What the HDSR article found about data analysis workflows
- Takeaways
- How we will use AI tools in this course

</v-clicks>

---

# Core Claim

LLMs are not just chatbots

<v-clicks>

- They are **general-purpose interfaces** to text, code, files, and tools
- They can help with **reading, writing, coding, summarizing, translating, and analysis**
- They are most useful when treated as **collaborators**, not oracles
- In this course, the goal is **better thinking and faster iteration**
- The goal is **not** outsourcing judgment

</v-clicks>

<!--
Frame the rest of the lecture around workflow, not hype.
-->

---

# A Good Mental Model

Think of an LLM as a system that can:

<v-clicks>

- Predict plausible next text
- Work over large amounts of context
- Use tools such as **search**, **Python**, and **code editors**
- Generate drafts very quickly
- Can still produce confident nonsense (always verify its output)

</v-clicks>

<br>

<v-click>

**Implication**: LLM output is a **starting point for inspection**, not the endpoint

</v-click>

---

# Work with LLM

- Prompt, prompt engineering
- Context window, the size limit
- Thinking vs non-thinking mode
- Tool use
- Mode of interaction: chatbot vs agent

---
layout: section
---

# Part 2: How Karpathy Uses LLMs

---

# Karpathy's Practical Use Cases

From the video, several use patterns stand out:

<v-clicks>

- **Search and explanation** for unfamiliar topics
- **Reading companion** for papers, books, and technical documents
- **Python interpreter / data analysis** for calculations and code execution
- **Coding in agentic IDEs** with project files in context
- **Image and multimodal input** for extracting and interrogating information
- **Custom workflows** through persistent instructions and reusable prompts

</v-clicks>

---

# Reading With LLMs

Karpathy's workflow is simple and strong:

<v-clicks>

- Start with a **summary** of the paper or chapter
- Read the source yourself
- Ask questions when something is unclear
- Use the model to unpack unfamiliar vocabulary or background knowledge
- Go back to the original text to verify understanding

</v-clicks>

<br>

<v-click>

This is especially useful when reading outside your domain

</v-click>

---

# Tool Use Changes the Game

An LLM with tools is different from an LLM alone

<v-clicks>

- Plain chat can draft answers
- **Search** can pull in current information
- **Python / data analysis** can compute, plot, and transform files
- **IDE agents** can read and edit real code in a project
- **Memory / custom instructions** can reduce repeated setup work

</v-clicks>

<br>

<v-click>

The useful question is not "Which chatbot is best?"

It is "What tool setup fits this task?"

</v-click>

---

# Coding With LLMs

Karpathy's message is clear: for serious coding, context matters

<v-clicks>

- Web chat is often too disconnected from the actual project
- IDE-based tools can see **files, folders, errors, and terminal output**
- This makes them better for:
  - editing existing code
  - debugging
  - refactoring
  - generating small apps and scripts
- You still need to read the code and test the result

</v-clicks>

---

# Coding Agents

As of April 2026, Coding agents (OpenAI's Codex, Anthropic's Claude Code, and Google's gemini cli) are very capable of the software development and data science tasks.

- Agency: autonomous decides steps to take: plan, execution, collect user inputs
- Tool use: select which tool to use
- Skill: read in instructions for specific tasks on the fly, e.g. office skills

---

# Prompting Patterns That Actually Help

Better prompts usually include:

<v-clicks>

- **Task**: what you want
- **Context**: what the model should know
- **Constraints**: format, scope, audience, tools, assumptions
- **Examples**: especially for structure and style
- **Verification request**: ask it to explain assumptions, edge cases, or failure points

</v-clicks>

<br>

<v-click>

Karpathy emphasizes **few-shot prompting** when you want consistent output

</v-click>

---
layout: section
---

# Part 3: What the HDSR Article Found

---

# The Article's Setup

Evkaya and de Carvalho evaluate ChatGPT's **Data Analysis** workflow as a quantitative copilot

<v-clicks>

- Upload a dataset
- Ask for summaries, plots, and models
- Let the system generate and run Python code
- Inspect both the outputs and the interpretations

</v-clicks>

<br>

<v-click>

Their key position: useful, but only with **human critique and oversight**

</v-click>

---

# Where It Worked Well

The article shows clear strengths:

<v-clicks>

- Easy onboarding from common file types like **CSV** and **XLSX**
- Fast generation of **descriptive statistics**
- Helpful suggestions for **next analytical steps**
- Strong support for **basic visualizations**
- Ability to move from questions to runnable Python without requiring the user to code directly

</v-clicks>

---

# Where It Failed

The same article also documents important failure modes:

<v-clicks>

- Mislabeling or misdescribing plots
- Interpreting numbers incorrectly even when the figure looks reasonable
- Choosing weak chart types for the task
- Suggesting analyses that do not really fit the data
- Inconsistent results across repeated prompts

</v-clicks>

<br>

<v-click>

Good-looking output is not the same as valid analysis

</v-click>

---

# Example Failure: Visualization

One reported problem:

<v-clicks>

- A histogram was described as being on a **log scale**
- But inspection of the underlying figure showed it was actually on the **original scale**

</v-clicks>

<br>

<v-click>

Lesson: always check the **axes, labels, encodings, and units**

</v-click>

---

# Example Failure: Interpretation

Another reported problem:

<v-clicks>

- The correlation heatmap displayed one value
- The accompanying written interpretation reported a different value
- The visualization looked acceptable
- The explanation was still wrong

</v-clicks>

<br>

<v-click>

Lesson: in quantitative work, verify claims against the actual output

</v-click>

---

# Human-in-the-Loop Workflow

The article strongly supports a workflow like this:

<v-clicks>

1. Use the model to draft an analysis plan
2. Let it generate code or summaries
3. Inspect the data, figures, and assumptions yourself
4. Re-prompt to fix, narrow, or clarify
5. Treat the result as provisional until checked

</v-clicks>

---

# What This Means for Data Science

LLMs can lower barriers to entry

<v-clicks>

- Nonprogrammers can do more than before
- Programmers can work faster
- Iteration becomes cheaper
- Exploration becomes easier

</v-clicks>

<br>

<v-click>

But the hard parts remain hard:

- problem formulation
- data quality judgment
- causal reasoning & research design
- validation
- communication

</v-click>

---
layout: section
---

# Part 4: How We Will Use AI in This Course

---

# Course Norms

AI use is encouraged on assignments

<v-clicks>

- Use LLMs to **brainstorm**, **debug**, **explain**, and **speed up routine work**
- Do not use them to avoid understanding your own project
- You are responsible for every line of code, chart, and claim you submit
- If the model gives you an answer you cannot explain, you do not understand it yet

</v-clicks>

---

# A Strong Workflow for This Class

For assignments and projects:

<v-clicks>

1. Start with your own question
2. Ask the model for a plan, not just an answer
3. Work in small steps
4. Run the code and inspect the output
5. Save intermediate results
6. Keep notes on what you changed and why

</v-clicks>

---

# What To Ask LLMs For

Useful requests:

<v-clicks>

- "Explain this error message"
- "Write a first draft of this function"
- "Suggest three ways to visualize this variable"
- "What assumptions does this analysis make?"
- "Refactor this code to be clearer"
- "Help me interpret this output, and say what could be misleading"

</v-clicks>

---

# What Not To Delegate

Be careful when asking the model to decide:

<v-clicks>

- whether the data is trustworthy
- whether a pattern is causal
- whether a map or chart is ethically appropriate
- whether the results make sense for Portland or Oregon policy contexts
- whether a conclusion is ready for public communication

</v-clicks>

<br>

<v-click>

These are analyst responsibilities

</v-click>

---

# In-Class Exercise

Take [2024 Oregon Crashes Geodatabase](https://www.oregon.gov/odot/Data/Crash%20Data%20Products/Statewide_Crashes_2024.gdb.zip) and try three prompts:

1. Summarize number of crashes by severity
2. Visualize number of crashes by severity
3. **Verify and Critique** the result

Compare which prompt gives the most reliable and usable output

---

# Key Takeaways

- LLMs are progressing incredibly fast, use the latest models whenever possible
- Create your own eval/benchmark for common tasks
- Evaluate different models from time to time
- Enable thinking + tool use
- In data science, **verification is part of the workflow**
- Your competitive advantage is not having AI access, but knowing **how to direct, check, and integrate** AI output

---
layout: center
---

# For Next Week

<div class="text-left">

**Read**:
- Yu & Barter, [Chapter 4: Data Preparation](https://vdsbook.com/04-data-prep)
- McKinney, [Chapters 6-8](https://wesmckinney.com/book/accessing-data)

**Do**:
- Continue DataCamp DC1 if needed
- Install and test at least one LLM tool you can use for coding or analysis
- Bring one example next week of a good AI interaction and one bad one

**Sources for today's slides**:
- Karpathy, [How I Use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw)
- Evkaya & de Carvalho, [Using ChatGPT for Data Science Analyses](https://hdsr.mitpress.mit.edu/pub/u6wp4cy3/release/2)

</div>
