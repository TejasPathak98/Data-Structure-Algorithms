class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def BFS():
            queue = deque()
            queue.append(0)
            seen = set()
            parent = {}
            #seen.add(0)

            while len(queue):
                node = queue.popleft()
                seen.add(node)
                for child in graph[node]:
                    if parent.get(node) == child:continue
                    #if child in seen:return False
                    if child in parent:return False
                    parent[child] = node
                    queue.append(child)
                    
            return len(seen) == n

        def DFS():
            stack = []
            stack.append(0)
            seen = set()
            parent = {}

            while len(stack):
                node = stack.pop()
                seen.add(node)
                for child in graph[node]:
                    if parent.get(node) == child:continue
                    if child in parent:return False
                    parent[child] = node
                    stack.append(child)
            
            return len(seen) == n

        
        return BFS()

        