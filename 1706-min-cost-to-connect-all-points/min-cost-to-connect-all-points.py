class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        best = [float('inf')] * n
        best[0] = 0
        heap = []
        heappush(heap, (0,0))
        visited = set()

        def helper(p1,p2):
            return abs(points[p1][0] - points[p2][0]) + abs(points[p2][1] - points[p1][1])


        while heap:

            cost, point_idx = heappop(heap)

            visited.add(point_idx)

            if cost > best[point_idx]:
                continue
            
            best[point_idx] = cost

            for j in range(n):
                if j != point_idx:
                    if j not in visited:
                        new_cost = helper(point_idx,j)
                        heappush(heap, (new_cost,j))


        return sum(best)



