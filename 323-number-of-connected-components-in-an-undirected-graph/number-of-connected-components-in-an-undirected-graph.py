class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        connected_components = 0
        visited = set()

        def dfs(x,visited):
            if x in visited:
                return
            
            visited.add(x)

            for nei in graph[x]:
                dfs(nei,visited)

        for i in range(n):
            if i not in visited:
                dfs(i,visited)
                connected_components += 1
        
        return connected_components