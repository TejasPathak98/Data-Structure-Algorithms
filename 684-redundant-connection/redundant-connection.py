class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank  = [1] * n

    def find(self,x): # O(1)
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def Union(self,x,y): #O(1)
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        last_edge = []

        for edge in edges:
            if uf.Union(edge[0] - 1,edge[1] - 1) == False:
                last_edge = edge
        
        return last_edge