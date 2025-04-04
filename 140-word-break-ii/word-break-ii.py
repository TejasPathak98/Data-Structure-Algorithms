class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        result = []

        def backtracking(index,temp): #temp will have all the words which are space separated and present in the dict(and also part of the original s)
            if index == len(s):
                result.append(" ".join(temp.copy()))
                return
            
            for j in range(index,len(s)):
                if s[index:j + 1] in wordDict:
                    temp.append(s[index:j + 1])
                    backtracking(j + 1, temp)
                    temp.pop()

        backtracking(0, [])
        return result
