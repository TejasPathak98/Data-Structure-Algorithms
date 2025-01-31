class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        n = len(board)
        m = len(board[0])

        def backtracking(i,j,word,count,visited):
            if count == len(word):return True

            if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or word[count] != board[i][j]:return False

            directions = [[-1,0],[1,0],[0,1],[0,-1]]

            visited[i][j] = True

            for dx,dy in directions:
                x = i + dx
                y = j + dy

                if backtracking(x, y, word, count + 1, visited) == True:return True
            
            visited[i][j] = False
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = [[False] * m for _ in range(n)]
                    if backtracking(i, j, word, 0, visited) == True:return True
        
        return False