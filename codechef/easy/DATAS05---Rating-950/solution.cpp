    # --- Layer 3: Shares (Stacked on Likes + Comments) ---
    # TODO: 9. Calculate the new bottom (likes + comments)
    bottom_heights = df['likes']+df['comments']
    
    # TODO: 10. Plot 'shares' vs 'post_id' using bottom=bottom_heights
    # Label="Shares", Color="#2ecc71"
    plt.bar(df['post_id'], df['shares'], bottom=bottom_heights, label="Shares", color="#2ecc71")

    # TODO: 11. Add title, labels, and legend
    # Title: "Engagement Composition per Post (Stacked)"
    plt.title("Engagement Composition per Post (Stacked)")
    plt.xlabel("Post ID")
    plt.ylabel("Count")
    
    filename = "engagement_composition.png"

    # TODO: Save the plot
    plt.savefig(filename)
    plt.legend()