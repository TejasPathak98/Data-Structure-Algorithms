class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        n = len(s)

        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        #dp[i][j] means s[i:j + 1] is a palindrome
        for i in range(n - 1,-1,-1):
            dp[i][i] = True

            for j in range(i + 1,n):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    l = j - i + 1
                    dp[i][j] = True
                    if l > max_len:
                        max_len = l
                        start = i

        return s[start:start + max_len]
