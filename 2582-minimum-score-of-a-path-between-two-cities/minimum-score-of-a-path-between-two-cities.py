class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        min_distance = float("inf")

        # def dfs(node,temp,visited,dist):
        #     nonlocal min_distance

        #     if node == n:
        #         print("Break",dist)
        #         temp.append(dist)
        #         tp = temp.copy()
        #         min_distance = min(min_distance,min(tp))
        #         return
            
        #     if node in visited:
        #         return
            
        #     visited.add(node)
        #     temp.append(dist)

        #     for neighbor,d in graph[node]:
        #         dfs(neighbor,temp,visited,d)
        
        # dfs(1,[],set(),10 ** 4 + 1)

        # return min_distance

        visited_edges = set()

        def dfs(node):
            nonlocal min_distance
            
            for neighbor,d in graph[node]:
                edge = tuple(sorted([node,neighbor]))
                
                if edge in visited_edges:
                    continue

                visited_edges.add(edge)

                min_distance = min(min_distance,d)

                if min_distance == 1:
                    return
                
                dfs(neighbor)
        
        dfs(1)
        return min_distance

            




        return min_distance
