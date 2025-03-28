class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        l = 0
        h = len(self.arr) - 1

        while l <= h:
            mid = (l + h) // 2

            if self.arr[mid] > num:
                h = mid - 1
            else:
                l = mid + 1
        
        self.arr.insert(l, num)  # TC : O(n ^2)

    def findMedian(self) -> float:
        if len(self.arr) % 2 == 1:
            return self.arr[len(self.arr) // 2]
        else:
            return (self.arr[len(self.arr) // 2] + self.arr[(len(self.arr) // 2) -1]) / 2.0


    # TC : O(n ^2)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# If num is greater than all elements, l ends up at the end, so num is inserted at the end.

# If num is smaller than all elements, l ends up at 0, so num is inserted at the beginning.

# Otherwise, l points to the exact position where num fits.