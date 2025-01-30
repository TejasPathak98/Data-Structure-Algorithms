class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def helper(start ,curr_sum,temp):
            if curr_sum == target:
                ans.append(temp.copy())
                return
            
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i- 1]:
                    continue
                if curr_sum + candidates[i] > target:
                    break
                
                temp.append(candidates[i])
                helper(i + 1,curr_sum + candidates[i],temp)
                temp.pop()

        helper(0,0,[])   
        return ans
        