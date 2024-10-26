class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        self.temp = 0
        for weight in w:
            self.temp += weight
            self.prefix.append(self.temp)
    
    def pickIndex(self) -> int:
        r = random.randint(1,self.temp)
        return bisect_left(self.prefix,r)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()