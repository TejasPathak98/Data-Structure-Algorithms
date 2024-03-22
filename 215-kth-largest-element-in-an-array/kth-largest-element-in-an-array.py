class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq 
        heap = nums 
        heapify(heap) 

        while len(heap) > k:
            heappop(heap) 
        
        return heap[0]
        