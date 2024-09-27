class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")

        current_num = 0
        my_stack = []
        operator = "+"

        for i,char in enumerate(s):
            if s[i].isdigit():
                current_num = 10*current_num + int(s[i])
            
            if not s[i].isdigit() or i == len(s) - 1:
                if operator == "+":
                    my_stack.append(current_num)
                elif operator == "-":
                    my_stack.append(-current_num)
                elif operator == "*":
                    my_stack[-1] = my_stack[-1] * current_num
                elif operator == "/":
                    print(my_stack[-1])
                    print(current_num)
                    my_stack[-1] = int(my_stack[-1] / current_num)
                    print(my_stack[-1])
                
                #print(my_stack)
                
                operator = char
                current_num = 0
        
        return sum(my_stack)

        