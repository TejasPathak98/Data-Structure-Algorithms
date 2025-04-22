class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        best = [[float('inf')] * n for _ in range(m)] # this is basically the matrix which keep track of the min obstacles used to reach point x,y (so far) ....if we reach that point from any other
        #way and with any other obstacle count, we will ignore it unless its less (its a more intelligent visited state)

        best[0][0] = 0
        queue = deque([(0,0,0)])

        path = 0

        while queue:
            
            for _ in range(len(queue)):
                x,y,used = queue.popleft()

                if x  == m -1 and y == n- 1:
                    return path

                if used > k:
                    continue
                
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n:
                        new_used = used + grid[nx][ny]

                        if new_used <= k and best[nx][ny] > new_used:
                            best[nx][ny] = new_used
                            queue.append((nx,ny,new_used))
            
            path += 1

        
        return -1
