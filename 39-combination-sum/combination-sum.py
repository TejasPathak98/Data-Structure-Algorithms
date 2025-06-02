class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtracking(curr_sum,temp,index):
            if curr_sum == target:
                result.append(temp.copy())
                return
            
            if curr_sum > target:
                return
            
            for j in range(index,len(nums)):
                if curr_sum + nums[j] > target:
                    continue
                
                temp.append(nums[j])
                backtracking(curr_sum + nums[j],temp,j)
                temp.pop()

        
        backtracking(0,[],0)

        return result