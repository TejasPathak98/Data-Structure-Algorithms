class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        if not rooms:
            return
        m = len(rooms)
        n = len(rooms[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))
        
        while queue:
            x,y = queue.popleft()
            dist = rooms[x][y] + 1
            for dx,dy in directions:
                x_ = x + dx
                y_ = y + dy

                if 0 <= x_ < m and 0 <= y_ < n and rooms[x_][y_] == 2147483647:
                    rooms[x_][y_] = dist
                    queue.append((x_,y_))
        
        



        