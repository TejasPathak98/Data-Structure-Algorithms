class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        InDegree = [0] * numCourses
        graph = defaultdict(list)

        for course,pre_req in prerequisites:
            graph[pre_req].append(course)
            InDegree[course] += 1
        
        queue = deque()

        for i in range(len(InDegree)):
            if InDegree[i] == 0:
                queue.append(i)
        
        res = []

        while queue:

            x = queue.popleft()

            res.append(x)

            for nei in graph[x]:
                InDegree[nei] -= 1

                if InDegree[nei] == 0:
                    queue.append(nei)

        
        return len(res) == numCourses
