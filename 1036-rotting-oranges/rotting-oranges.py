class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        rotten = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
        
        queue = deque(rotten)
        time = -1

        while queue:

            for _ in range(len(queue)):

                x,y = queue.popleft()
                

                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x_ = x + dx
                    y_ = y + dy

                    if 0 <= x_ < m and 0 <= y_ < n and grid[x_][y_] == 1:
                        queue.append((x_,y_))
                        grid[x_][y_] = 2

            time += 1

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        all_zero = all(val == 0 for row in grid for val in row)
        if all_zero:
            return 0

        return time


