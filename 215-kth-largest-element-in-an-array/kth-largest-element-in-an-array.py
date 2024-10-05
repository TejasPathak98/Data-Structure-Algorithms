class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -1 * num)

        while k:
            if k == 1:
                return -1 * heapq.heappop(heap)
            else:
                heapq.heappop(heap)
                k -= 1
            
        



       

        
        