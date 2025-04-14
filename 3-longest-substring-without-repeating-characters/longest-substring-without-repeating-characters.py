class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        char_dict = defaultdict(int)
        max_len = 0

        while r < len(s):
            if s[r] not in char_dict:
                char_dict[s[r]] = r
                max_len = max(max_len,r - l + 1)
                r += 1
            else:
                if char_dict[s[r]] >= l:
                    prev_pos = char_dict[s[r]]
                    char_dict[s[r]] = r
                    l = prev_pos + 1
                    max_len = max(max_len,r - l + 1)
                    r += 1
                else:
                    char_dict[s[r]] = r
                    max_len = max(max_len,r - l + 1)
                    r += 1
        
        return max_len

                    
