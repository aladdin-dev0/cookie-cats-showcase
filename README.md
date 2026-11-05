# 🐱 Cookie Cats: A/B Testing & Player Retention Optimization

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![A/B Testing](https://img.shields.io/badge/Experiment-A%2FB%20Testing-green.svg)](#)
[![Bootstrap Resampling](https://img.shields.io/badge/Method-Bootstrap%20Simulation-orange.svg)](#)

An end-to-end data science and statistical analysis project evaluating the impact of shifting in-game gate placement from **Level 30** (`gate_30` - Control) to **Level 40** (`gate_40` - Treatment) on **1-day and 7-day player retention** in the mobile puzzle game **Cookie Cats** (developed by Tactile Entertainment).

---

## 📌 Executive Summary & Key Verdict

> **Final Recommendation:** **DO NOT move the gate to Level 40. Keep the initial gate at Level 30.**
>
> Moving the gate to Level 40 leads to a **statistically significant decrease in 7-day retention** (from **19.02%** down to **18.20%**, $p = 0.0016$). Bootstrap resampling demonstrates a **99.9% probability** that Level 30 produces superior 7-day retention, preserving approximately **+4.5% relative retention advantage**.

---

## 📊 Summary of Experimental Results

| Metric | Gate 30 (Control) | Gate 40 (Treatment) | Relative Difference | Statistical Test | p-value | Significant? ($\alpha=0.05$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1-Day Retention** | **44.82%** | 44.23% | $+1.34\%$ | Two-Sample Z-Test | $0.0739$ | ❌ Marginal ($p > 0.05$) |
| **7-Day Retention** | **19.02%** | 18.20% | **$+4.50\%$** | Two-Sample Z-Test | **$0.0016$** | ✅ **Highly Significant** |
| **7-Day Chi-Square** | - | - | - | $\chi^2 = 9.92$ | **$0.0016$** | ✅ **Highly Significant** |
| **Gamerounds (Median)** | **17.0** | 16.0 | $+6.25\%$ | Mann-Whitney U | $0.0509$ | ❌ Borderline ($p \approx 0.05$) |
| **Bootstrap Day 7 $P(G30 > G40)$** | **99.9%** | - | - | 2,000 Resamples | 95% CI: $[+1.8\%, +7.5\%]$ | ✅ **Definitive Advantage** |

---

## 📂 Repository Structure

```text
cookie-cats-ab-testing/
│
├── data/
│   └── cookie_cats.csv              # Raw dataset (90,189 player records)
│
├── notebooks/
│   └── cookie_cats_ab_testing.ipynb # Interactive end-to-end analysis notebook
│
├── src/                             # Modular Python package
│   ├── __init__.py
│   ├── eda.py                       # Data loading, validation, outlier cleaning
│   ├── hypothesis_testing.py        # Z-test, Chi-square, Mann-Whitney U
│   ├── bootstrap.py                 # Resampling simulation and confidence intervals
│   └── visualization.py             # Publication-ready plotting functions
│
├── reports/
│   ├── executive_report.md          # Comprehensive executive business report
│   └── cookie_cats_presentation.pptx # Professional 16:9 PowerPoint presentation deck
│
├── figures/                         # Generated high-resolution charts
│   ├── gamerounds_distribution.png
│   ├── retention_comparison.png
│   ├── bootstrap_retention_1.png
│   └── bootstrap_retention_7.png
│
├── .gitignore                       # Git exclusion rules
├── requirements.txt                 # Project dependencies
└── README.md                        # Project documentation
```

---

## 🚀 Quickstart & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/cookie-cats-ab-testing.git
cd cookie-cats-ab-testing
```

### 2. Set up virtual environment and install dependencies
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Run the interactive notebook
```bash
jupyter notebook notebooks/cookie_cats_ab_testing.ipynb
```

### 4. View the Executive Presentation
Open [`reports/cookie_cats_presentation.pptx`](reports/cookie_cats_presentation.pptx) in Microsoft PowerPoint to view and present the executive slide deck.

---

## 🧠 Behavioral Economics: Why Gate 30 Wins

1. **Combating Hedonic Adaptation (Forced Pacing):**
   * Continuous play without forced breaks triggers sensory fatigue and burnout.
   * Placing the gate at Level 30 forces players to pause while they are still highly engaged, creating an anticipation loop that brings them back days later.
2. **Avoiding the Level 40 Exhaustion Cliff:**
   * Grinding to Level 40 without any cooldown drains casual players.
   * Encountering an artificial barrier *after* an exhausting session causes uninstalls rather than patience or monetization.

---

## 📜 License
This project is open-source under the [MIT License](LICENSE).
