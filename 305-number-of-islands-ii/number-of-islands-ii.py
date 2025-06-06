class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def add(self,node):
        if node not in self.parent:
            self.parent[node] = node
            self.rank[node] = 0

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):

        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return False
        
        if self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
        elif self.rank[rooty] > self.rank[rootx]:
            self.parent[rootx] = rooty
        else:
            self.parent[rooty] = rootx
            self.rank[rootx] += 1

        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        result = []
        land = set()
        count = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        uf = UnionFind()

        for pos in positions:
            pos = tuple(pos)
            if pos in land:
                result.append(count)
                continue
            

            land.add(pos)
            uf.add(pos)
            count += 1

            for direction in directions:
                nx = pos[0] + direction[0]
                ny = pos[1] + direction[1]
                new_pos = (nx,ny)

                if 0 <= nx < m and 0 <= ny < n and new_pos in land:
                    if uf.union(pos, new_pos):
                        count -= 1

            
            result.append(count)

        
        return result














        