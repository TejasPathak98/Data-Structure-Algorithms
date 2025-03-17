class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if x == 0:return 0
        if x == 1:return 1
        if n == 0:return 1
        if n == 1:return x
        if n == -1:return (1/x)

        half = x ** (n // 2)

        return half * half * (1 if n % 2 == 0 else x)