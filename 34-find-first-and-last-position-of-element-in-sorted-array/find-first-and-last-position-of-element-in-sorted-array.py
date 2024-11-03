class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        
        ans = [-1,-1]
        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = (l + h) // 2
            if target == nums[mid]:
                ans[0] = mid
                h = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                h = mid - 1

        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = (l + h) // 2
            if target == nums[mid]:
                ans[1] = mid
                l = mid + 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                h = mid - 1
        
        return ans