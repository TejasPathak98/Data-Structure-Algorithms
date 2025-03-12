class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        time_taken = 0
        time = [[float("inf")] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        time[0][0] = grid[0][0]

        min_heap = [(grid[0][0],0,0)]

        while min_heap:
            t , x, y = heapq.heappop(min_heap)
            time_taken = max(time_taken,t)
            visited[x][y] = True

            if x == n - 1 and y == n - 1:
                return time_taken

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x_ = x + dx
                y_ = y  + dy

                if 0 <= x_ < n and 0 <= y_ < n and grid[x_][y_] < time[x_][y_] and visited[x_][y_] != True:
                    heapq.heappush(min_heap, (grid[x_][y_],x_,y_))


        return -1
        
                
