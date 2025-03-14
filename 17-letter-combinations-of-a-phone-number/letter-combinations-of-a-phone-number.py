class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        char_dict  = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        }


        ans = []

        def helper(temp,next_digit):
            if len(temp) == len(digits):
                ans.append("".join(temp[:]))
                return

            if next_digit >= len(digits):
                return
            
            for ch in char_dict[digits[next_digit]]:
                temp.append(ch)
                helper(temp,next_digit + 1)
                temp.pop()

        helper([],0)
        return ans