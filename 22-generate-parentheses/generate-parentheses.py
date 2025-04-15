class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []

        def backtracking(temp,opening,closing):
            if len(temp) == 2 * n:
                ans.append("".join(temp[:]))
                return

            if len(temp) > 2*n:
                return
            
            if opening < n:
                temp.append("(")
                backtracking(temp, opening + 1, closing)
                temp.pop()
            if closing < opening:
                temp.append(")")
                backtracking(temp, opening, closing + 1)
                temp.pop()


        backtracking([], 0, 0)
        return ans

