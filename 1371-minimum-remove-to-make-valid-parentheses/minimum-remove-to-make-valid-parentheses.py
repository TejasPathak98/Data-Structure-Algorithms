class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid_indices = set()

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    invalid_indices.add(i)
        
        invalid_indices.update(stack)

        p = ""

        for i in range(len(s)):
            if i not in invalid_indices:
                p = p + s[i]
        
        return p
        