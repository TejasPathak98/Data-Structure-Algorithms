class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(self.nums)
        

    def pick(self, target: int) -> int:
        df = []
        for i in range(self.n):
            if self.nums[i] == target:
                df.append(i)
        return random.choice(df)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)