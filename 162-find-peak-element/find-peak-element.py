class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1

        if len(nums) == 1:
            return 0

        while l < h: #(not l <=h becauase we want mid + 1 to be valid)
            mid = (l + h) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]: #The peak element must exist on the right side
                l = mid + 1
            else: #the peak element must exist on left side
                h = mid
        
        return l #because in case of strictly increasing arr l will point to last element and in opposite case the first element
