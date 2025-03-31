class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Always remember parent trap in undirected graphs

        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def HasCycle(node,parent):
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in visited or HasCycle(nei, node):
                    return True
            return False
    
        if HasCycle(0,-1) == True:
            return False
        
        return len(visited) == n