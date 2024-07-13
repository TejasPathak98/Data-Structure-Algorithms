class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_prd = min_prd = res = nums[0]

        for i in range(1,len(nums)):
            if nums[i] < 0:
                max_prd,min_prd = min_prd,max_prd 

            max_prd = max(nums[i],nums[i] * max_prd)
            min_prd = min(nums[i],nums[i]*min_prd) 

            res = max(res,max_prd) 
        
        return res
        