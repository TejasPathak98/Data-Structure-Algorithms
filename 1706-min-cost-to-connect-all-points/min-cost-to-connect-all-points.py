class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Prim's Algo
        # Here you would have to have a total cost and a cost dict
        #the cost dict is for making the choice to insert correct values in the heap 
        # the values popped out from the heap are the final MST edges
        #While the cost dict wont have the correct updated MSY weight

        n = len(points)
        min_heap = [(0,0)]
        visited = set()
        total_cost = 0
        cost_dict = {i : float("inf") for i in range(n)}
        cost_dict[0] = 0

        def helper(a,b):
            return abs(points[a][0] - points[b][0]) + abs(points[a][1] - points[b][1])

        while min_heap:
            current_cost , node = heapq.heappop(min_heap)

            if node in visited:
                continue

            total_cost += current_cost

            visited.add(node)

            for j in range(n):
                if j not in visited:
                    new_cost = helper(node,j)
                    if new_cost < cost_dict[j]:
                        cost_dict[j] = new_cost
                        heapq.heappush(min_heap, (new_cost,j))


        return total_cost
