class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        phone_map = {
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

        def backtracking(index,temp):
            if index == len(digits):
                result.append("".join(temp[:]))
                return

            
            for ch in phone_map[digits[index]]:
                temp.append(ch)
                backtracking(index + 1, temp)
                temp.pop()

        
        backtracking(0,[])
        return result


