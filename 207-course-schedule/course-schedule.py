class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * (numCourses)
        graph = defaultdict(list)

        for course,pre_req in prerequisites:
            graph[pre_req].append(course)
            inDegree[course] += 1
        
        queue = deque()
        completed_courses = []

        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
                
        while queue:
            course = queue.popleft()
            completed_courses.append(course)

            for c in graph[course]:
                inDegree[c] -= 1
                if inDegree[c] == 0:
                    queue.append(c)
        
        return len(completed_courses) == numCourses 

        
