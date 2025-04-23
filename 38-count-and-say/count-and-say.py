class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
        
        x = "1"

        for _ in range(n - 1):
            x = self.helper(x)
        
        return x


    def helper(self,s):

        res = ""
        i = 0

        while i < len(s):

            count  = 1
            while i < len(s) - 1 and s[i] == s[i + 1]:
                count += 1
                i += 1
            
            res += str(count) + s[i]
            i += 1

        return res
