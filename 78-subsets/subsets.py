class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def helper(temp,i):
            if i == n:
                ans.append(temp.copy())
                return
            
            temp.append(nums[i])
            helper(temp,i + 1)

            temp.pop()
            helper(temp,i + 1)

    
        helper([],0)
        return ans
