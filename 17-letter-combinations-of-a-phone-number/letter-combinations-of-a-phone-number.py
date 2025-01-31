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

        def helper(pos,temp_string):
            if len(temp_string) == len(digits):
                result.append(temp_string)
                return
            for i in range(pos,len(digits)):
                for ch in digit_map[digits[i]]:
                    helper(i + 1,temp_string + ch)

        helper(0,"")
        return result


        