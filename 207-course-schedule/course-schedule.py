class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        
        return len(courses) == numCourses

