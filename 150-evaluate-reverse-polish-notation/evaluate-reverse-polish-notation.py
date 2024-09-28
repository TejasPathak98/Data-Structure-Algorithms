class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        i = 0
        

        while i < n:
            if tokens[i] not in ('+','-','*','/'):
                stack.append(int(tokens[i]))
            else:
                result = 0
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == '+':
                    result = b + a
                elif tokens[i] == '-':
                    result = b - a
                elif tokens[i] == '*':
                    result = b * a
                else:
                    result = int(b / a)
                
                if i == len(tokens) - 1:
                    return result
                else:
                    stack.append(result)
                
            i += 1

        return stack[-1]
