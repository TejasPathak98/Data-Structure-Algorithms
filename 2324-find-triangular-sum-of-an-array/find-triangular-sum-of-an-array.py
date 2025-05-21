class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        coeff = 1
        result = 0
        n = len(nums)

        for i in range(n):
            result  = (result + coeff*nums[i]) % 10 #C(n - 1,0)

            #update it to C(n - 1,i + 1)
            coeff = coeff * (n - 1 - i) // (i + 1) 

        return result

        #C(n,k + 1) = C(n,k) * ((n - k) / (k + 1))