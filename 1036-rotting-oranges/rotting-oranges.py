class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        s = sum(sum(row) for row in grid) 
        if s == 0:
            return 0

        if m == 1 and n == 1:
            if grid[0][0] == 1:return -1
            elif grid[0][0] == 2:return 0
            else: return 0

        rotten_oranges = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_oranges.append([i,j])
        
        visited = [[False] * n for _ in range(m)]
        queue = deque()
        for orange in rotten_oranges:
            queue.append(orange)
            visited[orange[0]][orange[1]] = True

        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        time = -1

        while queue:
            time += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx,dy in directions:
                    x_ = x + dx
                    y_ = y + dy

                    if x_ >= 0 and x_ < m and y_ >= 0 and y_ < n and not visited[x_][y_]:
                        if grid[x_][y_] == 1:
                            grid[x_][y_] = 2
                            queue.append([x_,y_])
                            visited[x_][y_] = True

        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return time
        




        