class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # Initialize each element's parent to themselves
        self.rank = [0] * n  # Initialize each element's rank to 0  
    
    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x 
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1
if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(0,1)
    uf.union(2,3)
    uf.union(0,4)
    
    print(uf.find(1))
    print(uf.find(3))
            