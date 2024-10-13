class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        c = Counter(nums)

        return heapq.nlargest(k, c.keys(),key = c.get)
        