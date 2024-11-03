class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        n = len(nums)

        def helper(nums,i):
            if i == n:
                ans.append(temp.copy())
                return

            temp.append(nums[i])

            helper(nums,i + 1)

            temp.pop()

            helper(nums,i + 1)

        helper(nums,0)
        return ans
            
