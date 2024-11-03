class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        i = 0
        ans = 0

        while i < len(s):
            if s[i] == "(":
                stack.append(i)
                i += 1
            else:
                if stack:
                    stack.pop()
                else:
                    ans += 1
                i += 1
        
        return ans + len(stack)


