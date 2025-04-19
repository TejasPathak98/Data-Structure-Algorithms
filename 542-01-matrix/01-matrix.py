class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        queue = deque()
        m = len(mat)
        n = len(mat[0])
        visited = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        
        path = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x,y = queue.popleft()

                if mat[x][y] == 1:
                    mat[x][y] = path
                
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited:
                        queue.append((nx,ny))
                        visited.add((nx,ny))

            path += 1

        
        return mat
