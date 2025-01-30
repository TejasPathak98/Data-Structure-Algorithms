class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        freq = Counter(tasks)
        heap = []
        timer = 0
        cooldown = deque()

        for k,v in freq.items():
            heapq.heappush(heap, -v)
        
        while heap or cooldown:

            if heap:
                task_count = -heapq.heappop(heap)
                if task_count > 1:
                    cooldown.append((task_count - 1,timer + n + 1))
            
            timer += 1

            while cooldown and cooldown[0][1] == timer:
                task_c , timing = cooldown[0]
                cooldown.popleft()
                heapq.heappush(heap, -task_c)
        
        return timer
        