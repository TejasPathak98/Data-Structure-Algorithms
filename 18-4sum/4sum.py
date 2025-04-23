class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        self.helper(nums,4,target,result,[])
        return result

    def helper(self,nums,N,target,result,intermediate_results):
        if N <= 1 or len(nums) < N:
            return
        elif N == 2:
            res = self.TwoSum(nums,target)
            if res != []:
                for r in res:
                    result.append(intermediate_results + r)
        else:
            end = len(nums) - N  + 1
            for i in range(end):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                if nums[i] * N > target or nums[-1] * N < target:
                    break
                self.helper(nums[i + 1:],N - 1,target - nums[i],result,[nums[i]] + intermediate_results)

    def TwoSum(self,nums,target):
        result = []

        l = 0
        r = len(nums) - 1

        while l < r:

            Sum = nums[l] + nums[r]

            if Sum == target:
                result.append([nums[l],nums[r]])

                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                
                l += 1
                r -= 1
            elif Sum < target:
                l += 1
            else:
                r -= 1
        
        return result
        


