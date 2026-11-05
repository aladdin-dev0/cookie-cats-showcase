"""
Hypothesis Testing module for Cookie Cats A/B Testing.
"""

from typing import Dict, Any
import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest


def test_retention_proportions(df: pd.DataFrame, retention_col: str) -> Dict[str, Any]:
    """
    Perform Two-Sample Z-Test and Chi-Squared test for retention proportions.
    H0: Retention rate in gate_30 == Retention rate in gate_40
    H1: Retention rate in gate_30 != Retention rate in gate_40
    """
    g30 = df[df['version'] == 'gate_30'][retention_col]
    g40 = df[df['version'] == 'gate_40'][retention_col]
    
    count = [g30.sum(), g40.sum()]
    nobs = [len(g30), len(g40)]
    
    rate_30 = g30.mean()
    rate_40 = g40.mean()
    diff = rate_30 - rate_40
    pct_diff = (diff / rate_40) * 100
    
    # Two-sample Z-test for proportions
    z_stat, p_val_z = proportions_ztest(count, nobs, alternative='two-sided')
    
    # Chi-square test
    contingency_table = pd.crosstab(df['version'], df[retention_col])
    chi2_stat, p_val_chi2, dof, _ = stats.chi2_contingency(contingency_table)
    
    return {
        'metric': retention_col,
        'rate_gate_30': float(rate_30),
        'rate_gate_40': float(rate_40),
        'absolute_diff': float(diff),
        'percentage_diff': float(pct_diff),
        'z_statistic': float(z_stat),
        'z_p_value': float(p_val_z),
        'chi2_statistic': float(chi2_stat),
        'chi2_p_value': float(p_val_chi2),
        'significant_at_0_05': bool(p_val_z < 0.05),
    }


def test_gamerounds_distribution(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Compare gamerounds distribution between gate_30 and gate_40 using Mann-Whitney U Test.
    (Non-parametric test suitable for skewed game rounds data)
    """
    g30_rounds = df[df['version'] == 'gate_30']['sum_gamerounds']
    g40_rounds = df[df['version'] == 'gate_40']['sum_gamerounds']
    
    u_stat, p_val = stats.mannwhitneyu(g30_rounds, g40_rounds, alternative='two-sided')
    
    return {
        'test': 'Mann-Whitney U Test',
        'mean_gate_30': float(g30_rounds.mean()),
        'median_gate_30': float(g30_rounds.median()),
        'mean_gate_40': float(g40_rounds.mean()),
        'median_gate_40': float(g40_rounds.median()),
        'u_statistic': float(u_stat),
        'p_value': float(p_val),
        'significant_at_0_05': bool(p_val < 0.05),
    }
