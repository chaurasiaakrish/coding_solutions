        # 5. Fix Types & Strings
        df = fix_data_types(df)
        
        df = remove_duplicates(df)
        
        
        # 4. Remove Duplicates
        df = clean_missing(df)

        # 3. Clean Missing Values

        # 2. Inspect
        inspect_data(df)
    if df is not None:
        print("Original Dataset Preview:")
        print(df.head())

    # 1. Load data
    df = load_data()

if __name__ == "__main__":
    print("Online Course Enrollment Data Cleaner...\n")

    print(f"\nCleaned data saved to '{filename}'")

    df.to_csv("cleaned_udemy_courses.csv",index=False)
    # TODO: Save the dataframe to "cleaned_udemy_courses.csv" without the index

    filename = "cleaned_udemy_courses.csv"
    """
    Save the cleaned DataFrame to a new CSV file.