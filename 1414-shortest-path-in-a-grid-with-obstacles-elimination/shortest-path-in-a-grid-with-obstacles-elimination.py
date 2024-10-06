class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        queue = deque([(0,0,k)])
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        steps = 0
        visited = set()
        visited.add((0,0,k))
        
        while queue:
            size = len(queue)
            for _ in range(size):
                r,c,rem = queue.popleft()

                if r == n - 1 and c == m - 1:
                    return steps
                
                for dx,dy in dir:
                    rx = dx + r
                    cy = dy + c

                    if rx < 0 or cy < 0 or rx >= n or cy >= m:
                        continue
                    elif grid[rx][cy] == 1 and rem > 0 and (rx,cy,rem - 1) not in visited:
                        queue.append((rx,cy,rem - 1))
                        visited.add((rx,cy,rem - 1))
                    elif grid[rx][cy] == 0 and (rx,cy,rem) not in visited:
                        queue.append((rx,cy,rem))
                        visited.add((rx,cy,rem))
            steps +=1
        
        return -1