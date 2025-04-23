class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))
        
        min_heap = []
        heappush(min_heap,(0,src,0))

        best = dict()

        while min_heap:

            cost , node , stops = heappop(min_heap)

            if stops > k + 1:
                continue
            
            if node == dst:
                return cost
            
            if (node,stops) in best and best[(node,stops)] <= cost:
                continue
            
            best[(node,stops)] = cost

            for nei,w in graph[node]:
                heappush(min_heap,(cost + w,nei,stops + 1))

        
        return -1