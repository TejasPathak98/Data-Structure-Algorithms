class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #DAG approach
        
        graph = defaultdict(list)
        answer = []

        for pre_req,course in prerequisites:
            graph[pre_req].append(course)
        

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

        


            




        
