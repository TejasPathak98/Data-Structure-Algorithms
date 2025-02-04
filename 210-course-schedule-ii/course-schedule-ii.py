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
        
        completed_course = []

        while queue:
            course = queue.popleft()
            completed_course.append(course)
            for c in graph[course]:
                inDegree[c] -= 1
                if inDegree[c] == 0:queue.append(c)
        
        return completed_course if len(completed_course) == numCourses else []

        