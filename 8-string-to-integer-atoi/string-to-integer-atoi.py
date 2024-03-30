class Solution:
    def myAtoi(self, s: str) -> int:
        value = 0 
        sign = 1
        state = 0
        pos = 0

        if len(s) == 0:
            return 0 
        
        while pos < len(s):
            ch = s[pos] 

            if state == 0:
                if ch == " ":
                    pass 
                elif ch == "+" or ch == "-":
                    state = 1 
                    sign = 1 if ch == "+" else -1 
                elif ch.isdigit():
                    state = 2 
                    value = 10*value + int(ch) 
                else:
                    return 0 
           
            elif state == 1:
                if ch.isdigit():
                    state = 2 
                    value = 10*value + int(ch)
                else:
                    return 0 

            elif state == 2:
                if ch.isdigit():
                    state = 2 
                    value = 10*value + int(ch)
                else:
                    break  
            else:
                return 0
            
            pos += 1

        value = sign * value
        value = min(value,2**31 - 1)
        value = max(value,-1 * (2**31)) 

        return value   
