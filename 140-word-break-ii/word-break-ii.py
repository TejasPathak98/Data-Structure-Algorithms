class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        result = []

        def backtracking(temp,index):
            if index == len(s):
                result.append(" ".join(temp))
                return
            
            for j in range(index,len(s)):
                if s[index:j + 1] in wordDict:
                    temp.append(s[index:j + 1])
                    backtracking(temp, j + 1)
                    temp.pop()


        backtracking([],0)
        return result