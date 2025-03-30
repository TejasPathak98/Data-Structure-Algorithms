class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #Dijsktra with Contraints
        #Push Liberally and Prune later

        graph = defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))
        
        best = dict()

        min_heap = [(0,src,0)]

        while min_heap:
            current_cost , node , stops = heapq.heappop(min_heap)

            if stops > k + 1:
                continue
            
            if node == dst:
                return current_cost
            
            if (node,stops) in best and best[(node,stops)] <= current_cost: # this is pruning step
                continue
            
            best[(node,stops)] = current_cost 

            for neighbor,weight in graph[node]:
                heapq.heappush(min_heap, (weight + current_cost,neighbor,stops + 1))
            
        
        return -1