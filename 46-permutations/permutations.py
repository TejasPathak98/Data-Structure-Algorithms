class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(idx,temp):
            if idx == n:
                res.append(temp.copy())
                return

            for j in range(idx,n):
                temp[idx] , temp[j] = temp[j] , temp[idx]
                backtrack(idx + 1,temp)
                temp[idx] , temp[j] = temp[j] , temp[idx]

        
        backtrack(0,nums)
        return res





