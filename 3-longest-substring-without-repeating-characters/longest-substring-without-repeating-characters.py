class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        max_length = 0

        n = len(s)
        if n == 0 or n == 1:
            return n

        l,r = 0,0 

        for r in range(n):
            if s[r] in mp and mp[s[r]] >= l:
                l = mp[s[r]] + 1 
            mp[s[r]] = r 
            max_length = max(max_length,r - l + 1) 
        return max_length

        