class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        l = 0
        h = n - 1

        while l < h:
            mid = (l + h) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                h = mid - 1
        
        return l
        