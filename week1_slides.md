---
theme: seriph
title: "USP 410/510 Urban Data Science - Week 1"
info: |
  USP 410/510 Urban Data Science
  Spring 2026, Portland State University
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Urban Data Science

## USP 410/510 | Spring 2026

Dr. Liming Wang

Portland State University

<!--
Welcome students, introduce yourself, and set expectations for the quarter.
-->

---
layout: section
---

# Part 1: Course Overview

---

# About This Course

An interdisciplinary approach to understanding, managing, and designing the city using **data-driven theories and methods**

<v-clicks>

- **Project-based** — learn by doing
- **AI-assisted** — learn to work with LLMs and coding agents
- **No prerequisites** — just curiosity and tolerance for experimentation
- Builds on information processing, statistics, and computer science for **urban applications**

</v-clicks>

<!--
Emphasize that this is a hands-on course. Students will be writing code from day one, but they don't need prior experience.
-->

---

# Course Objectives

<v-clicks>

1. **Code** — Automate tasks with Python
2. **AI tools** — Use LLMs and AI agents for coding, analysis, and problem solving
3. **Workflow** — Project management best practices for data work
4. **Data skills** — Access, clean, visualize, and analyze urban data
5. **Domain knowledge** — Combine technical and substantive expertise to solve urban problems

</v-clicks>

---

# Grading

| Component | USP 410 | USP 510 |
| :--- | :---: | :---: |
| DataCamp exercises (4 x 5pts) | 20% | 20% |
| Data science show & tell (2 x 5pts) | 10% | 10% |
| Assignments (2) | 30% | 20% |
| Project presentation | 10% | 10% |
| Project report | 30% | 40% |

---
layout: two-cols
---

# Assignments

Both use **ODOT crash data**

**A1 — Exploring Crash Data** (due W4)
- Investigate questions of your choosing
- e.g., Does DST increase crashes?
- e.g., Nighttime pedestrian fatality patterns

**A2 — Interactive Crash Map** (due W8)
- Go beyond ODOT's existing viewer
- Build a map with a point of view
- e.g., Dangerous corridors, equity, safe routes near schools

::right::

<div class="pl-4 pt-12">

# AI Policy

| Activity | AI Use |
| :--- | :--- |
| DataCamp | **Not permitted** |
| Show & tell | Research only |
| Assignments | **Encouraged** |
| Final project | **Encouraged** |

<br>

> AI use on assignments is **encouraged and recommended** — this is how modern data science is done.

</div>

---

# Class Project

The final product can be a **report**, **infographic**, or **dashboard**

- Generated using Python and/or Quarto
- Presentation: 20 min + 5 min Q&A

<br>

| Milestone | Due |
| :--- | :--- |
| Project idea | W3 (04/16) |
| Project proposal (1 page) | W6 (05/07) |
| Progress update | W8 (05/21) |
| Project presentation | W11 (06/11) |
| Final submission | 06/12 |

---

# Schedule at a Glance

| Week | Date | Topic |
| :---: | :--- | :--- |
| **W1** | **04/02** | **Overview, Setup, Intro to Python** |
| W2 | 04/09 | LLMs and AI agents |
| W3 | 04/16 | Data import/export, cleaning & processing |
| W4 | 04/23 | Workflow & project management |
| W5 | 04/30 | Exploring and visualizing data |
| W6 | 05/07 | Reproducible research; Quarto & Jupyter |
| W7 | 05/14 | Spatial data and maps |
| W8 | 05/21 | Public data from the web and APIs |
| W9 | 05/28 | Infographics and dashboards |
| W10 | 06/04 | Project workshop |
| W11 | 06/11 | Project presentations |

---

# Textbooks & Resources

All freely available online:

