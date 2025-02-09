class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []


        for i,ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(i)
        
        while stack and star:
            if stack[-1] > star[-1]:
                return False
            
            stack.pop()
            star.pop()
        
        return len(stack) == 0


        