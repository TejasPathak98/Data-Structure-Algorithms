class Solution:
    def numberToWords(self, num: int) -> str:
        below_Twenty = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen",
        "Nineteen"]

        Tens = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

        Thousands = ["","Thousand","Million","Billion"]

        if num == 0:
            return "Zero"
        

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_Twenty[n] + " "
            elif n < 100:
                return Tens[n // 10] + " " + helper(n % 10)
            else:
                return below_Twenty[n // 100] + " Hundred " + helper(n % 100)

        i = 0
        res = ""

        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + Thousands[i] + " "  + res
            num = num // 1000
            i += 1

        
        return res.strip()