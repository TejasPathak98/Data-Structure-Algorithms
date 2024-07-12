class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height) 

        p1 = 0 
        p2 = n - 1 
        max_area = 0 

        while p1 < p2:
            if height[p1] <= height[p2]:
                max_area = max(max_area,height[p1]*(p2 - p1))
                p1 += 1 
            else:
                max_area = max(max_area,height[p2]*(p2 - p1))
                p2 -= 1
        
        return max_area