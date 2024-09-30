class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        if not grid:
            return 0

        dir = [[-1,0],[0,1],[1,0],[0,-1]]

        def bfs(x,y):
            queue = deque([(x,y)])

            while queue:
                s,t = queue.popleft()
                for i in range(4):
                    dx = s + dir[i][0]
                    dy = t + dir[i][1]

                    if dx < 0 or dx >= m or dy < 0 or dy >= n or grid[dx][dy] != "1":
                        continue
                    else:
                        grid[dx][dy] = 2
                        queue.append([dx,dy])


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i,j)
                    ans += 1
                    print("Hi")
        
        return ans




        