from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        
        obstacles = SortedList()
        result = []
        max_x = max(q[1] for q in queries)
        Segment_Tree = SegTree(max_x)

        obstacles.add(0)
        Segment_Tree.update(0,0)

        for q in queries:
            if q[0] == 1:

                obstacle_value = q[1]
                position_in_obstacles = obstacles.bisect(obstacle_value)

                if position_in_obstacles < len(obstacles):
                    nxt = obstacles[position_in_obstacles]
                    Segment_Tree.update(nxt,nxt - obstacle_value)
                
                prev = obstacles[position_in_obstacles - 1]
                Segment_Tree.update(obstacle_value,obstacle_value - prev)

                obstacles.add(obstacle_value)
            else:
                x = q[1]
                sz = q[2]
                max_gap = 0

                if sz > x:
                    result.append(False)
                    continue

                position_in_obstacles = obstacles.bisect(x)
                prev = obstacles[position_in_obstacles - 1]

                max_gap = max(x - prev,Segment_Tree.query(prev))

                result.append(max_gap >= sz)
        
        return result

    
class SegTree:

    def __init__(self,size):
        self.n = 1 << (size.bit_length())
        self.tree = [0] * (2*self.n)

    def update(self,index,value):
        index += self.n
        self.tree[index] = value

        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[index*2],self.tree[index*2 + 1])
    

    def query(self,index):
        index += self.n
        res = self.tree[index]

        while index > 1:
            if index % 2 == 1:
                res = max(res,self.tree[index - 1])
            index //= 2
        
        return res
        

#The segment tree is mapped to 0.....max_x (the whole set of possible values so we pass the obstacle value itseld and not hte index)



                
