class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # l= 0
        # r = 0
        # s1_dict = Counter(s1)
        # sliding_window_dict = Counter(s2[:len(s1)])

        # l = 0
        # r = len(s1) - 1

        # while r < len(s2):
        #     if sliding_window_dict == s1_dict:
        #         return True
        #     else:
        #         sliding_window_dict[s2[l]] -= 1
        #         l += 1
        #         r += 1
        #         if r < len(s2):sliding_window_dict[s2[r]] += 1
        # return False

        # #O(l2* l1) becasue of dict comparison ; O(l1)

        if len(s1) > len(s2):return False

        l = 0
        s1_dict = Counter(s1)
        sliding_window_dict = Counter(s2[:len(s1)])
        match_count = sum((s1_dict[c] == sliding_window_dict[c] for c in s1_dict))

        for r in range(len(s1),len(s2)):
            if match_count == len(s1_dict):
                return True
            
            if s2[l] in s1_dict:
                if s1_dict[s2[l]] == sliding_window_dict[s2[l]]:
                    match_count -= 1
                sliding_window_dict[s2[l]] -= 1
                if s1_dict[s2[l]] == sliding_window_dict[s2[l]]:
                    match_count += 1 

            if s2[r] in s1_dict:
                if s1_dict[s2[r]] == sliding_window_dict[s2[r]]:
                    match_count -= 1
                sliding_window_dict[s2[r]] += 1
                if s1_dict[s2[r]] == sliding_window_dict[s2[r]]:
                    match_count += 1


            l += 1

        return len(s1_dict) == match_count 

        