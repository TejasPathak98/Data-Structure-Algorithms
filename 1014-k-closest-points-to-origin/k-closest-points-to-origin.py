class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points

        heap = []

        for point in points:
            x = point[0]
            y = point[1]

            dis = sqrt((x**2) +(y**2))

            heapq.heappush(heap,(dis,point))
        
        ans = []

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans

        