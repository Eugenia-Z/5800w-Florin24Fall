def Floyd_Warshall_All_Pairs(graph):
    # num of vertices in the graph
    n = len(graph)
    
    # initialize 3 types of value: edge exists, edge to itself, edge doesn't exist
    
    # Initialize the distance matrix with the graph values
    distance = [[float('inf')] * n for _ in range(n)]
    
    # Set the initial distances based on the input graph
    for i in range(n):
        for j in range(n):
            distance[i][j] = graph[i][j]
            
    # Set the diagnol to zero (distance from a node to itself is zero)
    for i in range(n):
        distance[i][i] = 0
        
    # 3 for loops to update the distances
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If the path through vertice k is shorter, update distance[i][j]
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance
    
# Example usage
graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]

distances = Floyd_Warshall_All_Pairs(graph)
for row in distances:
    print(row)