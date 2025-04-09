class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i,j,idx):
            if idx == len(word) - 1:
                return True
            
            temp = board[i][j]

            board[i][j] = "#"

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x = i + dx
                y = j + dy

                if 0 <= x < m and 0 <= y < n and board[x][y] == word[idx + 1]:
                    if dfs(x,y,idx + 1):
                        return True
            board[i][j] = temp
            return False 

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    #visited = [[False] * n for _ in range(m)]
                    if dfs(i,j,0):
                        return True
        
        return False