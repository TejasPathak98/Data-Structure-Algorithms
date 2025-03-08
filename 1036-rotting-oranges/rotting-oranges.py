class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if all(cell == 0 for row in grid for cell in row):
            return 0

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        return self.bfs(queue,grid)


    def bfs(self,queue,grid):
        time = -1
        m = len(grid)
        n = len(grid[0])

        while queue:
            size = len(queue)
            time += 1

            for _ in range(size):
                x,y = queue.popleft()

                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x_ = x + dx
                    y_ = y + dy

                    if x_ >= 0 and x_ < m and y_ >=0 and y_ < n and grid[x_][y_] == 1:
                        grid[x_][y_] = 2
                        queue.append((x_,y_))

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return time


