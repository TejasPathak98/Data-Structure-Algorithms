class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        temp_sum = 0

        for i in range(len(nums)):
            temp_sum = temp_sum + nums[i]
            ans = max(ans,temp_sum)
            if temp_sum < 0:
                temp_sum = 0
        
        return ans

        