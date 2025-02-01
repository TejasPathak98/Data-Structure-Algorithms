class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:return 0

        if x > 0:
            y = int(str(x)[::-1])
        else:
            x = -1*x
            y = int(str(x)[::-1])
            y = -y
        
        if -2 ** 31 <= y <= 2**31 - 1:
            return y
        else:
            return 0

        