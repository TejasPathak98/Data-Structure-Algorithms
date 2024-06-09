class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(ans,nums,index,l):

            if index >= len(nums):
                ans.append(l.copy())
                return
            
            l.append(nums[index])
            helper(ans, nums, index + 1, l)
            l.pop()
            helper(ans, nums, index + 1, l)

        helper(ans, nums, 0, [])
        return ans
        