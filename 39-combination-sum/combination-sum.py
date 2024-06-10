class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        candidates = sorted(candidates)

        def helper(candidates,result,var,index,sum):
            if sum == target:
                result.add(tuple(var))
                return
            
            elif index >= len(candidates):
                return

            elif sum > target:
                return
            
            helper(candidates, result, var + [candidates[index]], index, sum + candidates[index])
            helper(candidates, result, var, index + 1, sum)

        
        helper(candidates, result, [], 0, 0)
        return result



        