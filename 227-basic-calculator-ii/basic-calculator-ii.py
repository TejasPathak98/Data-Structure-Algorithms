class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        op = "+"
        stack = []
        num = 0

        for i , char in enumerate(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            
            if s[i] in ["+","-","*","/"] or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack[-1] = stack[-1] * num
                elif op == "/":
                    stack[-1] = int(stack[-1]/ num)
                
                num = 0
                op = s[i]

        return sum(stack)

        