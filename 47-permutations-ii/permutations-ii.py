class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)

        def helper(i):
            if i == n:
                ans.add(tuple(nums[:]))
                return
            
            for j in range(i,n):
                nums[i] , nums[j] = nums[j] , nums[i]
                helper(i + 1)
                nums[i] , nums[j] = nums[j] , nums[i]

        
        helper(0)
        return list(ans)
            

