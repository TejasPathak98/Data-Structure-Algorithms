class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        ans = []

        while i < len(encoded1) and j < len(encoded2):
            val1,freq1 = encoded1[i]
            val2,freq2 = encoded2[j]

            product = val1*val2
            freq = min(freq1,freq2)

            if ans and ans[-1][0] == product:
                ans[-1][1] += freq
            else:
                ans.append([product,freq])
            
            encoded1[i][1] -= freq
            encoded2[j][1] -= freq

            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
            
        return ans

        