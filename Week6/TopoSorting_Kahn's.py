# Python implementation of Kahn's topological ordering
from collections import deque, defaultdict

def topo_sorting(num_nodes, edges):
    # init gragh, in_degree array, queue to store 0-indegree nodes, res variable
    graph = defaultdict(list)
    in_degree = {i:0 for i in range(num_nodes)}
    res = []
    for src, dst in edges:
        graph[src].append(dst)
        in_degree[dst] += 1
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    
    while queue:
        curr = queue.popleft()
        res.append(curr)
        
        for neighbor in graph[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    # If topological ordering includes all nodes, return it;
    if len(res) == num_nodes:
        return res
    # Otherwise, return None, cycle detected 
    else:
        return None

# Example usage:
num_nodes = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print("Topological Order:", topo_sorting(num_nodes, edges))