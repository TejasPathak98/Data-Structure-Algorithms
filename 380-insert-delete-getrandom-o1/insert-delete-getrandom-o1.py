class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.map = {}

    def search(self,val) -> bool:
        return val in self.map

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        
        self.lst.append(val)
        self.map[val] = (len(self.lst) - 1)
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False

        idx = self.map[val]
        self.lst[idx] = self.lst[-1]
        self.map[self.lst[-1]] = idx
        self.lst.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()