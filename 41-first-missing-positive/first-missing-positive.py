class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        #the key idea here is that we only care about the numbers from range [1,n +1] as n is the length and if all numbers from 1 to N are present then N+1 is our greatest possible answer
        #so we re-arrange elements so that for any index i has number i + 1 and then check where this condition breaks

        # n = len(nums)

        # for i in range(n): 
        #     while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
        #         nums[i] , nums[nums[i] - 1] = nums[nums[i] - 1] , nums[i]
            
        # for i in range(n):
        #     if nums[i] != i + 1:
        #         return i + 1

        # return n + 1 


        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        
        n = len(nums)
        
        # Place each positive integer i at index i-1 if possible
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)
        
        # Find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positive integers from 1 to n are present, return n + 1
        return n + 1
