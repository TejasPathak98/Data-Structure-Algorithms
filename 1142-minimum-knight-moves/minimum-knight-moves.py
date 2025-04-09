class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        #BFS approach

        queue = deque([(0,0)])
        visited = set()
        visited.add((0,0))

        x = abs(x) # taking advantage of symmetry we only search in the 1st Quadrant
        y = abs(y)

        steps = 0

        while queue:
            
            for _ in range(len(queue)):
                r , c = queue.popleft()

                if r == x and c == y:
                    return steps
                
                for dr,dc in [(1,2),(2,1),(-1,2),(-2,1),(-1,-2),(-2,-1),(1,-2),(2,-1)]:
                    r_ = r + dr
                    c_ = c + dc

                    if (r_,c_) not in visited and r_ >= -2 and c_ >= -2 and r_ <= x + 2 and  c_ <= y + 2:
                        visited.add((r_,c_))
                        queue.append((r_,c_))

            steps += 1
        

        return -1
                    



            