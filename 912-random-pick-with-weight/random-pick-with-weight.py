class Solution:

    def __init__(self, w: List[int]):
        self.prefix_arr = []
        temp = 0

        for weight in w:
            temp = temp + weight
            self.prefix_arr.append(temp)
        self.total = temp
        

    def pickIndex(self) -> int:

        r = random.randint(1,self.total)

        return bisect_left(self.prefix_arr, r)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()