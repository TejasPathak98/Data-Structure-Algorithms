class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_freq = max(counter.values())

        max_freq_count = 0

        for key,value in counter.items():
            if value == max_freq:
                max_freq_count += 1

        return max(len(tasks),(max_freq - 1)*(n + 1) + max_freq_count)



