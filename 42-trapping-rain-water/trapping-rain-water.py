class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        leftMax = 0
        RightMax = 0

        while left < right:
            leftMax = max(leftMax,height[left])
            RightMax = max(RightMax,height[right])

            if leftMax <= RightMax:
                max_area += leftMax - height[left]
                left += 1
            else:
                max_area += RightMax - height[right]
                right -= 1

        return max_area
        