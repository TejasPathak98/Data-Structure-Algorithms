class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        islandOne = deque()
        q = deque()
        visited = set()
        m = len(grid)
        n = len(grid[0])
        dir = [[-1,0],[1,0],[0,1],[0,-1]]
        moves = 0

        def isValid(x,y):
            if x >=0 and x < m and y >= 0 and y < n:
                return True 
            else:
                return False

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    islandOne.append([i,j])
                    q.append([i,j])
                    visited.add((i,j))
                    break 
            if len(islandOne) == 1:
                break

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for i in range(4):
                    rx = r + dir[i][0]
                    ry = c + dir[i][1]

                    if isValid(rx,ry) and grid[rx][ry] == 1 and (rx,ry) not in visited:
                        islandOne.append([rx,ry])
                        q.append([rx,ry])
                        visited.add((rx,ry))
        
        while islandOne:
            for _ in range(len(islandOne)):
                r,c = islandOne.popleft()
                for i in range(4):
                    rx = r + dir[i][0]
                    ry = c + dir[i][1]

                    if isValid(rx,ry) and (rx,ry) not in visited:
                        if grid[rx][ry] == 1:
                            return moves 

                        islandOne.append([rx,ry])
                        visited.add((rx,ry))
            moves += 1


        



        