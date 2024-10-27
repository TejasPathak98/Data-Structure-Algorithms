class Solution:
    def calculate(self, s: str) -> int:
        while " " in s:
            s = s.replace(" ","")
        
        stack = []
        op = "+"
        i = 0
        number = 0
        operators = ["+","-","/","*"]

        while i < len(s):
            if s[i].isdigit():
                number = number*10 + int(s[i])
            if s[i] in operators or i == len(s) - 1:
                if op == "+":
                    stack.append(number)
                elif op == "-":
                    stack.append(-number)
                elif op == "*":
                    stack[-1] = stack[-1] * number
                elif op == "/":
                    stack[-1] = int(stack[-1]/ number)
                op = s[i]
                number = 0
            i += 1

        
        return sum(stack)


                

        