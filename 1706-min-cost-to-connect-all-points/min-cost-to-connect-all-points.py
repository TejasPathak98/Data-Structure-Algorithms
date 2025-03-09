class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Prim's Algo (Sequential)
        n = len(points)

        mst_weight = 0
        min_heap = [(0,0)]
        weights = {0:0}
        visited = [False] * n

        while min_heap:
            curr_weight,curr_node = heapq.heappop(min_heap)

            if visited[curr_node]:
                continue
            
            if weights.get(curr_node,float("inf")) < curr_weight:
                continue
            
            visited[curr_node] = True
            mst_weight += curr_weight

            for i in range(n):
                if not visited[i]:
                    dist = abs(points[i][0] - points[curr_node][0]) + abs(points[i][1] - points[curr_node][1])

                    if dist < weights.get(i,float("inf")):
                        heapq.heappush(min_heap, (dist,i))

        
        return mst_weight

