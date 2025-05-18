class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0
        my_dict = defaultdict(int)
        max_len = 0

        while r < len(s):
            my_dict[s[r]] += 1

            while (r - l + 1) - max(my_dict.values()) > k:
                my_dict[s[l]] -= 1
                l += 1

            max_len = max(max_len,r - l + 1)
            r += 1

        
        return max_len


