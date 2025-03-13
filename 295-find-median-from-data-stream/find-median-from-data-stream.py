class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        l = 0
        r = len(self.arr) - 1

        while l <= r:
            mid = (l + r) // 2

            if self.arr[mid] > num:
                r = mid - 1
            else:
                l = mid + 1
        
        
        self.arr.insert(l, num)


    def findMedian(self) -> float:
        l = len(self.arr)
        if l % 2 == 0:
            return (self.arr[l // 2] + self.arr[l // 2 - 1]) / 2.0
        else:
            return self.arr[l // 2]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()