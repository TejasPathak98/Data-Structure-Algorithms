class Solution:
    def countLetters(self, s: str) -> int:
        res = 0
        same_count = 1

        for i,c in enumerate(s):
            if i > 0:
                if s[i - 1] == c:
                    same_count += 1
                else:
                    same_count = 1
            res += same_count
        
        return res


        