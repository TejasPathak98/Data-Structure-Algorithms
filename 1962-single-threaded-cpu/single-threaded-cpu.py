class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)

        tasks_with_index = [(et,pt,idx) for idx,(et,pt) in enumerate(tasks)]

        tasks_with_index.sort()

        result = []
        task_idx = 0
        task_heap = []
        timer = 0

        while len(result) < n:

            while task_idx < n and tasks_with_index[task_idx][0] <= timer:
                et,pt,idx = tasks_with_index[task_idx]
                heapq.heappush(task_heap, (pt,idx))
                task_idx += 1

            if task_heap:
                pt,idx = heapq.heappop(task_heap)
                result.append(idx)
                timer += pt
            else:
                timer = max(timer,tasks_with_index[task_idx][0])
        

        return result


