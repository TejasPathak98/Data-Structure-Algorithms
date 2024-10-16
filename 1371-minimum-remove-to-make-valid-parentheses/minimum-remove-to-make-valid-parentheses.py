class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        i = 0
        while i < len(s):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s = s[:i] + s[i + 1:]
                    i -= 1
            i += 1
        
        while stack:
            pos = stack.pop()
            s = s[:pos] + s[pos + 1:]
        
        return s

        