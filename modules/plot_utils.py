# %%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def make_charts(dataframe: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=dataframe, x='Year', y='GDP (millions USD)',
                 hue='Country', ax=ax)
    ax.set_xlabel('Year')
    ax.set_ylabel('GDP (million USD)')
    ax.set_title('GDP series')
    ax.legend
    plt.tight_layout()
    plt.show()
