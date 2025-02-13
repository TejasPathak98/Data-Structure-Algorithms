class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":return "0"

        temp_num = []
        for ch in num1:
            digit = ord(ch) - ord("0")
            temp_num.append(digit)
        
        x = 0
        for i in range(len(temp_num)):
            x += temp_num[i] * (10 ** (len(temp_num) - 1 - i))
        
        temp = []
        for ch in num2:
            digit = ord(ch) - ord("0")
            temp.append(digit)
        
        y = 0
        for i in range(len(temp)):
            y += temp[i] * (10 ** (len(temp) - 1 - i))
        
        z = x*y
        result = []

        while z:
            result.append(chr(ord('0') + z  % 10))
            z = z // 10

        
        
        return "".join(result[::-1])


        