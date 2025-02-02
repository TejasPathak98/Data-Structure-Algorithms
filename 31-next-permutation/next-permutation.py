class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            return
        
        i = len(nums) - 1

        while i >= 1:
            if nums[i - 1] >= nums[i]:
                i -= 1
            else:
                pos = i - 1
                break
        
        if i == 0 and nums[0] >= nums[1]:
            nums.reverse()
            return None

        for j in range(len(nums) - 1,i - 1,-1):
            if nums[j] <= nums[pos]:
                continue
            else:
                nums[j] , nums[pos] = nums[pos] , nums[j]
                break

        nums[pos + 1:] = sorted(nums[pos + 1:])




        

            
        