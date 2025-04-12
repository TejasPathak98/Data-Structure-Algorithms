class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        def explore_land(start):
            queue = deque([start])
            area = 0
            water = set()

            while queue:
                x,y = queue.popleft()
                area += 1

                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n:

                        if grid[nx][ny] == 1:
                            grid[nx][ny] = -1
                            queue.append((nx,ny))
                        elif grid[nx][ny] == 0:
                            water.add((nx,ny))

            for w in water:
                water_area[w] += area

        m = len(grid)
        n = len(grid[0])

        water_area = defaultdict(int)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    explore_land((i,j))

        print(water_area)

        if water_area:
            return 1 + max(water_area.values())
        
        return 1 if grid[0][0] == 0 else m*n