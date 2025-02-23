class Solution:
    def dfs(self,matrix,memory,directions,x,y):
        if memory[x][y] != -1:
            return memory[x][y]
        
        max_path = 1

        for dx,dy in directions:
            x_ = x + dx
            y_ = y + dy
            if 0 <= x_ < len(matrix) and 0 <= y_ < len(matrix[0]) and matrix[x_][y_] > matrix[x][y]:
                max_path = max(max_path, 1 + self.dfs(matrix,memory,directions,x_,y_))
        
        memory[x][y] = max_path
        return max_path

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        if m == 1 and n == 1:
            return 1
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        memory = [[-1] * n for _ in range(m)]

        ans = 0

        for i in range(m):
            for j in range(n):
                ans = max(ans,self.dfs(matrix,memory,directions,i,j))

        return ans