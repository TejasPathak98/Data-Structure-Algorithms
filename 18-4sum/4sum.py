class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        self.helper(nums,results,4,target,[])
        return results

    def helper(self,nums,results,N,target,intermediate_res):
        if N < 2 or len(nums) < N:
            return
        
        elif N == 2:
            output_res = self.TwoSum(nums,target)
            if output_res != []:
                for idx in output_res:
                    results.append(intermediate_res + idx)
        
        else:
            for i in range(len(nums) - N + 1):
                if nums[i] * N > target or nums[-1] * N < target:
                    break
                elif i == 0 or nums[i] != nums[i - 1]:
                    self.helper(nums[i + 1:], results, N - 1, target - nums[i], [nums[i]] +  intermediate_res)

    def TwoSum(self,nums,target):
        res = []
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                res.append([nums[left],nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1

            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        
        return res

        


        