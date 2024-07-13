class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float("inf")
        n = len(nums)
        sum = 0

        for i in range(n):
            sum = sum + nums[i] 
            if max_sum < sum:
                max_sum = sum 
            if sum < 0:
                sum = 0 
        
        return max_sum

        