class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        #First count the smaller factors from (1 to Sqrt of N) 

        for i in range(1,int(math.sqrt(n)) + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        

        #we count for larger factors from (srqt N to N):

        for i in range(int(math.sqrt(n)),0,-1):
            if i * i == n: continue # we count that in the first loop
            if n % i == 0:
                k -= 1
                if k == 0:
                    return n // i


        return -1 