class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < min(candidates):
            return []
        
        ans = set()
        
        def helper(temp):
            if sum(temp) > target:
                return

            if sum(temp) == target:
                ans.add(tuple(sorted(temp.copy())))
                return
            
            for i in range(len(candidates)):
                temp.append(candidates[i])
                helper(temp)
                temp.pop()

        helper([])
        return list(ans)
        