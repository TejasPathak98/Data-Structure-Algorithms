class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        n = len(graph)


        def dfs(node,path):
            if node == n - 1:
                paths.append(path.copy())
                return



            for nei in graph[node]:
                path.append(nei)
                dfs(nei,path)
                path.pop()


        
        dfs(0,[0])
        return paths

        #

             