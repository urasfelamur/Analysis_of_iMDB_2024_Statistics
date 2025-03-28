import matplotlib.pyplot as plt
import seaborn as sns

# Plotting a bar chart of the given metric for the top actors.
def plot_actor_statistics(actor_stats, metric):
    """
    Parameters:
    - actor_stats (DataFrame): The DataFrame containing actor statistics.
    - metric (str): The column name in the DataFrame to plot.
    """
    plt.figure(figsize=(12, 6))
    sorted_df = actor_stats.sort_values(by=metric, ascending=False)
    sns.barplot(data=sorted_df, x="Actor", y=metric)
    plt.xticks(rotation=90)
    plt.title(f"Top Actors by {metric}")
    plt.tight_layout()
    plt.show()

