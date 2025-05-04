class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #Monotonic Increasing Stack
        stack = []

        for digit in num:
            while k and stack and digit < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(digit)

        
        while stack and k:
            stack.pop()
            k -= 1
        
        if not stack or all(x == "0" for x in stack):
            return "0"

        return "".join(stack).lstrip("0")


