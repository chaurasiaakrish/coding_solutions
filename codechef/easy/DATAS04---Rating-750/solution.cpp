import seaborn as sns

import matplotlib
matplotlib.use("Agg")  # headless mode (no GUI)

import matplotlib.pyplot as plt

# TODO: 1. Set the theme to "whitegrid" for better styling
sns.set_theme(style="whitegrid")

# 1. Load Penguin Dataset
def load_data():
    """
    Load the penguins dataset using seaborn and clean it.
    """
    # TODO: 2. Load the "penguins" dataset
    df = sns.load_dataset("penguins")
    
    # TODO: 3. Drop rows with missing values, this prevents errors during plotting
    df.dropna(inplace=True)
    
    print("Dataset loaded and cleaned successfully!")
    
    if df is not None:
        print("\nSample Data (first 5 rows):")

        # display only relevant columns (species, bill_length_mm, bill_depth_mm, body_mass_g)
        print(df[['species', 'bill_length_mm', 'bill_depth_mm', 'body_mass_g']].head(5))
    
    return df
