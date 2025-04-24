class AllOne:

    def __init__(self):
        self.map = {}
        self.max_heap = []
        self.min_heap = []
        
    def inc(self, key: str) -> None:
        if key not in self.map:
            self.map[key] = 1
        else:
            self.map[key] += 1
        heapq.heappush(self.max_heap,(-self.map[key],key))
        heapq.heappush(self.min_heap,(self.map[key],key))

    def dec(self, key: str) -> None:
        self.map[key] -= 1
        if self.map[key] == 0:
            del self.map[key]
            return
        
        heapq.heappush(self.max_heap,(-self.map[key],key))
        heapq.heappush(self.min_heap,(self.map[key],key))

    def getMaxKey(self) -> str:
        while self.max_heap:
            freq,key = heappop(self.max_heap)
            if key in self.map and self.map[key] == -freq:
                heappush(self.max_heap,(freq,key))
                return key
            else:
                continue

        return ""

    def getMinKey(self) -> str:
        while self.min_heap:
            freq,key = heappop(self.min_heap)
            if key in self.map and self.map[key] == freq:
                heappush(self.min_heap,(freq,key))
                return key
            else:
                continue

        return ""

    #This is all O(logN) amortized cost solution, using a DLL will get us the O(1) TC


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()