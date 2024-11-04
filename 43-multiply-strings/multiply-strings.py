class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        def decode(num):
            ans = 0
            for i in num:
                ans = ans*10 + (ord(i) - ord('0'))
            return ans
        
        def encode(num):
            x = ""
            while num:
                a = num % 10
                num = num // 10
                x = chr(ord('0') + a) + x
            return x
        
        return encode(decode(num1) * decode(num2))


        