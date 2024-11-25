class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        ans = 0
        self.li = set()

        def helper(x):
        
            dq = deque([x])
            
            while dq:
                y = dq.popleft()
                self.li.add(y)
                for neighbor in graph[y]:
                    if neighbor not in self.li:
                        dq.append(neighbor)
        
        for i in range(n):
            if i not in self.li:
                helper(i)
                ans += 1

        return ans
        
        
        


        



        