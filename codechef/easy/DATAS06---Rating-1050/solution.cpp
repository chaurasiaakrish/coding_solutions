import pandas as pd
import numpy as np

# 1. Load Financial Data
def load_data():
    """
    Create and return a DataFrame containing personal income and expense data.
    """
    # Pre-filled data (DO NOT EDIT THIS)
    data = {
        "date": [
            "2025-01-01", "2025-01-03", "2025-01-05", "2025-01-08",
            "2025-01-10", "2025-01-12", "2025-01-15", "2025-01-18",
            "2025-01-20", "2025-01-25", "2025-01-28", "2025-01-30",
            "2025-02-05", "Invalid Date", "2025-02-28"
        ],
        "type": [
            "Income", "Expense", "Expense", "Income",
            "Expense", "Expense", "Expense", "Expense",
            "Expense", "Income", "Expense", "Expense",
            "Expense", "Expense", "Income"
        ],
        "category": [
            "Salary", "Food", "Transport", "Freelance",
            "Rent", "Dining Out", "Shopping", "Entertainment",
            "Utilities", "Salary", "Groceries", "Shopping",
            "Transport", "Food", "Bonus"
        ],
        "amount": [
            50000, 1200, 800, 15000,
            18000, 2500, -5000, 2000,