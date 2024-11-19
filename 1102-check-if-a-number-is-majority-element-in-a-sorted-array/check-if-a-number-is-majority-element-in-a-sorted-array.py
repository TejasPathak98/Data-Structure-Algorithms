class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if nums.count(target) > n / 2:
            return True
        else:
            return False
        