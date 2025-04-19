class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        self.helper(nums,target,4,result,[])
        return result

    def helper(self,nums,target,N,result,intermediate_results):
        if N < 2 or len(nums) < N:
            return
        
        elif N == 2:
            res = self.TwoSum(nums,target)
            if res != []:
                for arr in res:
                    result.append(intermediate_results + arr)
        
        else:

            for i in range(len(nums) - N  + 1):
                if nums[i] * N > target or nums[-1] * N < target:
                    break
                elif i == 0 or nums[i] != nums[i - 1]:
                    self.helper(nums[i + 1:], target - nums[i], N - 1, result, [nums[i]] + intermediate_results)
        

    
    def TwoSum(self,nums,target):
        l = 0
        r = len(nums) - 1
        result = []

        while l < r:

            if nums[l] + nums[r] == target:
                result.append([nums[l],nums[r]])
            
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1

                l += 1
                r -= 1
            
            elif nums[l] + nums[r] < target:

                l += 1
            else:

                r -= 1
        
        return result






