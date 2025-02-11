class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        
        ans = 0

        dp = [[False] * n for _ in range(n)]

        for length in range(n):
            for i in range(n - length):
                j = i + length

                if s[i] == s[j]:
                    if length == 0 or length == 1:
                        dp[i][j] = 1
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = 1
                    
                    if dp[i][j]:
                        ans += 1
        
        return ans