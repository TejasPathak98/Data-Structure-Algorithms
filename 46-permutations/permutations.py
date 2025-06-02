class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def backtracking(index):
            if index == n:
                result.append(nums[:])
                return

            for j in range(index,n):
                nums[index] , nums[j] = nums[j] , nums[index]
                backtracking(index + 1)
                nums[index] , nums[j] = nums[j] , nums[index]

        backtracking(0)

        return result