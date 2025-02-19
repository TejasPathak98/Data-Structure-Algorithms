class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n

        def dfs(pos):
            if dp[pos] != 0:
                return dp[pos]
            
            res = 1

            for i in range(1,d + 1):
                j = pos - i 
                if j < 0 or arr[j] >= arr[pos]:
                    break
                res = max(res,1 + dfs(j))

            for i in range(1,d + 1):
                j = pos + i 
                if j >= n  or arr[j] >= arr[pos]:
                    break
                res = max(res,1 + dfs(j))
            
            dp[pos] = res
            return dp[pos]

        
        ans = 0
        for i in range(n):
            ans = max(ans,dfs(i))
        
        return ans
            

        