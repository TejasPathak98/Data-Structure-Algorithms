class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s[0]
        

        dp = [[False] * n for _ in range(n)]
        ans = [-1,-1]

        for length in range(n):
            for i in range(n - length):
                j = i + length

                if s[i] == s[j]:
                    if length == 0 or length == 1:
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True
                    
                    if dp[i][j]:
                        ans = [i,j]
        
        return s[ans[0]:ans[1] + 1]