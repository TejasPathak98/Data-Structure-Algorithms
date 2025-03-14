class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = set() 

        def helper(temp,i):
            if sum(temp) > target:
                return
            
            if sum(temp) == target:
                ans.add(tuple(temp.copy()))
                return
            
            for j in range(i,n):
                temp.append(candidates[j])
                
                helper(temp,j + 1)

                helper(temp,j)

                temp.pop()
                

        helper([],0)
        return list(ans)