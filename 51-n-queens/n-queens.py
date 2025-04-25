class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag = set()
        anti_diag = set()
        queens = [-1] * n
        result = [] 

        def backtrack(row):

            if row == n:
                board = []
                for r in queens:
                    s = r * "." + "Q" + "." * (n - r - 1)
                    board.append(s)
                result.append(board)
                return
            
            for c in range(n):
                if c in col or (row + c) in diag or (row - c) in anti_diag:
                    continue
            
                queens[row] = c
                col.add(c)
                diag.add(row + c)
                anti_diag.add(row - c)

                backtrack(row + 1)

                queens[row] = -1
                col.remove(c)
                diag.remove(row + c)
                anti_diag.remove(row - c)

        backtrack(0)
        return result

