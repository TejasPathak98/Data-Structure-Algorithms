class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        timer = 0
        max_heap = []  # for freq of job
        cooldown = deque() # for time 
        counter = Counter(tasks)

        for k,v in counter.items():
            heappush(max_heap,-v)

        while max_heap or cooldown:

            if max_heap:
                task_count = -heappop(max_heap)
                if task_count > 1:
                    cooldown.append((task_count - 1,timer + n + 1))

            timer += 1

            while cooldown and cooldown[0][1] == timer:
                tc,t = cooldown.popleft()
                if tc >= 1:
                    heappush(max_heap,-tc)

        return timer




