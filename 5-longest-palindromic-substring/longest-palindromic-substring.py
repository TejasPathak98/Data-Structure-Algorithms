class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        max_ans = ""
        max_len = 0

        def helper(i,j):
            nonlocal max_ans,max_len
            while i>= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_ans = s[i:j + 1]
                i -= 1
                j += 1

        i = 0
        while i < len(s) - 1:
            helper(i,i)
            helper(i,i + 1)
            i += 1
        
        return max_ans

        

        