class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backtracking(x,y,visited,count,word):
            if count == len(word):return True

            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            visited[x][y] = True

            for dx,dy in directions:
                x_ = x + dx
                y_ = y + dy

                if x_ >= 0 and x_ < m and y_ >=0 and y_ < n and not visited[x_][y_] and board[x_][y_] == word[count]:
                    if backtracking(x_,y_,visited,count + 1,word) == True:return True

            
            visited[x][y] = False
            return False

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = [[False] * n for _ in range(m)]
                    if backtracking(i,j,visited,1,word) == True:return True
        
        return False


        #O() ; O(MN)