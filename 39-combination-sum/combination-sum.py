class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return [] 
        
        ans = []

        candidates.sort()

        def helper(current_sum,index,list):
            if current_sum > target:
                return 
            elif current_sum == target:
                ans.append(list)
                return 
            else:
                for i in range(index,len(candidates)):
                    if current_sum + candidates[i] > target:
                        return 
                    helper(current_sum + candidates[i],i,list + [candidates[i]])
                
        helper(0,0,[])
        return ans
        