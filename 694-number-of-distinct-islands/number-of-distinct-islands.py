class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])


        def dfs(x,y,base_x,base_y,shape):

            if visited[x][y]:
                return
            
            visited[x][y] = True
            shape.append((x - base_x,y - base_y))

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x_ = x +dx
                y_ = y +dy

                if 0 <= x_ < m and 0 <= y_ < n and grid[x_][y_] == 1 and not visited[x_][y_]:
                    dfs(x_,y_,base_x,base_y,shape)

        islands = set()
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    shape = []
                    dfs(i,j,i,j,shape)
                    islands.add(tuple(shape))

        
        return len(islands)

