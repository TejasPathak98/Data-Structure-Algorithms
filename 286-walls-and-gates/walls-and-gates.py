class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        INF = 2147483647
        visited = set()

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

        while queue:
            x,y = queue.popleft()

            for dx,dy in directions:
                x_ = x + dx
                y_ = y + dy 

                if x_ >= 0 and x_ < len(rooms) and y_ >=0 and y_ < len(rooms[0]) and rooms[x_][y_] == INF and (x_,y_) not in visited:
                    queue.append((x_,y_))
                    visited.add((x_,y_))
                    rooms[x_][y_] = rooms[x][y] + 1







        

