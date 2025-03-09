class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,t in times:
            graph[u].append((v,t))

        queue = deque([k])
        time = [float("inf")] * (n + 1)
        time[k] = 0

        while queue:
            x = queue.popleft()

            for neighbor,time_taken in graph[x]:
                if time[x] + time_taken < time[neighbor]:
                    time[neighbor] = time[x] + time_taken
                    queue.append(neighbor)

        
        if max(time[1:]) == float("inf"):
            return -1
        else:
            return max(time[1:])

