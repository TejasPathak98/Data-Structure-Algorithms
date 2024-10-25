class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        max_area = 0
        visited = set()

        def bfs(x,y):
            nonlocal max_area
            queue = deque()
            queue.append((x,y))
            area = 0
            visited.add((x,y))

            while queue:
                x,y = queue.popleft()
                area += 1
                max_area = max(max_area,area)

                for dx,dy in directions:
                    x_new = x + dx
                    y_new = y + dy

                    if 0 <= x_new < n and 0 <= y_new < m and grid[x_new][y_new] == 1 and (x_new,y_new) not in visited:
                        visited.add((x_new,y_new))
                        queue.append((x_new,y_new))

        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in visited:
                    bfs(i,j)
        
        return max_area

        
            






        