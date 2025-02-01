class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        if len(s) == 1:
            return s[0]

        max_len = 0
        max_str = ""
        
        def helper(x,y):
            nonlocal max_str,max_len

            while x >= 0 and y < len(s) and s[x] == s[y]:
                if max_len < (y - x + 1):
                    max_str = s[x:y + 1]
                    max_len = max(max_len,y - x + 1)
                x -= 1
                y += 1
        
        for i in range(len(s) - 1):
            helper(i,i)
            helper(i,i + 1)
        
        return max_str
                

