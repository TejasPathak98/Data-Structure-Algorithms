class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area,self.bfs(grid,i,j))

        return max_area

    def bfs(self,grid,i,j):
        area = 0
        queue = deque([(i,j)])
        grid[i][j] = -1

        while queue:
            x,y = queue.popleft()
            area += 1

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x_ = x + dx
                y_ = y + dy

                if x_ >= 0 and x_ < len(grid) and y_ >= 0 and y_ < len(grid[0]) and grid[x_][y_] == 1:
                    grid[x_][y_] = -1
                    queue.append((x_,y_))

        return area
