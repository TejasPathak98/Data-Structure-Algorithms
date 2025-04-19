class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = 1

        if x == 0:
            return 0
        if x < 0:
            sign = -1
        x = x * sign
        
        result = 0

        while x:
            digit = x % 10
            x = x // 10

            #formula : result = result * 10 + digit
            #check for overflow

            if result > (INT_MAX - digit) // 10:
                return 0

            result = result * 10 + digit

        return result * sign 