class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        InDegree = [0] * numCourses

        for pre_req,course in prerequisites:
            graph[pre_req].append(course)
            InDegree[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if InDegree[course] == 0:
                queue.append(course)
        
        return self.topological_sort(graph,queue,numCourses,InDegree)

    def topological_sort(self,graph,queue,numCourses,InDegree):
        courses_done = []

        while queue:
            course = queue.popleft()
            courses_done.append(course)

            for related_course in graph[course]:
                InDegree[related_course] -= 1

                if InDegree[related_course] == 0:
                    queue.append(related_course)

        
        return len(courses_done) == numCourses