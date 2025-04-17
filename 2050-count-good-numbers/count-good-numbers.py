class Solution:
    MOD = (10 ** 9 + 7)

    def countGoodNumbers(self, n: int) -> int:
        even_digits = 0
        odd_digits = 0

        if n == 1:
            even_digits = 1
        else:
            if n % 2 == 0:
                even_digits = odd_digits = n // 2
            else:
                even_digits = n // 2 + 1
                odd_digits = n // 2

        
        return (self.helper(5,even_digits) * self.helper(4,odd_digits)) % self.MOD

   
    def helper(self,x,n):
        
        result = 1
        base = x % self.MOD 
        
        while n > 0:
            if n % 2 == 1:
                result = (result * base) % self.MOD
            base = (base * base) % self.MOD
            n = n //2

        return result 




            



