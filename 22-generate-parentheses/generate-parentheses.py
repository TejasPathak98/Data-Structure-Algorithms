class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def bt(s = '',left = 0,right = 0):
            if len(s) == 2 * n:
                result.append(s)
                return
            
            if left < n:
                bt(s + '(',left + 1,right)
            if right < left:
                bt(s + ')',left,right + 1)
        
        result = []
        bt()
        return result