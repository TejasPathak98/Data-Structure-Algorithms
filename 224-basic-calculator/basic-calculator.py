class Solution:
    def calculate(self, s: str) -> int:
        def evluate(stack,sign,num):
            stack.append(sign* num)
        
        #global trackers

        i = 0
        num = 0
        sign = 1
        stack = []
        state = []

        while i < len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] == "(":
                outer_sum = sum(stack)
                stack = []
                state.append((outer_sum,sign))
                sign = 1
                num = 0
            elif s[i] == ")":
                evluate(stack, sign, num)
                inner_sum = sum(stack)
                stack = []
                outer_sum,outer_sign = state.pop()
                total_sum = outer_sum + (outer_sign * inner_sum)
                stack.append(total_sum)
                sign = 1
                num = 0
            elif s[i] == "+":
                evluate(stack, sign, num)
                num = 0
                sign = 1
            elif s[i] == "-":
                evluate(stack, sign, num)
                num = 0
                sign = -1

            i += 1

        evluate(stack, sign, num)
        return sum(stack)
