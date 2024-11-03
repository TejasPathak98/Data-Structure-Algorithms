class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        i = 0

        while i < len(s):
            if s[i].isalpha():
                i += 1
                continue
            elif s[i] == "(":
                stack.append(i)
                i += 1
            else:
                if stack:
                    stack.pop()
                else:
                    s = s[:i] + s[i + 1:]
                    i -= 1
                i += 1

        print(stack)
        print(s)

        while stack:
            idx = stack.pop()
            s = s[:idx] + s[idx + 1:]
        
        return s