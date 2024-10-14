class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        h = n - 1

        while l <= h:
            mid = (l + h) // 2

            if target == nums[mid]:
                return mid 
            elif target > nums[mid]:
                l = mid + 1
            else:
                h = mid - 1
        
        return -1