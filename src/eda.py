"""
Exploratory Data Analysis module for Cookie Cats dataset.
"""

from typing import Tuple, Dict, Any
import pandas as pd
import numpy as np


def load_and_validate_data(filepath: str) -> pd.DataFrame:
    """
    Load dataset from CSV and perform structural validation.
    """
    df = pd.read_csv(filepath)
    
    # Check required columns
    expected_cols = {'userid', 'version', 'sum_gamerounds', 'retention_1', 'retention_7'}
    if not expected_cols.issubset(df.columns):
        missing = expected_cols - set(df.columns)
        raise ValueError(f"Missing expected columns: {missing}")
        
    return df


def detect_and_clean_outliers(df: pd.DataFrame, max_rounds_threshold: int = 10000) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Detect and filter extreme outliers in sum_gamerounds.
    Default threshold filters out impossible values (e.g., > 10,000 rounds in 14 days).
    """
    outliers = df[df['sum_gamerounds'] > max_rounds_threshold].copy()
    cleaned_df = df[df['sum_gamerounds'] <= max_rounds_threshold].copy()
    return cleaned_df, outliers


def get_dataset_summary(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Generate summary metrics for the dataset.
    """
    total_users = len(df)
    unique_users = df['userid'].nunique()
    null_counts = df.isnull().sum().to_dict()
    version_counts = df['version'].value_counts().to_dict()
    
    gamerounds_stats = df.groupby('version')['sum_gamerounds'].describe().to_dict()
    
    retention_1_rates = df.groupby('version')['retention_1'].mean().to_dict()
    retention_7_rates = df.groupby('version')['retention_7'].mean().to_dict()
    
    return {
        'total_users': total_users,
        'unique_users': unique_users,
        'null_counts': null_counts,
        'version_counts': version_counts,
        'gamerounds_stats': gamerounds_stats,
        'retention_1_rates': retention_1_rates,
        'retention_7_rates': retention_7_rates,
    }
