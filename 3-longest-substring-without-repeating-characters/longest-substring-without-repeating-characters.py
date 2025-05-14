class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        if s == "":
            return 0

        max_len = float('-inf')
        pos_dict = {}

        while r < len(s):
            if s[r] not in pos_dict or pos_dict[s[r]] < l:
                pos_dict[s[r]] = r
                max_len = max(max_len,(r - l + 1))
                r += 1
            else:
                earlier_pos = pos_dict[s[r]]
                l = earlier_pos + 1
                pos_dict[s[r]] = r
                max_len = max(max_len,(r - l + 1))
                r += 1

        
        return max_len



