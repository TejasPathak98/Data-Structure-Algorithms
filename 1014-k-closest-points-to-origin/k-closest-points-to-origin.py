class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for point in points:
            x = point[0]
            y = point[1]
            dist = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(min_heap, (dist,x,y))

        ans = []

        for _ in range(k):
            _,x,y = heapq.heappop(min_heap)
            ans.append([x,y])
        
        return ans
