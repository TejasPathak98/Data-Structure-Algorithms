class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        max_area = 0

        while left < right:
            if height[left] > leftMax:
                leftMax = height[left]
            if height[right] > rightMax:
                rightMax = height[right]
            
            if leftMax <= rightMax:
                max_area += (leftMax - height[left])
                left += 1
            else:
                max_area += (rightMax - height[right])
                right -= 1

        return max_area


