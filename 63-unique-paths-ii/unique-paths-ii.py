class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])

        # if obstacleGrid[0][0] == 1:
        #     return 0

        # if m == 1 and n == 1:
        #     if obstacleGrid[0][0] == 1:
        #         return 0
        #     else:
        #         return 1

        # self.paths = 0


        # def dfs(x,y,visited):
        #     if x == m - 1 and y == n - 1 and obstacleGrid[x][y] == 0:
        #         self.paths += 1
        #         return

        #     for dx,dy in [(1,0),(0,1)]:
        #         x_ = x + dx
        #         y_ = y + dy

        #         if 0 <= x_ < m and 0 <= y_ < n and obstacleGrid[x_][y_] == 0 and (x_,y_) not in visited:
        #             visited.add((x_,y_))
        #             dfs(x_,y_,visited)
        #             visited.remove((x_,y_))
                    

        # dfs(0,0,set([(0,0)]))
        # return self.paths

        #This is a DP problem, thats why its TLE...overlapping subproblems

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        #Recurrence Relation : dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        #0 if there is an Obstacle

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for i in range(1,m):
            if obstacleGrid[i][0] == 0 and dp[i - 1][0] == 1:
                dp[i][0] = 1
        
        for j in range(1,n):
            if obstacleGrid[0][j] == 0 and dp[0][j - 1] == 1:
                dp[0][j] = 1


        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        
        return dp[m- 1][n- 1]








