class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)

        for u,v in tickets:
            heapq.heappush(graph[u],v)
        
        path = []

        def dfs(node):

            while graph[node]:
                nei = heapq.heappop(graph[node])
                dfs(nei)
            
            path.append(node)

        dfs('JFK')

        return path[::-1]