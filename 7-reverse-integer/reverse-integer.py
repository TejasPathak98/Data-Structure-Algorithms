class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        if x > 0:
            ans = int(str(x)[::-1])
        if x < 0:
            x = -x
            ans = int(str(x)[::-1])
            ans = -ans
        
        if -2**31 <= ans <= 2**31 - 1:
            return ans
        else:
            return 0
