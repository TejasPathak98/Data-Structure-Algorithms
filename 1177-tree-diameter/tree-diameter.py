class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        self.diameter = 0

        def dfs(node,parent):
            max1 = max2 = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    depth = dfs(neighbor,node)
                    if depth > max1:
                        max2 = max1
                        max1 = depth
                    elif depth > max2:
                        max2 = depth
            self.diameter = max(self.diameter,max1 + max2)
            return max1 + 1
        

        dfs(0,-1)
        return self.diameter

        


