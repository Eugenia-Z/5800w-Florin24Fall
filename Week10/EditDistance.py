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

# Example Usage
s1 = "kitten"
s2 = "sitting"
print("Edit Distance:", edit_distance(s1, s2))