"""HW 7 Question 2 Bellman-Ford Algorithm 
"""

def bellman_ford(graph, start):
    """ Function to implement Bellman Ford algorithm """
    # Initialize ditances from start to all nodes as infinity
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    
    parent = {start: None}
    n = len(graph)
    for _ in range(n - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distance[node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[node] + weight
                    parent[neighbor] = node
    
    # check for negative-weight cycle              
    for node in graph:
        for neighbor, weight in graph[node]:
            if distance[node] + weight < distance[neighbor]:
                print("Graph has a negative-weight cycle")
                return None, None
    return distance, parent

def print_shortest_path_tree(parent):
    """Function to print the shortest-path tree
    """
    print("Shortest-path tree (node: parent): ")
    for node in parent:
        if parent[node] is not None:
            print(f"{node}: {parent[node]}")
            
if __name__ == "__main__":
    graph = {
    'A': [('B', 4), ('C', -2)],
    'B': [('G', -2), ('H', -4)],
    'C': [('D', 2), ('F', 1)],
    'D': [],
    'E': [('H', 3), ('F', -2)],
    'F': [],
    'G': [('I', -1)],
    'H': [('G', 1)],
    'I': [('H', 1)],
    'S': [('A', 7), ('C', 6), ('F', 5), ('E', 6)]
}
distance, parent = bellman_ford(graph, 'A')
print("Shortest distances from node A:")
for node in distance:
    print(f"Distance to {node}: {distance[node]}")
    
print_shortest_path_tree(parent)