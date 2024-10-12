class Solution:
    def __init__(self, w: List[int]):
        self.prefix = [0] * len(w)
        self.w = w
        x = 0
        for i in range(len(w)):
            x = x + w[i]
            self.prefix[i] = x
        self.tot = x

    def pickIndex(self) -> int:
        r = random.randint(1,self.tot)
        return bisect_left(self.prefix, r)



        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()