class Solution:
    #maxheap
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points
        
        heap = []

        for point in points:
            x = point[0]
            y = point[1]
            dis = sqrt((x**2) + (y**2))

            heapq.heappush(heap, (-dis,point))

            while len(heap) > k:
                heapq.heappop(heap)
            
            
                

        return [x[1] for x in heap] 