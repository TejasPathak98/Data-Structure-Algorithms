class MedianFinder:

    def __init__(self):
        self.maxheapforsmaller = []
        self.minheapforlarger = []

    def addNum(self, num: int) -> None:
        if len(self.maxheapforsmaller) == 0 or -self.maxheapforsmaller[0] >= num:
            heapq.heappush(self.maxheapforsmaller,-num)
        else:
            heapq.heappush(self.minheapforlarger, num)
        
        if len(self.maxheapforsmaller) > 1 + len(self.minheapforlarger):
            heapq.heappush(self.minheapforlarger,-heapq.heappop(self.maxheapforsmaller))
        elif len(self.maxheapforsmaller) < len(self.minheapforlarger):
            heapq.heappush(self.maxheapforsmaller, -heapq.heappop(self.minheapforlarger))
        
    def findMedian(self) -> float:
        if len(self.minheapforlarger) == len(self.maxheapforsmaller):
            return (-self.maxheapforsmaller[0] + self.minheapforlarger[0]) / 2
        else:
            return -self.maxheapforsmaller[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()