class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
       
        ans = []

        phone_mapping = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        def backtracking(digits,combination):
            if len(digits) == 0:
                ans.append(combination)
                return
            else:
                for letter in phone_mapping[digits[0]]:
                    backtracking(digits[1:], combination + letter)
        
        backtracking(digits,"")
        return ans


        