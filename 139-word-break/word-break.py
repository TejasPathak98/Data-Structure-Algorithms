class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        n = len(s)

        for j in range(1,n + 1):
            for i in range(j):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                    break
        
        return dp[n]