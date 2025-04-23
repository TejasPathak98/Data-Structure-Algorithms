class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        
        time_dict = [float('inf')] * (n + 1)
        time_dict[k] = 0

        min_heap = []
        heappush(min_heap,(0,k))

        while min_heap:
            cost,node = heappop(min_heap)

            if time_dict[node] < cost:
                continue
            
            for nei,w in graph[node]:
                new_cost = cost + w
                if new_cost < time_dict[nei]:
                    time_dict[nei] = new_cost
                    heappush(min_heap,(new_cost,nei))
        

        
        if any(x == float('inf') for x in time_dict[1:]):
            return -1
        else:
            return max(time_dict[1:])



