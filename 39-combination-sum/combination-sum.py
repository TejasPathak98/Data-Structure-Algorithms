class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []


        def backtracking(current_sum,temp,idx):
            if current_sum > target:
                return
            
            if current_sum == target:
                ans.append(temp.copy())
                return
            

            for j in range(idx,len(candidates)):
                temp.append(candidates[j])
                backtracking(current_sum + candidates[j],temp,j)
                temp.pop()

        backtracking(0, [], 0)

        return ans
            
