class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        
        ans = []

        def helper(i,temp):
            if i == len(nums):
                ans.append(temp.copy())
                return
            
            temp.append(nums[i])

            helper(i + 1,temp)

            temp.pop()

            helper(i+ 1,temp)
        
        helper(0,[])
        return ans