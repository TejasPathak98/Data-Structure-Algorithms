class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        leftMax = 0
        rightMax = 0

        left = 0
        right = n - 1
        max_area = 0

        while left < right:
            if height[left] > leftMax:
                leftMax = height[left]
            if height[right] > rightMax:
                rightMax = height[right]
            
            if rightMax <= leftMax:
                max_area += rightMax - height[right]
                right -= 1
            else:
                max_area += leftMax - height[left]
                left += 1

        return max_area



        
        