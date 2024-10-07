class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        if len(nums) == 2:
            if sum(nums)  % k == 0:
                return True
            else:
                return False
        
        remainder_map = {0:-1}
        cs_sum = 0

        for i in range(len(nums)):
            cs_sum += nums[i]

            cs_sum = cs_sum % k

            if cs_sum in remainder_map:
                if i - remainder_map[cs_sum] > 1:
                    return True
            else:
                remainder_map[cs_sum] = i 
        

        return False
