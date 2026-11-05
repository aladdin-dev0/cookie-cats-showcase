"""
Bootstrap Analysis module for Cookie Cats A/B Testing.
"""

from typing import Dict, Any, Tuple
import numpy as np
import pandas as pd


def run_bootstrap_retention(
    df: pd.DataFrame,
    retention_col: str,
    n_iterations: int = 2000,
    random_state: int = 42
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Perform bootstrap resampling to estimate the retention distribution and probability
    that gate_30 has higher retention than gate_40.
    """
    rng = np.random.default_rng(random_state)
    boot_30 = []
    boot_40 = []
    
    g30_data = df[df['version'] == 'gate_30'][retention_col].values
    g40_data = df[df['version'] == 'gate_40'][retention_col].values
    
    n_30 = len(g30_data)
    n_40 = len(g40_data)
    
    for _ in range(n_iterations):
        sample_30 = rng.choice(g30_data, size=n_30, replace=True)
        sample_40 = rng.choice(g40_data, size=n_40, replace=True)
        boot_30.append(sample_30.mean())
        boot_40.append(sample_40.mean())
        
    boot_df = pd.DataFrame({
        'gate_30': boot_30,
        'gate_40': boot_40
    })
    
    boot_df['diff'] = boot_df['gate_30'] - boot_df['gate_40']
    boot_df['pct_diff'] = (boot_df['gate_30'] - boot_df['gate_40']) / boot_df['gate_40'] * 100
    
    prob_gate_30_better = float((boot_df['pct_diff'] > 0).mean())
    ci_lower = float(np.percentile(boot_df['pct_diff'], 2.5))
    ci_upper = float(np.percentile(boot_df['pct_diff'], 97.5))
    mean_diff = float(boot_df['pct_diff'].mean())
    
    metrics = {
        'metric': retention_col,
        'iterations': n_iterations,
        'prob_gate_30_better': prob_gate_30_better,
        'mean_pct_difference': mean_diff,
        'ci_95_lower': ci_lower,
        'ci_95_upper': ci_upper,
    }
    
    return boot_df, metrics
