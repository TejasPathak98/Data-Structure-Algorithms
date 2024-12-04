class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = deque()
        self.avg = float('inf')
        
    def next(self, val: int) -> float:
        self.arr.append(val)
        if self.avg != float('inf'):
            if len(self.arr) <= self.size:
                self.avg = (self.avg *(len(self.arr) - 1) + self.arr[-1]) / len(self.arr)
            else:
                tot = self.avg * self.size - self.arr[-(self.size + 1)] + self.arr[-1]
                self.avg = tot / self.size
            return self.avg
        else:
            self.avg = sum(self.arr) / len(self.arr)
            return self.avg

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)