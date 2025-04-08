class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        self.visited = set()

        def dfs(node,nodes_edges):
            self.visited.add(node)

            nodes_edges[0] += 1
            nodes_edges[1] += len(graph[node])

            for nei in graph[node]:
                if nei not in self.visited:
                    dfs(nei,nodes_edges)
        
        count = 0

        for i in range(n):
            if i not in self.visited:
                nodes_edges = [0,0]
                dfs(i,nodes_edges)
                nodes, edges = nodes_edges

                if edges // 2 == (nodes * (nodes - 1)) // 2:
                    count += 1

        
        return count


        
