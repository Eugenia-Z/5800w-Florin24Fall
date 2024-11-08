from collections import defaultdict, deque

def topological_sort(V, adj):
    in_degree = [0] * V
    for u in range(V):
        for v, _ in adj[u]:
            in_degree[v] +9= 1
    
    # 入度为0的先入queue
    queue = deque([i for i in range(V) if in_degree[i] == 0])
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, _ in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)    
    return topo_order

# Function to find shortest path in a DAG:
def shortest_path_dag(V, adj, source):
    
    # Step 1: Topological sort the graph
    topo_order = topological_sort(V, adj)
    
    # Step 2: Initialize distances
    dist = [float('inf')] * V
    dist[source] = 0
    
    # Step 3: Relax edges in topological order
    for u in topo_order:
        if dist[u] != float('inf'):
            for v, weight in adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    return dist
    
if __name__ == "__main__":
    # Number of vertices
    V = 6
    
    # Adjacency list for the graph (node, weight)
    adj = defaultdict(list)
    adj[0].append((1, 5))
    adj[0].append((2, 3))
    adj[1].append((3, 6))
    adj[1].append((2, 2))
    adj[2].append((4, 4))
    adj[2].append((5, 2))
    adj[2].append((3, 7))
    adj[3].append((4, -1))
    adj[4].append((5, -2))
    
    # Source node
    source = 0
    
    # Find the shortest path
    shortest_distances = shortest_path_dag(V, adj, source)
    print("Shortest distances from source:" , shortest_distances)