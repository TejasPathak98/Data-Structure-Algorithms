class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        temp_sum = 0
        max_sum = float("-inf")

        for i,val in enumerate(nums):
            temp_sum += val
            if max_sum < temp_sum:
                max_sum = temp_sum
            if temp_sum < 0:
                temp_sum = 0
        
        return max_sum
        