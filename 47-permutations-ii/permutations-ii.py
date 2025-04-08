class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)
        nums.sort()

        def backtrack(temp):
            if len(temp) == len(nums):
                ans.append(temp.copy())
                return
            
            if len(temp) > len(nums):
                return

            for i in range(len(nums)):
                if used[i]: #the element nums[i] has already been used in our permutation path(we dont care about its location in the path, only that it exists)
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue #because if we dont skip then that element will become part of the path, where the same path was done before using the nums[i - 1] element , so its a repeat

                used[i] = True
                temp.append(nums[i])
                backtrack(temp)
                used[i] = False
                temp.pop()

        
        backtrack([])
        return ans
