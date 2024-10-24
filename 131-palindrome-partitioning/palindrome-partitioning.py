class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        def backtracking(start,path):
            if start == len(s):
                result.append(path)
                return
            for end in range(start + 1,len(s) + 1):
                if s[start:end] == s[start:end][::-1]:
                    backtracking(end, path + [s[start:end]])

        result = []
        backtracking(0,[])
        return result