class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n + 1))
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def UF(self,x,y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False
        else:
            self.parent[py] = px
            return True
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        the_edge = []
        uf = UnionFind(len(edges) + 1)

        for edge in edges:
            if not uf.UF(edge[0],edge[1]):
                the_edge = edge
        
        return the_edge

        