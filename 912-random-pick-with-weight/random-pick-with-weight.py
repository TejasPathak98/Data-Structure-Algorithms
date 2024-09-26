class Solution:

    def __init__(self, w: List[int]):
        self.prefix_arr = []
        total = 0

        for s in w:
            total += s 
            self.prefix_arr.append(total)
        self.tot = total 

        
    def pickIndex(self) -> int:
        
        r = random.randint(1,self.tot)

        return bisect.bisect_left(self.prefix_arr,r)




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()