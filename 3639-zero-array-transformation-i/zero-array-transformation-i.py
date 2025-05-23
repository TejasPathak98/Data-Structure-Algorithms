class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for start,end in queries:
            diff[start] += 1
            if end + 1 < len(diff):
                diff[end + 1] -= 1
        
        coverage = 0
        for i in range(n):
            coverage += diff[i]
            if coverage < nums[i]:
                return False

        return True
