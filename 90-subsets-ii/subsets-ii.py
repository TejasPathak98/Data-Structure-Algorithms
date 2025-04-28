class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        result = []

        def backtracking(temp,index):

            result.append(temp[:])

            
            for j in range(index,len(nums)):
                if j > index and nums[j] == nums[j - 1]:
                    continue
                temp.append(nums[j])
                backtracking(temp, j + 1)
                temp.pop()

        
        backtracking([], 0)
        return result

            

