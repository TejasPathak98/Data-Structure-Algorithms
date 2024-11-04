class Solution:
    def countSubstrings(self, s: str) -> int:
        max_ans = 0

        def helper(i,j):
            nonlocal max_ans
            while i >=0 and j < len(s) and s[i] == s[j]:
                max_ans += 1
                i -= 1
                j += 1

        i = 0
        while i < len(s) - 1:
            helper(i,i)
            helper(i,i + 1)
            i += 1

        return max_ans + 1

        