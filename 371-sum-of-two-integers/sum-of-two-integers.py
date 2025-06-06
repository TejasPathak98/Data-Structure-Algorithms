class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        maxInt = 2**31 - 1

        while b != 0:
            su = (a ^ b) & mask
            carry = (a & b) & mask
            a = su
            b = carry << 1

        return a if a <= maxInt else ~(a ^ mask) 