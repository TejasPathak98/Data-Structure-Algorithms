class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        
        l = 0
        h = len(nums) - 1
        pos = -1

        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                pos = mid
                break
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1

        print(mid)
        
        if pos == -1:
            return [-1,-1]
        else:
            j = pos
            while j > 0 and nums[j] == nums[j - 1]:
                j -= 1
            fp = j
            i = pos
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            sp = i
            return [fp,sp]



        




        