class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        total_cost = 0

        min_heap = [(0,0,0)]
        heapify(min_heap)

        cost = [[float('inf')] * n for _ in range(m)]

        cost[0][0] = 0

        while min_heap:
            current_cost , x, y = heapq.heappop(min_heap)

            #current_cost is maximum absolute difference in heights between two consecutive cells of the route seen until now


            if x == m - 1 and y == n - 1:
                return current_cost

            if current_cost > cost[x][y]:
                continue


            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x_ = x + dx
                y_ = y + dy

                if 0 <= x_ < m and 0 <= y_ <n:
                    potential_cost_incurred = abs(heights[x_][y_] - heights[x][y])
                    new_cost = max(potential_cost_incurred,current_cost)
                    if new_cost < cost[x_][y_]:
                        heapq.heappush(min_heap, (new_cost,x_,y_))
                        cost[x_][y_] = new_cost

        return -1


