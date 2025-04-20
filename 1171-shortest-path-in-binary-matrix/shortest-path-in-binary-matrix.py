class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque([(0,0)])
        visited = set()
        visited.add((0,0))

        if grid[0][0] == 1 or grid[n - 1][n- 1] == 1:
            return -1

        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

        path = 1
        while queue:

            for _ in range(len(queue)):

                x,y = queue.popleft()

                if x == n - 1 and y == n - 1:
                    return path
                
                for dx,dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited and grid[nx][ny] == 0:
                        queue.append((nx,ny))
                        visited.add((nx,ny))
            
            path += 1
        
        return -1




