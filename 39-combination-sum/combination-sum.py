class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < min(candidates):
            return []
        
        ans = []
        
        def helper(x,temp):
            if sum(temp) > target:
                return

            if sum(temp) == target:
                #ans.add(tuple(sorted(temp.copy())))
                ans.append(temp.copy())
                return
            
            for i in range(x,len(candidates)):
                temp.append(candidates[i])
                helper(i,temp)
                temp.pop()

        helper(0,[])
        return ans
        