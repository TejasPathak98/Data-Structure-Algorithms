class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        list_adj = {}
        
        for road in roads:
            a,b,d = road
            if a not in list_adj:
                list_adj[a] = []
            if b not in list_adj:
                list_adj[b] = []
            list_adj[a].append((b,d))
            list_adj[b].append((a,d))

        q = [1]
        dist = []
        seen = set()

        while q:
            a = q.pop()
            if a in seen:
                continue
            seen.add(a)
            for children in list_adj[a]:
                c,d = children
                q.append(c)
                dist.append(d)

        return min(dist)
            
            



        