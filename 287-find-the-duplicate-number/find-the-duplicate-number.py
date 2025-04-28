class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)

        def swap(i,j):
            nums[i],nums[j] = nums[j],nums[i]

        for i in range(n):
            while 0 < nums[i] <= n - 1 and nums[i] != nums[nums[i] - 1]:
                 swap(i,nums[i] - 1)

        
        for i in range(n):
            if i + 1 != nums[i]:
                return nums[i]

        
        return -1
            

        