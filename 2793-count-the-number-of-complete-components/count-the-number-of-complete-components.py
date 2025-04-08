class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        #the key idea is that every subgraph with k nodes will have k*(k  - 1) / 2 edges

        graph = defaultdict(list)
        count_complete_components = 0

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                edges_count = 0
                nodes = 0

                queue = deque([i])
                visited[i] = True

                while queue:
                    node = queue.popleft()

                    nodes += 1
                    edges_count += len(graph[node])

                    for nei in graph[node]:
                        if not visited[nei]:
                            visited[nei] = True
                            queue.append(nei)

                
                if edges_count // 2 == (nodes * (nodes - 1)) // 2:
                    count_complete_components += 1

        

        return count_complete_components


                

            
