class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        i = 0
        stack = []
        
        while i < len(s):
            if s[i] == "(":
                stack.append((s[i],i))
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s = s[:i] + s[i + 1:]
                    i -= 1
            else:
                i += 1
                continue
            i += 1
        
        while stack:
            _ , index = stack.pop()
            s = s[:index] + s[index + 1:]
        
        return s




            
        