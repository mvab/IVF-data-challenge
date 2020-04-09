# Cleaning and modelling

## Setup

Use [environment.yml](./environment.yml) in conda.

## Raw cleaning

1. Download ivf data from HFEA, place them under "./data/raw_data".
2. Open ms excel and convert those xlsb files to csv.
3. Run `python3 -m scripts.concat` to concatenate per cohort datasets together into "./data/hfea-ivf.csv".

## Analysis

1. `early_cleaning.ipynb`: early and temporary data cleaning and EDA.
2. `birth_minimal.ipynb`: full steps from data cleaning to modelling (using boost_tree).
3. Other `birth_**.ipynb` files: reuse the cleaned dataset from `birth_minimal.ipynb` to be used in other experiments (different preprocessing or different models).
4. `summary.ipynb`: summary of metrics.
