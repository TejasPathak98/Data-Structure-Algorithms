class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        connected_components = 0

        def dfs(i,j):
            visited[i][j] = True
            count = 1

            for row in range(m):
                if row != i and grid[row][j] == 1 and visited[row][j] == False:
                    count += dfs(row,j)
            
            for col in range(n):
                if col != j and grid[i][col] == 1 and visited[i][col] == False:
                    count += dfs(i,col)

            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] == False:
                    groupSize = dfs(i,j)
                    if groupSize > 1:
                        connected_components += groupSize


        
        return connected_components
