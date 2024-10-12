class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []

        for num in nums:
            heapq.heappush(heap,num)

            while len(heap) > k:
                heapq.heappop(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return heap[0]

        # for num in nums:
        #     heapq.heappush(heap,-num)

        # while k:
        #     x = heapq.heappop(heap)
        #     k -= 1
        
        # return -1* x

