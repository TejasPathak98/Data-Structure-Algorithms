class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        i = len(nums) - 2

        while i >= 0:
            if nums[i] >= nums[i + 1]:
                i -= 1
            else:
                break
        
        

        j = len(nums) - 1
        if i >= 0:
            while j > i:
                if nums[i] >= nums[j]:
                    j -= 1
                else:
                    break
        
         

        nums[i] , nums[j] = nums[j] , nums[i]

        nums[i + 1:] = reversed(nums[i + 1:])