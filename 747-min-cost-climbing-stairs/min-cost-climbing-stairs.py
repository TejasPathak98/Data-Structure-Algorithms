class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # dp = [0] * (n + 1)
        # for i in range(2,n + 1):
        #     dp[i] = min(dp[i - 1] + cost[i - 1],dp[i - 2] + cost[i - 2])
        # return dp[n] 

        n = len(cost)

        @lru_cache
        def dp(i):
            if i <= 1:
                return 0
            
            return min(dp(i - 1) + cost[i - 1] , dp(i - 2) + cost[i - 2])
        
        return dp(n)


