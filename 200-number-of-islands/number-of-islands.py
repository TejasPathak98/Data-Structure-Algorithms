class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if m == 1 and n == 1:
            if grid[0][0] == "1":
                return 1
            else:
                return 0
        
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        ans = 0

        # def bfs(x,y):
        #     nonlocal visited
        #     visited[x][y] = True
        #     queue = deque()
        #     queue.append((x,y))

        #     while queue:
        #         x1,y1 = queue.popleft()

        #         for dx,dy in dir:
        #             rx = dx + x1
        #             ry = dy + y1

        #             if rx < 0 or rx >= n or ry < 0 or ry >=m or grid[rx][ry] == "0" or visited[rx][ry] == True:
        #                 continue
        #             else:
        #                 visited[rx][ry] = True
        #                 queue.append((rx,ry))

        def dfs(x,y):
            grid[x][y] = "0"

            for dx,dy in dir:
                rx = dx + x
                ry = dy + y

                if 0 <= rx < n and 0 <= ry < m and grid[rx][ry] == "1":
                    dfs(rx,ry)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":  #and visited[i][j] == False:
                    dfs(i,j)
                    ans += 1

        return ans

        #O(nm) ; O(nm)
        
            

        