- **Yu & Barter** — *Veridical Data Science* ([vdsbook.com](https://vdsbook.com/))
- **Downey** — *Think Python*, 3rd Ed. ([allendowney.github.io/ThinkPython](https://allendowney.github.io/ThinkPython/))
- **Turrell** — *Python for Data Science* ([aeturrell.github.io/python4DS](https://aeturrell.github.io/python4DS/))
- **McKinney** — *Python for Data Analysis*, 3rd Ed. ([wesmckinney.com/book](https://wesmckinney.com/book/))
- **Rey et al.** — *Geographic Data Science with Python* ([geographicdata.science/book](https://geographicdata.science/book/))

<br>

**DataCamp**: Free access via DataCamp Classroom program

---
layout: section
---

# Part 2: The Data Science Life Cycle

Based on Yu & Barter, *Veridical Data Science*, Chapter 2

---

# What is the Data Science Life Cycle?

A **six-stage framework** for how data science projects progress

<div class="flex justify-center mt-4">
  <img
    src="https://vdsbook.com/Figures-External/intro/data_science_life_cycle.png"
    alt="Data Science Life Cycle"
    style="max-height: 400px; width: auto;"
  />
</div>

<div class="text-xs mt-2 opacity-75">
Source: Yu & Barter, <em>Veridical Data Science</em>, <a href="https://vdsbook.com/">vdsbook.com</a>
</div>

<!--
Key point: this is not a linear process. You cycle back constantly.
-->

---

# Stage 1: Problem Formulation & Data Collection

<v-clicks>

- **Collaborate with domain experts** to turn vague questions into answerable ones
- Identify what data is available — or what needs to be collected
- Understanding the project goals drives data requirements

</v-clicks>

<br>

<v-click>

### Urban data science example

> "Is Portland getting less safe for pedestrians?"

becomes

> "Have pedestrian-involved crashes in Portland increased in frequency or severity from 2015 to 2024, controlling for changes in population and VMT?"

</v-click>

---

# Stage 2: Data Cleaning & EDA

The stage where you spend **most of your time**

<v-clicks>

- **Data cleaning**: Make datasets tidy, properly formatted, unambiguous
- **Preprocessing**: Adapt cleaned data for specific analyses
- **Exploratory Data Analysis (EDA)**: Summaries and visualizations to understand patterns
- **Explanatory Data Analysis**: Refine exploratory work for external audiences

</v-clicks>

<br>

<v-click>

> "The process of data cleaning is necessarily subjective and involves making assumptions about the underlying real-world quantities being measured."
>
> — Yu & Barter

</v-click>

---

# Stages 3–6

**Stage 3: Intrinsic Structures** (optional)
- Dimensionality reduction, cluster analysis
- Discover natural groupings in the data

**Stage 4: Prediction & Inference** (optional)
- Supervised learning, regression, classification
- Focus on accuracy with validation/test data

**Stage 5: Evaluation**
- Is the result *stable* and *predictable*? (PCS framework)
- Consult domain experts; use negative controls

**Stage 6: Communication**
- Reports, infographics, dashboards, applications
- Tailor the message to the audience

---

# Key Concepts from DSLC

<v-clicks>

**Data structure vocabulary**
- **Variables/features** = columns; **observations** = rows
- **High-dimensional** = many variables (>100)

**Data quality**
- **Live data**: actively maintained, errors corrected
- **Dead data**: static snapshots, no monitoring

**Data snooping** ⚠️
- Presenting discovered patterns as proven conclusions
- Veridical Data Science counters this with *predictability* and *stability*

**Non-linear progression**
- You will cycle back through stages — that's normal and expected

</v-clicks>

---
layout: section
---

# Part 3: Computer Setup

---
layout: two-cols
---

# Tools We'll Use

<v-clicks>

**Python** (via Miniconda or uv)
- The programming language for this course

**Google Antigravity**
- AI-powered IDE with built-in coding agents
- Free, based on VS Code, supports Gemini & Claude models

**Quarto**
- Render notebooks to HTML/PDF/Word

**Git & GitHub**
- Version control and collaboration

</v-clicks>

::right::

<div class="pl-8 pt-8">

<v-click>

## Setup checklist

- [ ] Install Python
- [ ] Install [Google Antigravity](https://antigravity.google/)
- [ ] Install Quarto
- [ ] Create a GitHub account
- [ ] Verify: `python --version`
- [ ] Verify: `quarto --version`

</v-click>

</div>

<!--
Walk through the setup process live. Have students follow along. Antigravity is free with generous Gemini rate limits.
-->

---

# Why Python?

<v-clicks>

- **Free and open source** — no license barriers
- **General purpose** — not just for statistics (unlike R)
- **Massive ecosystem** — pandas, matplotlib, geopandas, folium, streamlit, ...
- **Industry standard** — used at Google, Meta, NASA, city governments
- **AI tools work best with Python** — first-class support in Antigravity, Claude Code, and other AI coding agents
- **Readable syntax** — designed to be close to natural language

</v-clicks>

---

# Google Antigravity

Our IDE for the course — an **agent-first** development environment

<v-clicks>

- **Free** with generous Gemini rate limits; also supports Claude models
- Built on VS Code — familiar editor interface with all the extensions you know
- **Two views**:
  - **Editor view** — write code with an AI agent sidebar (like Copilot, but deeper)
  - **Manager view** — orchestrate multiple agents working in parallel
- Agents can **plan, execute, and verify** tasks across your editor, terminal, and browser
- Download at [antigravity.google](https://antigravity.google/)

</v-clicks>

<!--
Demo Antigravity if time permits — show the editor view and agent sidebar. Students should install it before next week.
-->

---
layout: section
---

# Part 4: Introduction to Python

Based on Downey, *Think Python*, Chapter 1

---

# Programming as a Way of Thinking

Programming combines features from:

<v-clicks>

- **Mathematics** — formal notation, abstract reasoning
- **Engineering** — building things that work, testing and debugging
- **Natural science** — observing behavior, forming hypotheses, experimenting

</v-clicks>

<br>

<v-click>

> The most important skill is **learning to experiment** — try things, break things, read error messages, and try again.

</v-click>

---

# Arithmetic in Python

Python as a calculator:

```python
30 + 12        # Addition → 42
43 - 1         # Subtraction → 42
6 * 7          # Multiplication → 42
84 / 2         # Division → 42.0 (always returns a float!)
85 // 2        # Integer division → 42
7 ** 2         # Exponentiation → 49
```

<v-click>

**Order of operations**: same as math (PEMDAS)

```python
(12 + 5) * 6   # → 102  (parentheses first)
12 + 5 * 6     # → 42   (multiplication before addition)
```

</v-click>

---

# Data Types

Every value in Python has a **type**

```python
type(42)       # → int     (integer — whole numbers)
type(42.0)     # → float   (floating point — decimals)
type('hello')  # → str     (string — text)
```

<v-click>

**Type conversion**:
```python
int(42.9)      # → 42     (truncates, does not round!)
float(42)      # → 42.0
str(42)        # → '42'
```

</v-click>

<v-click>

**Watch out**: division always returns a float

```python
84 / 2         # → 42.0   (not 42)
```

</v-click>

---

# Strings

Text is enclosed in quotes (single `'...'` or double `"..."`)

```python
'Hello' + ' ' + 'World'   # Concatenation → 'Hello World'
'Spam, ' * 3               # Repetition → 'Spam, Spam, Spam, '
len('Portland')            # Length → 8
```

<v-click>

**Note**: `+` and `*` behave differently for strings vs. numbers

```python
3 + 4          # → 7        (arithmetic)
'3' + '4'      # → '34'     (concatenation)
```

</v-click>

<v-click>

**Common error**:
```python
'3' + 4        # → TypeError! Can't mix strings and numbers
```

</v-click>

---

# Built-in Functions

Functions take inputs and produce outputs:

```python
round(3.14159)       # → 3
round(3.14159, 2)    # → 3.14
abs(-7)              # → 7
len('data science')  # → 12
type(42)             # → <class 'int'>
print('Hello!')      # displays: Hello!
```

<v-click>

**Calling a function**: `function_name(argument1, argument2, ...)`

You've already been using functions — `type()`, `len()`, `int()`, `float()`, `str()` are all functions

</v-click>

---

# Formal vs. Natural Languages

| | Natural Language | Programming Language |
| :--- | :--- | :--- |
| **Ambiguity** | Common and tolerated | Not allowed |
| **Redundancy** | Verbose for clarity | Concise and precise |
| **Literalness** | Full of idioms and metaphor | Means exactly what it says |

<br>

<v-click>

**Implication for learning**:

- You can't skim code the way you skim English
- Small differences in spelling and punctuation matter
- **Error messages are your friend** — read them carefully

</v-click>

---

# Let's Try It

Open a Python interpreter or Jupyter notebook and try:

```python
# What is your age in days (approximately)?
age_years = 25
age_days = age_years * 365
print(age_days)

# How many seconds in a year?
seconds_per_year = 365 * 24 * 60 * 60
print(seconds_per_year)

# What type is each of these?
print(type(age_years))
print(type(age_years / 2))
print(type('Portland'))
```

<v-click>

**Experiment**: What happens if you type `age_years / 0`?

</v-click>

<!--
Live coding demo. Have students follow along. Encourage them to try variations.
-->

---
layout: center
---

# For Next Week

<div class="text-left">

**Read**:
- Karpathy, [How I Use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw) (video)
- Evkaya & de Carvalho, [Using ChatGPT for Data Science Analyses](https://hdsr.mitpress.mit.edu/pub/u6wp4cy3/release/2) (HDSR, 2026)

**Do**:
- Complete computer setup (Python, VS Code, Quarto, GitHub)
- Start **DataCamp DC1**: [Introduction to Python](https://www.datacamp.com/courses/intro-to-python-for-data-science) (due W3)
- Sign up for show & tell slots in the [shared Google Doc](https://docs.google.com/document/d/11sKw7m1eQ1ffYCejjVv3_7qH5gVpCMeMkfx7Zidvtwc/edit?usp=sharing)

</div>
