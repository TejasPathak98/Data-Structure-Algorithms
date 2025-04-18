class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        factors = []

        for x in range(1,int(math.sqrt(n)) + 1):
            if n % x == 0:
                y = n // x
                factors.append(x)
                factors.append(y)

        factors = list(set(factors))
        print(factors)
        factors.sort()
        
        if k <= len(factors):
            return factors[k - 1]
        else:
            return -1

