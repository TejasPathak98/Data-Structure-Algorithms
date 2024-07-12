class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums) 
        arr = [1] * n 

        left_product =  1
        right_product = 1

        for i in range(0,n):
            arr[i] = left_product
            left_product = left_product * nums[i]
        
        print(arr)

        for i in range(n - 1,-1, -1):
            arr[i] = arr[i] * right_product
            right_product = right_product * nums[i]

        return arr
            


        