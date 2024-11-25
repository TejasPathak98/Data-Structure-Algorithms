class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
        onPath = [False] * n
        seen = [False] * n

        def dfs(node):
            if onPath[node]:
                return False

            if seen[node]:
                return True

            if not graph[node]:
                return node == destination

            onPath[node] = True

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    onPath[node] = False
                    return False

            onPath[node] = False
            seen[node] = True

            return True

        if destination and graph[destination]:
            return False

        return dfs(source)        