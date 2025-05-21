import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kruskal
import numpy as np

def load_and_combine_data(benin_path: str, sierra_leone_path: str, togo_path: str) -> pd.DataFrame:
    """Load and combine cleaned datasets from multiple countries.

    Args:
        benin_path (str): Path to Benin's cleaned CSV.
        sierra_leone_path (str): Path to Sierra Leone's cleaned CSV.
        togo_path (str): Path to Togo's cleaned CSV.

    Returns:
        pd.DataFrame: Combined DataFrame with 'Country' column.
    """
    benin = pd.read_csv(benin_path)
    sierra_leone = pd.read_csv(sierra_leone_path)
    togo = pd.read_csv(togo_path)
    benin['Country'] = 'Benin'
    sierra_leone['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'
    return pd.concat([benin, sierra_leone, togo], ignore_index=True)

def plot_metric_boxplots(df: pd.DataFrame, metrics: list, save_path: str) -> None:
    """Plot side-by-side boxplots for specified metrics across countries.

    Args:
        df (pd.DataFrame): Combined DataFrame with 'Country' and metric columns.
        metrics (list): List of metrics to plot (e.g., ['GHI', 'DNI', 'DHI']).
        save_path (str): Path to save the plot.
    """
    fig, axes = plt.subplots(1, len(metrics), figsize=(15, 5))
    for i, metric in enumerate(metrics):
        sns.boxplot(x='Country', y=metric, data=df, ax=axes[i])
        axes[i].set_title(f'{metric} Distribution')
        axes[i].set_xlabel('Country')
        axes[i].set_ylabel(f'{metric} (W/m²)')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def create_summary_table(df: pd.DataFrame, metrics: list) -> pd.DataFrame:
    """Create a summary table of mean, median, and std for metrics by country.

    Args:
        df (pd.DataFrame): Combined DataFrame with 'Country' and metric columns.
        metrics (list): List of metrics (e.g., ['GHI', 'DNI', 'DHI']).

    Returns:
        pd.DataFrame: Summary table with mean, median, std per metric and country.
    """
    summary = []
    for country in df['Country'].unique():
        country_data = df[df['Country'] == country]
        stats = {'Country': country}
        for metric in metrics:
            stats[f'{metric}_Mean'] = country_data[metric].mean()
            stats[f'{metric}_Median'] = country_data[metric].median()
            stats[f'{metric}_Std'] = country_data[metric].std()
        summary.append(stats)
    return pd.DataFrame(summary)

def run_kruskal_wallis(df: pd.DataFrame, metric: str) -> tuple:
    """Run Kruskal-Wallis test on a metric across countries.

    Args:
        df (pd.DataFrame): Combined DataFrame with 'Country' and metric columns.
        metric (str): Metric to test (e.g., 'GHI').

    Returns:
        tuple: Statistic and p-value.
    """
    groups = [df[df['Country'] == country][metric].dropna() for country in df['Country'].unique()]
    stat, p_value = kruskal(*groups)
    return stat, p_value

def plot_ghi_ranking(df: pd.DataFrame, save_path: str) -> None:
    """Plot a bar chart ranking countries by average GHI.

    Args:
        df (pd.DataFrame): Combined DataFrame with 'Country' and 'GHI' columns.
        save_path (str): Path to save the plot.
    """
    ghi_means = df.groupby('Country')['GHI'].mean().sort_values(ascending=False)
    plt.figure(figsize=(8, 6))
    sns.barplot(x=ghi_means.values, y=ghi_means.index)
    plt.title('Average GHI Ranking by Country')
    plt.xlabel('Average GHI (W/m²)')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
