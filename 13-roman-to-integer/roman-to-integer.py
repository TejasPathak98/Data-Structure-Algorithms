class Solution:
    def romanToInt(self, s: str) -> int:
        
        values = {

            "I" : 1,
            "IV" : 4,
            "V" : 5,
            "IX" : 9,
            "X" : 10,
            "XL" : 40,
            "L" : 50,
            "XC" : 90,
            "C" : 100,
            "CD" : 400,
            "D" : 500,
            "CM" : 900,
            "M" : 1000
        }

        number = 0
        n = len(s)
        j = n - 1

        while j >= 0:
            if j - 1 >=0 and s[j - 1:j + 1] in ("IX","IV","XL","XC","CD","CM"):
                number += values[s[j - 1:j + 1]]
                j -= 2
            else:
                number += values[s[j]]
                j -= 1

        
        return number


