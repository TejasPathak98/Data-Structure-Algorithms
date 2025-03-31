class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = [0] * numCourses

        for course,pre_req in prerequisites:
            graph[pre_req].append(course)
            inDegree[course] += 1

        visited = [0] * numCourses # 0 for unvisited , 1 for visiting , 2 and for visited

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            
            visited[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            visited[node] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

            