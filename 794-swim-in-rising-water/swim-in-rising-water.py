class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #This is Dijsktra problem because the weights are implicit, we are finding the most optimal at very step

        min_heap = [(grid[0][0],0,0)]
        visited = set([0,0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        n = len(grid)

        while min_heap:
            t , x, y = heapq.heappop(min_heap)

            if x == n - 1 and y == n - 1:
                return t
            
            for dx,dy in directions:
                x_ = x + dx
                y_= y + dy

                if 0 <= x_ < n and 0 <= y_ < n and (x_,y_) not in visited:
                    new_t= max(t,grid[x_][y_])
                    heapq.heappush(min_heap, (new_t,x_,y_))
                    visited.add((x_,y_))

        
        return -1


    

            

