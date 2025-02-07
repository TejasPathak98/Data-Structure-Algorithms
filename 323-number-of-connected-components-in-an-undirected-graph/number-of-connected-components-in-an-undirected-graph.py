class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cc = 0
        visited = set()
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(x):
            visited.add(x)
            for neighbor in graph[x]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                cc += 1
        
        return cc
        





        