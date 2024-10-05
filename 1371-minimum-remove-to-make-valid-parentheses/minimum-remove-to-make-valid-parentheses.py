class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        stack = []
        i = 0
        
        while i < len(s):
            orr = ord(s[i]) - ord('a')
            
            if 0 <= orr < 26:
                i += 1
                continue
            elif s[i] == "(":
                stack.append((s[i],i))
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s = s[:i] + s[i + 1:]
                    i -= 1
            i += 1
        
        for _, index in reversed(stack):
            s = s[:index] + s[index + 1:]


        return s

        