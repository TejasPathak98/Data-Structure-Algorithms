class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        my_dict = defaultdict(list)
        indegree = [0] * numCourses
        for course,pre_req in prerequisites:
            my_dict[pre_req].append(course)
            indegree[course] += 1
        
        ans = []
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            c = queue.popleft()
            ans.append(c)
            print(ans)
            for neighbor in my_dict[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(ans) == numCourses:
            return ans
        else:
            return []
        


