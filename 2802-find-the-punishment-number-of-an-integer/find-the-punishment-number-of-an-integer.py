class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0

        @cache(lru_cache)
        def helper(s,number_of_interest):
            n = len(s)

            for i in range(1,n):
                prefix = s[:i]
                suffix = s[i:]

                if int(prefix) + int(suffix) == number_of_interest:
                    return True
                elif helper(suffix,number_of_interest - int(prefix)):
                    return True
            
            return False

        for i in range(1,n + 1):
            x = i*i
            x_s = str(x)

            if helper(x_s,i):
                ans += x
        

        return ans + 1

        #O(N * L^2) ; O(L)       

