class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        
        left_pos = -1
        right_pos = -1
        
        def left_search():
            nonlocal left_pos
            l = 0
            h = len(nums) - 1
            while l <= h:
                mid = (l + h) // 2
                if nums[mid] == target:
                    left_pos = mid
                    h = mid - 1 
                elif nums[mid] > target:
                    h = mid - 1
                else:
                    l = mid + 1
            return left_pos
        
        def right_search():
            nonlocal right_pos
            l = 0
            h = len(nums) - 1
            while l <= h:
                mid = (l + h) // 2
                if nums[mid] == target:
                    right_pos = mid
                    l = mid + 1
                elif nums[mid] > target:
                    h = mid - 1
                else:
                    l = mid + 1
            return right_pos

        left_search()
        right_search()
        return [left_pos,right_pos]
        


        
        



        




        