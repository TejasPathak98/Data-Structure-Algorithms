class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        j = 0
        max_len = 1
        my_dict = defaultdict(int)

        while j < len(s):
            if s[j] not in my_dict:
                my_dict[s[j]] = j
                max_len = max(max_len,j - i + 1)
                j += 1
            else:
                if my_dict[s[j]] >= i:
                    i = my_dict[s[j]] + 1
                my_dict[s[j]] = j
                max_len = max(max_len,j - i + 1)
                j += 1

        return max_len


                
            




        