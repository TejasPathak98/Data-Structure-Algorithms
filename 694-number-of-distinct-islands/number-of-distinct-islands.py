class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = set()


        def dfs(x,y,base_x,base_y,shape):

            shape.append((base_x - x, base_y - y))

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    dfs(nx,ny,base_x,base_y,shape)
                    

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    shape  = []
                    dfs(i,j,i,j,shape)
                    islands.add(tuple(shape))

        
        return len(islands)
