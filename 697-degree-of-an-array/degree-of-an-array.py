class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = Counter()
        first = {}
        last = {}

        for i in range(len(nums)):
            counter[nums[i]] += 1

            if nums[i] not in first:
                first[nums[i]] = i

            last[nums[i]] = i

        max_freq = max(counter.values())

        min_len = float('inf')

        for x,f in counter.items():
            if f == max_freq:
                min_len = min(min_len,last[x] - first[x] + 1)
        
        return min_len