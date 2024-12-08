# Using dict actually makes it a higher dimension, storing all the actual strings! Impressive! 
def lcs(X, Y):
    V = {}  # init to dict
    for i in range(len(X) + 1): 
        V[(i, 0)] = ""
    for j in range(len(Y) + 1): 
        V[(0, j)] = ""
    
    # Fill in the 2D dp table
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            if x == y:
                V[(i+1, j+1)] = V[(i,j)] + x
            else:
                V[(i+1, j+1)] = max([V[(i+1, j)],V[(i,j+1)]], key=len)
    return V[(len(X), len(Y))]
print(lcs('xxxxxaxxxbxxc', 'abc'))



def LCS_2d(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]



def lcs_1d(str1, str2):
    m = len(str1)
    n = len(str2)
    
    dp = [0] * (n+1) # DP array to store the row
    
    for i in range(1, m+1):
        diagnol_val = 0  # prev to store the diagnol value in 2D (before starting a new row, it's always set to zero because our initialization)
        for j in range(1, n+1):
            temp = dp[j] # use temp variable to store curr dp[j] from last iteration (before overwritting.) This dp[j] serves as the top value in current iteration and diagnol value in the next iteration (move to the right by 1)
            if str1[i-1] == str2[j-1]:
                dp[j] = diagnol_val + 1
            else:
                dp[j] = max(dp[j], dp[j-1]) # here the dp[j] is the top value from previous iteration, dp[j-1] is the left value
            diagnol_val = temp # use the previous dp[j] (before overwritting) as the new diagnol value, which stored in prev
    return dp[n]
            