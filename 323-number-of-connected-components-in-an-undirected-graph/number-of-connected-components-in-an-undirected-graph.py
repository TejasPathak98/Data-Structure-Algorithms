class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        nodes = set()

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            nodes.add(u)
            nodes.add(v)
        

        visited = set()

        def dfs(x):
            if x in visited:
                return

            visited.add(x)

            for nei in graph[x]:
                if nei not in visited:
                    dfs(nei)

        
        count = 0

        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1

        
        return count

