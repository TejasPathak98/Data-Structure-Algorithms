class Solution:
    def maxCoins(self, lane1: List[int], lane2: List[int]) -> int:
        lanes = [lane1,lane2]
        n = len(lane1)

        @lru_cache(None)
        def dfs(lane,switch,index):
            if index == n:
                return 0

            current = lanes[lane%2][index]
            stay = dfs(lane,switch,index + 1)
            switched = 0
            if switch < 2:
                switched = dfs(lane + 1,switch + 1,index + 1)
            
            return current + max(0,stay,switched)


        res = -inf
        for i in range(n):
            x1 = dfs(0,0,i)
            x2 = dfs(1,1,i)
            res = max(res,x1,x2)

        return res
