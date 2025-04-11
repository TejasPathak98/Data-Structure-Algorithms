class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        #the number of nodes(nodes - 1) // 2 should be equal to the number of edges 
        
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)


        visited = set()

        def dfs(node,node_and_edge):
            visited.add(node)

            node_and_edge[0] += 1
            node_and_edge[1] += len(graph[node])

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei,node_and_edge)

        count = 0

        for i in range(n):
            if i not in visited:
                node_and_edge = [0,0]
                dfs(i,node_and_edge)

                nodes = node_and_edge[0]
                edges = node_and_edge[1]

                if edges // 2 == nodes*(nodes - 1) // 2:
                    count += 1


        return count 
