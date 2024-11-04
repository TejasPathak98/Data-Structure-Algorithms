class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        ans = []

        def helper(l,nums):
            nonlocal ans
            if len(l) == len(nums):
                ans.append(l.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in l:
                    l.append(nums[i])
                    helper(l,nums)
                    l.pop()
                
        helper([],nums)
        return ans


       
        