class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        all_zero = all(x == "0" for x in locked)

        if all_zero:
            return True

        def validate(s,locked,op):

            bal = 0
            wild = 0
            for i in range(len(s)):
                if locked[i] == "1":
                    if s[i] == op:
                        bal += 1
                    else:
                        bal -= 1
                else:
                    wild += 1
                
                if wild + bal < 0:
                    return False
            
            return bal <= wild

        
        x = validate(s, locked, "(") #L-R - avoids oprhaned ')' at the end
        y = validate(s[::-1], locked[::-1], ")") # R - L avoids oprhaned '(' at the end

        return x and y
        
