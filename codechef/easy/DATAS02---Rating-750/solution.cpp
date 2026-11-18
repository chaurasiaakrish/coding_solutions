# 3. Count Movies vs TV Shows
def count_content_types(df):
    """
    TODO:
    Count and print how many Movies and TV Shows are present.
    """

    print("\nContent Type Distribution:")
    content_counts = print("\nContent Type Distribution:")
    content_counts = df['type'].value_counts() 

    print("\nDataset Overview:")
    print("Shape of the dataset:", df.shape)
    print("Column Names:", list(df.columns))

    """
    - Column names of the dataset
    - Shape of the dataset
    Print:
    TODO: