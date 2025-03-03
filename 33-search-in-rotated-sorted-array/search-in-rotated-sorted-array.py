class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] == target:return 0
            else:return -1
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target and nums[mid] >= nums[0]:
                if target >= nums[0]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] > target and nums[mid] < nums[0]:
                r = mid - 1
            elif nums[mid] < target and nums[mid] >= nums[0]:
                l = mid + 1
            elif nums[mid] < target and nums[mid] < nums[0]:
                if target >= nums[0]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1
        