class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # freq_counter = Counter(tasks)
        # max_heap = []
        # cooldown = deque()
        # timer = 0

        # for k,v in freq_counter.items():
        #     heapq.heappush(max_heap, -v)

        # while max_heap or cooldown:

        #     if max_heap:
        #         f = -heapq.heappop(max_heap)

        #         if f > 1:
        #             cooldown.append((f - 1,timer + n + 1))

        #     timer += 1

        #     while cooldown and cooldown[0][1] == timer:
        #         task_c, time = cooldown.popleft()
        #         heapq.heappush(max_heap, -task_c)

        
        # return timer

        #O(klogk) ; o(k)

        counter = Counter(tasks)
        max_freq = max(counter.values())
        max_freq_items = sum(1 for item in counter.values() if item == max_freq)
        return max(len(tasks),(max_freq - 1)*(n + 1) + max_freq_items)







