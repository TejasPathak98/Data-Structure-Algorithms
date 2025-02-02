class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        result = []

        def helper(temp,left_bracket,right_bracket):
            if len(temp) == 2*n:
                result.append(temp)
                return
            if left_bracket < n:
                helper(temp + "(",left_bracket + 1,right_bracket)
            if right_bracket < left_bracket:
                helper(temp + ")",left_bracket,right_bracket + 1)
        
        helper("",0,0)
        return result
        