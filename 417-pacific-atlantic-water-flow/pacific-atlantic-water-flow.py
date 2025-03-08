class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        visited_p = set()
        visited_a = set()

        pacific_queue = deque()
        atlantic_queue = deque()

        for i in range(m):
            pacific_queue.append((i,0))
            atlantic_queue.append((i,n - 1))
            visited_p.add((i,0))
            visited_a.add((i,n - 1))

        for j in range(n):
            pacific_queue.append((0,j))
            atlantic_queue.append((m - 1,j))
            visited_p.add((0,j))
            visited_a.add((m - 1,j))
        
        pacific_set = self.bfs(pacific_queue,heights,visited_p)
        atlantic_set = self.bfs(atlantic_queue,heights,visited_a)
        return list(pacific_set & atlantic_set)

    
    def bfs(self,queue,heights,visited):
        while queue:
            x,y = queue.popleft()

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x_ = x + dx
                y_ = y + dy
                
                print(x_,y_)
                if x_ >=0 and x_ < len(heights) and y_ >=0 and y_ < len(heights[0]) and heights[x_][y_] >= heights[x][y] and (x_,y_) not in visited:
                    queue.append((x_,y_))
                    visited.add((x_,y_))
        
        return visited

    #O(MN) ;O(MN)


