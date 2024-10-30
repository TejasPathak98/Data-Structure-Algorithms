class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        def helper(x):
            if x == len(nums):
                ans.append(temp.copy())
                return
            
            temp.append(nums[x])
            helper(x + 1)

            temp.pop()
            helper(x + 1)
        
        helper(0)
    
        return ans