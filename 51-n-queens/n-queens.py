class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(r):
            if r == n:
                copy = matrix[:]
                temp = []
                for c in copy:
                    temp.append("".join(c[:]))
                ans.append(temp)
                return
            
            for c in range(n):
                if c in cols or r + c in posDiag or r - c in negDiag:
                    continue
                
                matrix[r][c] = "Q"
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)

                matrix[r][c] = "."
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        matrix = [["."] * n for _ in range(n)]

        cols =  set()
        posDiag = set()
        negDiag = set()
        ans = []

        backtrack(0)
        return ans


