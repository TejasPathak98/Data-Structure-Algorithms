class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtracking(temp,current_sum,idx):
            if current_sum > target:
                return
            
            if current_sum == target:
                ans.append(temp.copy())
                return
            
            for j in range(idx,len(candidates)):
                if candidates[j] == candidates[j - 1] and j > idx:
                    continue
                if current_sum + candidates[j] > target:
                    break
                temp.append(candidates[j])
                backtracking(temp, current_sum + candidates[j], j + 1)
                temp.pop()

        backtracking([], 0, 0)
        return ans

