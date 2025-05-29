class Solution:
    def smallestNumber(self, pattern: str) -> str:
        #stack problem, recognize it by the increasing/decreasing pattern

        n = len(pattern)
        stack = []
        result = ""

        for i in range(n + 1):
            stack.append(i + 1)

            if i == n or pattern[i] == "I":
                while stack:
                    result += str(stack.pop())

        return result 