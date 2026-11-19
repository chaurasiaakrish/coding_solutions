        print("\nData cleaned successfully!")
        print(df.head())

    # 3. Monthly Summary (Income vs Expense)
    print("\nMonthly Savings Summary:")
    print(calculate_savings(df))

    # 4. Category-wise Analysis
    print("\nExpense Breakdown by Category:")
    if df is not None:
    df = clean_data(df)
    # 2. Data Cleaning
    
    print("Financial data loaded successfully!")
    df = load_data()
    # 1. Load Data

    print("Personal Financial Analysis System\n")
if __name__ == "__main__":


    return insights_df

    insights_df = pd.DataFrame([insights])
    else:
        insights = {}

    # TODO: 14. Convert the insights dictionary to a DataFrame for better display
        }
            "Std Dev": np.std(expense_values)         
            "Min Expense": np.min(expense_values),    