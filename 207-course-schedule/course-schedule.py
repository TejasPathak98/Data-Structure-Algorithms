class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for c in prerequisites:
            graph[c[1]].append(c[0])
            indegree[c[0]] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        processed_courses = 0

        while queue:
            x = queue.popleft()
            processed_courses += 1

            for y in graph[x]:
                indegree[y] -= 1
                if indegree[y] == 0:
                    queue.append(y)
        
        return processed_courses == numCourses
        



        