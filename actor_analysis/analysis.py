from collections import Counter
import pandas as pd

def calculate_general_statistics(df):
    budget_mean_general = round(df["Budget"].mean(), 2)
    revenue_mean_general = round(df["Revenue"].mean(), 2)
    vote_mean_general = round(df["Vote_Average"].mean(), 2)
    general_profit = round((revenue_mean_general - budget_mean_general) / df.size, 2)
    return budget_mean_general, revenue_mean_general, vote_mean_general, general_profit

def get_top_actors(cast_list, top_n=50):
    name_counts = Counter(cast_list)
    top_actors = name_counts.most_common(top_n)
    return top_actors

def calculate_actor_statistics(df, top_actors, general_stats):
    actor_stats = []
    budget_mean_general, revenue_mean_general, vote_mean_general, general_profit = general_stats

    for actor, _ in top_actors:
        actor_data = {"Actor": actor}
        actor_data['Budget_Mean_General'] = budget_mean_general
        actor_data['Revenue_Mean_General'] = revenue_mean_general
        actor_data['Vote_Average_General'] = vote_mean_general
        actor_data['Profit_Mean_General'] = general_profit

        actor_movies = df[df["Cast"].str.contains(actor, case=False, na=False)]
        actor_data["Budget_Mean_Actor"] = round(actor_movies["Budget"].mean(), 2)
        actor_data["Revenue_Mean_Actor"] = round(actor_movies["Revenue"].mean(), 2)
        actor_data["Vote_Average_Actor"] = round(actor_movies["Vote_Average"].mean(), 2)
        actor_data["Profit_Mean_Actor"] = round(actor_data["Revenue_Mean_Actor"] - actor_data["Budget_Mean_Actor"], 2)

        actor_data["isProfitable"] = "Yes" if actor_data["Profit_Mean_Actor"] > general_profit else "No"
        actor_data["isLiked"] = "Yes" if actor_data["Vote_Average_Actor"] > vote_mean_general else "No"

        actor_stats.append(actor_data)

    return pd.DataFrame(actor_stats)
