class RandomizedSet:

    def __init__(self):
        self.my_dict = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.my_dict:
            return False
        else:
            self.values.append(val)
            self.my_dict[val] = len(self.values) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.my_dict:
            return False
        else:

            idx = self.my_dict[val]
            self.values[idx] = self.values[-1]
            self.my_dict[self.values[-1]] = idx
            self.values.pop()
            del self.my_dict[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()