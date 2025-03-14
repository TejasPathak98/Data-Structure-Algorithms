class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # #candidates = list(set(candidates))
        # candidates = sorted(candidates)
        # n = len(candidates)
        # ans = set()

        # def helper(temp,i,current_sum):
        #     if current_sum > target:
        #         return
            
        #     if current_sum == target:
        #         ans.add(tuple(temp[:]))
        #         return
            
        #     if i >= n:
        #         return
            
        #     temp.append(candidates[i])
        #     helper(temp,i + 1,current_sum + candidates[i])

        #     temp.pop()
        #     helper(temp,i + 1,current_sum)
        

        # helper([],0,0)
        # return list(ans)

        #this(above) gives TLE 

        # candidates = sorted(candidates)
        # n = len(candidates)
        # ans = set()

        # def helper(temp,i,current_sum):
        #     if current_sum > target:
        #         return
            
        #     if current_sum == target:
        #         ans.add(tuple(temp[:]))
        #         return
            
        #     for j in range(i,n):
        #         if current_sum + candidates[j] > target:
        #             return
        #         temp.append(candidates[j])
        #         helper(temp,j + 1,current_sum + candidates[j])
        #         temp.pop()
        #         helper(temp,j + 1,current_sum)  # this call is redudant because the  loop handles it implicitly

            
        # helper([],0,0,)
        # return list(ans)


        candidates = sorted(candidates)
        n = len(candidates)

        ans = []

        def helper(temp,i,current_sum):            
            if current_sum == target:
                ans.append(temp[:])
                return  
            
            for j in range(i,n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if current_sum + candidates[j] > target:
                    break
                temp.append(candidates[j])
                helper(temp,j + 1,current_sum + candidates[j])
                temp.pop()

        
        helper([],0,0)
        return ans