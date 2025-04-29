class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        canBreak = [False] * (n + 1)
        canBreak[0] = True

        for end in range(1,n + 1):
            for start in range(end):
                if canBreak[start] and s[start:end] in wordSet:
                    canBreak[end] = True
                    break
        

        return canBreak[n]