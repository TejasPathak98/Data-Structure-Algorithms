class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        min_heap = [(grid[0][0],0,0)]

        minTime = [[float('inf')] * n for _ in range(n)]

        minTime[0][0] = grid[0][0]

       
        while min_heap:
            time,x,y, = heapq.heappop(min_heap)

            if x == n - 1 and y == n - 1:
                return time
            
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    new_time = max(time,grid[nx][ny])

                    if new_time < minTime[nx][ny]:
                        minTime[nx][ny] = new_time
                        heapq.heappush(min_heap,(new_time,nx,ny))
    

        return -1
