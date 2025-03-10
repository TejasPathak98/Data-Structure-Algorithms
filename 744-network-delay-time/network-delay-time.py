class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph = defaultdict(list)

        # for u,v,t in times:
        #     graph[u].append((v,t))

        # queue = deque([k])
        # time = [float("inf")] * (n + 1)
        # time[k] = 0

        # while queue:
        #     x = queue.popleft()

        #     for neighbor,time_taken in graph[x]:
        #         if time[x] + time_taken < time[neighbor]:
        #             time[neighbor] = time[x] + time_taken
        #             queue.append(neighbor)

        
        # if max(time[1:]) == float("inf"):
        #     return -1
        # else:
        #     return max(time[1:])

        # #O(V + E)  ; O(V + E)

        graph = defaultdict(list)

        for u,v,t in times:
            graph[u].append((v,t)) #....O(E)

        time = {i : float("inf") for i in range(1, n+ 1)}
        min_heap = [(0,k)]
        heapify(min_heap)
        time[k] = 0

        while min_heap:
            curr_time,curr_node = heapq.heappop(min_heap) #O(VlogV)

            if time[curr_node] < curr_time:
                continue
            
            for neighbor,t in graph[curr_node]:
                if t + curr_time < time[neighbor]:
                    time[neighbor] = t + curr_time
                    heapq.heappush(min_heap, (t + curr_time,neighbor)) #O(ElogV)


        if max(time.values()) == float("inf"):return -1
        else: return max(time.values())

        #O(Vlogv) + O(Elogv) + O(E) ; O(E + V)



