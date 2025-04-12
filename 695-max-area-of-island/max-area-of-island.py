class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.dfs(i,j,grid)
                    max_area = max(max_area,area)


        return max_area


    def dfs(self,x,y,grid):

        grid[x][y] = 0
        count = 1

        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            x_ = x + dx
            y_ = y + dy

            if 0 <= x_ < len(grid) and 0 <= y_ < len(grid[0]) and grid[x_][y_] == 1:
                count += self.dfs(x_,y_,grid)

        return count


