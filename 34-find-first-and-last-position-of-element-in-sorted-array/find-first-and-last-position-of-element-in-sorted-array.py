class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(left_bias):
            l = 0
            r = len(nums) - 1
            ans = -1

            while l <= r:

                mid = (l + r) // 2

                if nums[mid] == target:
                    ans = mid

                    if left_bias:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return ans
            
        left_pos = binarySearch(True)
        right_pos = binarySearch(False)

        return [left_pos,right_pos]