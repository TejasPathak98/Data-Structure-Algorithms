class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        #BFS with constraints

        queue = deque([(0,0,0)])
        steps = -1
        visited = set()
        visited.add((0,0,0))

        while queue:
            steps += 1
            
            for _ in range(len(queue)):

                x,y,obstacle_count = queue.popleft()

                if x == m - 1 and y == n - 1:
                    return steps
                
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x_ = x + dx
                    y_ = y + dy

                    if 0 <= x_ < m and 0 <= y_ < n:
                        new_obstacle_count = obstacle_count + grid[x_][y_]
                        if new_obstacle_count <= k and (x_,y_,new_obstacle_count) not in visited:
                            queue.append((x_,y_,new_obstacle_count))
                            visited.add((x_,y_,new_obstacle_count))

        return -1

