class Solution:
    def checkValidString(self, s: str) -> bool:
        bracket_stack = []
        star_stack = []

        i = 0

        while i < len(s):
            if s[i] == "(":
                bracket_stack.append(i)
            elif s[i] == ")":
                if bracket_stack:
                    bracket_stack.pop()
                else:
                    if star_stack:
                        star_stack.pop()
                    else:
                        return False
            else:
                star_stack.append(i)
            i += 1
        

        if not bracket_stack:
            return True
        else:
            while bracket_stack:
                idx = bracket_stack.pop()
                if star_stack:
                    if star_stack[-1] > idx:
                        star_stack.pop()
                    else:
                        return False
                else:
                    return False


        return True 
