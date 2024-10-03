class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def helper(l,r):
            nonlocal ans,max_count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if max_count < r - l + 1:
                    max_count = max(max_count,r - l + 1)
                    ans = s[l:r + 1]
                l -= 1
                r += 1

        ans = ""
        max_count = 0

        for i in range(0,len(s) - 1):
            helper(i,i)
            helper(i,i+1)
        
        return ans