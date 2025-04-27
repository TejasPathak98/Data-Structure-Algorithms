class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        wordDict = set(wordDict)

        def backtracking(index,temp):
            if index == len(s):
                result.append(" ".join(temp[:]))
                return
            
            for j in range(index,len(s)):
                if s[index:j + 1] in wordDict:
                    temp.append(s[index:j + 1])
                    backtracking(j + 1, temp)
                    temp.pop()

        backtracking(0,[])
        return result

