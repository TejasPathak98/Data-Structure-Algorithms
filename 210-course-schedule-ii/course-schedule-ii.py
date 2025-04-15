class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        graph = defaultdict(list)

        for course,pre_req in prerequisites:
            graph[pre_req].append(course)
            inDegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        courses = []

        while queue:
            course = queue.popleft()
            courses.append(course)

            for nei in graph[course]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)

        
        if len(courses) == numCourses:
            return courses
        else:
            return []

        visited = []

        path = []

        def dfs(node):
            if visited[node] == 2:
                return True
            
            if visited[node] == 1:
                return False

            
            visited[node] = 1
            path.append(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visited[node] = 2
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return path


