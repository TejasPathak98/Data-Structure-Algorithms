class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i : [] for i in range(n)}

        for u,v,w in flights:
            adj[u].append((v,w))
        
        heap = [(0,src,0)]
        best_cost = {}

        while heap:
            cost,node,stops = heapq.heappop(heap)


            if node == dst:
                return cost

            if stops > k:
                continue
            
            for new_node,weight in adj[node]:
                new_cost = weight + cost
                if (new_node,stops + 1) not in best_cost or new_cost < best_cost[(new_node,stops + 1)]:
                    best_cost[(new_node,stops + 1)] = new_cost
                    heapq.heappush(heap, (new_cost,new_node,stops+ 1))
            


        return -1     
