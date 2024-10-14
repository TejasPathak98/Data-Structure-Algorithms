class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.dic = defaultdict(list)
        for i in range(self.n):
            self.dic[nums[i]].append(i)
        

    def pick(self, target: int) -> int:
        return random.choice(self.dic[target])

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)