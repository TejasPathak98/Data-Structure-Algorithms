class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        wordDict = set(wordDict)

        for j in range(1,n + 1):
            for i in range(j):

                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                    break
        
        return dp[n]