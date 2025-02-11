class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        

        max_val = float("inf")
        dp = [max_val] * (amount + 1)
        dp[0] = 0

        for i in range(1,amount + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    if dp[i - coins[j]] != max_val and 1 + dp[i - coins[j]] < dp[i]:
                        dp[i] = 1 + dp[i - coins[j]]

        if dp[amount] == max_val:return -1 
        else: return dp[amount]


