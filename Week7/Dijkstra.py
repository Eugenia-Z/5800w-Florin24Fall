"""HW 7 Question1 Dijkstra Algorithm"""
import heapq

def dijkstra(graph, start):
    """ Function to implement Dijkstra's algorithm
    """
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    pq = [(0, start)]
    parent = {start: None}

    while pq:
        curr_dist, curr_node = heapq.heappop(pq) 
        if curr_dist > distance[curr_node]:
            continue
        for neighbor, weight in graph[curr_node]:
            dist = curr_dist + weight
            if dist < distance[neighbor]:
                distance[neighbor] = dist
                parent[neighbor] = curr_node
                heapq.heappush(pq, (dist, neighbor))
    return distance, parent

def print_shortest_path_tree(parent):
    """Function to print the shortest-path tree
    """
    print("Shortest-path tree (node: parent):")
    for node in parent:
        if parent[node] is not None:
            print(f"{node} : {parent[node]}")

if __name__ == "__main__":
    graph = {
    'A': [('B', 1), ('E', 4), ('F', 8)],
    'B': [('C', 2), ('F', 6), ('G', 6)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 1), ('H', 4)],
    'E': [('F', 5)],
    'F': [],
    'G': [('F', 1), ('H', 1)],
    'H': []
}
    distances, parent = dijkstra(graph, 'A')
    print("Shortest distance from node A: ")
    for node in distances:
        print(f"Distance to {node}: {distances[node]}")
    print_shortest_path_tree(parent)
    