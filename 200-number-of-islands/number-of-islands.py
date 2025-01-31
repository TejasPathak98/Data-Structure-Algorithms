class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        visited = set()

        def bfs(x,y):
            queue = deque()
            queue.append((x,y))
            visited.add((x,y))

            while queue:
                a,b = queue.popleft()
                grid[a][b] = "0"

                for dx,dy in directions:
                    x_ = a + dx
                    y_ = b + dy
                    if x_ >= 0 and x_ < n and y_ >= 0 and y_ < m and grid[x_][y_] == "1" and (x_,y_) not in visited:
                        queue.append((x_,y_))
                        visited.add((x_,y_))

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    ans += 1
        
        return ans
        