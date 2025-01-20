class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        c1 = Counter(s1)
        c2 = Counter(s2[:n1 - 1])
        j = 0 

        for i in range(n1 - 1,n2):
            c2[s2[i]] += 1
            if c1 == c2:
                return True
            
            c2[s2[j]] -= 1
            if c2[s2[j]] < 0:
                del c2[s2[j]]
            j += 1
        
        return False
        