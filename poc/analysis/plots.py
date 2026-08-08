import matplotlib.pyplot as plt
import pandas as pd


def trend(df: pd.DataFrame):
    ax = df.groupby("period")["value"].sum().plot(title="Trend")
    plt.tight_layout()
    return ax.figure


def by_category(df: pd.DataFrame):
    ax = df.groupby("category")["value"].sum().plot.bar(title="By line")
    plt.tight_layout()
    return ax.figure
