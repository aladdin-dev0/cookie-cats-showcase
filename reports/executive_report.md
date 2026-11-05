# Executive Business Report: Cookie Cats A/B Testing & Retention Optimization

**Author:** Data Science & Analytics Team  
**Date:** November 2026  
**Status:** Completed & Validated  
**Target Audience:** VP of Product, Lead Game Designers, Monetization Strategy Team  

---

## 1. Executive Summary

In mobile free-to-play (F2P) gaming, optimizing player retention while monetizing engagement is the central operational challenge. Tactile Entertainment's **Cookie Cats** conducted an A/B test on **90,189 new players** to evaluate the impact of shifting the game's initial progress gate from **Level 30** (`gate_30` - Control group) to **Level 40** (`gate_40` - Treatment group).

### 🎯 Key Takeaway & Strategic Decision
> **Recommendation:** **DO NOT move the gate to Level 40. Maintain the initial gate at Level 30.**
> 
> Shifting the gate to Level 40 causes a **statistically significant decline in 7-day player retention** from **19.02% down to 18.20%** ($p = 0.0016$). Bootstrap resampling demonstrates a **99.9% probability** that Level 30 yields superior long-term retention. 

Maintaining the gate at Level 30 preserves approximately **0.82% absolute retention advantage** (a **+4.5% relative gain**), translating directly into hundreds of thousands of retained monthly active users (MAU) and preserved lifetime value (LTV).

---

## 2. Business Context & Problem Formulation

### 2.1 The Role of "Gates"
As players advance through Cookie Cats, they hit "gates" that present three choices:
1. Wait a fixed duration (time delay).
2. Pay in-game currency / real money.
3. Request keys/help from Facebook friends.

### 2.2 The Conflict of Hypotheses
* **The Product Hypothesis for Gate 40:**
  * *Assumption:* By delaying the first gate to Level 40, players experience uninterrupted gameplay longer, become more hooked on the core mechanics, and are less likely to bounce early.
* **The Behavioral Counter-Hypothesis (Hedonic Adaptation):**
  * *Theory:* Continuous play leads to sensory fatigue and boredom. Introducing a pause at Level 30 forces players to take a natural break, prolonging their enjoyment and creating an anticipation loop that drives them back days later.

---

## 3. Data Auditing & Exploration (EDA)

The dataset contains **90,189** distinct players with zero missing values across all dimensions.

### 3.1 Sample Balance & Distribution
| Variant | Sample Size ($N$) | Allocation Share | Mean Rounds (Raw) | Median Rounds |
| :--- | :---: | :---: | :---: | :---: |
| **Control (`gate_30`)** | 44,700 | 49.56% | 52.46 | 17.0 |
| **Treatment (`gate_40`)** | 45,489 | 50.44% | 51.30 | 16.0 |
| **Total** | **90,189** | **100.0%** | **51.87** | **17.0** |

*Both variants have virtually identical sample sizes (~50/50 split), confirming valid random assignment.*

### 3.2 Outlier Remediation
During descriptive profiling, a severe outlier was detected in `gate_30`:
* Player `userid: 545094` logged **49,854 game rounds** within 14 days (an impossible rate of ~148 rounds/hour continuous play), indicating automated scripting or a tracking anomaly.
* This single record artificially skewed the raw mean of `gate_30` from 51.34 to 52.46.
* **Action:** The record was cleanly filtered out, leaving **90,188 validated records**.

---

## 4. Empirical Findings & Statistical Rigor

### 4.1 One-Day Retention Analysis (`retention_1`)
* **`gate_30`:** 44.82% ($N = 20,034$)
* **`gate_40`:** 44.23% ($N = 20,119$)
* **Absolute Difference:** $+0.59\%$
* **Relative Advantage:** $+1.34\%$
* **Statistical Tests:**
  * Two-sample Z-test: $z = 1.787$, $p = 0.0739$
  * Chi-square test: $\chi^2 = 3.170$, $p = 0.0750$
* **Interpretation:** At a standard significance threshold of $\alpha = 0.05$, the 1-day difference is **marginally significant**. However, it hints at an early negative trend for `gate_40`.

---

### 4.2 Seven-Day Retention Analysis (`retention_7`)
Seven-day retention is the gold standard for player lifetime value and sustained monetization.
* **`gate_30`:** **19.02%** ($N = 8,501$)
* **`gate_40`:** **18.20%** ($N = 8,279$)
* **Absolute Difference:** $+0.82\%$
* **Relative Advantage:** $+4.50\%$
* **Statistical Tests:**
  * Two-sample Z-test: $z = 3.157$, **$p = 0.00159$**
  * Chi-square test: $\chi^2 = 9.915$, **$p = 0.00164$**
* **Interpretation:** The decline in 7-day retention under `gate_40` is **highly statistically significant** ($p < 0.01$). We firmly reject the null hypothesis of equal retention rates.

---

### 4.3 Bootstrap Resampling Simulation ($B = 2,000$ Iterations)
To account for sampling variability without relying on strict parametric assumptions, we performed non-parametric bootstrap resampling:

| Retention Horizon | P(Gate 30 > Gate 40) | Mean % Difference | 95% Confidence Interval | Result |
| :---: | :---: | :---: | :---: | :---: |
| **1-Day Retention** | **96.5%** | $+1.33\%$ | $[-0.09\%, +2.83\%]$ | Likely positive, CI touches zero |
| **7-Day Retention** | **99.9%** | **$+4.56\%$** | **$[+1.77\%, +7.51\%]$** | **Strictly positive advantage** |

> **Key Observation:** The 95% Confidence Interval for 7-day retention is strictly above zero. There is virtually zero probability ($0.1\%$) that moving the gate to Level 40 improves 7-day retention.

---

## 5. Behavioral Economics: Why Does Gate 30 Win?

The counter-intuitive result—that placing a roadblock *earlier* improves retention—is explained by two established psychological phenomena:

1. **Combating Hedonic Adaptation (The Forced Pause):**
   * When players enjoy an engaging game endlessly without friction, their enjoyment rapidly plateaus and fatigue sets in.
   * Enforcing a gate at Level 30 introduces a natural stopping point before the player exhausts their excitement.
2. **The Cliff of Over-Exertion at Level 40:**
   * Reaching Level 40 without any forced break requires extensive continuous screen time.
   * By the time casual players hit Level 40, they feel drained, and encountering a barrier then triggers an irreversible uninstall rather than patience or purchase.

---

## 6. Financial & Churn Impact Projection

Assuming a game scale of **500,000 monthly installs**:

* **Players retained at Day 7 under Gate 30:** $500,000 \times 19.02\% = 95,100$ active players.
* **Players retained at Day 7 under Gate 40:** $500,000 \times 18.20\% = 91,000$ active players.
* **Net Loss of Active Players per Month:** **$-4,100$ players per cohort**.
* Over an annualized period (12 cohorts), adopting Gate 40 would bleed approximately **49,200 committed players**, severely depressing ad impressions, in-app purchase frequency, and organic referrals.

---

## 7. Actionable Strategic Recommendations

1. **Rollback / Reject Gate 40:** Keep Gate 30 as the universal baseline for all global cohorts.
2. **Optimize Gate 30 Experience:**
   * Test social unlocking mechanics (e.g., lower friend key requirements).
   * Test introductory starter packs at Level 30 with dynamic discount pricing.
3. **Conduct Multi-Variant Granular Testing:**
   * Test an intermediate placement (e.g., Level 35) or personalized gate triggers based on session duration rather than level number alone.
4. **Instrument Churn Telemetry:**
   * Track drop-off rates at the exact level screen where the gate appears to identify friction hotspots.
