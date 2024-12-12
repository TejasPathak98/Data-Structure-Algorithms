class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        inc = True
        for i in range(len(nums) - 1):
            if inc != (nums[i] <= nums[i + 1]):
                nums[i] , nums[i + 1] = nums[i + 1] , nums[i]
            inc = not inc
            
