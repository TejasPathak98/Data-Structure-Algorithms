class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        n = len(s)
        i = 0
        temp = ""
        neg = False
        sign_set = False

        while i < n:
            if s[i] == " ":
                if temp or sign_set:
                    break
                i += 1
                continue
            elif s[i] == '-':
                if temp or sign_set:
                    break
                else:
                    sign_set = True
                    neg = True
            elif s[i] == '+':
                if temp or sign_set:
                    break
                else:
                    sign_set = True
            elif s[i].isdigit():
                temp = temp + s[i]
            else:
                break
            print(i)
            i += 1
        
        if len(temp) == 0:
            return 0

        number = int(temp)
        if neg:
            number = -1 * number
        
        if number < 0:
            number = max(number,-1 * (2 ** 31))
        else:
            number = min(number,2 ** 31 - 1)

        return number

                    
            
            

        