class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        if grid[0][0] == 1 or grid[n][n] == 1:
            return -1
        if n == 0:
            return 1

        queue = deque([(0,0)])
        level = 1
        dir = [[-1,0],[-1,-1],[-1,1],[1,0],[1,-1],[0,1],[0,-1],[1,1]]

        while queue:

            for _ in range(len(queue)):
                x,y = queue.popleft()

                if x == n and y == n:
                    return level

                for i in range(8):
                    dx = x + dir[i][0]
                    dy = y + dir[i][1]

                    if dx < 0 or dx > n or dy < 0 or dy > n or grid[dx][dy] != 0:
                        continue
                    else:
                        grid[dx][dy] = 2
                        queue.append([dx,dy])
                    
            level +=1
        
        return -1
                


        