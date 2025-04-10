class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num) #Add to Max_heap

        if len(self.max_heap) > len(self.min_heap) + 1:  #Balance according to size
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]: #Balance according to root element of heap
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.max_heap) < len(self.min_heap): #Rebalance if necessary
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        total_length = len(self.min_heap) + len(self.max_heap)

        if total_length % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()