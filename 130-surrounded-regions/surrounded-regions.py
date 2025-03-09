class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    #     m = len(board)
    #     n = len(board[0])
    #     visited = set()

    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] == "O" and i not in (0,m - 1) and j not in (0,n - 1) and (i,j) not in visited:
    #                 self.bfs(board,i,j,visited)
        

    # def bfs(self,board,i,j,visited):
    #     m = len(board)
    #     n = len(board[0])
    #     queue = deque([(i,j)])
    #     local_visited = set()
    #     local_visited.add((i,j))
    #     revert_back = False

    #     while queue:
    #         x,y = queue.popleft()
    #         if x in (0,m - 1) or  y in (0,n - 1):
    #             revert_back = True
    #         board[x][y] = "X"

    #         for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
    #             x_ = x + dx
    #             y_ = y + dy

    #             if x_ >= 0 and x_ <= m - 1 and y_ >= 0 and y_ < n and board[x_][y_] == "O" and (x_,y_) not in local_visited: 
    #                 queue.append((x_,y_))
    #                 local_visited.add((x_,y_))
        
    #     if revert_back:
    #         for a,b in local_visited:
    #             board[a][b] = "O"

    #     visited |= local_visited

    #     #O(MN) ;O(MN)


        m = len(board)
        n = len(board[0])
        queue = deque()

        for i in range(m):
            for j in [0,n - 1]:
                if board[i][j] == "O":
                    queue.append((i,j))
                    board[i][j] = "T"

        for i in range(n):
            for j in [0,m - 1]:
                if board[j][i] == "O":
                    queue.append((j,i))
                    board[j][i] = "T"

        self.bfs(queue,board)

        
    def bfs(self,queue,board):

        while queue:
            x,y = queue.popleft()

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x_ = x + dx
                y_ = y + dy

                if x_ >= 0 and x_ < len(board) and y_ >= 0 and y_ < len(board[0]) and board[x_][y_] == "O":
                    board[x_][y_] = "T"
                    queue.append((x_,y_))


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
                









