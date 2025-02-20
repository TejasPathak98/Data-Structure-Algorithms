class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        memo = {}
        
        @cache
        def dp(idx,state,transactions):
            if (idx,state,transactions) in memo:
                return memo[(idx,state,transactions)]
            
            if idx >= len(prices):
                return 0
            if transactions >= k:
                return 0
            
            if not state:
                memo[(idx,state,transactions)] = max(dp(idx + 1,not state,transactions) - prices[idx], dp(idx + 1,state,transactions))
            else:
                memo[(idx,state,transactions)] = max(dp(idx + 1,not state,transactions + 1) + prices[idx], dp(idx + 1,state,transactions))
            
            return memo[(idx,state,transactions)]
        
        return dp(0,False,0)

        #O(4 * N) ;  O(N)

        

