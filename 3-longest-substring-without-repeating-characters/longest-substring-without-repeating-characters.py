class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        i = j = 0
        max_len = 0
        pos_dict = {}

        while j < len(s):
            if s[j] not in pos_dict:
                pos_dict[s[j]] = j
                max_len = max(max_len,j - i + 1)
                j += 1
            else:
                old_pos = pos_dict[s[j]]
                if old_pos >= i:
                    i = old_pos + 1
                    max_len = max(max_len,j - i + 1)
                    pos_dict[s[j]] = j
                else:
                    max_len = max(max_len,j - i + 1)
                    pos_dict[s[j]] = j
                j += 1
        
        return max_len

        # O(N) ; O(N)


        