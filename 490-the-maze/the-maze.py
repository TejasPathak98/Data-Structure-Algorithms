class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not start or not destination or not maze:
            return False
        if start == destination:
            return True
        
        m = len(maze)
        n = len(maze[0])

        x = start[0]
        y = start[1]
        visited = set()

        queue = deque()
        queue.append((x,y))
        visited.add((x,y))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            x_ , y_ = queue.popleft()
            if x_ == destination[0] and y_ == destination[1]:
                return True
            
            for dx,dy in directions:
                x_new = x_ + dx
                y_new = y_ + dy

                while 0 <= x_new < m and 0 <= y_new < n and maze[x_new][y_new] == 0:
                    x_new += dx
                    y_new += dy
                
                rolled_x = x_new - dx
                rolled_y = y_new - dy

                if (rolled_x,rolled_y) not in visited:
                    visited.add((rolled_x,rolled_y))
                    queue.append((rolled_x,rolled_y))

        return False
            

        