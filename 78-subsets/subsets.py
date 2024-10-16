class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(ans,nums,i,l):
            if i == len(nums):
                ans.append(l.copy())
                return
            
            l.append(nums[i])
            helper(ans,nums,i + 1,l)
            l.pop()
            helper(ans,nums,i+1,l)

        helper(ans,nums,0,[])
        return ans