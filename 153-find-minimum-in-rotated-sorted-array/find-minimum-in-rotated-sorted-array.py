class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] >= nums[h]: #left half is sorted (We use h instead of 0 so that window is dynamic)
                l = mid + 1
            else:
                h = mid
        
        return nums[h]