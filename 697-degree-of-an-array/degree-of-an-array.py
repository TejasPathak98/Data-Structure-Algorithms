class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter()
        first = {}
        last = {}

        for i in range(len(nums)):
            count[nums[i]] += 1

            if nums[i] not in first:
                first[nums[i]] = i
            
            last[nums[i]] = i
        
        max_freq = max(count.values())

        return min((last[x] - first[x] + 1) for x,fre in count.items() if fre == max_freq)

