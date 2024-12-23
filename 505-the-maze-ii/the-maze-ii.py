class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        dist = [[float('inf')] * len(maze[0]) for _ in range(len(maze))]
        dist[start[0]][start[1]] = 0

        hq = [(0,start[0],start[1])]
        heapq.heapify(hq)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while hq:
            curr_dist,x,y = heapq.heappop(hq)

            if curr_dist > dist[x][y]:
                continue
            
            if x == destination[0] and y == destination[1]:
                return curr_dist
            
            for dx,dy in directions:
                new_x = x
                new_y = y
                steps = 0

                while 0 <= new_x + dx < len(maze) and 0 <= new_y + dy < len(maze[0]) and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    steps += 1
                
                if steps + curr_dist < dist[new_x][new_y]:
                    dist[new_x][new_y] = steps + curr_dist
                    heapq.heappush(hq,(steps + curr_dist,new_x,new_y))


        return -1
                

            



        