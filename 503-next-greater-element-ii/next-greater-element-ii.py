class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #Decreasing Monotonic Stack approach

        stack = [] #indices of element(whose values are in descreasing order)
        result = [-1] * len(nums)
        n = len(nums)

        #since its a circular queue, thats why we iterate twice
        for i in range(2*n - 1):
            while stack and nums[i % n] > nums[stack[-1]]:
                top_index = stack.pop()
                result[top_index] = nums[i % n]

            if i < n:
                stack.append(i)

        
        return result
