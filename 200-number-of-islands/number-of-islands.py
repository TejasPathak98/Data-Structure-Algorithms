class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        no_of_islands = 0

        def dfs(x,y):
            grid[x][y] = 0

            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                x_ = x + dx
                y_ = y + dy

                if 0 <= x_ < m and 0 <=  y_ < n and grid[x_][y_] == "1":
                    dfs(x_,y_)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    no_of_islands += 1
                    dfs(i,j)


        return no_of_islands
