class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)

        while k:
            x = heapq.heappop(heap)
            k -= 1
        
        return  -1 * x



        