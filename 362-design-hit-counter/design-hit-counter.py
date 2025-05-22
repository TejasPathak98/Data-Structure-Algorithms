class HitCounter:

    def __init__(self):
        self.window_size = 300
        self.times = [0] * self.window_size
        self.hits = [0] * self.window_size

        #its basically a ring buffer with 300 slots, in each of the slots, a timestamp and corresponding hit count is stored

    def hit(self, timestamp: int) -> None:
        index = timestamp % self.window_size

        if self.times[index] != timestamp: #older timestamp stored currently
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

    def getHits(self, timestamp: int) -> int:
        total_hits = 0

        for i in range(self.window_size):
            if timestamp - self.times[i] < 300:
                total_hits += self.hits[i]

        return total_hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)