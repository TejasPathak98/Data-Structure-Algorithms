class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        if n1 == s2:
            if Counter(n1) == Counter(n2):
                return True
            else:
                return False

        counter1 = Counter(s1)

        l = 0
        r = 0

        temp_dict = defaultdict(int)

        while r < len(s2):
            temp_dict[s2[r]] += 1

            if temp_dict == counter1:
                return True

            if s2[r] not in counter1:
                r += 1
                l = r
                temp_dict.clear()
                continue
            
            if temp_dict[s2[r]] == counter1[s2[r]] + 1:

                while l < r and temp_dict[s2[r]] != counter1[s2[r]]:
                    temp_dict[s2[l]] -= 1
                    l += 1
            
            r += 1
        
        return False



