class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:return 0

        sell = 0
        cool_down = 0
        hold = float("-inf")

        for stock_price_of_the_day in prices:
            prev_sell = sell
            prev_cool_down = cool_down
            prev_hold = hold

            cool_down = max(prev_cool_down,prev_sell)

            sell = prev_hold + stock_price_of_the_day

            hold = max(prev_hold,prev_cool_down - stock_price_of_the_day)
        
        return max(sell,cool_down)
        