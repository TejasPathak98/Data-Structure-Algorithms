class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False for _ in range(m)] for _ in range(n)]

        ans = 0

        def bfs(x,y):
            queue = deque()
            queue.append((x,y))
            visited[x][y] = True

            while queue:
                x,y = queue.popleft()

                for dx,dy in directions:
                    new_x= x + dx
                    new_y = y + dy
                    if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y] and grid[new_x][new_y] == "1":
                        queue.append((new_x,new_y))
                        visited[new_x][new_y] = True


        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i,j)
                    ans += 1

        return ans