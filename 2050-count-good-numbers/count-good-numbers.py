class Solution:

    MOD = 10**9 + 7

    def countGoodNumbers(self, n: int) -> int:
        even_digits = (n + 1) // 2
        odd_digits = n // 2

        return (self.helper(5,even_digits) * self.helper(4,odd_digits)) % self.MOD
    
    def helper(self,base,n):

        base = base % self.MOD
        result = 1

        while n > 0:
            if n % 2 == 1:
                result = (result * base) % self. MOD
            base = (base * base) % self.MOD
            n = n // 2
        
        return result