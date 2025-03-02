class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #increasing monotonic queue
        
        stack = [-1]
        max_area = 0
        i = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = (i - 1) - stack[-1]
                max_area = max(max_area,h*w)
            stack.append(i)

        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = (len(heights) - 1) - (stack[-1])
            max_area = max(max_area,h*w)
        
        return max_area