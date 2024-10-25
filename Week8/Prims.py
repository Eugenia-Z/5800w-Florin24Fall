import heapq

def prim(n, graph):
    
    start_node = list(graph.keys())[0]
    min_heap = [(0, start_node, None)]  # (weight, node) starting with node A
    mst = []
    visited = set()
    total_cost = 0
    
    while len(mst) < n - 1 and min_heap:
        weight, curr, parent = heapq.heappop(min_heap)
        
        if curr in visited:
            continue
        
        visited.add(curr)
        total_cost += weight
        
        # Add edges to the heap
        if parent is not None:
            mst.append((parent, curr, weight))
        
        for neighbor, neighbor_weight in graph[curr]:
            heapq.heappush(min_heap, (neighbor_weight, neighbor, curr))
                
    return mst, total_cost

if __name__ == "__main__":
    graph = {
        'A': [('B', 6), ('E', 1)],     # A: B-'G', E-'B'
        'B': [('A', 6), ('C', 5), ('F', 2), ('E', 2)],  # B: A-'G', C-'F', F-'C', E-'C'
        'C': [('B', 5), ('F', 5), ('G', 4), ('D', 6)],  # C: B-'F', F-'F', G-'E', D-'G'
        'D': [('C', 6), ('G', 5), ('H', 7)],  # D: C-'G', G-'F', H-'H'
        'E': [('A', 1), ('B', 2), ('F', 1)],  # E: A-'B', B-'C', F-'B'
        'F': [('B', 2), ('E', 1), ('C', 5), ('G', 3)],  # F: B-'C', E-'B', C-'F', G-'D'
        'G': [('F', 3), ('C', 4), ('D', 5), ('H', 3)],  # G: F-'D', C-'E', D-'F', H-'D'
        'H': [('D', 7), ('G', 3)]  # H: D-'H', G-'D'
    }
    n = 8
    mst, cost = prim(n, graph)
    print("Prim's MST: ", mst)
    print("Total cost of MST: ", cost)
    