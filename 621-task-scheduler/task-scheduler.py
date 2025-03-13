class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = []
        cooldown = deque()
        timer = 0

        for k,v in freq.items():
            heapq.heappush(max_heap, -v)

        while max_heap or cooldown:

            if max_heap:
                task_count = -heapq.heappop(max_heap)
                if task_count > 1:
                    cooldown.append((task_count - 1,timer + n + 1))
            
            timer += 1

            while cooldown and cooldown[0][1] == timer:
                tc , t = cooldown[0]
                cooldown.popleft()
                heappush(max_heap,-tc)
        
        return timer

        #O(klogk) ; O(k)