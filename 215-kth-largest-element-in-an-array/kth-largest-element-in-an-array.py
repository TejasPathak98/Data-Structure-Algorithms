class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -1 * num)

        #res= []

        while k:
            ans = -1 * heapq.heappop(heap)
            k -= 1
            if k == 0:
                return ans
        
        return res[-1]


       

        
        