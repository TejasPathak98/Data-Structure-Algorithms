class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.bfs(i,j,grid)
                    count +=1
        
        return count

    def bfs(self,x,y,grid):
        queue = deque([(x,y)])
        grid[x][y] = "-1"

        while queue:
            cx,cy = queue.popleft()

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x_ = cx + dx
                y_ = cy + dy

                if x_ >= 0 and x_ < len(grid) and y_ >=0 and y_ < len(grid[0]) and grid[x_][y_] == "1":
                    grid[x_][y_] = "-1"
                    queue.append((x_,y_))

    
    #O(MN) ; O(min(M,N))