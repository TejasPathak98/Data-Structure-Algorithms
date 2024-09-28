class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        n = len(height)
        max_area = 0

        p1 = 0
        p2 = n - 1

        while p1 < p2:
            area = (p2 - p1) * min(height[p1],height[p2])
            max_area = max(max_area,area)
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        
        return max_area

        