class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(stack,sign,num):
            stack.append(num * sign)
        

        i = 0
        stack = []
        states = []
        sign = 1
        num = 0

        while i < len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] == "(":
                outer_sum = sum(stack)
                stack = []
                states.append((outer_sum,sign))
                sign = 1
                num = 0
            elif s[i] == ")":
                evaluate(stack, sign, num)
                inner_sum = sum(stack)
                outer_sum,outer_sign = states.pop()
                val = outer_sum + (outer_sign * inner_sum)
                stack = []
                stack.append(val)
                sign = 1
                num = 0
            elif s[i] == "+":
                evaluate(stack, sign, num)
                sign = 1
                num = 0
            elif s[i] == "-":
                evaluate(stack, sign, num)
                sign = -1
                num = 0
            
            i += 1
        
        evaluate(stack, sign, num)
        return sum(stack)