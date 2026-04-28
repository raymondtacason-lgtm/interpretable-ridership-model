# paste the content here


"""
feature_engineering.py

Handles encoding, scaling, feature creation, and PCA transformation.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA

def split_data(df: pd.DataFrame, target: str):
    """Split dataset into train and test sets."""
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def build_preprocessor(categorical_cols, numeric_cols):
    """Create preprocessing pipeline for categorical and numeric features."""
    return ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", StandardScaler(), numeric_cols)
        ]
    )

def apply_pca(X_train, X_test, n_components=6):
    """Apply PCA to reduce dimensionality."""
    pca = PCA(n_components=n_components)
    X_train_pca = pca.fit_transform(X_train)
    X_test_pca = pca.transform(X_test)
    return X_train_pca, X_test_pca, pca
