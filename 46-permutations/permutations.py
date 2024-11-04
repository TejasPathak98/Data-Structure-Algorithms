class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        ans = []

        def helper(l):
            nonlocal ans
            if len(l) == len(nums):
                ans.append(l.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in l:
                    l.append(nums[i])
                    helper(l)
                    l.pop()
                
        helper([])
        return ans


       
        