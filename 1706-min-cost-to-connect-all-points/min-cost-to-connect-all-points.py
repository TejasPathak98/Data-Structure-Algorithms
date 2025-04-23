class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def helper(i,j):
            x = points[i]
            y = points[j]
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        
        n = len(points)
        cost_dict = [float('inf')] * n
        cost_dict[0] = 0
        min_heap = [(0,0)]
        heapify(min_heap)
        visited = set()


        while len(visited) < n:
            cost,idx = heappop(min_heap)

            visited.add(idx)

            if cost > cost_dict[idx]:
                continue
            
            for j in range(n):
                if j != idx and j not in visited:
                    new_cost = helper(idx,j)
                    if new_cost < cost_dict[j]:
                        cost_dict[j] = new_cost
                        heappush(min_heap,(new_cost,j))

        
        return sum(cost_dict)

