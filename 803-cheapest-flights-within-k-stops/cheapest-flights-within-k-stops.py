class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))
        
        min_heap = [(0,src,0)]

        best = dict()

        while min_heap:
            cost,node,steps = heapq.heappop(min_heap)

            if steps > k + 1:
                continue

            if node == dst:
                return cost

            if (node,steps) in best and best[(node,steps)] <= cost:
                continue

            best[(node,steps)] = cost

            for neighbor,cost_weight in graph[node]:
                heapq.heappush(min_heap, (cost + cost_weight,neighbor,steps + 1))
        
        return -1

            
