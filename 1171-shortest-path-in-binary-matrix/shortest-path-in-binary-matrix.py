class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
            return -1
        
        queue = deque()
        queue.append((0,0))
        dir = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        visited = set()
        visited.add((0,0))
        path = 0
        
        while queue:
            size = len(queue)
            path += 1
            for _ in range(size):
                x,y = queue.popleft()

                if x == n - 1 and y == m - 1:
                    return path

                for dx,dy in dir:
                    new_x = x + dx
                    new_y = y + dy

                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 0 and (new_x,new_y) not in visited:
                        queue.append((new_x,new_y))
                        visited.add((new_x,new_y))

        return -1



        