import pandas as pd
import ast

def load_data(file_path):
    df = pd.read_csv(file_path, sep=",")
    df.columns = ['Budget', 'Home_Page', 'Movie_Name', 'Genres', 'Overview', 'Cast',
                'Original_Language', 'Storyline', 'Production_Company', 'Release_Date',
                'Revenue', 'Run_Time', 'Tagline', 'Vote_Average', 'Vote_Count']
    return df

def preprocess_data(df):
    df = df.drop(columns=["Home_Page", "Movie_Name", "Genres", "Overview", "Storyline",
                        "Production_Company", "Release_Date", "Run_Time", "Tagline", "Vote_Count"])
    df = df[df["Budget"].str.contains("\$", na=False)]
    df = df[df["Revenue"].str.contains("\$", na=False)]
    df["Budget"] = df["Budget"].str.replace(r"[^\d]", "", regex=True).astype(int)
    df["Revenue"] = df["Revenue"].str.replace(r"[^\d]", "", regex=True).astype(int)
    df["Vote_Average"] = df["Vote_Average"].astype(int)
    return df

def extract_cast_list(df):
    all_names_list = []
    for row in df['Cast']:
        name_list = ast.literal_eval(row)
        all_names_list += name_list
    return all_names_list
