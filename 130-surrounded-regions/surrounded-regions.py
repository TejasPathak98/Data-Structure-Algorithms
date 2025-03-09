class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = set()

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and i not in (0,m - 1) and j not in (0,n - 1) and (i,j) not in visited:
                    self.bfs(board,i,j,visited)
        

    def bfs(self,board,i,j,visited):
        m = len(board)
        n = len(board[0])
        queue = deque([(i,j)])
        local_visited = set()
        local_visited.add((i,j))
        revert_back = False

        while queue:
            x,y = queue.popleft()
            if x in (0,m - 1) or  y in (0,n - 1):
                revert_back = True
            board[x][y] = "X"

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x_ = x + dx
                y_ = y + dy

                if x_ >= 0 and x_ <= m - 1 and y_ >= 0 and y_ < n and board[x_][y_] == "O" and (x_,y_) not in local_visited: 
                    queue.append((x_,y_))
                    local_visited.add((x_,y_))
        
        if revert_back:
            for a,b in local_visited:
                board[a][b] = "O"

        visited |= local_visited








