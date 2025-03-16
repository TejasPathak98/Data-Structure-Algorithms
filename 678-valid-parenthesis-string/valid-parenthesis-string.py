class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star_stack = []
        count =0 

        i = 0

        while i < len(s):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    if star_stack:
                        count += 1
                        star_stack.pop()
                    else:
                        return False
            else:
                star_stack.append(i)
            i += 1
        
        if len(stack) == 0:
            return True
        else:
            if len(star_stack) >= len(stack):
                j = 0
                c = 0
                k = 0

                while star_stack and stack and k < len(star_stack) and j < len(stack):
                    if star_stack[k] > stack[j]:
                        j += 1
                        c += 1
                    k += 1
                
                if c == len(stack):
                    return True
                else:
                    return False
            else:
                return False
        