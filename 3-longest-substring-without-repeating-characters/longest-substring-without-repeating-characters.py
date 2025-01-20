class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = j = 0
        max_len = 0
        my_dict = {}

        while j < n:
            if s[j] not in my_dict:
                my_dict[s[j]] = j
                max_len = max(max_len, j - i + 1)
                j += 1
            else:
                pos = my_dict[s[j]]
                if i <= pos:
                    i = pos + 1
                my_dict[s[j]] = j
                max_len = max(max_len, j - i + 1)
                print(max_len,i,j)
                j += 1
        
        return max_len

