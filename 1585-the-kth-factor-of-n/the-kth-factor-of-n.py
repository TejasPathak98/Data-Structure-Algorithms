class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        # factors = []

        # for x in range(1,int(math.sqrt(n)) + 1):
        #     if n % x == 0:
        #         y = n // x
        #         factors.append(x)
        #         factors.append(y)

        # factors = list(set(factors))
        # factors.sort()
        
        # if k <= len(factors):
        #     return factors[k - 1]
        # else:
        #     return -1


        for i in range(1,int(math.sqrt(n)) + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        
        for i in range(int(math.sqrt(n)),0,-1):
            if i** 2  == n: continue
            if n % i == 0:
                k -= 1
                if k == 0:
                    return n // i

        return -1

