class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:return False
        target_sum = sum(nums) // 2

        dp = [False] * (target_sum + 1)
        dp[0] = True
        
        for num in nums:
            for j in range(target_sum,num - 1,- 1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target_sum]


        