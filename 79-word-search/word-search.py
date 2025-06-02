class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

    
        def dfs(x,y,word_pos):
            if word_pos == len(word) - 1:
                return True

            ch = board[x][y]

            board[x][y] = "#"

            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[word_pos + 1]:
                    if dfs(nx,ny,word_pos + 1):
                        return True
            
            board[x][y] = ch
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True

        
        return False

