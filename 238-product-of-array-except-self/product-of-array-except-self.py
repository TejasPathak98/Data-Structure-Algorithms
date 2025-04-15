class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = 1
        right_product = 1
        product = [1] * len(nums)

        for i in range(1,len(nums)):
            left_product = left_product * nums[i - 1]
            product[i] = product[i] * left_product

        for i in range(len(nums) - 2,-1,-1):
            right_product = right_product * nums[i + 1]
            product[i] = product[i] * right_product

        return product


