class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        while len(nums) > 1:

            n = len(nums)
            new_nums = [0] * (n - 1)

            for i in range(0,n - 1):
                new_nums[i] = (nums[i] + nums[i + 1]) % 10
            
            nums = new_nums

        return nums[0]

