class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = [-1] * (n + 1)

        def dfs(person,c):

            if color[person] == -1:
                color[person] = c

            for nei in graph[person]:
                if color[nei] == c:
                    return False
                elif color[nei] == -1:
                    if not dfs(nei,1 - c):
                        return False

            return True

        for i in range(1,n + 1):
            if color[i] == -1:
                if not dfs(i,0):
                    return False

        
        return True