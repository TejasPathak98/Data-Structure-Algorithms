class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     graph = defaultdict(list)
    #     InDegree = [0] * numCourses

    #     for course,pre_req in prerequisites:
    #         graph[pre_req].append(course)
    #         InDegree[course] += 1
        
    #     queue = deque()
    #     for course in range(numCourses):
    #         if InDegree[course] == 0:
    #             queue.append(course)
        
    #     return self.topological_sort(graph,queue,numCourses,InDegree)

    # def topological_sort(self,graph,queue,numCourses,InDegree):
    #     courses_done = []

    #     while queue:
    #         course = queue.popleft()
    #         courses_done.append(course)

    #         for related_course in graph[course]:
    #             InDegree[related_course] -= 1

    #             if InDegree[related_course] == 0:
    #                 queue.append(related_course)

        
    #     return len(courses_done) == numCourses

    # #o(V + E) ; O(V + E)...for graph + queue


        graph = defaultdict(list)
        for course,pre_req in prerequisites:
            graph[course].append(pre_req)

        visited = [0] * numCourses # 1 is visiting, 2 is visited , 0 is un visited


        def hasCycle(course):
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False

            
            visited[course] = 1
            for pre_req in graph[course]:
                if hasCycle(pre_req):
                    return True
            visited[course] = 2
            return False

        
        for course in range(numCourses):
            if hasCycle(course):
                return False
        return True




