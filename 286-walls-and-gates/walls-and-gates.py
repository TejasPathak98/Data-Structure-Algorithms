class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        n = len(rooms)
        m = len(rooms[0])
        queue = deque()
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue.append((i,j))
        
        dir = [(-1,0),(0,1),(1,0),(0,-1)]

        while queue:
            x,y = queue.popleft()
            dist = rooms[x][y] + 1
            for dx,dy in dir:
                new_x = dx + x 
                new_y = dy + y
                if 0<= new_x < n and 0 <= new_y < m and rooms[new_x][new_y] == 2147483647:
                    rooms[new_x][new_y] = dist
                    queue.append((new_x,new_y))
        
