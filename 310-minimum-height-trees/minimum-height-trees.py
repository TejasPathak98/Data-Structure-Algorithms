class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1 or not edges:
            return [0]
        
        ans = []

        graph = collections.defaultdict(set) 

        for u,v in edges:
            graph[u].add(v) 
            graph[v].add(u) 

        for label,child in graph.items():
            if len(child) == 1:
                ans.append(label) 
        

        while n > 2:
            n = n - len(ans) 
            leaves = [] 
            for leaf in ans:
                u = next(iter(graph[leaf]))
                graph[u].remove(leaf) 
                if len(graph[u]) == 1:
                    leaves.append(u) 
            ans = leaves 
        
        return ans
        