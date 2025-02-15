class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i : [] for i in range(1,n + 1)}

        for u,v,w in times:
            adj[u].append((v,w))

        network = {i : float('inf') for i in range(1,n + 1)}
        network[k] = 0 
        heap = [(0,k)]

        while heap:
            curr_time,curr_node = heapq.heappop(heap)

            for node,time in adj[curr_node]:
                if time + curr_time < network[node]:
                    network[node] = time + curr_time
                    heapq.heappush(heap, (network[node],node))
        
        t = max(network.values())
        if t == float("inf"):return -1
        else:return t

        