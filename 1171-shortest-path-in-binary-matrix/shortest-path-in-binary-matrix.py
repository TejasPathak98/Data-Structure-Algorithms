class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        queue = deque([(0,0,1)])
        dir = [(-1,0),(1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while queue:
            for _ in range(len(queue)):
                x,y,steps = queue.popleft()
            
                if x == n - 1 and y == n - 1:
                    return steps
                
                for dx,dy in dir:
                    x_,y_ = x + dx, y + dy
                    if x_ < 0 or y_ < 0 or x_ >= n or y_ >= n or grid[x_][y_] == 1 or visited[x_][y_] == True:
                        continue
                    else:
                        queue.append((x_,y_,steps + 1))
                        visited[x_][y_] = True
        
        return -1
            

        