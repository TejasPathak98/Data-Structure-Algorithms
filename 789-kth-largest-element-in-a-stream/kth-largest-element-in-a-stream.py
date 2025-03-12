class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k

        heapq.heapify(self.min_heap) # O(N)...Flyods method inplace

        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap) #O(logK)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val) #O(logK)

        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap) #O(logK)
        
        return self.min_heap[0]

    
        #O(N) + O(logK) ; O(N)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)