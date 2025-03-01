class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l= 0
        r = 0
        s1_dict = Counter(s1)
        sliding_window_dict = Counter(s2[:len(s1)])

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if sliding_window_dict == s1_dict:
                return True
            else:
                sliding_window_dict[s2[l]] -= 1
                l += 1
                r += 1
                if r < len(s2):sliding_window_dict[s2[r]] += 1
        return False

        #O(l1 + l2) ; O() 