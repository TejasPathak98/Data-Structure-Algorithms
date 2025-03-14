class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # n = len(candidates)
        # ans = set() 

        # def helper(temp,i):
        #     if sum(temp) > target:
        #         return
            
        #     if sum(temp) == target:
        #         ans.add(tuple(temp.copy()))
        #         return
            
        #     for j in range(i,n):
        #         temp.append(candidates[j])
                
        #         helper(temp,j + 1)

        #         helper(temp,j)

        #         temp.pop()
                

        # helper([],0)
        # return list(ans)

        #the issue in my code is redundant sum calculation and also the helper call should be combined

        n = len(candidates)
        ans = [] 

        def helper(temp,current_sum,i):
            if current_sum > target:
                return
            
            if current_sum == target:
                ans.append(temp[:])
                return
            
            for j in range(i,n):
                temp.append(candidates[j])
                helper(temp,current_sum + candidates[j],j) #Combining those 2 recursive calls
                temp.pop()


        helper([],0,0)
        return ans