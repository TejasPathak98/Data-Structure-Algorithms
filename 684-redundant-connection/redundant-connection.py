class UnionFind:
    def __init__(self,N):
        self.parents = list(range(N + 1))
        self.ranks = [0] * (N + 1)

    def find(self,x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
            self.ranks[px] += 1
        else:
            self.parents[px] = py
            self.ranks[py] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        the_edge = []

        for edge in edges:
            if not uf.union(edge[0],edge[1]):
                the_edge = edge
        
        return the_edge
        



        