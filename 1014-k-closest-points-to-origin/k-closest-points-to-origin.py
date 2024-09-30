class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []
        heap = []
        ans = []

        for p in points:
            px = p[0]
            py = p[1]
            dist = math.sqrt((px ** 2) + (py ** 2))
            heapq.heappush(heap,[dist,px,py])
        
        for i in range(k):
            dx,px,py = heapq.heappop(heap)
            ans.append([px,py])
        
        return ans



        