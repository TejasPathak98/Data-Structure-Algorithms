class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(stack,number,sign):
            stack.append(number * sign)
        
        stack = []
        state = []
        number = 0
        sign = 1
        i = 0

        while i < len(s):
            if s[i].isdigit():
                number = number * 10 + int(s[i])
            else:
                if s[i] == "(":
                    evaluate(stack, number, sign)
                    outer_sum = sum(stack)
                    stack = []
                    state.append((outer_sum,sign))
                    number = 0
                    sign = 1
                elif s[i] == ")":
                    evaluate(stack, number, sign)
                    inner_sum = sum(stack)
                    stack = []
                    outer_sum,outer_sign = state.pop()
                    stack.append(inner_sum*outer_sign + outer_sum)
                    number = 0
                    sign = 1
                elif s[i] == "+":
                    evaluate(stack, number, sign)
                    sign = 1
                    number = 0
                elif s[i] == "-":
                    evaluate(stack, number, sign)
                    sign = -1
                    number = 0
            i += 1
        
        evaluate(stack, number, sign)
        return sum(stack)

                    


        