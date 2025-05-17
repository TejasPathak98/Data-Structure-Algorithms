class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # m = len(grid)
        # n = len(grid[0])
        # perimeter = 0

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             perimeter += 4
        #             if i > 0 and grid[i - 1][j] == 1:
        #                 perimeter -= 2
        #             if j > 0 and grid[i][j - 1] == 1:
        #                 perimeter -= 2
        
        # return perimeter


        m = len(grid)
        n = len(grid[0])
        perimeter = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return 1
            if grid[r][c] == -1:
                return 0
            grid[r][c] = -1

            return (dfs(r - 1,c) + dfs(r + 1,c) + dfs(r,c - 1) + dfs(r,c + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += dfs(i,j)
        
        return perimeter


