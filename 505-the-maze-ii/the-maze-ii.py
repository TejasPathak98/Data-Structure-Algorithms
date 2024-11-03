class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])

        visited = {}
        start = tuple(start)
        destination = tuple(destination)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        queue = deque([(0,start)])

        while queue:
            size = len(queue)
            for _ in range(size):
                dist , coordinate = queue.popleft()

                if coordinate in visited and visited[coordinate] <= dist:
                    continue
                
                visited[coordinate] = dist
                

                for direction in directions:
                    i,j = coordinate
                    new_dist = 0
                    while (0 <= (direction[0] + i) < n) and (0 <= (direction[1] + j) < m) and maze[i + direction[0]][j + direction[1]] == 0:
                        i += direction[0]
                        j += direction[1]
                        new_dist += 1

                    queue.append((new_dist + dist,(i,j)))

        
        if destination in visited:
            return visited[destination]
        else:
            return -1


            


        