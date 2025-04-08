class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #Monotonic Decreasing Stack

        stack = []
        n = len(nums)
        result = [-1] * n

        #For cicurlar go twice
        for i in range(2*n  - 1):
            while stack and nums[i % n] > nums[stack[-1]]:
                top_index = stack.pop()
                result[top_index] = nums[i % n]

            if i < n:
                stack.append(i)

        return result