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
        var = list(reversed(var))
        print(var)

        s = ""

        for x in var:
            if x >= 1000:
                f = x // 1000
                s = s + "M" * f
            elif 100 <= x < 1000:
                if x == 500:
                    s = s + "D"
                elif x == 900:
                    s = s + "CM"
                elif x == 400:
                    s = s + "CD"
                elif x < 400:
                    f = x // 100
                    s = s + "C" * f
                elif x > 500:
                    f = (x - 500) // 100
                    s = s + "D" + "C" * f
            elif 10 <= x < 100:
                if x == 50:
                    s = s + "L"
                elif x == 90:
                    s = s + "XC"
                elif x == 40:
                    s = s + "XL"
                elif x < 40:
                    f = x // 10
                    s = s + "X" * f
                elif x > 50:
                    f = (x - 50) // 10
                    s = s + "L" + "X" * f
            else:
                if x == 5:
                    s = s + "V"
                elif x == 4:
                    s = s + "IV"
                elif x == 9:
                    s = s + "IX"
                elif x < 4:
                    f = x
                    s = s + "I" * f
                elif x > 5:
                    f = (x - 5)
                    s = s + "V" + "I" * f
        
        return s
