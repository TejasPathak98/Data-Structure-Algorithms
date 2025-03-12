class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # The below is a min heap operation but can be converted to Max heap for O(klogN) TC...least distance...remember rule of thumb
        # min_heap = []

        # for point in points:
        #     x = point[0]
        #     y = point[1]
        #     dist = math.sqrt(x ** 2 + y ** 2)
        #     heapq.heappush(min_heap, (dist,x,y))

        # ans = []

        # for _ in range(k):
        #     _,x,y = heapq.heappop(min_heap)
        #     ans.append([x,y])
        
        # return ans

        # #O(NlogN) ; O(N)

        max_heap = []

        for point in points:
            x = point[0]
            y = point[1]
            dist = -1 * math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(max_heap, (dist,x,y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [[x,y] for _,x,y in max_heap]


