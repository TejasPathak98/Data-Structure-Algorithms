class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course,pre_req in prerequisites:
            adj_list[pre_req].append(course)
            indegree[course] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        processed_courses = 0

        while queue:
            p_course = queue.popleft()
            processed_courses += 1

            for nei in adj_list[p_course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return processed_courses == numCourses 



        