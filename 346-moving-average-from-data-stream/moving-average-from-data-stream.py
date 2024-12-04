class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = []
        
    def next(self, val: int) -> float:
        self.arr.append(val)
        if len(self.arr) <= self.size:
            return sum(self.arr) / len(self.arr)
        else:
            return sum(self.arr[-self.size:]) / self.size

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)