class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        hq = []
        hq.append((0,ball[0],ball[1],""))
        heapq.heapify(hq)
        directions = [(-1,0,"u"),(1,0,"d"),(0,1,"r"),(0,-1,"l")]
        distances = [[float(inf)] * len(maze[0]) for _ in range(len(maze))]
        distances[ball[0]][ball[1]] = 0
        ans = []

        while hq:
            dist,x,y,ds = heapq.heappop(hq)

            if distances[x][y] < dist:
                continue
            
            for dx,dy,st in directions:
                new_x = x
                new_y = y
                steps = 0
                while 0 <= new_x + dx < len(maze) and 0 <= new_y + dy < len(maze[0]) and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    steps += 1

                    if new_x == hole[0] and new_y == hole[1]:
                        ans.append((ds + st,dist + steps))
                        break
                
                if new_x == x and new_y == y:
                    continue
                        
                if distances[new_x][new_y] >= steps + dist:
                    distances[new_x][new_y] = steps + dist
                    heapq.heappush(hq, (steps + dist,new_x,new_y,ds + st))
                
        if not ans:
            return "impossible"
  
        ans = sorted(ans,key = lambda x : (x[1],x[0]))
        print(ans)
        return ans[0][0]



        