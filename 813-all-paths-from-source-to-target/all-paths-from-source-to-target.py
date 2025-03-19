class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        def dfs(node,temp):
            if node == len(graph) - 1:
                paths.append(temp.copy())
                return

            for neighbor in graph[node]:
                dfs(neighbor,temp + [neighbor])


        
        dfs(0,[0])
        return paths
