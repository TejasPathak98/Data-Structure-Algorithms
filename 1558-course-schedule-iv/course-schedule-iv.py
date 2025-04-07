class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #DAG approach
        
        graph = defaultdict(list)
        inDegree = [0] * numCourses
        answer = []

        for pre_req,course in prerequisites:
            graph[pre_req].append(course)
            inDegree[course] += 1
        

        # for idx,query in enumerate(queries):
        #     pre_req = query[0]
        #     course = query[1]

        #     queue = deque([pre_req])
        #     InDegree_copy = inDegree[:]
        #     Flag = False


        #     while queue:
        #         node = queue.popleft()

        #         if node == course:
        #             answer.append(True)
        #             Flag = True
        #             break
                
        #         for neighbor in graph[node]:
        #             InDegree_copy[neighbor] -= 1
        #             if InDegree_copy[neighbor] >= 0:
        #                 queue.append(neighbor)

        #     if Flag == False:
        #         answer.append(False)
            

        # return answer

        # answer = [False] * len(queries)

        # queue = deque()

        # if len(graph) > 0:
        #     for c in range(numCourses):
        #         if inDegree[c] == 0:
        #             queue.append(c)

        # courses = []
        # while queue:
        #     node = queue.popleft()

        #     courses.append(node)

        #     for neighbor in graph[node]:
        #         inDegree[neighbor] -= 1
        #         if inDegree[neighbor] == 0:
        #             queue.append(neighbor)

        # course_position_dict = {}

        # for idx,c in enumerate(courses):
        #     course_position_dict[c] = idx

        # for idx,query in enumerate(queries):
        #     pre_req = query[0]
        #     course = query[1]

        #     if len(course_position_dict) > 0:
        #         if course_position_dict[pre_req] < course_position_dict[course]:
        #             answer[idx] = True
        #         else:
        #             answer[idx] = False
        #     else:
        #         answer[idx] = False
        
        # return answer

        def dfs(course,target_course,visited):
            if course == target_course:
                return True

            if course in visited:
                return

            visited.add(course)
            
            for nei in graph[course]:
                if nei not in visited:
                    if dfs(nei,target_course,visited):
                        return True
            
            return False


        for idx,query in enumerate(queries):
            pre_req = query[0]
            course = query[1]

            if dfs(pre_req,course,set()):
                answer.append(True)
            else:
                answer.append(False)

        return answer

        


            




        
