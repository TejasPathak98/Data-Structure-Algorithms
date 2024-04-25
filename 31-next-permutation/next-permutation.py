class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
       i = j = len(nums) - 1 

       while i > 0 and nums[i - 1] >= nums[i]:
        i = i - 1

       if i == 0:
        nums.reverse()
        return
       
       print(nums[i-1])

       #pivot -> i - 1 

       #successor  

       while j > 0 and nums[j] <= nums[i-1]:
        j -= 1
       
       print(nums[j])


       nums[j],nums[i-1] = nums[i-1],nums[j] 

       nums[i:] = nums[len(nums) - 1:i - 1:-1] 

       return

     

        
       



        