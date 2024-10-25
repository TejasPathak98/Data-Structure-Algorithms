class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not start or not destination:
            return False
        
        if start[0] == destination[0] and start[1] == destination[1]: #start == destination:
            return True

        n = len(maze)
        m = len(maze[0])

        queue = deque()
        queue.append(start)
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        visited.add((start[0],start[1]))


        while queue:
            curr = queue.popleft()
            if curr[0] == destination[0] and curr[1] == destination[1]:
                return True
            
            for dir in directions:
                x = curr[0] + dir[0]
                y = curr[1] + dir[1]

                while 0 <= x < n and 0 <= y < m and maze[x][y] == 0:
                    x = x + dir[0]
                    y = y + dir[1]
                
                rolled_x = x - dir[0]
                rolled_y = y - dir[1]
                if (rolled_x,rolled_y) not in visited:
                    visited.add((rolled_x,rolled_y))
                    queue.append([rolled_x,rolled_y])

        return False



            

        