class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if x == 0:return 0
        if x == 1:return 1
        if n == 0:return 1
        if n == 1:return x
        if n == -1: return 1/x


        res = self.myPow(x, n // 2)

        return  res * res * (x if n % 2 == 1 else 1)
        