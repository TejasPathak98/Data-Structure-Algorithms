class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        Sum = sum(nums)
        diff = Sum - target
        if diff < 0 or diff % 2 == 1:return 0
        diff = diff // 2

        dp = [[0] * (diff + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1,n + 1):
            for s in range(diff + 1):
                dp[i][s] = dp[i - 1][s]

                if s >= nums[i - 1]:
                    dp[i][s] += dp[i - 1][s - nums[i - 1]]
                

        return dp[n][diff]