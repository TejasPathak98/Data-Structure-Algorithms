class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        cost_dict = [[float('inf')] * n for _ in range(m)]
        cost_dict[0][0] = 0

        min_heap = [(0,0,0)]
        heapify(min_heap)
        

        while min_heap:
            cost,x,y = heapq.heappop(min_heap)

            if x == m - 1 and y == n - 1:
                return cost
            
            if cost > cost_dict[x][y]:
                continue

            
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = max(cost,abs(heights[nx][ny] - heights[x][y]))
                    if new_cost < cost_dict[nx][ny]:
                        cost_dict[nx][ny] = new_cost
                        heapq.heappush(min_heap,(new_cost,nx,ny))


        return -1 
            





