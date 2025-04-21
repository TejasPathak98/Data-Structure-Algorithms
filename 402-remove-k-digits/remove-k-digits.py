class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []

        for digit in num:
            while k and stack and digit < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k and stack:
            stack.pop()
            k -= 1

        print(stack)

        if not stack or all(x == '0' for x in stack):
            print("br")
            return "0"
        
        return "".join(stack).lstrip("0")