class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        directions = (0,1,0,-1,0)
        m = len(heightMap)
        n = len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0

        area = 0
        boundary = []
        water_level = 0

        for i in range(m):
            boundary.append((heightMap[i][0],i,0))
            boundary.append((heightMap[i][-1],i,n-1))
            heightMap[i][0] = heightMap[i][-1] = -1
        
        for i in range(n):
            boundary.append((heightMap[0][i],0,i))
            boundary.append((heightMap[-1][i],m - 1,i))
            heightMap[0][i] = heightMap[-1][i] = -1
        
        heapq.heapify(boundary)

        while boundary:

            level,i,j = heapq.heappop(boundary)
            water_level = max(water_level,level)

            for a in range(4):
                x = i + directions[a]
                y = j + directions[a + 1]
                
                if x< 0 or y < 0 or x >= m or y >= n or heightMap[x][y] == -1:
                    continue

                curr_height = heightMap[x][y]
                
                if curr_height < water_level:
                    area += (water_level - curr_height)
                
                heightMap[x][y] = -1

                heapq.heappush(boundary, (curr_height,x,y))
        

        return area
                



            




        
