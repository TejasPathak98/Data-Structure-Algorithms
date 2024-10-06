class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        i = 0
        stack = []
        ans = 0

        while i < len(s):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    ans += 1
            i += 1

        return ans + len(stack)

            

        