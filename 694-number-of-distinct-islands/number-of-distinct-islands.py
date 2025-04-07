class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # we take a dfs based approach for the capturing the shape of the islands

        m = len(grid)
        n = len(grid[0])
        unique_shapes = set()
        visited = [[False] * n for _ in range(m)]


        def dfs(i,j,base_i,base_j,shape):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j]:
                return

            visited[i][j] = True
            
            shape.append((i - base_i,j - base_j))

            dfs(i + 1,j,base_i,base_j,shape)
            dfs(i - 1,j,base_i,base_j,shape)
            dfs(i ,j + 1,base_i,base_j,shape)
            dfs(i,j - 1,base_i,base_j,shape)

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == False:
                    shape = []
                    dfs(i,j,i,j,shape)
                    unique_shapes.add(tuple(shape))



        return len(unique_shapes)

