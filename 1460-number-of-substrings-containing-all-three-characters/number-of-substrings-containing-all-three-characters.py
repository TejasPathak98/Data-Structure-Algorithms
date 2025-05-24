class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        r = 0
        count = 0
        freq_dict = defaultdict(int)
        required = 3
        calc = 0

        def helper():
            if freq_dict['a'] >= 1 and freq_dict['b'] >= 1 and freq_dict['c'] >= 1:
                return True 

        while r < len(s):
            freq_dict[s[r]] += 1

            if helper():
                count += 1 + (len(s) - 1 - r)

                while l < r and helper():
                    freq_dict[s[l]] -= 1

                    if helper():
                        count += 1 + (len(s) - 1 - r)
                        l += 1
                    else:
                        l += 1
            
            r += 1
            
        
        return count





