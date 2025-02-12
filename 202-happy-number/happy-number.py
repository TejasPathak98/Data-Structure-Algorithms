class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(x):
            sq_sum = 0
            
            while x:
                sq_sum += (x% 10) * (x % 10)
                x = x // 10
            
            return sq_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = helper(n)
            
        
        return n == 1

        