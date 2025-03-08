class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])

        queue = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))


        while queue:
            x,y = queue.popleft()

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x_ = x + dx
                y_ = y + dy

                if x_ >=0 and x_ < m and y_ >= 0 and y_ < n and rooms[x_][y_] == 2147483647:
                    rooms[x_][y_] = rooms[x][y] + 1
                    queue.append((x_,y_))


