class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        heap = []
        heappush(heap, (0,0,0,1))
        m = len(moveTime)
        n = len(moveTime[0])
        
        time_dict = [[[float('inf')] * 3 for _ in range(n)] for _ in range(m)]

        time_dict[0][0][1] = 0

        while heap:

            time_cost , x, y , factor = heappop(heap)

            if x == m - 1 and y == n - 1:
                return time_cost

            if time_cost > time_dict[x][y][factor]:
                continue
            
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    wait_time = max(moveTime[nx][ny] - time_cost,0)
                    new_cost = wait_time + time_cost + factor
                    next_factor = 2 if factor == 1 else 1

                    if new_cost < time_dict[nx][ny][next_factor]:
                        time_dict[nx][ny][next_factor] = new_cost
                        heappush(heap, (new_cost,nx,ny,next_factor))

        return -1
            

            


