class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        s = set()

        def helper(x):
            if x == 1:
                return True
            if x in s:
                return False
            
            s.add(x)

            the_sum = 0

            while x > 0:
                the_sum += (x % 10) * (x % 10)
                x = x // 10
            
            return helper(the_sum)


        return helper(n)
