class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        m = 0

        for i in range(n):
            m = max(m,len(nums[i]))
        ans = [[] for _ in range(n + m - 1)]

        for i in range(n):
            for j in range(len(nums[i])):
                ans[i + j].append(nums[i][j])
        
        sol = []

        for v in ans:
            sol.extend(v[::-1])
        
        return sol

        