class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            if prices[i] > buy_price:
                max_profit += (prices[i] - buy_price)
                buy_price = prices[i]
        
        return max_profit


