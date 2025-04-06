class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #Sliding window approach

        l = 0
        total_sum = 0
        res = 0

        nums.sort() # Very important to sort the nums

        for r in range(len(nums)):
            total_sum += nums[r]

            if nums[r] * (r - l + 1) - total_sum > k:
                total_sum -= nums[l]
                l += 1
            
            res = max(res, r - l + 1)
        

        return res