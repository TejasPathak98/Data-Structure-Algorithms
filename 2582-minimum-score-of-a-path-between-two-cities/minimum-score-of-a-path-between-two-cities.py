class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v,distance in roads:
            graph[u].append((v,distance))
            graph[v].append((u,distance))

        
        #we just need to get the least road cost amongst all the connected componenets of 1

        min_cost = float("inf")
        visited = set()

        def dfs(node):
            nonlocal min_cost
            visited.add(node)

            for nei,distance in graph[node]:
                min_cost = min(min_cost,distance)
                if nei not in visited:
                    dfs(nei)

        dfs(1)
        return min_cost
