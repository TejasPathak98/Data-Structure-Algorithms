class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))

        time = - 1

        while queue:

            for _ in range(len(queue)):

                x,y = queue.popleft()

                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        queue.append((nx,ny))
                        grid[nx][ny] = 2

            time += 1

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        all_zero = all(grid[i][j] == 0 for i in range(m) for j in range(n))
        if all_zero:
            return 0
        
        return time



