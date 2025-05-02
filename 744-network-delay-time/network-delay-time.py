class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        best_time = {i : float('inf') for i in range(1,n + 1)}
        best_time[k] = 0

        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))



        heap = []
        heappush(heap, (0,k))

        while heap:
            cost,x = heappop(heap)

            if best_time[x] < cost:
                continue
        
            for nei, w in graph[x]:
                new_cost = w + cost
                if new_cost < best_time[nei]:
                    best_time[nei] = new_cost
                    heappush(heap, (new_cost,nei))
        

        
        return max(best_time.values()) if max(best_time.values()) != float('inf') else -1



