class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #Monotonic Increasing stack

        stack = []

        for i in num:
            while stack and k > 0 and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        while stack and k:
            stack.pop()
            k -= 1
        
        result = "".join(stack).lstrip("0")

        return result if result else "0"

