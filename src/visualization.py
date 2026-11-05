"""
Visualization module for Cookie Cats A/B Testing.
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def setup_style():
    """Configure modern plotting style."""
    sns.set_theme(style="whitegrid", font="sans-serif")
    plt.rcParams['figure.dpi'] = 150
    plt.rcParams['font.size'] = 11


def plot_gamerounds_distribution(df: pd.DataFrame, save_path: str):
    """Plot distribution of sum_gamerounds up to 100 rounds."""
    setup_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # 1. Histogram / KDE (0 to 100 rounds)
    subset = df[df['sum_gamerounds'] <= 100]
    sns.histplot(
        data=subset,
        x='sum_gamerounds',
        hue='version',
        kde=True,
        element='step',
        palette={'gate_30': '#2b5c8f', 'gate_40': '#e26d5c'},
        alpha=0.4,
        ax=axes[0]
    )
    axes[0].set_title('Distribution of Game Rounds (≤ 100 rounds)', fontsize=13, fontweight='bold')
    axes[0].set_xlabel('Rounds Played')
    axes[0].set_ylabel('Number of Players')
    
    # 2. Boxplot (0 to 150 rounds)
    sns.boxplot(
        data=df[df['sum_gamerounds'] <= 150],
        x='version',
        y='sum_gamerounds',
        hue='version',
        palette={'gate_30': '#2b5c8f', 'gate_40': '#e26d5c'},
        legend=False,
        ax=axes[1],
        width=0.4
    )
    axes[1].set_title('Game Rounds by Version (Truncated at 150)', fontsize=13, fontweight='bold')
    axes[1].set_xlabel('Game Version')
    axes[1].set_ylabel('Rounds Played')
    
    plt.tight_layout()
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()


def plot_retention_comparison(df: pd.DataFrame, save_path: str):
    """Plot 1-day and 7-day retention comparison bar chart."""
    setup_style()
    
    ret_summary = pd.DataFrame({
        'Version': ['gate_30', 'gate_40', 'gate_30', 'gate_40'],
        'Metric': ['1-Day Retention', '1-Day Retention', '7-Day Retention', '7-Day Retention'],
        'Retention Rate': [
            df[df['version'] == 'gate_30']['retention_1'].mean() * 100,
            df[df['version'] == 'gate_40']['retention_1'].mean() * 100,
            df[df['version'] == 'gate_30']['retention_7'].mean() * 100,
            df[df['version'] == 'gate_40']['retention_7'].mean() * 100,
        ]
    })
    
    fig, ax = plt.subplots(figsize=(8, 5))
    palette = {'gate_30': '#2b5c8f', 'gate_40': '#e26d5c'}
    
    bars = sns.barplot(
        data=ret_summary,
        x='Metric',
        y='Retention Rate',
        hue='Version',
        palette=palette,
        ax=ax,
        edgecolor='black',
        linewidth=0.8
    )
    
    ax.set_title('Retention Rate Comparison: Gate 30 vs Gate 40', fontsize=13, fontweight='bold')
    ax.set_ylabel('Retention Rate (%)')
    ax.set_xlabel('')
    ax.set_ylim(0, 55)
    
    # Add data labels
    for p in bars.patches:
        height = p.get_height()
        if height > 0:
            ax.annotate(f"{height:.2f}%",
                        (p.get_x() + p.get_width() / 2., height + 1),
                        ha='center', va='bottom', fontsize=10, fontweight='bold')
            
    plt.tight_layout()
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()


def plot_bootstrap_distribution(boot_df: pd.DataFrame, metric_name: str, metrics: dict, save_path: str):
    """Plot bootstrap distribution of percentage difference."""
    setup_style()
    fig, ax = plt.subplots(figsize=(9, 5))
    
    sns.kdeplot(boot_df['pct_diff'], fill=True, color='#2b5c8f', alpha=0.5, ax=ax, linewidth=2)
    
    # Reference lines
    ax.axvline(0, color='red', linestyle='--', linewidth=1.5, label='0% Difference (No Effect)')
    ax.axvline(metrics['mean_pct_difference'], color='navy', linestyle='-', linewidth=2,
               label=f"Mean Diff: {metrics['mean_pct_difference']:.2f}%")
    ax.axvline(metrics['ci_95_lower'], color='orange', linestyle=':', linewidth=1.5,
               label=f"95% CI Lower: {metrics['ci_95_lower']:.2f}%")
    ax.axvline(metrics['ci_95_upper'], color='orange', linestyle=':', linewidth=1.5,
               label=f"95% CI Upper: {metrics['ci_95_upper']:.2f}%")
    
    ax.set_title(f"Bootstrap Distribution of % Difference (Gate 30 vs Gate 40) - {metric_name}",
                 fontsize=12, fontweight='bold')
    ax.set_xlabel('% Difference in Retention: (gate_30 - gate_40) / gate_40 * 100')
    ax.set_ylabel('Density')
    
    # Text annotation
    prob_text = f"P(gate_30 > gate_40) = {metrics['prob_gate_30_better']*100:.1f}%"
    ax.text(0.05, 0.85, prob_text, transform=ax.transAxes,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='navy', alpha=0.9),
            fontsize=11, fontweight='bold', color='navy')
    
    ax.legend(loc='upper right')
    plt.tight_layout()
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()
