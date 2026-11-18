import pandas as pd


# 1. Load Netflix dataset
def load_data():
    """
    TODO:
    Load the Netflix dataset from the CSV file:
    - File path: "./netflix.csv"
    

    Print:
    - First 5 rows showing: title, type, release_year

    Return:
        Pandas DataFrame
    """

    df = pd.read_csv("./netflix.csv")
    print("Dataset loaded successfully!")

    print("\nSample Data (first 5 rows):")
    print(df[['title', 'type', 'release_year']].head(5))

    return df


# 2. Display basic dataset information
def explore_dataset(df):
    """
    TODO: