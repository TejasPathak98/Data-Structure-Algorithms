class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        InDegree = [0] * numCourses

        for course,pre_req in prerequisites:
            graph[pre_req].append(course)
            InDegree[course] += 1

        queue = deque()

        for i in range(numCourses):
            if InDegree[i] == 0:
                queue.append(i)


        return self.bfs(queue,graph,numCourses,InDegree)

    def bfs(self,queue,graph,numCourses,InDegree):
        courses_order = []

        while queue:
            course = queue.popleft()
            courses_order.append(course)

            for c in graph[course]:
                InDegree[c] -= 1

                if InDegree[c] == 0:
                    queue.append(c)

        if len(courses_order) == numCourses:
            return courses_order
        else:
            return []

