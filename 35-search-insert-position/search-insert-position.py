class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l = 0
        h = n - 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        
        return l
        