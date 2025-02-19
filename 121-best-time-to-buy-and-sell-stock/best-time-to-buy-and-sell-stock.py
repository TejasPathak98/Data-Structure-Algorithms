class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float("inf")
        max_profit = float("-inf")

        for i in range(len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]
            if max_profit < prices[i] - buy_price:
                max_profit = prices[i] - buy_price
        
        return max_profit