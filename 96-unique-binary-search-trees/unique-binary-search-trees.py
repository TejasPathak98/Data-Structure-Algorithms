class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        catalan = [0] * (n + 1)
        catalan[0],catalan[1] = 1,1

        for i in range(2,n + 1):
            for j in range(i):
                catalan[i] += catalan[j]*catalan[i - 1 -j]
        
        return catalan[n]