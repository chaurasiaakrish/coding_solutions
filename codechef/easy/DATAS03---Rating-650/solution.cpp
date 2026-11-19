import matplotlib
matplotlib.use("Agg")  # headless mode (no GUI)

import matplotlib.pyplot as plt


# 1. Load Data
def load_sales_data():
    """
    Returns lists of months and sales figures.
    """
    # TODO: 1. Create a list of strings for months (Jan, Feb, ...)
    months = ['Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 
    
    # TODO: 2. Create a list of integers for sales amounts (e.g., 12000, 15000...)
    sales = [12000, 15000, 17000, 16000, 18000, 20000, 22000, 21000, 19000, 23000, 25000, 27000]
    
    return months, sales


# 2. Line Plot (Trend)
def plot_sales_trend(months, sales):
    """
    Create a line chart and save it to a file.
    """
    # TODO: 3. Set the figure size to (10, 6)
    plt.figure(figsize=(10,6))
    
    # TODO: 4. Plot the data using plt.plot()
    # Hint: Pass 'months', 'sales', color='blue', and marker='o', linestyle='-', linewidth=2
    # Important: specify label="Monthly Sales" for the legend