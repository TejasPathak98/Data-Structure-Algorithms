class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s) 
        if not s:
            return 0
        if len(s) == 1:
            return 1

        count = 0 
        max_len = 0
        l = 0

        i = 0
        j = 1
        prev = -1

        while j < n:
            if s[j] == s[j - 1]:
                count += 1
                
                if count > 1:
                    i = prev 
                    j = i + 1
                    count = 0
                    continue
                elif count == 1:
                    prev = j
                    max_len = max(max_len,j - i + 1)
                    j += 1
                print("br1")
                print(max_len)
            else:
                max_len = max(max_len,j - i + 1)
                j += 1
                print("br2")
                print(max_len)
        
        return max_len

                    



        