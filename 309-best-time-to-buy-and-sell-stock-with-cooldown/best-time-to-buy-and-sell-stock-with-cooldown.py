class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        sell = 0
        hold = float('-inf')
        cooldown = 0

        for current_price in prices:
            prev_hold = hold
            prev_cooldown = cooldown
            prev_sell = sell

            cooldown = max(prev_cooldown,prev_sell)
            
            sell = prev_hold + current_price

            hold = max(prev_hold,prev_cooldown - current_price)

        return max(cooldown,sell)