# python solution to weighted interval schedule problem using python bisect function
from bisect import bisect_right
def WIS(intervals):
    # Step1: sort the intervals based on the finished time 
    intervals.sort(key = lambda x:x[1])
    # Step2: extract the end times for later binary search
    endTimes = [interval[1] for interval in intervals]
    
    # Step3: initialize the DP array
    n = len(intervals)
    dp = [0] * n
    dp[0] = intervals[0][2]
    
    for i in range(1, n):
        # include
        include_weight = intervals[i][2]
        last_non_overlapping = bisect_right(endTimes, intervals[i][0]) - 1
        if last_non_overlapping != -1:
            include_weight += dp[last_non_overlapping]
            
        # exclude   
        exclude_weight = dp[i-1]
        
        dp[i] = max(include_weight, exclude_weight)
    return dp[-1]
            
# Test case
intervals = [(1, 3, 50), (2, 5, 20), (4, 6, 70), (6, 7, 60), (5, 8, 30), (7, 9, 40)]
# Each tuple represents (start time, end time, weight)
print("Maximum weight:", WIS(intervals))