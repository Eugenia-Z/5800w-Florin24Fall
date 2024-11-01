# Helper function to find the last non-overlapping interval index
def find_last_non_overlapping(intervals, i):
    low, high = 0, i-1
    while low <= high:
        mid = (low + high) // 2
        if intervals[mid][1] <= intervals[i][0]:
            if intervals[mid+1][1] <= intervals[i][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1

def weighted_intervals_scheduling(intervals):
    # Step1: sort the intervals based on end times
    intervals = sorted(intervals, key = lambda x: x[1])
    n = len(intervals)

    # DP array to store the maximum weight achievable at each interval
    dp = [0] * n
    dp[0] = intervals[0][2]
    
    for i in range(1, n):
        # include current interval
        include_weight = intervals[i][2]
        
        #Find the last interval that doesn't overlap
        last_non_overlap = find_last_non_overlapping(intervals, i)
        if last_non_overlap != -1:
            include_weight += dp[last_non_overlap]
        
        # exclude current interval
        exclude_weight = dp[i-1]
        
        # Maximum weight at this interval is max of including or excluding it
        dp[i] = max(include_weight, exclude_weight)
    
    # The maximum weight is at the last interval
    return dp[-1]


# Test case
intervals = [(1, 3, 50), (2, 5, 20), (4, 6, 70), (6, 7, 60), (5, 8, 30), (7, 9, 40)]
# Each tuple represents (start time, end time, weight)
print("Maximum weight:", weighted_intervals_scheduling(intervals))