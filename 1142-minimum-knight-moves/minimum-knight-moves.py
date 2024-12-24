class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

        queue = deque()
        queue.append((0,0))
        dist = -1
        visited = set()
        visited.add((0,0))

        while queue:
            dist += 1
            for _ in range(len(queue)):
                a,b = queue.popleft()
                
                if a == x and b == y:
                    return dist
                
                for dx,dy in directions:
                    a_ = a + dx
                    b_ = b + dy

                    if (a_,b_) not in visited:
                        visited.add((a_,b_))
                        queue.append((a_,b_))
        
        return -1


                



        