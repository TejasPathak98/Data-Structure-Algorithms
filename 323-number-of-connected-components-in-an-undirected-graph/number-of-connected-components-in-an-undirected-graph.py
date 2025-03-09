class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        count = 0
        visited = set()

        for i in range(n):
            if i not in visited:
                count += 1
                self.bfs(i,graph,visited)

        return count
        
    def bfs(self,i,graph,visited):

        queue = deque([i])
        visited.add(i)

        while queue:
            x = queue.popleft()

            for neighbor in graph[x]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    