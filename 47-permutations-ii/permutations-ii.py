class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] *  len(nums)
        
        nums.sort()

        def backtrack(temp):
            if len(temp) == len(nums):
                res.append(temp.copy())
                return 
            
            if len(temp) > len(nums):
                return
            

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                

                temp.append(nums[i])
                used[i] = True
                backtrack(temp)
                used[i] = False
                temp.pop()
        

        backtrack([])
        return res