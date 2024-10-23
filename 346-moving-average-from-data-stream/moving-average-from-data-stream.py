class MovingAverage:

    def __init__(self, size: int):
        self.window_size = size
        self.queue = deque()
        
    def next(self, val: int) -> float:
        if len(self.queue) < self.window_size:
            self.queue.append(val)
            return sum(self.queue) / len(self.queue)
        else:
            self.queue.popleft()
            self.queue.append(val)
            return sum(self.queue) / len(self.queue)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)