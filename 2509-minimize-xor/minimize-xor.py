class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        no_of_bits = 0
        temp = num2

        for _ in range(32):
            if (temp & 1) == 1:
                no_of_bits += 1
            temp = temp >> 1
        result = 0

        for i in range(31,-1,-1):
            if num1 & (1 << i) and no_of_bits > 0:
                result |= (1 << i)
                no_of_bits -= 1
        
        for i in range(32):
            if no_of_bits > 0 and not (result & (1 << i)):
                result |= (1 << i)
                no_of_bits -= 1

        
        return result



