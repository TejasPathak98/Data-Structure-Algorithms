class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        phone_map = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        result = []

        def helper(combination,next_digits):
            if len(next_digits) == 0:
                result.append(combination)
                return
            for ch in phone_map[next_digits[0]]:
                helper(combination + ch,next_digits[1:])
        
        helper("",digits)
        return result