class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_product = 1
        right_product = 1
        res = [1] * n

        for i in range(1,n):
            res[i] = left_product * nums[i - 1]
            left_product = left_product * nums[i - 1]

        for i in range(n - 1,-1,-1):
            res[i] = res[i] * right_product
            right_product = right_product * nums[i]
        
        return res

        