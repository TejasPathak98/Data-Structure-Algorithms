class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph = [[] for i in range(n)]
        for u,v,w in roads:
            graph[u - 1].append((v - 1,w))
            graph[v - 1].append((u - 1,w))
        
        ans = [float("inf")]*n 

        for i in range(n):
            dist = [float("inf")]*n
            dist[i] = 0
            pq = []
            heapq.heappush(pq, (0,i))

            while pq:
                d , u = heapq.heappop(pq)
                ans[i] = min(ans[i],k*d + d + appleCost[u])
                for v , w in graph[u]:
                    if dist[v] > w + dist[u]:
                        dist[v] = dist[u] + w 
                        heapq.heappush(pq, (dist[v],v))
        
        return ans


        