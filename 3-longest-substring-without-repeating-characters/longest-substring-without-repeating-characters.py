class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        max_len = 0
        char_dict = {}

        while r < len(s):
            if s[r] not in char_dict:
                char_dict[s[r]] = r
                max_len = max(max_len,r - l + 1)
                r += 1
            else:
                if char_dict[s[r]] >= l:
                    prev_pos = char_dict[s[r]]
                    l = prev_pos + 1
                    char_dict[s[r]] = r
                    r += 1
                else:
                    char_dict[s[r]] = r
                    max_len = max(max_len,r - l + 1)
                    r += 1

        
        return max_len
