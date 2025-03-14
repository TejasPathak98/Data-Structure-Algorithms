class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        temp_sum = 0

        for num in nums:
            temp_sum += num
            ans = max(ans,temp_sum)
            if temp_sum < 0:
                temp_sum = 0
        
        return ans