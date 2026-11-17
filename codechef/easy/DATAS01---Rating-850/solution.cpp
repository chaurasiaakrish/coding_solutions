
# 3. Analyze and print performance insights
def analyze_performance(marks, average_marks):
    """
    Analyze performance: Find students above average and those who failed.
    """

    return average, median, std_deviation
    # Returning all three values as a tuple

    print("Standard Deviation: ", std_deviation)
    print("Median Marks: ", median)
    # TODO: Filter 'marks' to find those greater than 'average_marks'
    above_average = [m for m in marks if m > average_marks] 
    
    # TODO: Filter 'marks' to find those less than 35 (Fail threshold)
    failed_students = [m for m in marks if m<35]

    print("\n--- Performance Insights ---")