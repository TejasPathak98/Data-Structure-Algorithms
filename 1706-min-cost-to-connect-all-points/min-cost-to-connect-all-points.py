class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n

        mst_weight = 0
        weight_dict = {0:0}
        heap = [(0,0)]


        while heap:
            curr_weight,curr_index = heapq.heappop(heap)
            #u = points[curr_index]

            if visited[curr_index] or weight_dict.get(curr_index,float("inf")) < curr_weight:
                continue
            
            visited[curr_index] = True
            mst_weight += curr_weight

            for i in range(n):
                if not visited[i]:
                    new_distance = abs(points[i][0] - points[curr_index][0]) + abs(points[i][1] - points[curr_index][1])

                    if new_distance < weight_dict.get(i,float("inf")):
                        weight_dict[i] = new_distance
                        heapq.heappush(heap, (new_distance,i))
            

        return mst_weight



        