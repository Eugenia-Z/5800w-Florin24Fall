import numpy as np

def find_paths(adj_matrix):
    # Get the number of vertices (size of the adjacency matrix)
    n = adj_matrix.shape[0]
    
    # Create the identity matrix I of size n x n
    I = np.eye(n, dtype=int)
    
    # Compute (I + A)^(n-1)
    result_matrix = np.linalg.matrix_power(I + adj_matrix, n - 1)
    
    return result_matrix

def check_path(result_matrix, s, t):
    # Check if there is a path from vertex s to vertex t
    return result_matrix[s, t] != 0

# Example usage
if __name__ == "__main__":
    # Example graph with 4 vertices and no self-loops
    # Adjacency matrix for the graph:
    # 0 -> 1, 1 -> 2, 2 -> 3, 3 -> 0
    adj_matrix = np.array([[0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1],
                           [1, 0, 0, 0]])

    # Compute the result matrix (I + A)^(n-1)
    result_matrix = find_paths(adj_matrix)

    print("Result Matrix (I + A)^(n-1):")
    print(result_matrix)

    # Check if there's a path between specific vertices
    s, t = 0, 3  # Check if there's a path from vertex 0 to vertex 3
    if check_path(result_matrix, s, t):
        print(f"There is a path from vertex {s} to vertex {t}.")
    else:
        print(f"There is no path from vertex {s} to vertex {t}.")
