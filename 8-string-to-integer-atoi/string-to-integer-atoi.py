class Solution:
    def myAtoi(self, s: str) -> int:
        sign = True
        sign_set = False
        s = s.lstrip()

        i = 0
        ans = ""
        while i < len(s):
            if s[i].isalpha():
                break
            elif s[i].isnumeric():
                ans += s[i]
                i += 1
            elif s[i] == "-":
                if len(ans) > 0 or sign_set:
                    break
                else:
                    sign = False
                    sign_set = True
                    i += 1
            elif s[i] == "+":
                if len(ans) > 0 or sign_set:
                    break
                else:
                    sign_set = True
                    i += 1
            else:
                break
        
        if len(ans) > 0:
            if sign:
                return min(int(ans),(2 ** 31) - 1)
            else:
                return max(-int(ans), -(2**31))
        else:
            return 0
        
            

        
        