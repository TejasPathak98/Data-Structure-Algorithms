class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        max_area = 0

        i = 0
        j = n - 1

        while i < j:
            if height[i] >= height[j]:
                max_area = max(max_area,(j - i) * height[j])
                j -= 1
            else:
                max_area = max(max_area,(j - i) * height[i])
                i += 1

        return max_area
        