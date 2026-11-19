    """
    Create a bar chart and save it to a file.
    """
    # TODO: 8. Set the figure size to (10, 6)
def plot_sales_bar_chart(months, sales):
# 3. Bar Chart (Comparison)


    print(f"Chart saved: {filename}")


    print("Saving Line Chart as 'sales_trend.png'...")
    plt.savefig(filename)
    
    filename = "sales_trend.png"
    # TODO: 7. Save the plot as "sales_trend.png"
    
    plt.legend()
    plt.grid(True)