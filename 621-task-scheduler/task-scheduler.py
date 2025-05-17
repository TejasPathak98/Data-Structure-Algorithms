class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        cooldown = deque()

        heap = []

        for task,freq in counter.items():
            heapq.heappush(heap,-freq)

        
        timer = 0
        

        while heap or cooldown:

            if heap:
                freq = -heappop(heap)

                if freq > 1:
                    cooldown.append((timer + n + 1,freq - 1))
                
            
            timer += 1


            while cooldown and cooldown[0][0] <= timer:
                _,freq = cooldown.popleft()
                if freq >= 1:
                    heappush(heap, -freq)

        
        return timer





