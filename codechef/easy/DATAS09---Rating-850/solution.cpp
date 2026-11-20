    plt.ylim(0, 1.1 * df['likes'].max())

    # TODO: Save the plot as "scatter_plot.png"
    plt.savefig("scatter_plot.png")

    print("Chart saved: scatter_plot.png")


# 3. Side-by-Side Bar Chart
    # ylim: 0 to 110% of max likes
    plt.xlim(0, 1.1 * df['views'].max())

    # TODO: Set Axis Limits
    # xlim: 0 to 110% of max views
    # TODO: Enable grid with alpha=0.5
    plt.grid(True, alpha=0.5)

    plt.ylabel("Likes")


    # TODO: Add Title, X-label, and Y-label
    plt.title("Views vs Likes (Size = Comment Count)")
    plt.xlabel("Views")
        alpha=0.5,
        edgecolors='black'
    )
        color='purple',
        df['likes'],
        s=0.3 * df['comment_count'],
        df['views'],
    plt.scatter(