class Solution:
    from functools import cache
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = collections.defaultdict(int)
        
        #@cache
        def dp(idx,state,trans):
            if idx >= len(prices):
                return 0 
            if trans >= 2:
                return 0 
            
            # buying
            if (idx,state,trans) not in memo:
                if not state:
                    memo[(idx,state,trans)] = max(dp(idx + 1,not state,trans) - prices[idx],dp(idx + 1,state,trans))
                else:
                    memo[(idx,state,trans)] = max(dp(idx + 1,not state,trans + 1) + prices[idx],dp(idx + 1,state,trans))
                
            return memo[(idx,state,trans)]
        
        return dp(0,False,0)




