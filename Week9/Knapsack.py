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
print(knapsack([60, 100, 120],[10, 20, 30], 50))
                