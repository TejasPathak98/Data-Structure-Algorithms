class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        i = 0
        max_a = ""
        max_len = 0

        def helper(a,b):
            nonlocal max_len,max_a
            while a >= 0 and b < len(s) and s[a] == s[b]:
                if b - a + 1 > max_len:
                    print("br")
                    max_a = s[a:b + 1]
                    print(max_a)
                    max_len = b - a + 1
                a -= 1
                b += 1
            

        while i < n - 1:
            helper(i,i)
            helper(i,i +1)
            i += 1

        return max_a
        