class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        duplicate_check_dict = {}

        while r < len(s):
            if (s[r] not in duplicate_check_dict) or (duplicate_check_dict[s[r]] < l):
                duplicate_check_dict[s[r]] = r
                max_len = max(max_len,r - l + 1)
                r += 1
            else:
                pos = duplicate_check_dict[s[r]]
                duplicate_check_dict[s[r]] = r
                l = pos + 1
                r += 1

        return max_len

        #O(N) ; O(N)

