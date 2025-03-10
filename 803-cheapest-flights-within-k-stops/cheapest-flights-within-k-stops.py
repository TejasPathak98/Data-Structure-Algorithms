class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # The key idea is the inclusion of stops in the min_heap and cost_dict, as the stops is another factor in finding the lowest cost, which is different than a standard Dijkstra problem

        graph = defaultdict(list)

        for s,d,cost in flights:
            graph[s].append((d,cost))
        
        min_heap = [(0,src,0)] #cost,node,stops
        cost_dict = {} # (node,stops) : (cost)

        while min_heap:
            curr_cost, node , stops = heapq.heappop(min_heap)

            if node == dst and stops <= k + 1:
                return curr_cost
            
            if stops > k + 1:
                continue

            for neighbor,cost in graph[node]:
                new_cost = cost + curr_cost
                
                if (neighbor,stops + 1) not in cost_dict or new_cost < cost_dict.get((neighbor,stops + 1)):
                    heapq.heappush(min_heap, (new_cost,neighbor,stops + 1))
                    cost_dict[(neighbor,stops + 1)] = new_cost

        
        return -1
            

