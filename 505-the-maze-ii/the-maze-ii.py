class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])

        visited = set()
        start = tuple(start)
        destination = tuple(destination)
        heap = [(0,start)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while heap:
            dist,coordinate = heapq.heappop(heap)

            if coordinate == destination:
                return dist
            
            if coordinate in visited:
                continue
            
            visited.add(coordinate)

            for direction in directions:
                new_dist = 0
                i,j = coordinate

                while (0 <= i + direction[0] < n) and (0 <= j + direction[1] < m) and (maze[i + direction[0]][j + direction[1]] == 0):
                    i += direction[0]
                    j += direction[1]
                    new_dist += 1

                heapq.heappush(heap,(new_dist + dist,(i,j)))
        

        return -1


        