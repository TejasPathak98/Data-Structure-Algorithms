class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if x == 1:return 1
        if x == 0:return 0
        if n == 1:return x
        if n == 0:return 1
        if n == -1:return 1 / x 

        half = self.myPow(x, n // 2)

        return half * half * self.myPow(x, n % 2)


        