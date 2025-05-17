class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n  = len(nums)

        def swap(i,j):
            nums[i] , nums[j] = nums[j] , nums[i]
        

        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i]  - 1]:
                swap(i,nums[i] - 1)
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

        