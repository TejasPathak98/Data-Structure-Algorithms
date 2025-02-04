class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        pacific_q = deque()
        atlantic_q = deque()
        m = len(heights)
        n = len(heights[0])

        for i in range(m):
            pacific_q.append((i,0))
            atlantic_q.append((i,n - 1))
        
        for i in range(n):
            pacific_q.append((0,i))
            atlantic_q.append((m - 1,i))

        def bfs(queue):
            reachable = set()
            for x,y in queue:
                reachable.add((x,y))

            while queue:
                x,y = queue.popleft()
                

                for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                    x_ = x + dx
                    y_ = y + dy
                
                    if x_ < 0 or x_ >= m or y_ < 0 or y_ >= n:
                        continue
                    
                    if (x_,y_) in reachable:
                        continue
                    
                    if heights[x_][y_] < heights[x][y]:
                        continue
                    
                    queue.append((x_,y_))
                    reachable.add((x_,y_))
            

            return reachable
        
        p = bfs(pacific_q)
        q = bfs(atlantic_q)
        return list(p.intersection(q))

        