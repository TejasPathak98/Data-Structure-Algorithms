class FirstUnique:

    def __init__(self, nums: List[int]):
        self.count = Counter()
        self.queue = deque()
        for num in nums:
            self.add(num)
        
    def showFirstUnique(self) -> int:
        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.popleft()
        return self.queue[0] if self.queue else -1
        
    def add(self, value: int) -> None:
        if value not in self.count:
            self.queue.append(value)
        self.count[value] += 1
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)