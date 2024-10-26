class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self,u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
                
def kruskal(n, graph):
    # Map characters to integer indices
    node_map = {node:idx for idx, node in enumerate(graph.keys())}
    
    edges = []
    for u in graph:
        for v, weight in graph[u]:
            if (node_map[u], node_map[v], weight) not in edges:
                edges.append((node_map[u], node_map[v], weight)) # convert graph dict to a list of tuples
    edges.sort(key=lambda x:(x[2],x[0],x[1]))
    uf = UnionFind(n)
    mst = []
    total_cost = 0
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u,v,weight))
            total_cost += weight
    mst_with_labels = [(list(node_map.keys())[u],list(node_map.keys())[v], weight) for u, v, weight in mst]
    return mst_with_labels, total_cost

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
    n = len(graph)
    mst, cost = kruskal(n, graph)
    print("Kruskal MST: ", mst)
    print("Total cost of MST: ", cost)
        