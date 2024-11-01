# Prof Florin's Sol: Mathmetical
def knapsack(v, w, W):
    V = [[0 for x in range(W+1)] for x in range(len(v) + 1)]  # init a 2D table
    for i in range(len(v) + 1):
        for j in range(W + 1):
            if i == 0:
                V[i][j] = 0
            elif w[i-1] > j:  # the curr size of knapsack can't fit in the curr weight w[i-1]
                V[i][j] = V[i-1][j]
            else:
                V[i][j] = max(V[i-1][j-w[i-1]] + v[i-1], V[i-1][j])  # here to remember[j-w[i-1]], the previous status doesn't have w[i-1], then for this iteration, we add v[i-1]
    return V[len(v)][W]
# print(knapsack([60, 100, 120],[10, 20, 30], 50))
                
# More interpretable sol:
def knapsack1(values, weights, capacity):
    n = len(values)
    
    # Create a DP array to store maximum value at each capacity
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    # BUild the DP table in bottom-up matter
    for i in range(1, n+1):
        for w in range(capacity + 1):
            # if including item i exceeds current capacity, exclude it
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of including the item and excluding the item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i-1]] + values[i-1])
    return dp[n][capacity]
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print("Maximum value:", knapsack(values, weights, capacity))