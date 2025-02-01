class Solution:
    def intToRoman(self, num: int) -> str:
        temp = num
        var = []

        while temp:
            x = temp % 10
            temp = temp // 10
            var.append(x)
        
        for i in range(len(var)):
            var[i] = var[i] * (10 ** i)
        
        var = var[::-1]
        result = ""
        print(var)

        for i in range(len(var)):
            x = var[i]
            print(len(var))
            print(var[i])
            if x >= 1000:
                result = result + "M" * (x // 1000)
            elif 100 <= x < 1000:
                if x == 500:
                    result = result + "D"
                elif x == 400:
                    result += "CD"
                elif x == 900:
                    result += "CM"
                elif x < 400:
                    result += (x // 100) * "C"
                elif x > 500:
                    result += "D" + ((x - 500) // 100) * "C"
            elif 10 <= x < 100:
                if x == 50:
                    result = result + "L"
                elif x == 40:
                    result += "XL"
                elif x == 90:
                    result += "XC"
                elif x < 40:
                    result += (x // 10) * "X"
                elif x > 50:
                    result += "L" + ((x - 50) // 10) * "X"
            elif 1 <= x < 10:
                if x == 5:
                    result = result + "V"
                elif x == 4:
                    result += "IV"
                elif x == 9:
                    result += "IX"
                elif x < 4:
                    result += (x) * "I"
                elif x > 5:
                    result += "V" + (x - 5) * "I"
            

        return result

        