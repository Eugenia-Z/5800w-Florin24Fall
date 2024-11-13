# a GPT solution to sequence alignment problem
def sequence_alignment(X, Y, match_score = 1, mismatch_penalty = -1, gap_penalty = -2):
    m, n = len(X), len(Y)
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Initialize base case
    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] + gap_penalty
    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] + gap_penalty
        
    # Fill the dp matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            match = dp[i-1][j-1] + (match_score if X[i-1] == Y[i-1] else mismatch_penalty)
            delete = dp[i-1][j] + gap_penalty
            insert = dp[i][j-1] + gap_penalty
            dp[i][j] = max(match, delete, insert)
    
    # We need dp[m][n]
    alignment_score = dp[m][n]
    return alignment_score, dp

# Example usage:
X="GATTACA"
Y="GCATGCU"
alignment_score, dp_matrix = sequence_alignment(X, Y, 1, -1, -2)
print("The Ailgnment Score is ", alignment_score)
print("DP matrix: ")
for row in dp_matrix:
    print(row)
