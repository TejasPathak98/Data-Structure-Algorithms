class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        right = 0
        curr_product = 1

        while right < len(nums):

            curr_product = curr_product * nums[right]

            if curr_product < k:
                count += (right - left) + 1
            else:
                while left <= right and curr_product >= k:
                    curr_product = curr_product // nums[left]
                    left += 1
                
                count += (right - left) + 1
                
            right += 1
        

        return count

