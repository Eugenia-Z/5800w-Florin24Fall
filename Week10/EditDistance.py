# Python code to implement edit distance (Levenshtein Distance)
def edit_distance(s1, s2):
    # init the dp table
    m, n = len(s1), len(s2)
    
    # Initialize the dp table with size (m+1) * (n+1)
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # fill the base cases for transforming an empty string to a substring
    for i in range(m+1):
        dp[i][0] = i # Deleting all characters from s1 to get an empty s2
    for j in range(n+1):
        dp[0][j] = j # Inserting all characters of s2 into an empty s1
        
    # traverse two strings, determine to delete, insert or replace 
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]: # Characters match, no operation needed
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + 1, # delete 
                               dp[i][j-1] + 1, # insert
                               dp[i-1][j-1] + 1 # replace
                               )
    return dp[m][n]


def edit_distance_1d(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [0] * (n+1)
    
    # still need to init the first row with all the value of another str length
    for j in range(1, n+1):
        dp[j] = j
    
    # populate the row and update for m times
    for i in range(1, m+1):
        # init prev (diagnol value in 2D to dp[0])
        prev = dp[0]
        # init the dp[0] value: the distance itself is the index
        dp[0] = i
        for j in range(1, n+1):    
            # use a temp value to store dp[j] from last iteration to prevent overwriting
            temp = dp[j]
            if s1[i-1] == s2[j-1]:
                dp[j] = prev 
            else:
                dp[j] = min(dp[j], dp[j-1], prev) + 1 # choose the min cost from top, left, and diagnol
            prev = temp # store the dp[j] as the diagnol value for next iteration
        return dp[n]
    
    
# Example Usage
s1 = "kitten"
s2 = "sitting"
print("Edit Distance:", edit_distance(s1, s2))