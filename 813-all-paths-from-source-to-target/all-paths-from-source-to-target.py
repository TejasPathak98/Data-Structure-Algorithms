class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)
 
        def dfs(x,var):
            if x == n - 1:
                ans.append(var.copy())

            if len(graph[x]) != 0:
                for neighbor in graph[x]:
                    var.append(neighbor)
                    dfs(neighbor,var)
                    var.pop()
        
        dfs(0,[0])

        return ans

            
