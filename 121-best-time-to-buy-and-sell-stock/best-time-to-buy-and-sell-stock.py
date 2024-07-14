class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -float("inf")
        buy_price = float("inf") 
 
        for i in range(len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i] 
            max_profit = max(max_profit,prices[i] - buy_price)

        return max_profit
            
        