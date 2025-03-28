# Actor Performance Analysis of iMDB 2024 Statistics

**Actor Analysis** is a Python package that helps you analyze the financial and audience-based performance of movie actors using IMDb 2024 data.  
It computes profitability, average ratings, and more for the top 50 most frequently appearing actors in the dataset.

The dataset can be found here: https://www.kaggle.com/datasets/anandshaw2001/imdb-movies-and-tv-shows/data

We have derived new statistics from this dataset and attained new columns, their explanations are as goes:
- Actor: Names of actors
- Budget_Mean_General: The mean of all movie budgets in the processed dataset.
- Revenue_Mean_General: The mean of all movies' revenues in the processed dataset.	
- Vote_Average_General: The mean of all votes in the processed dataset.	
- Profit_Mean_General: 	The mean of all movies' profits in the processed dataset via: (General Mean Revenue - General Mean Budget)/Size of the Dataset .
- Budget_Mean_Actor: The mean of all movie budgets depending on actor in the processed dataset.
- Revenue_Mean_Actor: The mean of all movies' revenue depending on actor in the processed dataset.	
- Vote_Average_Actor: The mean of all votes depending on actor in the processed dataset.		
- Profit_Mean_Actor: The mean of all movies' profits depending on actor in the processed dataset	
- isProfitable: States if the actor on row is more profitable than the general.	
- isLiked: States if the actor on row has more of an vote average than the general.

---

## Features

- Load and preprocess IMDb data
- Identify top 50 most frequent actors
- Analyze and compare:
  - Average budget & revenue
  - Profitability vs general mean
  - Audience rating vs general average
- Visualize key metrics using Matplotlib & Seaborn
- Includes a Jupyter notebook tutorial to walk you through

---

## Quick Start

1. Clone the repository

    ```bash
    git clone https://github.com/your-username/actor-analysis.git
    cd actor-analysis

2. Install the package
    
    pip install -e .

3. Run the tutorial notebook

    jupyter notebook TUTORIAL.ipynb

## Package Structure

actor_analysis/
├── data_processing.py      # Load & preprocess data
├── analysis.py             # Actor and general statistics
├── visualization.py        # Visual plots
└── __init__.py             # Public imports
TUTORIAL.ipynb              # Walkthrough with code & charts
pyproject.toml              # Build system
LICENSE.txt                 # MIT License
README.md                   # README file
IMDb2024                    # Dataset file

## License

This project is licensed under the MIT License.
See LICENSE.txt for more info.

## Authors
Made by Uras Felamur and Zeynep Kucukfalay for the Introduction to Python Course Project.