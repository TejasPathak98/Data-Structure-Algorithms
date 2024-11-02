class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        m = 0

        for i in nums:
            m = max(m,len(i))
        
        arr = [[] for _ in range(n + m - 1)]

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                arr[i + j].append(nums[i][j])
        
        ans = []
        for v in arr:
            ans.extend(v[::-1])
        
        return ans


        

        