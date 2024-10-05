class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        stack = []
        operator = "+"
        n = len(s)
        i = 0
        num = 0

        for i,char in enumerate(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            
            if not s[i].isdigit() or i == len(s) - 1:
                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    stack[-1] = stack[-1] * num
                elif operator == "/":
                    stack[-1] = int(stack[-1] / num)
            
                operator = char
                num = 0
        
        return sum(stack)

        