# paste your code here
"""
data_preprocessing.py

Handles data loading, cleaning, and preprocessing steps.
"""

import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load dataset from a CSV file."""
    return pd.read_csv(path)

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows from the dataset."""
    return df.drop_duplicates()

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill or drop missing values depending on the strategy."""
    return df.fillna(method='ffill').fillna(method='bfill')

def handle_outliers(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Cap outliers using IQR method."""
    df_clean = df.copy()
    for col in columns:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 - 1.5 * IQR
        df_clean[col] = df_clean[col].clip(lower, upper)
    return df_clean
