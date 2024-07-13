class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = min_p = res = nums[0] 

        for i in range(1,len(nums)):
            if nums[i] < 0:
                max_p,min_p = min_p,max_p 

            max_p = max(max_p * nums[i],nums[i])
            min_p = min(min_p * nums[i],nums[i]) 

            res = max(res,max_p) 

        return res 
        