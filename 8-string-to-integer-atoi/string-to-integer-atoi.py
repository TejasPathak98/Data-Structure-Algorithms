class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        i = 0
        while i < n and s[i] == " ":
            i += 1

        num = ""
        
        is_sign_set = False
        sign = 0
        
        while i < len(s):
            if s[i] == " ":
                print(i)
                break
            elif s[i].isdigit():
                num += s[i]
            elif s[i] == "+" and is_sign_set == False:
                if len(num) != 0:
                    break
                sign = 0
                is_sign_set = True
            elif s[i] == "-" and is_sign_set == False:
                if len(num) != 0:
                    break
                sign = 1
                is_sign_set = True
            elif s[i] == "+" or s[i] == "-" and is_sign_set == True:
                break
            elif s[i].isalpha():
                break
            else:
                break
            i += 1
        
        if len(num) == 0:
            return 0
        num = int(num)
        if sign == 0:
            return min(num,2**31 - 1)
        else:
            return -min((2**31),num)

        



        