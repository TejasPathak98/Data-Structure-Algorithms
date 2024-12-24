class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        missing = lambda idx : nums[idx] - nums[0] - idx

        if missing(r) < k:
            return nums[-1] + k - missing(r)
        
        while r - l > 1:
            mid = l + (r - l) // 2
            x = missing(mid)

            if x >=k:
                r = mid
            else:
                l = mid
        
        return nums[l] + k - missing(l)
        