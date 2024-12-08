# A python solution to Maximum Indepedent Set(MIS) problem
from collections import defaultdict
# this solution applies to mul-ti branches
# for binary trees, using variables instead of DP table will suffice.

def max_independent_set(tree, root = 0):
    n = len(tree)
    dp = [[0, 0] for _ in range(n)]
    visited =[False] * n
    
    # DFS function to fill dp table
    def dfs(u):
        visited[u] = True
        dp[u][0] = 0  # When u is not include in the independent set
        dp[u][1] = 1  # When u is included in the independent set
        
        # this for loop allows for multi-branches
        for v in tree[u]:
            if not visited[v]:
                dfs(v)
                dp[u][0] += max(dp[v][0], dp[v][1]) # when not inclu u, can include or not inclue its child v
                dp[u][1] += dp[v][0]  # when inclu u, must not inclue its child v
                
    # Start DFS from the root
    dfs(root)
    
    # The answer is the maximum of including or excluding the root
    return max(dp[root][0], dp[root][1])


# Example Usage
# Construct a sample tree as an adjacency list
tree = defaultdict(list)
tree[0].extend([1, 2])
tree[1].extend([0, 3, 4])
tree[2].extend([0])
tree[3].extend([1])
tree[4].extend([1])

# Compute the maximum independent set size
result = max_independent_set(tree)
print("Maximum Independent Set Size:", result)