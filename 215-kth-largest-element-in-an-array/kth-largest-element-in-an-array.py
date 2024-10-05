class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -1 * num)

        res= []

        while k:
            res.append(-1 * heapq.heappop(heap))
            k -= 1
        
        return res[-1]


       

        
        