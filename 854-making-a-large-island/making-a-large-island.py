class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        def bfs(i,j):
            water_set = set()

            queue = deque()
            queue.append((i,j))
            visited.add((i,j))
            area = 0

            while queue:
                x,y = queue.popleft()

                area += 1

                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x_ = x + dx
                    y_ = y + dy

                    if 0 <= x_  < m and 0 <= y_ < n and (x_,y_) not in visited:

                        if grid[x_][y_] == 1:
                            queue.append((x_,y_))
                            visited.add((x_,y_))
                        else:
                            water_set.add((x_,y_))
            
            for cell in water_set:
                water_dict[cell] += area

        m = len(grid)
        n = len(grid[0])

        water_dict = defaultdict(int)
        visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in visited:
                    bfs(i,j)

        if len(water_dict) > 0:
            return 1 + max(water_dict.values())
        
        if grid[0][0] == 1:
            return m*n
        else:
            return 1