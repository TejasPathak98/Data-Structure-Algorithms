class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
        n = len(s)
        ans = 0

        i = 0
        while i < n:
            if s[i] == '(':
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
                else:
                    ans += 1
            i += 1
        
        return ans + len(stack)
        