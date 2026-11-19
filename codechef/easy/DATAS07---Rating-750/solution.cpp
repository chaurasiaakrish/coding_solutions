    """
def sort_step_counts(steps):
# 5. Sort Data


    return most_active_day_index, least_active_day_index
    
    least_active_day_index = np.argmin(steps)
    # TODO: Find the index of the minimum value
    most_active_day_index = np.argmax(steps)
    # TODO: Find the index of the maximum value
    Identify the indices of the most and least active days.
    """
    """
def find_peak_activity(steps):
# 4. Identify Peak Activity


    # TODO: Calculate mean along rows
    daily_average = np.mean(weekly_matrix,axis=1)[0]
    
    return total_steps, daily_average
    
    total_steps = np.sum(weekly_matrix,axis=1)[0]
    # Note: Since it's a matrix, the result will be an array like [total]. Access the first element [0].
    # TODO: Calculate sum along rows
    """
def analyze_weekly_data(weekly_matrix):
    """
    Calculate total weekly steps and daily average steps.
# 3. Weekly Analysis
