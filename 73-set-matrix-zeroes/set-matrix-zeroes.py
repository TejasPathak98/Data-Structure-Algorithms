class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        cols = set()
        rows = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(i)
        
        for r in rows:
            for i in range(n):
                matrix[r][i] = 0
        
        for c in cols:
            for i in range(m):
                matrix[i][c] = 0
        
        return


