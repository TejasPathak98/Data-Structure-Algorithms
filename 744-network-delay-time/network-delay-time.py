class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Normal Dijsktra

        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        
        min_heap = [(0,k)]

        time_dict = {i : float("inf") for i in range(1,n + 1)}
        time_dict[k] = 0

        total_time = 0

        heapify(min_heap)


        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            for neighbor,weight in graph[node]:
                new_weight = weight + current_time
                if new_weight < time_dict[neighbor]:
                    heapq.heappush(min_heap, (new_weight,neighbor))
                    time_dict[neighbor] = new_weight
        

        if max(time_dict.values()) == float("inf"):
            return -1
        else:
            return max(time_dict.values())



