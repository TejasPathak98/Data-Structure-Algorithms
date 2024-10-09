class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        m = 0
        for i in nums:
            m = max(m,len(i))
        ans = [[] for i in range(n + m - 1)]

        for i in range(n):
            for j in range(len(nums[i])):
                ans[i + j].append(nums[i][j])
        
        sol = []

        for v in ans:
            for j in range(len(v) - 1,-1,-1):
                sol.append(v[j])
        
        return sol
        