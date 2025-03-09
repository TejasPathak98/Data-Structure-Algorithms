class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def hasCycle(node,parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited or hasCycle(neighbor, node):
                    return True
            return False

        
        if hasCycle(0,-1) == True:
            return False
        
        return len(visited) == n
