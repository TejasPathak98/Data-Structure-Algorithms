class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float("-inf")
        temp_prod_2 = 1
        tp = 1

        for i in range(len(nums)):
            temp_prod_2 *= nums[i]
            max_product = max(max_product,temp_prod_2)
            if temp_prod_2 == 0:
                temp_prod_2 = 1
        
        for i in range(len(nums) - 1,-1,-1):
            tp *= nums[i]
            max_product = max(max_product,tp)
            if tp == 0:
                tp = 1
        
        return max_product
            
        # O(N) ; O(1)
        