class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 0:
            return False
        if n == 1:
            if nums[0] != target:
                return False 
            else:
                return True
        
        l = 0
        h = n - 1
        lb = -1
        rb = -1

        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                lb = mid
                h = mid - 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1

        l = 0
        h = n - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                rb = mid
                l = mid + 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1

        if (rb - lb + 1) > n /2:
            return True
        else:
            return False
        

