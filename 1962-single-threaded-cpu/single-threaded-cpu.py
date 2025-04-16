class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks_with_idx = [(et,pt,idx) for idx,(et,pt) in enumerate(tasks)]
        tasks_with_idx.sort()
        result = []
        task_idx = 0
        task_heap = []
        timer = 0


        while len(result) < n:

            while task_idx < n and tasks_with_idx[task_idx][0] <= timer:
                et,pt,ind = tasks_with_idx[task_idx]
                heapq.heappush(task_heap, (pt,ind))
                task_idx += 1

            if task_heap:
                pt,ind = heapq.heappop(task_heap)
                result.append(ind)
                timer += pt
            else:
                timer = max(timer,tasks_with_idx[task_idx][0])

        return result

