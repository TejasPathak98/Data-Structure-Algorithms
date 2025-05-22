class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[(0,0)] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                dp[i][j] = (dp[i][j][0] + dp[i - 1][j][0] + 1, dp[i][j][1] + dp[i][j - 1][1] + 1)

        max_elements = 0
        
        for win in range(min(m,n) - 1,-1,-1):
            for i in range(m - win):
                for j in range(n - win):
                    if grid[i][j] == 0:
                        continue
                    x1,y1 = dp[i][j] #top left
                    x2,y2 = dp[i + win][j] #bottom left
                    x3,y3 = dp[i][j + win] #top right
                    x4,y4 = dp[i + win][j + win] #bottom right

                    

                    if x2 - x1 == x4 - x3 == y3 - y1 == y4 - y2 == win:
                        return (win + 1) * (win + 1)


        return max_elements

