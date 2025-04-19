class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1 #only 1 way to make 0 amount

        for coin in coins: # iterate over the number of coins and set the record straight about each coins contribution to each amount
            for j in range(coin,amount + 1): # iterate over the amounts for each coin
                dp[j] = dp[j] + dp[j - coin] #this is basically, the current dp[j](current no of ways) + (no of ways that we would get after taking into acc the coins contribution)

        return dp[amount]