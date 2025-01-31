class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        result = []

        def helper(pos,temp):
            if len(temp) == len(digits):
                result.append(temp)
                return
            for i in range(pos,len(digits)):
                for s in digit_map[digits[i]]:
                    helper(i + 1,temp + s)

        helper(0,"")
        return result


        