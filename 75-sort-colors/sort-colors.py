class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p1 = 0
        p2 = len(nums) - 1
        idx = 0

        while idx <= p2:
            if nums[idx] == 0:
                nums[idx] = nums[p1]
                nums[p1] = 0
                p1 += 1
            elif nums[idx] == 2:
                nums[idx] = nums[p2]
                nums[p2] = 2
                p2 -= 1
                idx -=1
            idx += 1
        