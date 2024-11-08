# DP appraoch to matric chain multiplication problem
import sys
def matrix_chain_order(dims):
    # Number of matrices
    n = len(dims)-1
    
    # #m[i][j] will hold the minimum number of multiplications needed to multiply matrices from i to j
    m = [[0] * n for _ in range(n)]
    
    # s[i][j] will store the index of the optimizal split point
    s = [[0] * n for _ in range(n)]
    
    # L is the length of the chain 
    for L in range(2, n+1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize # Set to infinity initially 
            for k in range(i, j):
                # q is the number of scalar multiplications
                q = m[i][k] + m[k+1][j] + dims[i] * dims[k+1] * dims[j+1]
                if q < m[i][j]: 
                    # Update minimum count and the split index
                    m[i][j] = q
                    s[i][j] = k
    # return the cost matrix and split matrix
    return m, s 


# Function to print the optimal order of multiplication
def print_optimal_order(s, i, j):
    if i == j:
        print(f"A{i+1}", end="") # Matrix indices start from a
    else:
        print("(", end="")
        print_optimal_order(s, i, s[i][j])
        print_optimal_order(s, s[i][j] + 1, j)
        print(")", end="")

# Example Usage
dims = [30, 35, 15, 5, 10, 20, 25]
m, s = matrix_chain_order(dims)
print("Minimum number of multiplications is: ", m[0][len(dims) - 2])
print("Optimzal multiplication order: ")
print_optimal_order(s, 0, len(dims)-2)