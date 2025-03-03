class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        if len(nums) == 1:
            return nums[0]

        while l <=r:
            mid = (l + r) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if mid < len(nums) -1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1