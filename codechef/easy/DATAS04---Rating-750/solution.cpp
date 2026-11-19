    # TODO: 5. Create a scatterplot
    # Arguments: data=df, x="bill_length_mm", y="bill_depth_mm", hue="species"
    # Styling: palette="deep", s=100
    sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species",palette="deep", s=100)

    # TODO: 6. Add Title and Axis Labels
    # Title: "Bill Length vs Bill Depth by Penguin Species"
    # X-label: "Bill Length (mm)", Y-label: "Bill Depth (mm)"
    plt.title("Bill Length vs Bill Depth by Penguin Species")
    plt.xlabel("Bill Length (mm)")
    plt.ylabel("Bill Depth (mm)")
    
    # TODO: 7. Save the plot as "bill_comparison.png"
    filename = "bill_comparison.png"
    plt.savefig(filename)
    
    print(f"Scatter plot saved as: {filename}")


# 3. Box Plot: Body Mass Distribution