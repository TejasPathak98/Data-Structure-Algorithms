class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"


        Below_Twenty = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen",
        "Nineteen"]

        Tens = ["","","Twenty" ,"Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

        Thousands = ["","Thousand","Million","Billion"]


        def helper(number):
            if number == 0:
                return ""
            if number < 20:
                return Below_Twenty[number] + " "
            elif number < 100:
                return Tens[number // 10] + " " + helper(number % 10)
            else:
                return Below_Twenty[number // 100] + " Hundred " + helper(number % 100)

        ans = ""
        i = 0

        while num > 0:
            if num % 1000 != 0:
                ans = helper(num % 1000) + Thousands[i] + " " + ans
            num = num // 1000
            i += 1

        
        return ans.strip()