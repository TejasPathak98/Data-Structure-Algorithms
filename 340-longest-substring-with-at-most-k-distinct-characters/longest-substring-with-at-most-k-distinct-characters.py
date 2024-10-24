class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i = 0
        j = 0
        my_dict = {}
        max_len = 0
        cnt = 0

        while j < len(s):
            if s[j] not in my_dict:
                my_dict[s[j]] = j
                cnt += 1
            else:
                my_dict[s[j]] = j
            
            if cnt > k:
                pos = min(my_dict.values())
                del my_dict[s[pos]]
                i = pos + 1
                cnt -= 1
            
            max_len = max(max_len,j - i + 1)
            j += 1

        
        return max_len
        