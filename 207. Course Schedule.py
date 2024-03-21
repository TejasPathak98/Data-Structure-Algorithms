class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])
        
        visited = [-1] * numCourses

        def helper(x):
            visited[x] = 0
            ans = 1

            for i in graph[x]:
                if visited[i] == -1:
                    ans = ans & helper(i)
                else:
                    ans = ans & visited[i]      
            if ans == 1:
                visited[x] = 1 
                return 1 
            else:
                visited[x] = 0 
                return 0

        for i in range(numCourses):
            if visited[i] == -1:
                if helper(i) == 0:
                    return False 
        
        return True

        
        