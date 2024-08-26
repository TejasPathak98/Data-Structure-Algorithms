class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = [[False]*n for _ in range(m)]
        max_area = 0

        def dfs(i,j):
            nonlocal dir
            area = 1
            visited[i][j] = True

            for k in range(len(dir)):
                x = i + dir[k][0]
                y = j + dir[k][1]

                if x >=0 and x < len(grid) and y >= 0 and y < len(grid[0]) and visited[x][y] == False and grid[x][y] == 1:
                    print("Hi")
                    area += dfs(x,y)
            
            return area

        

        for i in range(m):
            for j in range(n):
                area = 0
                if visited[i][j] == False and grid[i][j] == 1:
                    print("Hi2")
                    max_area = max(max_area,dfs(i,j))
        
        return max_area
        