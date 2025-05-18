class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        best = {}
        graph = defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))

        heap = []
        heappush(heap, (0,src,0))

        while heap:

            cost , node , stops = heappop(heap)

            if node == dst:
                return cost
            
            if stops > k:
                continue
            
            if (node,stops) in best and best[(node,stops)] <= cost:
                continue
            
            best[(node,stops)] = cost

            for nei,w in graph[node]:
                new_cost = cost + w
                heappush(heap, (new_cost,nei,stops + 1))

        
        return -1

