class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        #we build a monotonically decreasing stack to store the left starting points of the ramp
        n = len(nums)

        max_width = float('-inf')

        for i in range(n):
            if not stack or nums[i]  < nums[stack[-1]]:
                stack.append(i)
            
        #this loop is for identifying ending points of the ramp that satisy the conditions
        for i in range(n - 1,- 1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                j = stack.pop()
                if i > j:
                    max_width = max(max_width,i - j)

        
        return max_width if max_width != float('-inf') else 0

