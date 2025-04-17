class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1


        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1,amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i],  1 + dp[i - coin])

        
        return -1 if dp[amount] == float('inf') else dp[amount]

