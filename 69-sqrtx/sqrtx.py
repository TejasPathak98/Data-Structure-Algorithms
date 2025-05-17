class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        first = 1
        last = x

        while first <= last:
            mid = (first + last) // 2

            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1

        
        return last