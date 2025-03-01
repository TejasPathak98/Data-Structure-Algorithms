class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l= 0
        r = 0
        s1_dict = Counter(s1)

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if Counter(s2[l:r + 1]) == s1_dict:
                return True
            else:
                r += 1
                l += 1

        return False 