class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        #Add to Max_heap first all the time
        heappush(self.max_heap, -num)

        #Balance the max of max_heap and min of min_heap
        if self.max_heap and self.min_heap and -self.max_heap[0]  > self.min_heap[0]:
            heappush(self.min_heap, -heappop(self.max_heap))

        #Balance the Min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        
        #Balance the Max_heap
        if len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
        
        
    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()