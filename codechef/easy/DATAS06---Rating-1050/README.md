# DATAS06 - Rating 1050

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Personal Financial Analysis System Project

 **Hello developers!**  Welcome to  **Project 5: Personal Financial Analysis System!**  💰📊

Chef has realized that tracking finances manually is a nightmare! 🤯 He has a raw dataset of his recent transactions, but it's a mess. There are typos (negative numbers where they shouldn't be), missing dates, and even some invalid entries.

He needs  **you**  to build a robust  **Financial Analysis System**  that can:

- Clean the messy data (remove errors and invalid rows).
- Calculate his total savings (Income - Expenses).
- Analyze where his money is going (category-wise breakdown).
- Compute statistics (Mean, Median, Std Dev) using NumPy.

Your task is to use  **Pandas and NumPy**  to clean raw financial data, perform meaningful aggregations, and extract actionable financial insights.

 **Important Notes** 

- Do NOT change function names: The testing system relies on them.
- Do NOT modify the provided dataset values.
- You must complete only the missing logic marked with TODO and __________.

 **Dataset** 
You are given a  **pre-filled financial dataset**  inside `load_data()`.
The dataset contains the following columns:

- date: Transaction date (may contain invalid values)
- type: "Income" or "Expense"
- category: Category of income or expense
- amount: Transaction amount (may include negative values or NaN)
### Your Tasks

Open `main.py` and complete the missing logic step by step.

- Load Financial Data Inside the function load_data():
- Create a Pandas DataFrame using the provided dictionary.
- Return the DataFrame. Docs: pd.DataFrame()
- Clean the Financial Data Inside the function clean_data(df):
- Perform the following cleaning steps: Convert the date column to datetime format Use errors="coerce" to handle invalid date strings. Remove rows where date conversion failed (NaT values). Keep only rows with positive amounts (amount > 0) This removes negative typos and missing values automatically. Return the cleaned DataFrame. Docs: pd.to_datetime() function, df.dropna() Method
- Monthly Savings Summary Inside the function calculate_savings(df):
- Group the data by the type column (Income vs Expense).
- Calculate: Total Income Total Expense
- Compute Net Savings using the formula: Net Savings = Total Income − Total Expense
- Return a DataFrame with: Total Income Total Expense Net Savings Docs: df.groupby() Method
- Category-wise Expense Analysis Inside the function analyze_expenses_by_category(df):
- Filter: Create a dataframe containing only rows where type is "Expense".
- Group & Sort: Group by category and sum the amount. Sort the results in descending order (highest expense at the top). Reset Index: Ensure the result is a standard DataFrame, not a Series.
- Return the sorted DataFrame. Docs: df.groupby() Method, df.sort_values() Method, df.reset_index() Method
- Financial Insights Inside the function calculate_advanced_stats(df):
- Extract expense amounts as a NumPy array.
- Using NumPy, calculate: Average Expense Median Expense Maximum Expense Minimum Expense Standard Deviation
- Return: A DataFrame containing these 5 statistical insights. Docs: np.mean() function, np.median() function, np.std() function

 **Expected Output:** 

```
Personal Financial Analysis System

Financial data loaded successfully!

Data cleaned successfully!
        date     type   category   amount
0 2025-01-01   Income     Salary  50000.0
1 2025-01-03  Expense       Food   1200.0
2 2025-01-05  Expense  Transport    800.0
3 2025-01-08   Income  Freelance  15000.0
4 2025-01-10  Expense       Rent  18000.0

Monthly Savings Summary:
   Total Income  Total Expense  Net Savings
0      121000.0        39000.0      82000.0

Expense Breakdown by Category:
        category   amount
0           Rent  18000.0
1       Shopping   7000.0
2      Groceries   4500.0
3      Utilities   3000.0
4     Dining Out   2500.0
5  Entertainment   2000.0
6           Food   1200.0
7      Transport    800.0

NumPy Statistics:
   Average Expense  Median Expense  Max Expense  Min Expense      Std Dev
0           4875.0          2750.0      18000.0        800.0  5296.874078

```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-19T18:58:48.987Z  

```cpp
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
```

---

[View on CodeChef](https://www.codechef.com/problems/DATAS06)