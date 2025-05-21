"""
Data loading, filtering, and KPI computation utilities for the Solar Potential Dashboard.

Functions:
- load_data: Loads and combines cleaned solar datasets for Benin, Sierra Leone, and Togo.
- filter_data: Filters the dataset based on selected countries and a value range for a solar metric.
- calculate_kpis: Calculates average values of a selected metric per country for KPI display.
"""

import pandas as pd
import sys
import os
import streamlit as st

# Enable import from parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.viz_utils import load_and_combine_data

@st.cache_data
def load_data():
    """
    Loads and combines cleaned CSV data for Benin, Sierra Leone, and Togo into a single DataFrame.

    Returns:
        pd.DataFrame: Combined solar data with a 'Country' column added.
    """
    df2 = load_and_combine_data(
        'https://drive.google.com/uc?export=download&id=14P7X9d7TPNMsnUliGy3CmWtW5yb-FYEq',
        'https://drive.google.com/uc?export=download&id=1j65ix7VopeFT1uxtD6-YA3icHzofUd-D',
        'https://drive.google.com/uc?export=download&id=1V1rqrXynBK0p7HKO4L_aLxab_9fbLQZg'
    )

    # df = load_and_combine_data(
    #     'data/benin_clean.csv',
    #     'data/sierraleone_clean.csv',
    #     'data/togo_clean.csv'
    # )
    return df2

def filter_data(df: pd.DataFrame, countries: list, metric: str, min_val: float, max_val: float) -> pd.DataFrame:
    """
    Filters the solar dataset based on selected countries and a numeric range for a given metric.

    Args:
        df (pd.DataFrame): Combined solar dataset.
        countries (list): List of countries to include.
        metric (str): Column name of the metric to filter on (e.g., 'GHI').
        min_val (float): Minimum acceptable value for the metric.
        max_val (float): Maximum acceptable value for the metric.

    Returns:
        pd.DataFrame: Filtered subset of the dataset.
    """
    return df[
        (df['Country'].isin(countries)) &
        (df[metric] >= min_val) &
        (df[metric] <= max_val)
    ]

def calculate_kpis(filtered_df: pd.DataFrame, metric: str) -> pd.DataFrame:
    """
    Calculates the average value of a selected metric per country.

    Args:
        filtered_df (pd.DataFrame): Filtered solar dataset.
        metric (str): Metric to calculate KPIs for.

    Returns:
        pd.DataFrame: DataFrame with 'Country' and average metric value, sorted by metric.
    """
    return filtered_df.groupby('Country')[metric].mean().reset_index().sort_values(by=metric, ascending=True)
