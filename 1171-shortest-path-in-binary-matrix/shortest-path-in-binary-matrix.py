class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        queue.append((0,0,1))

        if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
            return -1

        directions = [(-1,0),(1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        visited = [[[False] for _ in range(m)] for _ in range(n)]
        visited[0][0] = True

        while queue:
            for _ in range(len(queue)):
                x,y,step = queue.popleft()
                print(x,y,step)

                if x == n - 1 and y == m - 1:
                    return step
                
                for dx,dy in directions:
                    rx = dx + x
                    ry = dy + y

                    if rx < 0 or rx >= n or ry < 0 or ry >= m or grid[rx][ry] == 1 or visited[rx][ry] == True:
                        continue
                    else:
                        visited[rx][ry] = True
                        queue.append((rx,ry,step + 1))
        
        return -1


