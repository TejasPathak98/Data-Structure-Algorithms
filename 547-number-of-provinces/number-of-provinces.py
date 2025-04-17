class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    graph[i].append(j)
                    graph[j].append(i)
        
        count = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in graph[node]:
                dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        
        return count

