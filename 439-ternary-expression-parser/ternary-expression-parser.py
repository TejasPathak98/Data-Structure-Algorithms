class Solution:
    def parseTernary(self, expression: str) -> str:
        n = len(expression)
        i = n - 1
        stack = []

        while i >= 0:
            if expression[i].isdigit() or expression[i] in ['T','F']:
                stack += [expression[i]]
                i -= 1
            elif expression[i] == ":":
                i -= 1
            elif expression[i] == "?":
                condition = expression[i - 1]
                first = stack.pop()
                second = stack.pop()
                if condition == "T":
                    stack += [first]
                else:
                    stack += [second]
                i -= 2
                
        return stack[0]


        