# DATAS09 - Rating 850

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### YouTube Content Strategy Analyzer Project

 **Hello developers!**  Welcome to  **Project 3: YouTube Content Strategy Analyzer!**  🎯📊

Chef loves watching YouTube! He has collected data from his  **favourite YouTube channels**  to understand what makes a video successful. The dataset contains metrics like  **views**,  **likes**, and  **comments**  for various trending videos.

Chef wants you to build a Visual Dashboard to answer questions like:

- Which videos are watched the most?
- Do more views actually translate into more likes?
- Which videos create the most discussion?

Your  **task**  is to turn this raw data into beautiful, insightful charts!

 **Important Notes** 
You are given a single file: `main.py`:

- Do NOT change function names: The testing system relies on them.
- Do NOT use plt.show(): This project runs in a "headless" environment (no screen). You must use plt.savefig("filename.png") to generate output.
- Do NOT close the plot after saving: Do not call plt.close() or similar functions after saving the plot.
- All functions are already defined in main.py. You need to complete the missing logic.

 **Dataset** 
You will work with the file `youtube.csv`. It contains columns such as:

- title (Video Name)
- channel_title (Channel Name)
- views (Total Views)
- likes (Total Likes)
- comment_count (Total Comments)
### Your Tasks
- Load the YouTube Dataset Inside load_data(): Read the CSV file using Pandas. Docs: pd.read_csv()
- Visualize Views vs. Likes (Scatter Plot) Inside plot_scatter(df): This chart will show if popular videos (high views) also get appreciated (high likes). We will also use bubble size to show comments!
- Setup: Set figure size to 10 inches by 6 inches.
- Plotting: Create a scatter plot where: X-axis: views Y-axis: likes Size (s): comment_count * 0.3 (Scaling down for readability) Color: "purple" Transparency (alpha): 0.5 Edge Color: "black"
- Styling: Title: "Views vs Likes (Size = Comment Count)" Labels: X-label="Views", Y-label="Likes" Grid: Enable grid with alpha 0.5.
- Limits: Stretch axes to 110% of max values ((max value of columns) * 1.1) to let the data breathe.
- Save: Save the chart as scatter_plot.png. Docs: plt.scatter() | plt.grid() | plt.xlim() | plt.savefig() | plt.title() function | plt.xlabel() function | plt.ylabel() function
- Compare Likes vs. Comments (Side-by-Side Bar Chart) Inside bar_chart_side_by_side(df): This chart compares two different metrics for the same video side-by-side.
- Setup: Set figure size to 12 inches by 6 inches (wider for video titles).
- Logic: We need to manually shift the bars so they don't overlap: Likes: Shift Left (x - width/2), Color: "skyblue". Comments: Shift Right (x + width/2), Color: "orange".
- Styling: Title: "Engagement Analysis: Likes vs Comments" Labels: X-label="Video Title", Y-label="Count" Rotation: Rotate x-axis labels vertically so they don't overlap. Legend: Add a legend to explain the colors. Grid: Enable grid only on the Y-axis with alpha 0.7.
- Final Touch: We have written plt.tight_layout() to ensure long titles aren't cut off (Code already provided).
- Save: Save the chart as bar_chart.png. Docs: plt.bar() | plt.xticks() | plt.legend() | plt.tight_layout() | plt.title() function | plt.xlabel() function | plt.ylabel() function

 **Expected Output:** 
When you run the code, your program should print the  **following messages**  and  **generate two image files**  in the same directory:

- Console Output:

```
YouTube Content Strategy Analyzer...

Dataset Preview:
               title   channel_title    views  likes  dislikes  comment_count
0   The New SpotMini  BostonDynamics    75752   9419        52           1230
1   VLOG Delhi Metro   TravelIndiaYT   204889   6031       225            510
2  U2 - The Blackout          U2VEVO    60506   5389       106            455
3  NF - Let You Down          NFVEVO  1774018  40417      5002           1686
4   Live in the now!       poofables    95085   7909      1652            593
Chart saved: scatter_plot.png
Chart saved: bar_chart.png

```

- Generated Files:
- scatter_plot.png
- bar_chart.png

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-20T21:21:13.317Z  

```cpp
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
```

---

[View on CodeChef](https://www.codechef.com/problems/DATAS09)