class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        # dp = [[0] * (n + 1) for _ in range(m + 1)]

        # for i in range(m + 1):
        #     dp[i][0] = 1

        # for i in range(1,m + 1):
        #     for j in range(1,n + 1):
        #         dp[i][j] = dp[i - 1][j]

        #         if s[i - 1] == t[j - 1]:
        #             dp[i][j] += dp[i - 1][j - 1]
        
        # return dp[m][n]
        
        #O(MN) O(MN)
        

        prev = [0] * (n + 1)
        prev[0] = 1

        for i in range(1,m + 1):
            curr = [1] + [0] * n
            for j in range(1,n + 1):
                curr[j] = prev[j]

                if s[i - 1] == t[j - 1]:
                    curr[j] += prev[j - 1]
        
            prev = curr
        
        return prev[n]
