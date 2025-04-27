class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        counter1 = Counter(s1)
        counter2 = Counter()

        for i in range(n2):

            counter2[s2[i]] += 1

            if i >= n1:
                counter2[s2[i - n1]] -= 1

                if counter2[s2[i - n1]] == 0:
                    del counter2[s2[i - n1]]
                
            
            if counter1 == counter2:
                return True
    

        return False