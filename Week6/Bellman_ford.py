"""CS 5800 HW6 Problem 2&3"""
def bellman_ford(graph, s):
    # Step1: Initialize distances from source to all other vertices as INFINITE
    distances = {node: float('inf') for node in graph}
    distances[s] = 0
    
    # Step2: Relax all edges |V| - 1 times
    for _ in range((len(graph)) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    # Step3: Check for negative-weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                print ("Graph contains negative weight cycles")
                return
    return distances

if __name__ == "__main__":
    graph = {
        1: {2:11, 3:10},
        2: {4:5},
        3: {5:8},
        4: {3:9},
        5: {4:-20},
        # 5: {4:-16},
    }
    
    # Run Bellman-Ford algorithm with source node 1
    source = 1
    distances = bellman_ford(graph, source)
    
    # Print the results
    if distances:
        print(f"Shortest distances from node {source}: ")
        for node, distance in sorted(distances.items()):
            print(f"Node {node}:{distance}")