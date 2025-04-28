class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        result = []

        def backtracking(index):
            if index == n:
                result.append(nums[:])
                return
            
            for j in range(index,len(nums)):
                nums[j] , nums[index] = nums[index] , nums[j]
                backtracking(index + 1)
                nums[j] , nums[index] = nums[index] , nums[j]

        
        backtracking(0)
        return result


