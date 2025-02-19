class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = collections.defaultdict(int)

        #@cache
        def dp(idx,state,transactions):
            if idx >= len(prices):
                return 0
            if transactions >= 2:
                return 0
            
            if (idx,state,transactions) not in memo:
                if not state:
                    memo[(idx,state,transactions)] = max(dp(idx + 1 ,not state,transactions) - prices[idx],dp(idx + 1,state,transactions))
                else:
                    memo[(idx,state,transactions)] = max(dp(idx + 1 ,not state,transactions + 1) + prices[idx],dp(idx + 1,state,transactions))
            
            return memo[(idx,state,transactions)]
        
        return dp(0,False,0)