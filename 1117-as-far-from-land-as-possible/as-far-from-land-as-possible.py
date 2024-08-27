class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dir = [[-1,0],[1,0],[0,1],[0,-1]]

        if max(max(grid)) == 0 or min(min(grid)) == 1:
            return -1
        
        queue = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j,0))
                    visited.add((i,j))

        res = 0
        while queue:
            r,c,dist = queue.popleft()
            for i in range(4):
                rx = r + dir[i][0]
                ry = c + dir[i][1]

                if 0 <= rx < m and 0 <= ry < n and (rx,ry) not in visited:
                    new_dist = dist + 1
                    res = max(res,new_dist)
                    queue.append((rx,ry,new_dist))
                    visited.add((rx,ry))
        
        return res



        
        