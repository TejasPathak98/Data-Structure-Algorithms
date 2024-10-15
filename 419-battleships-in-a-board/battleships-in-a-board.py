class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        ans = 0

        def helper(x,y):
            nonlocal board,n,m
            queue = deque()
            queue.append((x,y))
            board[x][y] = "*"

            while queue:
                x1,y1 = queue.popleft()
                for dx,dy in directions:
                    rx = dx + x1
                    ry = dy + y1

                    if rx < 0 or rx >= m or ry < 0 or ry >= n or board[rx][ry] == "." or board[rx][ry] == "*":
                        continue
                    else:
                        print("Br")
                        board[rx][ry] = "*"
                        queue.append((rx,ry))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    ans += 1
                    helper(i,j)

        return ans


    

