class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0],0,0)]
        visited = [[False] * n for _ in range(n)]

        while heap:
            elevation,x,y = heapq.heappop(heap)

            if visited[x][y] == True:
                continue
            
            if x == n - 1 and y == n - 1:
                return elevation
            
            visited[x][y] = True

            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                x_ = x + dx
                y_ = y + dy
                if 0 <= x_ < n and 0 <= y_ < n and not visited[x_][y_]:
                    heapq.heappush(heap,(max(elevation,grid[x_][y_]),x_,y_))

        
        return -1
                     

