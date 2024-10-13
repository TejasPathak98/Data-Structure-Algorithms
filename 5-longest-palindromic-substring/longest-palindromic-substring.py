class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        max_s = ""
        max_l = 0

        def helper(i,j):
            nonlocal max_l,max_s
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    if j - i + 1 > max_l:
                        max_s = s[i:j + 1]
                        max_l = j - i + 1
                    i -= 1
                    j += 1
                else:
                    break
        
        for i in range(0,len(s) - 1):
            helper(i,i)
            helper(i,i+1)

        return max_s

        

        